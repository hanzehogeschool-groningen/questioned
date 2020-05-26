"""
This module defines the manual open question.
"""

import base64
import random
import logging

from .question import Question


class ManualMultipleChoiceQuestion(Question):
    """
    Defines a question that is input manually using the exam_spec file.

    This question type requires the student to select an answer from a given
    group of answers. One of these answers is correct.

    The question text is passed through the ``question`` parameter.

    The correct answer is passed using the ``correct_answer`` parameter.
    There must be only one of these.

    The incorrect answers, otherwise known as distractors, are provided as
    a list to the ``incorrect_answers`` parameter. This list may be
    arbitrarily long, but be aware that blackboard does not support more
    than 255 total answers, including the correct answer.

    Though, creating a list of options this long may have other practical
    implication.

    Supports the inclusion of images above the question text, similar to
    :py:class:`ManualOpenQuestion <questioned.questions.manual_open_question.ManualOpenQuestion>`.

    The order of choices is randomized.

    Exam Spec example:
    ::
        manual_multiple_choice_questions:
        - question: "What is the Answer to the Ultimate Question of Life, the Universe, and Everything?"
          correct_answer: "42"
          incorrect_answers:
            - "12"
            - "24"
            - "-1"
    """

    def render_markdown(self):
        """
        Renders the markdown output for this question.
        """
        out = f"{self.question}\n"
        possible_answers =  self.incorrect_answers + [self.answer]
        random.shuffle(possible_answers)
        for possible_answer in possible_answers:
            out += f" - {possible_answer}\n"
        return out

    def render_blackboard(self):
        """
        Renders the blackboard question.
        """
        out_question = self.question.replace('\n', '<br />')
        out = f"MC\t{out_question}\t"
        answers = [(self.answer, 'correct')]
        for incorrect_answer in self.incorrect_answers:
            answers.append( (incorrect_answer, 'incorrect') )

        random.shuffle(answers)
        for answer in answers:
            out += f'{answer[0]}\t{answer[1]}\t'
        
        out = out[:-1]  # We drop the last tab here
        out += '\n'

        return out


    @classmethod
    def generate(cls, exam_spec, count: int = 5):
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
            out.append(
                cls(
                    exam_spec,
                    question_text,
                    selected_question['correct_answer'],
                    incorrect_answers=selected_question['incorrect_answers']
                )
            )
        return out
