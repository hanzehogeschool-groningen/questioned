"""
This module defines the manual open question.
"""

from questioned.utils import select_questions

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
    def generate(cls, exam_spec, count: int = 5, section_data = {}):
        """
        Generates an amount of manually input questions.
        """
        # Pylint gets this wrong:
        # pylint: disable=unsubscriptable-object

        out = []
        
        selection = select_questions(cls, exam_spec, 'manual_open_questions', count, section_data)

        for selected_question in selection:
            out.append(
                cls(
                    exam_spec,
                    selected_question['question'],
                    selected_question['answer'],
                    question_data = selected_question
                )
            )
        return out
