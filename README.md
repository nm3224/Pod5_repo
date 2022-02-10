# Pod5_repo
Pod Test Repo

Now that you have created your own repo and you'll now learn how to do git collaborations. Inside this repo, each of you will see a directory in your name. This is where you will now submit your completed challenges. Below is the set of instructions on how to do this and best practices.
Keep up the great work. I am happy to be a part of your journey!

## To do before each breakout session:
- `git status` to check if you are on the **main** branch.
- If you are not on the main branch, run the command `git switch main`
- `git pull` on the **main** branch.

### Make a copy of the challenge file:

When you pull, you will get all the new files and changes made by our pod.
You will also be able to find the class challenges in the challenge folder.

If there is a prewritten python file for the challenge, make a copy of it into your folder like this:

From **inside the folder where the challenge file is--this may require cd-ing into the folder: ex. `cd week_2`**:

`cp [FILE NAME TO COPY] [DESTINATION OF COPY]`

`cp temperature.py ../serena_killion_folder`

This should create a copy of the file you were working on inside your name folder.
Double click your name folder and open the copy. **Continue working on the challenge in this file--not the one inside the week folder.**

# To do after you complete your challenge:

**Please do not push on main!**

Create your own branch. A good branch name should describe be description.
for our purposes, using your name and the challenge name is sufficient.
For example: `serena-temperature`

- `git checkout -b [YOUR_BRANCH_NAME]` --> `git checkout -b serena-temperature`
- `git status` -> check for new or modified files
- `git add [FILE NAME]` --> add file so git will track it
- `git commit -m "YOUR_COMMIT_MESSAGE"` --> commit file to git
- `git push` --> push it to the repo

- Now go to your pod's repo on GitHub.com and find the button to create a pull request.
- Make sure your base is **your pod's repo** (for example: `pod5_test_repo`) and **not** `Justice-Through_Code/pod_test_repo`
- Give a short description of your code and any questions you might have
- Create Pull Request

Your T.A will review your pull request, make any comments, and merge into the pod repo!

Quick CheatSheet:
chdir == returns your current directory location
dir === listing out what's in your working directory
cd == change directory
cd.. == hop out of directory to previous directory
md == make directory
type == printcd

# CHECK WHICH PYTHON COMMAND LINE 
- To check what to use on your command lines for running .py files
- Ff you are using a mac, it should be `python3`. 
- For windows 11, it should be `py`. 
- If these don't work--run `python -v` to check if the version is 2.7 or 3.8. 
- If it's 2.7, then use python3 -v to see if there is a new version of python available, and if it returns a newer python version, then the command should be `python3`. 
- If it's 3.x.x, then the command is `python`
