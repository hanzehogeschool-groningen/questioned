"""
This module defines the manual entry question.
"""

import random
import logging
import html

from .question import Question


class ParsonsProblem(Question):
    """
    Defines a question that is input manually using the exam_spec file.
    """

    def render_blackboard(self):
        """
        Render the parsons problem for blackboard.
        Uses the JUMBLED_SENTENCE type.
        """
        # Create choice-answer pairs
        ca_tuples = []
        answer_lines = self.answer.split('\n')
        question_lines = self.question.split('\n')
        for line_nr in range(len(answer_lines)-1):
            ca_tuples.append([line_nr, answer_lines[line_nr], question_lines[line_nr]])

        out = f"JUMBLED_SENTENCE\tPlease reassemble the following code snippets to form a {self.description}.<br/><br/>"
        out += "<pre>"
        for line in question_lines:
            if line.strip() == '':
                continue
            escaped_line = html.escape(
                line.replace('[', '&#91;')\
                    .replace(']', '&#93;')
            )
            out += ' - '
            out += escaped_line.strip()
            out += '<br />'

        out += '</pre>'

        # Place variable fields:
        for tup in ca_tuples:
            out += f"[{tup[0]}]<br/>"

        out += '\t'

        # Add answers
        for tup in random.sample(ca_tuples, k=len(ca_tuples)):
            out += f'{tup[1]}\t{tup[0]}\t\t'

        out = out[:-2] # Remove extraneous tabs

        out += '\n'
        return out


    def render_markdown(self):
        """
        Render the parsons problem to markdown.
        """
        out = f"Please reassemble the following code snippets to form a {self.description}.\n\n"
        for line in self.question.split('\n'):
            out += f"\t {line.strip()}\n"

        return out

    @classmethod
    def generate(cls, exam_spec, count: int = 1):
        """
        Generates an amount of manually input questions.
        """
        out = []
        selection = list(random.sample(exam_spec['parsons_problems'], count))
        for selected_problem in selection:
            lines = selected_problem['code'].split('\n')
            jumbled_lines = random.sample(lines, k=len(lines))

            jumbled_str = "\n".join(jumbled_lines)

            problem = cls(exam_spec,
                          jumbled_str,
                          selected_problem['code'],
                          description=selected_problem['description']
                         )
            out.append(problem)
        return out
