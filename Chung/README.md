<p align="center"><img width="100" src="./images/avatar.png" /></p>
<h2 align="center">Chung Kao's</h2>
<h4 align="center">Challenge Submissions</h4>
<p align="center">Columbia University - Justice Through Code</p>
<p align="center"><img width="600" src="./images/jtc_site_screenshot.png" /></p>

## About Me

Gratefully parttaking Justice Through Code's Spring 2022 cohort, I intend to leverage this opportunity to expand my knowledge of code as well as professional connections so to prepare for the career that seek, a full-stack software engineer. I have undergone a 18-month career technical training with the Californai Prison Inductry Authority, sponsored by The Last Mile, in software development, to wit, frontend and backend fundamentals and JavaScript algorithm. I've continued to learn code after leaving prison and have completed Code the Dream's Frontend Fundamentals and React courses and am in a CTD Practicum team working collaboratively to develop a real-life, deployable web app bootstrapped with [Create-Next-App](https://nextjs.org/docs/api-reference/create-next-app). [Head over](https://github.com/Sanlung) over to my GitHub account to check out the Practicum project in progress and check out my porfolio page [here](https://sanlung.github.io/) and my React final project [here](https://remindme-abd87.web.app/Reading).

While behind bars, I self-taught Python by reading books and coded it with a pencil and paper. I was able to attain a level of understanding sufficient to write some basic command line games such as _tic tac toe_ and _hangman_ and to code algorithm for quick, merge, bubble, insertion sorts. For example, here's the _hangman_ game I wrote with pencil:

![hangman game](./images/hangman.gif)

## Journey with JTC

### Goal

To have gained demonstrable proficiency in the command of the Python langauge by the end of Justice Through Code training. Success is measured against what I have started off as illustrated in the About Me seciton.

#### Week 1

- Curriculum: Setting up the develpment environment and gaining familiarity with the command line and Git and GitHub.
- Progess: Within knowledge and expeirience.

#### Week 2

- Curriculum: Phyton syntax with `print` statement and comments, primitive data types and operators and conditional statements.
- Progress: Within knowledge and experience.

#### Week 3

- Curriculum: Lists, loops and dictionaries in Python.
- Progress: Mostly within knowledge and experience. However, I learned:
  1. the string that takes the `.join()` method is termed a _separator_ in Python jargon
  2. scope in Python is delimited only by functions (_global_, _nonlocal_, _local_ scopes). Thus, a variable is not scoped to conditional statements (code blocks) in which it is delared and can be referenced outside of the statements, and the following will output the value assigned to the last `item` extracted by the `for` loop:
     ```
     for item in list:
         do something
     print(item)
     ```
  3. Self studied list comprehesion from code literacies.

#### Week 4

- Curriculum: functions and import modules.
- Progress: Mostly within knowledge and experience. New understandings includes:

  1.  The Python interpreter is indiscriminate as to the space between the function name and the parameer parentheses in the function definition.
  2.  The Python interpreter is indiscriminate to the lack of space between the `return` keyword and the object being returned if the object is closed in parenteses. In that regard, Python appears not care about whether the object being returned is wrapped in parentheses.
  3.  Self studied lambda functions and higher-order functions in Python.
  4.  The submodules (variables) in a module/file, or the module as a whole, does not have to be expressly exported in the file to be imported in other files.
  5.  Import the whole module and use the submodules like so:
      ```
      import moldule
      module.submodule()
      ```
      Or import every submodule with a wildcard and use them like so:
      ```
      from module import *
      submodule()
      ```
      Or import the submodules expressly like so:
      ```
      from module import submodule1, submodule2, submodule3
      submodule1()
      submodule2()
      submodule3()
      ```

#### Project 1

Check out my Tip Calculator [here](https://github.com/Sanlung/tip-calculator-jtc2022.git).

#### Week 5

- Curriculum: Exception handling and nested list and dictionary mixes.
- Progress: Mostly within knowledge and experience. New understanding includes:

  1. Python error handling may be of the `try`-`except`(-`except*`), `try`-`except`-`else` and `try`-`except`-`finally` forms, and to raise an exception use `raise`.

#### Week 6

- Curriculum: Python objects and Object oriented programming.
- Progress: Mostly within knowledge and experience. New understanding includes:

  1. Python obejcts inherit from another object by invoking the parent inside the parenthses, like so:

  ```
  class Children(Parent):

  ```

  2. Python objects are all descendants of the `<class /object'>` so `class Children:` is just `class Children(object):`

#### Week 7

- Curriculum: HTML, CSS and the web.
- Progress: Within knowledge and experience.

#### Week 8

- Curriculum: Django framework (week 1) - Django fundamentals.
- Progress: Somehow challenging to go through the django.org's seven-part tutorial for django fundamentals. The three mini projects for the week are rather simple to complete; however, they do not adequately address the learners' need for a holistic understanding of the framework or a grasp of any particular areas of technology that the framework encompasses. The Django tutorial has to some extent supplemented what the classes did not cover, however basic it is.

##### Django project #1

Check out my Hello World Django app [here](https://github.com/Sanlung/python-hello-world).

##### Django project #2

Check out my Color Picker Django app [here](https://github.com/Sanlung/django-color-picker).

##### Django project #3

Check out my Sandwich Maker Django app [here](https://github.com/Sanlung/django-sandwich-maker)

#### Week 9

- Curriculum: Pair programming and relational database design.
- Progress: Have prior exposure to pair programming as well as having collaborated in dev teams to edevelop real-life, deployable web applications. Most recent is with the Code the Dream, React - Red Egret, Slaty Egret Practicum team in designing, developing and deploying a [Whatodo](https://github.com/Sanlung/ctd-practicum-slaty-egret) todo app bootstrapped with [Create Next App](https://create-next-app.js.org/) using [Firebase](https://firebase.google.com/) authentication and Cloud Firestore.

#### Project 2

Check out my collaborative Django project, New York City guide, [here](https://github.com/Sanlung/jtc-nyc-guide).

### Author

[![Chung Kao](./images/Chung_button.svg)](https://github.com/Sanlung)
