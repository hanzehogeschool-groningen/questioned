"""
This module defines the conversion entry question.
"""

import random

from .question import Question


class ConversionQuestion(Question):
    """
    Defines a question that is input manually using the exam_spec file.
    """

    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Generates an amount of manually input questions.
        """
        out = []
        for _ in range(count):

            # Choose a random target to convert to
            conversion_target = random.choice(['hexadecimal', 'binary'])

            # Generate a random number, such that it's maximally a byte in size
            number = random.randrange(128, 255)

            # Convert the number
            if conversion_target == 'hexadecimal':
                converted = hex(number)
            elif conversion_target == 'binary':
                converted = bin(number)

            # Determine the direction for the question
            to_decimal = random.choice([True, False])

            if to_decimal:
                out.append(
                    cls(
                        exam_spec,
                        f'Convert {converted} from {conversion_target} to decimal.',
                        f'{number}'
                    )
                )
            else:
                out.append(
                    cls(
                        exam_spec,
                        f'Convert {number} from decimal to {conversion_target}.',
                        f'{converted}'
                    )
                )
        return out
