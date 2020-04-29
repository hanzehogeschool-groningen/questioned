"""
The questions module contains all the different question object types.
"""

from .question import Question
from .conversion_question import ConversionQuestion
from .manual_entry_question import ManualEntryQuestion
from .logic_problem import LogicProblem
from .parsons_problem import ParsonsProblem

QUESTION_TYPES = {
    Question.__name__: Question,
    ConversionQuestion.__name__: ConversionQuestion,
    ManualEntryQuestion.__name__: ManualEntryQuestion,
    LogicProblem.__name__: LogicProblem,
    ParsonsProblem.__name__: ParsonsProblem
}
