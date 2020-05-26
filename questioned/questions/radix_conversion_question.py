"""
This module defines the conversion entry question.
"""

import random

from .question import Question


class RadixConversionQuestion(Question):
    """
    Defines a radix conversion question.

    This question type requires the student to convert a number from one base
    to another. For example from hexadecimal to decimal, or from binary to
    decimal, etc.

    This question type requires no extra information from the exam_spec.
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
