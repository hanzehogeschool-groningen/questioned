'''
Superclass for all question objects.
'''


class Question():
    '''
    Superclass for all questions in the program.

    Can be extended to create different types of question.
    '''

    def __init__(self, exam_spec: dict, question: str, answer: str):
        """
        Constructor for question objects.
        """
        self._exam_spec = exam_spec
        self.question = question
        self.answer = answer

    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Returns an amount of this object.
        """
        out = []
        for _ in range(count):
            out.append(cls(exam_spec, "<<Generic Question>>", "<<Generic Answer>>"))
        return out
