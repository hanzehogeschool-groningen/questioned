"""
This module defines the manual entry question.
"""

import random

from .question import Question


class ManualEntryQuestion(Question):
    """
    Defines a question that is input manually using the exam_spec file.
    """

    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Generates an amount of manually input questions.
        """
        out = []
        selection = list(random.sample(exam_spec['manual_entry_questions'], count))
        for selected_question in selection:
            out.append(
                cls(
                    exam_spec,
                    selected_question['question'],
                    selected_question['answer']
                )
            )
        return out
