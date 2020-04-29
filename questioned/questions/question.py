'''
Superclass for all question objects.
'''


class Question():
    '''
    Superclass for all questions in the program.

    Can be extended to create different types of question.
    '''

    def __init__(self, exam_spec: dict, question: str, answer: str, **kwargs):
        """
        Constructor for question objects.
        """
        self._exam_spec = exam_spec
        self.question = question
        self.answer = answer

        for kwarg, value in kwargs.items():
            setattr(self, kwarg, value)

    def render(self, output_format, *args, **kwargs) -> str:
        """
        Delegates to the applicable render format based on the output_format.

        Renderer is selected based on function name, for example:
        render('markdown') will call the render_markdown method.
        render('blackboard') will call the render_blackboard method.
        etc.

        This functionality should probably be left alone when implementing your
        own question classes.
        """
        if not hasattr(self, f'render_{output_format}'):
            raise Exception(f'Renderer for {output_format} not available for {type(self)}')

        renderer = getattr(self, f"render_{output_format}")

        if not hasattr(renderer, '__call__'):
            raise Exception(f"Renderer function render_{output_format} is not a function.")

        return renderer(*args, **kwargs)

    def render_markdown(self):
        """
        Renders the question to markdown.
        """
        out = f"{self.question}\n"
        return out

    def render_blackboard(self):
        """
        Renders the question for blackboard.
        """
        out_question = self.question.replace('\n', '<br />')
        out = f"FIB\t{out_question}\t{self.answer}\n"
        return out

    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Returns an amount of this object.
        """
        out = []
        for _ in range(count):
            out.append(cls(exam_spec, "<<Generic Question>>", "<<Generic Answer>>"))
        return out
