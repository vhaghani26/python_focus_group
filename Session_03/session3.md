# Session 3: GitHub Desktop

By: Viktoria Haghani

Session Date: 2022-01-18

Last Updated: 2022-01-18

Session Recording: TBD

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Introduction to GitHub Desktop

Up to now, we have done all of our GitHub work at the command line. Fortunately, there is an easier way to push things to GitHub. Now you may be thinking, "if there's an easier way, why are you being cruel and making me use the command line instead?" Rest assured; there is a good answer! 

Any remote work, such as using the cluster (i.e. epigenerate) cannot work with GitHub Desktop. This means that further down the line if/when you begin doing more computationally and resource heavy work, you will **need** to rely on command-line GitHub commands. You will not have the nice option of using GitHub Desktop. However, now that you should be comfortable with the command line method of Git pushing, we're going to make your life easier.

GitHub Desktop is a software that can be downloaded on your personal laptop/computer that can help manage your GitHub repositories. It's both visually appealing and mouse-friendly! We're going to have to do some set up and clean up stuff here, so bear with me as we work through this.

## Installing GitHub Desktop

First, we're going to install GitHub Desktop. There are some great instructions [here](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop) (albiet specific to Windows) on how to install it, but we will run through it together. First, visit the download page for GitHub Desktop. You will notice a link towards the bottom that says "Download for macOS." Click it and download the software.

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/gitdesktop_install.png)

Double-click the GitHub Desktop setup file (it usually defaults to the "Downloads" folder if you did not specify otherwise). Go through the on-screen instructions, which include setting up the software and logging into your GitHub account on the app.

## Cleaning Up Previous Work

GitHub Desktop will ask you about cloning repositories. **Before** you proceed, we have some cleanup to do. If you created `python_focus_group/` on the cluster somewhere, then DO NOT do the clean-up portion. Instead, practice creating a local copy for editing (next section). If you only have a local copy, then we're going to go through these steps.

GitHub Desktop puts your repositories in a folder called "GitHub," which is typically a sub-folder in "Documents." Because we don't want two local copies, we will delete the old copy and clone the repository through GitHub Desktop. First, navigate to wherever your original **local** copy of `python_focus_group/` is. Enter the directory and verify that all your changes are synced with GitHub:

```
git status
```

If you do not have the all clear, sync whatever remaining changes you may have:

```
git add --all
git commit -m "sync all local edits"
git push
```

Remember you might have to use your Personal Access Token during the above step. 

If GitHub gives you the all clear that everything is synced, go to the parent directory of `python_focus_group/` (likely just your home directory). You should know how to do this by now! Just in case, I'll put a reminder here:

```
cd ..
```

Note that this will be the last time I remind you about navigating up a directory, so be sure to remember, keep Google at your ready, or have an old session's notes open for reference. 

Now, verify that you are in the parent directory by listing the directory contents.

```
ls
```

You should see `python_focus_group` listed here. Since all your changes are synced, we are going to delete this local copy:

```
rm -rf python_focus_group
```

Recall that you can tab complete so you don't have to type out "python_focus_group" for this command. Since you are running a remove command, make sure to double check the command before you click enter and delete something you didn't intend to. If you have typed it correctly, pull the trigger and delete the folder.

## Cloning through GitHub Desktop

Go back to the GitHub Desktop app. Under the "File" menu tab, you should see an option to clone a repository. If you have nothing set up on GitHub Desktop yet, you will likely have a different home screen than depicted below. This should also give you the option to clone a repo.

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/clone_repo_gitdesktop.png)

Once you click "Clone a repository," you will be taken to pop-up window (see image below) that asks you which repository you would like to clone in addition to what local path it stores that repository in. Even though you can change the local path, bioinformatics uses a lot of "behind the scenes" paths and defaults. I've found that if you change locations of things manually, it tends to give you issues with other things down the line, so it's best to just accept and download into the default location.

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/choose_repo.png)

Select the `python_focus_group` repository and click the "Clone" button at the bottom. Because we don't have much in our repository, it will probably take less than a minute to download and sync. Using the file finder, you can now navigate to the repository and its see its contents.

