Getting started 
==============================

Welcome to questioned.

This page will guide you through generating your first exam.
If you have not yet installed questioned, please see the :doc:`installation`.

Running Questioned
------------------
Questioned can be run by executing ``qst`` from the shell.
Running questioned without any arguments will produce a simple help text:
::
    Usage: qst [OPTIONS] COMMAND [ARGS]...

      Questioned is a tool for generating random exams. These exams are exported
      in markdown.
    
    Options:
      --help  Show this message and exit.
    
    Commands:
      generate-exam  Exam generation command entrypoint.
             

The ``--help`` flag may be passed to any commandto show a
similar help text for that command.

For example, with the ``generate-exam`` command:
::
    Usage: qst generate-exam [OPTIONS]
    
      Exam generation command entrypoint.
    
    Options:
      -f, --specfile FILE       Path to exam specification file
      -o, --output_file FILE    The file to write the exam to.
      -d, --debug
      -t, --output_format TEXT
      --help                    Show this message and exit.:

A simple exam spec
------------------

Generating an exam in questioned starts with an exam spec file.
This file contians the basic information about the layout and 
questions in your exam, as well as information about the questions
themselves.

The exam spec file is formatted as a yaml_ file. By convention this file is
called ``exam_spec.yml``. Questioned will automatically search for a file
of this name in the current working directory and use it as input. A file may
otherwise be specified using the ``-f`` flag.

.. _yaml: https://yaml.org/

A very simple ``exam_spec.yml`` may look like this:
::
    meta:
      title: "Test Exam"
      introduction: "Have fun!"

    exam_content:
    - type: ManualOpenQuestion
      count: 1

    manual_open_questions:
    - question: "Isn't this great!?"
      answer: yes

This will create a very simple exam with only one question.

There are three main blocks in this spec:
 - meta
 - exam_content
 - manual_open_questions

The ``meta`` block allows us to define contextual information about our exam.
Think of this as the first part of a traditional exam paper. This contains
the title of the exam, and a (usually) short introductory text.

The ``exam_content`` block allows us to define the layout of our exam. In this
case we have specified we want only a single open question section. Using the
``type`` field we specifiy which question type we want, the ``count`` field then
allows us to specify how many of these questions we want.

In this case we have opted for a single :py:class:`ManualOpenQuestion <questioned.questions.manual_open_question.ManualOpenQuestion>`.
This question type will randomly select a sample of questions from the 
``manual_open_questions`` block. Since we only have a single question, it will
always select that one.

To now finally generate the exam, we execute the following command:
::
    $ qst generate-exam -f exam_spec.yml -o exam.md

This command will read the spec from ``exam_spec.yml`` and write the exam to
``exam.md``. The output file will now contain:
::
    Test Exam
    =========
    
    Have fun!This exam contains 1 questions.
    
    ## Questions 
    
    ### Question 1
    Isn't this great!?
    
    ## Answers 
    
    1. True

