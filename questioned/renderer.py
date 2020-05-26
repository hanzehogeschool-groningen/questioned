"""
Contains functions for rendering to md.
"""


def render_output(output_format, exam_questions, exam_spec, *args, **kwargs):
    """
    Delegates to the correct renderer based on the output_format.
    """

    # Use old markdown renderer if requested
    if output_format == 'markdown':
        exam = introduction_section_md(exam_questions, exam_spec['meta'])
        exam += question_section_md(exam_questions)
        exam += answers_section_md(exam_questions)
        return exam

    # Otherwise delegate to objects
    exam = ""
    for question in exam_questions:
        exam += question.render(output_format, *args, **kwargs)
    return exam


def introduction_section_md(questions, meta: str) -> str:
    """
    Renders out an introduction section.
    """
    out = f"{meta['title']}\n"
    out += '='.ljust(len(meta['title']), '=') + '\n\n'
    out += meta['introduction']

    out += f"This exam contains {len(questions)} questions.\n\n"

    return out


def question_section_md(questions) -> str:
    """
    Renders out the question section to md.
    """
    out = "## Questions \n\n"
    for number, question in enumerate(questions):
        out += f"### Question {number +1}\n"
        out += question.render('markdown')
        out += '\n'
    out += '\n\n'
    return out


def answers_section_md(questions) -> str:
    """
    Renders out the answers section to md.
    """
    out = "## Answers \n\n"
    for number, question in enumerate(questions):
        out += f"{number +1}. {question.answer}\n"
    return out
