"""
Contains the main application entry point.
"""

import random
import logging

import click
import yaml

from questioned import renderer

@click.group()
def cli():
    """
    Command group to function as the main program entrypoint. Just a label. Can be empty.
    """


@cli.command()
@click.option(
    "-c", "--question_count", default=5, help="Amount of questions to put in the exam."
)
@click.option(
    "-f",
    "--question_file",
    type=click.Path(exists=True, readable=True, dir_okay=False),
    default="questions.yml",
    help="Path to question definition file",
)
@click.option(
    "-o",
    "--output_file",
    type=click.Path(writable=True, dir_okay=False),
    default="exam.md",
    help="The file to write the exam to.",
)
@click.option("-d", "--debug", is_flag=True, default=False)
def generate_exam(question_count, question_file, output_file, debug):
    """
    Exam generation command entrypoint.
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info("Loading Question Data")
    question_data = yaml.load(open(question_file, "r"), Loader=yaml.SafeLoader)
    logging.debug("Question Data loaded:")
    logging.debug("\n, %s", yaml.dump(question_data))

    logging.info("Selecting Questions")
    selected_questions = select_questions(question_data, amount=question_count)

    logging.info("Rendering Exam")
    exam = renderer.introduction_section_md(selected_questions, question_data['meta'])
    exam += renderer.question_section_md(selected_questions)
    exam += renderer.answers_section_md(selected_questions)

    logging.debug("Exam Output: \n %s", exam)

    logging.info("Writing exam to file")
    with open(output_file, 'w') as outfile:
        outfile.write(exam)


def select_questions(question_data: dict, *, amount: int = 1) -> list:
    """
    Selects a random list of questions from the question dataset.
    """
    return list(random.sample(question_data["questions"], amount))
