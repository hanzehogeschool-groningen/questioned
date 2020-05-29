'''
Superclass for all question objects.
'''

import logging
import base64

class Question():
    '''
    Superclass for all questions in the program.

    Can be extended to create different types of question.
    '''

    def __init__(self, exam_spec: dict, question: str, answer: str, *, question_data: dict = {}, **kwargs):
        """
        Constructor for question objects.
        """
        self._exam_spec = exam_spec
        self.question = question
        self.answer = answer
        self.question_data = question_data

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
        out = ""
        if self.image is not None:
            out += self.image
        out += f"{self.question}\n"
        return out

    def render_blackboard(self):
        """
        Renders the question for blackboard.
        """
        out_question = self.question.replace('\n', '<br />')
        if self.image is not None:
            out_question = self.image + out_question
        out = f"FIB\t{out_question}\t{self.answer}\n"
        return out

    @property
    def image(self) -> str:
        """
        Returns the image encapsulated in an html ``img`` tag in its
        base64 encoded form.

        Requires that the ``image_path`` attribute be set.
        """
        if not 'image' in self.question_data.keys():
            return None
        
        image_path = self.question_data['image']

        logging.debug('Encountered question with image path %s, encoding..', image_path)
        with open(image_path, 'rb') as image_file:
            image_base64 = base64.b64encode(image_file.read())
            if 'jpeg' in image_path or 'jpg' in image_path:
                return f'<img src="data:image/jpeg;base64, {image_base64.decode("utf-8")}" /><br/><br/>'
            elif 'png' in image_path:
                return f'<img src="data:image/png;base64, {image_base64.decode("utf-8")}" /><br/><br/>'
            else:
                raise ValueError(f'Unsupported image type for image: {self.image_path}')

    @classmethod
    def generate(cls, exam_spec, count: int = 5, section_data = {}):
        """
        Returns an amount of this object.
        """
        out = []
        for _ in range(count):
            out.append(cls(exam_spec, "<<Generic Question>>", "<<Generic Answer>>"))
        return out
