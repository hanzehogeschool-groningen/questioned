"""
Contains the main application entry point.
"""

import random
import logging

import click
import yaml

from questioned import renderer
from questioned.questions import QUESTION_TYPES

@click.group()
def cli():
    """
    Questioned is a tool for generating random exams. These exams are exported in markdown.
    """


@cli.command()
@click.option(
    "-c", "--question_count", default=5, help="Amount of questions to put in the exam."
)
@click.option(
    "-f",
    "--specfile",
    type=click.Path(exists=True, readable=True, dir_okay=False),
    default="exam_spec.yml",
    help="Path to exam specification file",
)
@click.option(
    "-o",
    "--output_file",
    type=click.Path(writable=True, dir_okay=False),
    default="exam.md",
    help="The file to write the exam to.",
)
@click.option("-d", "--debug", is_flag=True, default=False)
def generate_exam(question_count, specfile, output_file, debug):
    """
    Exam generation command entrypoint.
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("Loading Exam Spec")
    exam_spec = yaml.load(open(specfile, "r"), Loader=yaml.SafeLoader)
    logging.debug("Manual Entry Question Data loaded:")
    logging.debug("\n, %s", yaml.dump(exam_spec['manual_entry_questions']))

    exam_questions = generate_questions(exam_spec)

    logging.info("Rendering Exam")
    exam = renderer.introduction_section_md(exam_questions, exam_spec['meta'])
    exam += renderer.question_section_md(exam_questions)
    exam += renderer.answers_section_md(exam_questions)

    logging.debug("Exam Output: \n %s", exam)

    logging.info("Writing exam to file")
    with open(output_file, 'w') as outfile:
        outfile.write(exam)


def generate_questions(exam_spec) -> list:
    """
    Selects a random list of questions from the question dataset.
    """
    exam_layout = exam_spec['exam_content']
    out = []

    for section in exam_layout:
        out += QUESTION_TYPES[section['type']].generate(exam_spec, count=section['count'])

    return out
