"""
The questions module contains all the different question object types.
"""

from .question import Question
from .conversion_question import ConversionQuestion
from .manual_entry_question import ManualEntryQuestion

QUESTION_TYPES = {
    Question.__name__: Question,
    ConversionQuestion.__name__: ConversionQuestion,
    ManualEntryQuestion.__name__: ManualEntryQuestion
}
