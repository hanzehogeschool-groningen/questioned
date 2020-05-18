"""
The questions module contains all the different question object types.
"""

from .question import Question
from .conversion_question import ConversionQuestion
from .manual_open_question import ManualOpenQuestion
from .manual_multiple_choice_question import ManualMultipleChoiceQuestion
from .logic_problem import LogicProblem
from .parsons_problem import ParsonsProblem

QUESTION_TYPES = {
    Question.__name__: Question,
    ConversionQuestion.__name__: ConversionQuestion,
    ManualOpenQuestion.__name__: ManualOpenQuestion,
    ManualMultipleChoiceQuestion.__name__: ManualMultipleChoiceQuestion,
    LogicProblem.__name__: LogicProblem,
    ParsonsProblem.__name__: ParsonsProblem
}
