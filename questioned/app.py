"""
Contains the main application entry point.
"""

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('-q','--question_count', default=10, help='Amount of questions to put in the exam.')
@click.option('-f','--question_file', type=click.Path(exists=True, readable=True, dir_okay=False), default='questions.yml', help='Path to question definition file')
def generate_exam(question_count):
    click.echo("Generating exam")
