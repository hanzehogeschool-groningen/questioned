"""
Contains uncategorized utility functions.

These usually leave this module when features are expanded upon.
"""

import sys
import logging
import random


def select_questions(question_class, exam_spec, block_name, count, section_data):
    """
    Selects questions from a block in the exam spec.

    Can filter for a certain group name.
    """
    pool = exam_spec[block_name]

    if count > len(pool):
        logging.error("More questions requested of %s than were provided in exam_spec.", question_class)
        sys.exit(1)

    if 'group' in section_data.keys():
        pool = [q for q in pool if 'group' in q.keys() and q['group'] == section_data['group']]

        if count > len(pool):
            logging.error("More questions requested of %s for group %s than were provided in exam_spec.",
                          question_class, section_data['group'])
            sys.exit(1)

    return list(random.sample(pool, count))
