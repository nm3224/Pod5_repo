# Converting temperatures

<img src="https://storage.googleapis.com/ltkcms.appspot.com/fs/yd/images/cover/thermometer-in-snow.base?v=1591222156" width="650">

## Setup
In your personal folder inside your pod git repo, make a script called `temperature.py` and run it using `python3 temperature.py` to verify you get the expected output.

### The formula for converting between fahrenheit and celsius is to first subtract 32, then multiply by 5/9. Can you do the following in python?

1. Convert a temperature of 100 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_100`, and use `print()` to print out the value
    * Is the resulting temperature you get an integer or float? How do you know?
2. Convert a temperature of 0 degrees fahrenheit to celsius
    * Save this to a variable called `celsius_0`, and use `print()` to print out the value
3. Convert a temperature of 34.2 degrees fahrenheit to celsius
    * Do this one all in one print statement **without** saving any variables


### Now, can you convert back?

4. Convert a temperature of 5 degrees celsius to fahrenheit?
5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?


### Make sure everything is documented!

6. If you haven't already, go through your script and add a comment for questions 1-5 explaining what your code is doing.

### Awesome job! Now, add, commit, and push your completed script to your pod Github repo on your branch, then submit a pull request

Remember, you'll do this from the command line. First

Make sure you're on your branch
```console
$ git checkout -b <your-branch-name>
```

Then add:
```console
$ git add temperature.py
```

Then commit to take a 'snapshot':
```console
$ git commit -m 'add temperature.py challenge'
```

Then push to GitHub!

```console
$ git push
```

Now, go to your pod github repository and make sure the changes have been pushed correctly to your branch, then submit a pull request!

**Congrats, challenge complete!!**