Note that you can now create and manipulate files using the file finder instead of the command line. For our Python Focus Group, we will still be using the command line for these things. There is, however, a method to the madness: (1) if you do any work on the cluster, you no longer have the ability to use a file finder or similar file visualization program, so you need to know how to use the command line to manipulate files, (2) you will get to a point where you run scripts that are automated and run commands from within the script, so knowing the commands is extremely useful, and (3) command line file manipulation can make your life a lot easier in many instances (wildcards being an example), so it will help save you time and energy down the line when you do more complicated work.

## Interacting with the GitHub Repo at the Command Line

Since our goal is to run Python scripts from this repository, we need to find the directory at the command line. Return to your terminal and try to find the repository. If you're having trouble, you can use `ls` as you navigate through different directories until you find it. Most often, it will be in whatever parent folder contains `Documents/`, so it will end up looking like: `Documents/GitHub/python_focus_group/`. If you cannot find it, please let Viki know. 

Enter `python_focus_group` and create a new sub-directory called `session_03`. Enter `session_03/` and create a new file called `github_desktop_practice.txt` and put some comments in it:

```
nano github_desktop_practice.txt
```

In mine, I will write:

```
I am creating this file to demonstrate how to push something to GitHub Desktop
```

Save and close the file.

## Pushing to GitHub from GitHub Desktop

Open GitHub Desktop, ensuring that you are looking at your `python_focus_group` repository (check the top left corner). You should now see that GitHub Desktop automatically detected that you created a new file. It will display additions to the file in green highlighting and deletions in red highlighting as a way for you to track your changes.

Remember that the normal process of Git pushing looks like this:

(1) `git add Session_03/github_desktop_practice.txt`

(2) `git commit -m "practice using github desktop"`

(3) `git push`

Well, GitHub Desktop makes these steps a lot easier. To add something to GitHub, you just check the box for the file(s) you want to sync:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/git_add.png)

Once you have selected your files, you type the message you would normally type for the `git commit` command in the following text box:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/git_commit_1.png)

Then, you register that you want to add that change as a commit:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/git_commit_2.png)

Now you push the commit through! You can do this using the menu at the top or using the button on the main screen:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/git_push.png)

## GitHub Desktop Exercise

Create another file called "second_practice.txt." You can leave this file empty or include some text in it. Using GitHub Desktop, write a commit message and push the file to your GitHub repo. 

Once you have pushed it, go to your GitHub repo online (i.e. using a browser) and verify that all your changes have correctly synced. 

Congratulations! You learned how to use GitHub Desktop! :)

## Installing Python

Now that we have set up GitHub and made some files, we are going to try making our first Python script. This requires us to install Python. Based on your operating system, the instructions for installation vary. I have included some helpful sources that will walk you through how to install Python. For those of you who already use Python or are doing this in `spitfire` or `epigenerate`, you can use the command `module load anaconda3` to load Python.

**Note for Cluster Users**: The default version of Python in the cluster is OLD, so you need to specify `anaconda3` so you are using Python 3 instead of Python 2 (the default). 

