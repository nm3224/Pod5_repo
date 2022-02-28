<p align="center"><img width="100" src="./images/avatar.png" /></p>
<h2 align="center">Chung Kao's</h2>
<h4 align="center">Challenge Submissions</h4>
<p align="center">Columbia University - Justice Through Code</p>
<p align="center"><img width="600" src="./images/jtc_site_screenshot.png" /></p>

## About Me

Gratefully parttaking Justice Through Code's Spring 2022 cohort, I intend to leverage this opportunity to expand my knowledge of code as well as professional connections so to prepare for the career that seek, a full-stack software engineer. I have undergone a 18-month career technical training with the Californai Prison Inductry Authority, sponsored by The Last Mile, in software development, to wit, frontend and backend fundamentals and JavaScript algorithm. I've continued to learn code after leaving prison and have completed Code the Dream's Frontend Fundamentals and React courses and am in a CTD Practicum team working collaboratively to develop a real-life, deployable web app bootstrapped with [Create-Next-App](https://nextjs.org/docs/api-reference/create-next-app). [Head over](https://github.com/Sanlung) over to my GitHub account to check out the Practicum project in progress and check out my porfolio page [here](https://sanlung.github.io/) and my React final project [here](https://remindme-abd87.web.app/Reading).

While behind bars, I self-taught Python by reading books and coded it with a pencil and paper. I was able to attain a level of understanding sufficient to write some basic command line games such as _tic tac toe_ and _hangman_ and to code algorithm for quick, merge, bubble, insertion sorts. For example, here's the _tic tac toe_ game I wrote with pencil:

```python
# A game of Tic Tac Toe

from random import randrange

class TicTacToe():

    def __init__(self, choice):
        """define class attributes"""
        self.wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.moves = [" " for n in range(9)]
        self.player = choice
        self.oppnt = "X" if choice == "O" else "O"
        self.next = "X"
        self.end = False
        self.move = -1

    def turn(self):
        """alternate players"""
        self.next = "X" if self.next == "O" else "O"

    def display(self):
        """print board/moves"""
        print(f'\n\t{self.moves[0]}|{self.moves[1]}|{self.moves[2]}',
            f'\t{self.moves[3]}|{self.moves[4]}|{self.moves[5]}',
            f'\t{self.moves[6]}|{self.moves[7]}|{self.moves[8]}\n',
            sep='\n\t-----\n')

    def check(self):
        """check winning move/end game"""
        win = [self.next for n in range(3)]
        for w in self.wins:
            comb = [self.moves[w[i]] for i in range(3)]
            if " " in comb:
                continue
            if comb == win:
                if self.next == self.player:
                    print("You won.")
                else:
                    print("You lost.")
                self.end = True
                break
        if " " not in self.moves and not self.end:
            print("Game over. It's a tie.")
            self.end = True

    def first_move(self):
        """make initial move"""
        if self.player == "X":
            try:
                self.move = int(input("Make a move (0-8): "))
            except ValueError:
                print("Invalid! Must input an integer.")
                self.first_move()
            else:
                if self.move not in range(9):
                    print("Invalid! Number must be 0 <= n <= 8.")
                    self.first_move()
                else:
                    self.moves[self.move] = self.player
        elif self.player == "O":
            self.move = randrange(9)
            self.moves[self.move] = self.oppnt
        else:
            self.player = input("Invalid! Pick X or O: ").upper()
            self.first_move()
        self.display()
        self.turn()

    def next_move(self):
        """make subsequent moves"""
        if self.next == self.player:
            try:
                self.move = int(input("Make a move (0-8): "))
            except ValueError:
                print("Invalid! Must input an integer.")
                self.next_move()
        else:
            self.move = randrange(9)
        if self.move not in range(9) or self.moves[self.move] != " ":
                if self.next == self.player:
                    print("Invalid number or duplicate move!")
                self.next_move()
        else:
            self.moves[self.move] = self.next
            self.display()
            self.check()
            self.turn()

    def play(self):
        """play game/loop thru moves"""
        self.first_move()
        while not self.end:
            self.next_move()

# create instance of class and play game
game = TicTacToe(input("Pick which to play (X or O): ").upper())

game.play()
```

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

### Author

[![Chung Kao](./images/Chung_button.svg)](https://github.com/Sanlung)
