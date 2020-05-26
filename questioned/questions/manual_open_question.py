"""
This module defines the manual open question.
"""

import base64
import random
import logging

from .question import Question


class ManualOpenQuestion(Question):
    """
    Defines a question that is input manually using the exam_spec file.

    This question type requires the student to fill in a specific answer.
    
    It is generally advised to keep these answers short and simple, so as
    to avoid errors with automatic grading systems. It is also advised to
    be specific as to how the answer is to be filled in in the question text.

    For example: 
    *What is the atomic symbol for gold? Provide your answer in capital letters
    (e.g. HE).*

    Optionally the question support the inclusion of images above the image
    text using the ``image`` property. A valid path must be entered or the 
    program will fail.

    Exam Spec example:
    ::
        manual_open_questions:
        - question: "Does this graph look cool?"
          answer: 'Yes'
          image: "testimage.png"
        - question: "Do you like computers?"
          answer: 'Yes'
    """

    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Generates an amount of manually input questions.
        """
        # Pylint gets this wrong:
        # pylint: disable=unsubscriptable-object

        out = []
        selection = list(random.sample(exam_spec['manual_open_questions'], count))
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
                    selected_question['answer']
                )
            )
        return out