### Mac OS
[How to Install Python3 on Mac](https://www.youtube.com/watch?v=0hGzGdRQeak) (I recommend this source, as it's easier to follow and requires less command-line knowledge)

[Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

### Linux
[Installing Python 3 on Linux](https://docs.python-guide.org/starting/install3/linux/)

### Windows
[How to Install Python 3 on Ubuntu 18.04 or 20.04](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)

## Verifying Python Installation

Once you have installed Python, verify that you have installed it by running the command:

```
python --version
```

In some cases, you may have to use the following instead:

```
python3 --version
```

If you receive an output with a version number, ideally 3.10.1, then you have succeeded! If not, pause and ask Viki to help you with the installation.

## Python at the Command Line

Let's run our first Python command! To activate Python, run the command:

```
python3
```

Now, you should be able to run Python code at the command line. As any experienced coder knows, "Hello, World!" is where we'll start. This is just a convention people go by when unning their first line of a new language. Here is [The History of Hello World](https://www.thesoftwareguild.com/blog/the-history-of-hello-world/) for those who are interested. Let's run the command:

```
print("Hello, World!")
```

Your terminal should print back, "Hello, World!" Congratulations! You ran your first Python command! `print()` is one of the most widely used functions, and thus presents a good place to start. We will discuss how functions work in more depth later, but for now, I will explain briefly. A function looks something like this: `function()`, where the function name is outside of the parentheses, and the parentheses are there to take arguments. An argument is something you give a function as an input. In this case, our function is `print`, and our argument (input) is "Hello, World!". Try printing your name! In my case, it would look like this:

```
print("Viki")
```

Note that `print(Viki)` does not work, as the absence of quotation marks interprets "Viki" as a variable (we will learn more about variables in the future). Try a few more commands and see what you can do! Note that you can also use single quotations to print as long as the quotations marks flanking the statement are the same style (single vs. double).

```print("My name is Viki")
print("I have many pets")
print("I enjoy learning Python!")
print('Here I am using single quotation marks')```

Now try running this:

```
print('I don't want to do anything today')
```

This will give you an error because you have three single quotation marks and `print()` can't understand what you're trying to print. So how do we deal with this? There are a few ways we can do this. 

(1) Use single quotes to print double quotes

```
print('Whenever I get home, I walk up to my iguana's cage and say, "What are you doing, Stella?"')
print('She said her name was "Viki"')
```

(2) Use double quotes to print single quotes (this is useful for using apostrophes) 

```
print("You shouldn't need to worry about using apostrophes since you can use double quotes")
```

There are very rare instances that these two methods will not work for you, and in those cases, you can try some of the other methods listed [here](https://www.kite.com/python/answers/how-to-print-quotation-marks-in-python). Personally, I have never run had to use a different method from the ones above.

To exit the Python prompt, type:

```
exit()
```

Notice that the parentheses after `exit`. This means that `exit()` is a function. You should be back in your normal terminal now where you can run Unix language. 

## Python Scripts

The majority of the time, you will be running Python scripts, not command line Python. Navigate to your `session_01` directory (you should know how to do this now, but please ask if you are still confused). Using `nano`, edit the `hello_world.py` file we created earlier.

```
nano hello_world.py
```

Make sure that whatever you name your file has the `.py` file extension at the end. This indicates that the content in this file is Python code. In the file, include the following text, save, and exit:

```
#!/usr/bin/env python3

print('Hello, World!')
```

Line 1 is what's known as an interpreter directive. It's also sometimes called a hashbang. It tells the shell which interpreter to use when the program executed. Line 2 is a blank line. Use blank lines to separate thoughts from each other. The hashbang is one such thought and the other is a print statement. Blank lines do not do anything in scripts, but they are helpful for organization. Line 3 prints 'hello world to the terminal. Now let's try running the command from the shell.

```
python3 hello_world.py
```

If everything worked okay, you should see "Hello, World!" in your terminal. If not, don't go on. Ask for help fixing your computing environment.

Congratulations! You wrote your first Python script! Go back to the `python_focus_group` directory, then push it to GitHub using the terminal commands you see below or using GitHub Desktop.

```
git add session_02/hello_world.py
git commit -m "prints hello world"
git push
```

## Exit Ticket: Update `README.md`

In your main `python_focus_group` directory, you should have a file called `README.md`. Your assignment is to navigate to the file and edit it to reflect the content in your repository, then Git push it. An example of the text you can include is:

```
This repository is for the LaSalle Lab Python Focus Group, where we are learning how to code using Python.

## Session_01
foo.txt: A file containing random phrases that was created using `touch`
bar.txt: A file containing random phases that was created using `nano`
git_test.txt: An empty file created to practice pushing files to GitHub

## Session _02
NA; worked on UNIX commands only

## Session_03
hello_world.py: A Python script that prints "Hello, World!" when run
```

Note that since the file extension is `.md`, a markdown file, it is written in markdown language. For the most part, you can just use text. However, if you want to make it fancy, you can include things like bolded text, headings, and code blocks. This document is actually written in [markdown](https://www.markdownguide.org/basic-syntax/). In the above example, the `##` in front of `Session_01` indicates that that line is a heading. This is not necessary, but it does look organized. If you do not want to have `Session_01` as a heading, simply remove the `##` in front of it.

### Solution

Assuming you start in `session_03/`, you can carry out the following:

```
cd ..
nano README.md
# Edit and save the file
git add --all
git commit -m "finish session 3 work"
git push
```