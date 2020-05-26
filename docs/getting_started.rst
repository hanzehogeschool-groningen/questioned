Getting started 
==============================

Welcome to questioned.

This page will guide you through generating your first exam and show you some
of the features of questioned.
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

*Please note that adding a count higher than the amount of provided questions will
cause the program to fail.*

In this case we have opted for a single :py:class:`ManualOpenQuestion <questioned.questions.manual_open_question.ManualOpenQuestion>`.
(a full listing of question types can be found at :doc:`questioned.questions` )
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


Rendering to different formats
------------------------------

Questioned can output to multiple formats. At the time of writing, 
these formats are supported:
 - markdown
 - blackboard

The different output formats can be selected using the ``-t`` flag.

For example, the following command will write out a blackboard-importable
questions file:
::
    $ qst generate-exam -f exam_spec.yml -o exam.txt -t blackboard

The file ``exam.txt`` will then contain the following output:
::
    FIB     Isn't this great!?      True

This file can then be imported into a blackboard exam.


A more complex exam spec
------------------------
Now that we've learned how to create a simple exam_spec, we can expand upon that
spec to create a larger, more varied exam.

Let us take the following ``exam_spec.yml`` as an example:
::
    meta:
      title: Computer Architectures Practice Exam
      introduction: |
        Welcome to this computer architectures practice exam.
    
        * The exam must be completed within 90 minutes.
        * You may not use a calculator.
        * Please clearly note your name and student number on each page.
    
        Good luck!
    
    exam_content:
    - type: ParsonsProblem
      count: 1
    - type: LogicProblem
      count: 5
    - type: RadixConversionQuestion
      count: 10
    - type: ManualOpenQuestion
      count: 2
    - type: ManualMultipleChoiceQuestion
      count: 1
    
    manual_open_questions:
    - question: "Does this graph look cool?"
      answer: 'Yes'
      image: "testimage.png"
    - question: "Do you like computers?"
      answer: 'Yes'
    
    manual_multiple_choice_questions:
    - question: "What is the Answer to the Ultimate Question of Life, the Universe, and Everything?"
      correct_answer: "42"
      incorrect_answers:
        - "12"
        - "24"
        - "-1"
    
    parsons_problems:
    - description: "Pyramid printing function."
      code: |
        #include<stdio.h>
        int main() {
            int i, j, rows;
            printf("Enter number of rows: ");
            scanf("%d", &rows);
            for (i=1; i<=rows; ++i) {
                for (j=1; j<=i; ++j)
                { printf("* "); }
                printf("\n");}
            return 0;}

This larger exam spec contains more blocks, but the basic structure remains
the same. We still define our exam title and introduction in the ``meta`` block.
We still define our layout in the ``exam_content`` block.

Let us walk through the ``exam_content`` block item-by-item:

We start off the exam with a single :py:class:`ParsonsProblem <questioned.questions.parsons_problem.ParsonsProblem>`. 
These require the student to reassemble a piece of jumbled code based on its 
description. This question type requires some manually input information, which
we provide via the ``parsons_problems`` block.

Then we move onto the next item :py:class:`LogicProblem <questioned.questions.logic_problem.LogicProblem>`.
We specify we would like five of these. As these require no further information,
we need not specify a block for it.

After these questions we add 10 instances of the :py:class:`RadixConversionQuestion <questioned.questions.radix_conversion_question.RadixConversionQuestion>`.
These also require no extra information, so we can move on.

We now a section of two :py:class:`ManualOpenQuestion <questioned.questions.manual_open_question.ManualOpenQuestion>` questions as we did in the earlier example.

We close the exam with a single :py:class:`ManualMultipleChoiceQuestion <questioned.questions.manual_multiple_choice_question.ManualMultipleChoiceQuestion>` question.
We define the pool of questions to choose from with the 
``manual_multiple_choice_questions`` block. 

This ``exam_spec.yml`` will generate an exam similar to the following:
*Though question order may differ within sections*

::

    Computer Architectures Practice Exam
    ====================================
    
    Welcome to this computer architectures practice exam.
    
    * The exam must be completed within 90 minutes.
    * You may not use a calculator.
    * Please clearly note your name and student number on each page.
    
    Good luck!
    This exam contains 19 questions.
    
    ## Questions 
    
    ### Question 1
    Please reassemble the following code snippets to form a Pyramid printing function..
    
             #include<stdio.h>
             printf("\n");}
             for (i=1; i<=rows; ++i) {
             printf("Enter number of rows: ");
             int main() {
             int i, j, rows;
             return 0;}
             for (j=1; j<=i; ++j)
             { printf("* "); }
             
             scanf("%d", &rows);
    
    ### Question 2
    Given the following expression:
    q = ((c or b) and (c or a))
    And the following starting values:
    a = False
    b = True
    c = False
    
    What is the resulting value for q?
    
    
    ### Question 3
    Given the following expression:
    q = ((c and a) or (b nor c))
    And the following starting values:
    a = True
    b = False
    c = True
    
    What is the resulting value for q?
    
    
    ### Question 4
    Given the following expression:
    q = (((a nor b) xor (b and c)) and a)
    And the following starting values:
    a = True
    b = True
    c = False
    
    What is the resulting value for q?
    
    
    ### Question 5
    Given the following expression:
    q = (b or (b or c))
    And the following starting values:
    a = False
    b = False
    c = True
    
    What is the resulting value for q?
    
    
    ### Question 6
    Given the following expression:
    q = ((b and c) or (b and a))
    And the following starting values:
    a = False
    b = True
    c = True
    
    What is the resulting value for q?
    
    
    ### Question 7
    Convert 0b11010101 from binary to decimal.
    
    ### Question 8
    Convert 249 from decimal to hexadecimal.
    
    ### Question 9
    Convert 0xf5 from hexadecimal to decimal.
    
    ### Question 10
    Convert 152 from decimal to hexadecimal.
    
    ### Question 11
    Convert 166 from decimal to hexadecimal.
    
    ### Question 12
    Convert 0b10111010 from binary to decimal.
    
    ### Question 13
    Convert 0b11000011 from binary to decimal.
    
    ### Question 14
    Convert 0xeb from hexadecimal to decimal.
    
    ### Question 15
    Convert 135 from decimal to hexadecimal.
    
    ### Question 16
    Convert 190 from decimal to hexadecimal.
    
    ### Question 17
    Do you like computers?
    
    ### Question 18
    <img src="data:image/png;base64, [IMAGE DATA LEFT OUT]" /><br/><br/>Does this graph look cool?
    
    ### Question 19
    What is the Answer to the Ultimate Question of Life, the Universe, and Everything?
     - 42
     - 24
     - -1
     - 12
    
    
    
    ## Answers 
    
    1. #include<stdio.h>
    int main() {
        int i, j, rows;
        printf("Enter number of rows: ");
        scanf("%d", &rows);
        for (i=1; i<=rows; ++i) {
            for (j=1; j<=i; ++j)
            { printf("* "); }
            printf("\n");}
        return 0;}
    
    2. False
    3. True
    4. False
    5. True
    6. True
    7. 213
    8. 0xf9
    9. 245
    10. 0x98
    11. 0xa6
    12. 186
    13. 195
    14. 235
    15. 0x87
    16. 0xbe
    17. Yes
    18. Yes
    19. 42
