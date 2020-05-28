"""
This module defines the manual open question.
"""

import base64
import random
import logging

from IPython import embed

from .question import Question


class ManualMultipleChoiceQuestion(Question):
    """
    Defines a question that is input manually using the exam_spec file.

    This question type requires the student to select an answer from a given
    group of answers. Only one of these answers is correct.

    The question text is passed through the ``question`` parameter.

    The possible answers is provided as a list through the ``answers`` parameter.

    This list contains the answers, as well as whether or not they are correct.

    This list can arbitrarily long, but be aware that blackboard does not support more
    than 255 total answers, including the correct answer.

    Though, creating a list of options this long may have other practical
    implication.

    By default, the list is shuffled by the software, but the list can be
    ordered manually by setting the ``randomize_order`` parameter to
    ``False``. In that case, answers are stated in the order they are provided.

    Supports the inclusion of images above the question text, similar to
    :py:class:`ManualOpenQuestion <questioned.questions.manual_open_question.ManualOpenQuestion>`.

    The order of choices is randomized.

    Exam Spec example:
    ::
        manual_multiple_choice_questions:
        - question: "What is the Answer to the Ultimate Question of Life, the Universe, and Everything?"
          randomize_order: False
          answers:
            - "-1": False
            - "12": False
            - "24": False
            - "42": True
    """


    def __init__(self, exam_spec: dict, question:str, raw_answers: list, **kwargs):
        """
        Constructor for this question object.
        Overrides the standard constructor to support the
        multiple answers scheme.
        """
        self._exam_spec = exam_spec

        self.question = question

        if not 'randomize_order' in kwargs:
            self.randomize_order = True

        for kwarg, value in kwargs.items():
            setattr(self, kwarg, value)
        
        self._answers = self.process_answers(raw_answers)

        if len(self.correct_answers) > 1:
            raise ValueError(f"Multiple correct answers provided for multiple choice question:\n\t{raw_answers}")

    
    def process_answers(self, raw_answers):
        """
        Formats the raw answer input into something more usable.
        """
        out = []
        for raw_answer in raw_answers:
            item = list(raw_answer.items())[0] # Get first and only item.
            out.append(item)

        if self.randomize_order:
            random.shuffle(out)
        
        return out


    @property
    def answer(self) -> str:
        """
        Gives the string representation of the correct answer.
        """
        for possible_answer, correct in self._answers:
            if correct:
                return possible_answer

    @property
    def correct_answers(self) -> list:
        """
        Returns a list of all answers deemed correct by the question.
        """
        out = []
        for possible_answer, correct in self._answers:
            if correct:
                out.append(possible_answer)
        return out


    @property
    def incorrect_answers(self) -> list:
        """
        Returns a list of all answers deemed incorrect by the question.
        """
        out = []
        for possible_answer, correct in self._answers:
            if not correct:
                out.append(possible_answer)
        return out


    def render_markdown(self) -> str:
        """
        Renders the markdown output for this question.
        """
        out = f"{self.question}\n"
        possible_answers = self._answers
   
        for possible_answer, correctness in possible_answers:
            out += f" - {possible_answer}\n"
        return out


    def render_blackboard(self) -> str:
        """
        Renders the blackboard question.
        """
        out_question = self.question.replace('\n', '<br />')
        out = f"MC\t{out_question}\t"

        for answer, correct in self._answers:
            correct_text = 'incorrect'
            if correct:
                correct_text = 'correct'
            
            out += f'{answer}\t{correct_text}\t'

        out = out[:-1]  # We drop the last tab here
        out += '\n'

        return out


    @classmethod
    def generate(cls, exam_spec, count: int = 5) -> list:
        """
        Generates an amount of manually input questions.
        """
        # Pylint gets this wrong:
        # pylint: disable=unsubscriptable-object

        out = []
        selection = list(random.sample(exam_spec['manual_multiple_choice_questions'], count))
        for selected_question in selection:
            question_text = ""
            if 'image' in selected_question.keys():
                logging.debug('Encountered question with image path %s', selected_question['image'])
                with open(selected_question['image'], 'rb') as image_file:
                    image_base64 = base64.b64encode(image_file.read())
                    if 'jpeg' in selected_question['image'] or 'jpg' in selected_question['image']:
                        question_text += f'<img src="data:image/jpeg;base64, {image_base64.decode("utf-8")}" /><br/><br/>'
                    if 'png' in selected_question['image']:
                        question_text += f'<img src="data:image/png;base64, {image_base64.decode("utf-8")}" /><br/><br/>'

            question_text += selected_question['question']
            if 'randomize_order' in selected_question.keys():
                out.append(
                    cls(
                        exam_spec,
                        question_text,
                        selected_question['answers'],
                        randomize_order=selected_question['randomize_order'],
                    )
                )
            else:
                out.append(
                    cls(
                        exam_spec,
                        question_text,
                        selected_question['answers'],
                    )
                )
        return out
