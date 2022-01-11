# Session 3: GitHub Desktop

By: Viktoria Haghani

Session Date: 2022-01-18

Last Updated: 2022-01-11

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

## Exit Ticket

Create another file called "second_practice.txt." You can leave this file empty or include some text in it. Using GitHub Desktop, write a commit message and push the file to your GitHub repo. 

Once you have pushed it, go to your GitHub repo online (i.e. using a browser) and verify that all your changes have correctly synced. 

Congratulations! You learned how to use GitHub Desktop! :)



