"""
The questions module contains all the different question object types.
"""

from .question import Question
from .radix_conversion_question import RadixConversionQuestion
from .manual_open_question import ManualOpenQuestion
from .manual_multiple_choice_question import ManualMultipleChoiceQuestion
from .logic_problem import LogicProblem
from .parsons_problem import ParsonsProblem

QUESTION_TYPES = {
    Question.__name__: Question,
    RadixConversionQuestion.__name__: RadixConversionQuestion,
    ManualOpenQuestion.__name__: ManualOpenQuestion,
    ManualMultipleChoiceQuestion.__name__: ManualMultipleChoiceQuestion,
    LogicProblem.__name__: LogicProblem,
    ParsonsProblem.__name__: ParsonsProblem
}
