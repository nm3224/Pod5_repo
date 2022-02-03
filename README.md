# Pod Repo

# To do before each breakout session:

`git pull` on the **main** branch.
- To check which branch you are on, use `git branch`
- To change to main use, `git checkout main`.
- Then you can do `git pull`.

When you pull, you will get all the new files and changes made by our pod.
You will also be able to find the class challenges in the challenge folder.

# Make a copy of the challenge file

If there is a prewritten python file for the challenge, make a copy of it into your folder like this:

From inside the folder where the challenge file is:

`cp [FILE NAME TO COPY] [DESTINATION OF COPY]`

`cp temperature.py ../../serena_killion_folder`


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
