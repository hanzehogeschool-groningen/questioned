"""
This module defines the logic problem question.
"""

import random

from .question import Question


class LogicProblem(Question):
    """
    Defines a question that requires the student to solve a logical problem.

    The student is provided with a boolean logic expressions and a set of initial
    values. The student is then required to evaluate the expression and 
    provide the resulting value in the form of a boolean (True or False)

    These logical problems are fully randomly generated and require no
    input through the exam_spec.
    """

    def render_blackboard(self):
        """
        Renders the question for blackboard. Uses the True/False type.
        """
        out_question = self.question.replace('\n', '<br />')
        question_section = f"{out_question}"
        answer = str(self.answer).lower()
        out = f"TF\t{question_section}\t{answer}\n"
        return out


    @classmethod
    def generate(cls, exam_spec, count: int = 5):
        """
        Generates an amount of manually input questions.
        """
        out = []
        for _ in range(count):
            variables = [
                {"name": "a", "value": random.choice((True, False))},
                {"name": "b", "value": random.choice((True, False))},
                {"name": "c", "value": random.choice((True, False))},
            ]
            tree = LogicTreeNode(variables)
            question_text = "Given the following expression:\n"
            question_text += f"q = {str(tree)}\n"
            question_text += "And the following starting values:\n"
            for var in variables:
                question_text += f"{var['name']} = {var['value']}\n"
            question_text += "\nWhat is the resulting value for q?\n"

            out.append(cls(exam_spec, question_text, str(tree.solution)))

        return out

class LogicTreeNode():
    """
    Node of a tree for a logical expression.
    """

    def __init__(self, variables, depth=0):
        """
        Generates a subtree.
        """
        self.type = random.choice(["and", "or", "xor", "nand", "nor"])

        # Generate Left
        if random.choice([True, False] + [False]*depth):
            self.left = LogicTreeNode(variables, depth=depth+1)
        else:
            self.left = random.choice(variables)

        if random.choice([True, False] + [False]*depth):
            self.right = LogicTreeNode(variables, depth=depth+1)
        else:
            self.right = random.choice(variables)

        self.variables = variables

    def __str__(self):
        """
        Returns the string representation of the logical expression.
        """
        if isinstance(self.left, LogicTreeNode):
            left = self.left
        else:
            left = self.left["name"]


        if isinstance(self.right, LogicTreeNode):
            right = self.right
        else:
            right = self.right["name"]

        return f"({str(left)} {self.type} {str(right)})"

    @property
    def solution(self) -> bool:
        """
        Returns the solution of the logical expression.
        """
        if isinstance(self.left, LogicTreeNode):
            left = self.left.solution
        else:
            left = self.left["value"]


        if isinstance(self.right, LogicTreeNode):
            right = self.right.solution
        else:
            right = self.right["value"]

        if self.type == "and":
            return left and right
        if self.type == "or":
            return left or right
        if self.type == "xor":
            return (left and not right) or (not left and right)
        if self.type == "nand":
            return not (left and right)
        if self.type == "nor":
            return not (left or right)
        raise Exception(f"Unknown operator in logic tree: {self.type}")
