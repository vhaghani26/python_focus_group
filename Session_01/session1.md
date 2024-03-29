# Session 1: Getting Started

By: Viktoria Haghani & Osman Sharifi

Session Date: 2021-12-14

Last Updated: 2023-06-16

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Terminals

Modern bioinformatics primarily uses Unix or a Unix-based operating system. Navigating a command line requires you to know Unix commands. Unix language is used in a shell program, aka a terminal. Depending on a user's operating system (Windows, Mac OS, Linux), different steps must be taken to access a Unix-based terminal. Fortunately, both Mac OS and Linux use Unix-based terminals by default. Windows, on the other hand, requires a few extra steps. The native Windows command prompt (terminal) does not use the Unix language required by most software. This means that Windows users need to install a different terminal capable of using Unix. One of the most common terminals for download is the Linux distribution: Ubuntu. Use of Ubuntu requires enabling WSL1 or WSL2 (Windows Subsystem for Linux). Detailed instructions can be found using a simple search, but these are instructions that I find helpful for the [download of Ubuntu](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) and [enabling WSL2](https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/). 

## Opening the Terminal

### Mac OS

(1) Click the Launchpad icon in the Dock, type "Terminal" in the search field, then click "Terminal"
(2) In the Finder, open the /Applications/Utilities folder, then double-click "Terminal"
[Source](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)

### Linux

This may vary depending on the Linux distribution being used, but at its simplest, you can open the terminal by directly pressing ctrl+alt+T or searching it up by clicking the "Dash" icon, typing "terminal" in the search box, and opening the Terminal application.  
[Source](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955)

### Windows

Open the start menu and type "Ubuntu." Open the application. Using Ubuntu, you will be prompted to create an account requiring a username and password. The password is required at times for installing or updating software, so it is important to keep note of your password. 

## Using the Terminal

In order to use the terminal, you will need to use Unix-based language. At the end of this document, I will include a Unix cheat sheet for easy reference. For now, we will start with something basic. Try running the `pwd` command by typing `pwd` into the terminal and clicking "Enter" on your keyboard:

```
pwd
```

This command stands for "**p**rint **w**orking **d**irectory," and it does exactly that. Your terminal output should show the directory you are in. 

## Directories

Many Unix commands are named in a relatively straightforward way. Just like the `pwd` command, we can make a directory using the command `mkdir` which stands for "**m**a**k**e **dir**ectory." Let's practice navigating directories. First, we will make a new directory.

```
mkdir new_dir
```

This created a directory called `new_dir` in your profile. To enter this directory, we use the `cd` command, which stands for "**c**hange **d**irectory." 

```
cd new_dir
```

Now if we use `pwd`, it will show that you are in `new_dir/`. Note that directory notation typically uses forward slashes. Often times, we will have to navigate directories. Since we are in a child directory now, we are going to navigate back to your parent directory, aka the directory you were in before changing into `new_dir/`. To do this, we can use `..`, which is used to symbolize the parent directory/directory above where you are.

```
cd ..
```

Now try `pwd` again. You will see that we are in the original directory we started in. Note that when rerunning a command, there are two ways you can do it. The first is to manually retype the command. For short commands or commands that haven't been run very recently, this may be easier. However, for longer commands, you can use the up arrow on your keyboard to navigate the commands you previously ran. Try using your up arrow to see the commands you have run. When you get to `pwd`, run it and see that it will print your working directory again. Try using your up arrow one more time. Isn't it powerful? I think it's helpful!

## GitHub

If you plan on doing anything with bioinformatics in your career, you will need to add your GitHub account to your CV, and likely submit the link in job applications. GitHub helps log your code activity (how often you code and what you code) as well as provide a place to work on your code. If you keep your GitHub up to date, then you are able to work on the same code from any computer.

First, make sure that you have a GitHub account. Keep in mind that you will probably have to submit a link to your profile to someone down the line, so choose your username carefully. Please sign up for an account [here](https://github.com/join). Choose the free plan and answer whatever questions you are asked about your interests. Also make sure that you verify your email address. 

 Now, we are going to make a GitHub repository for your account. Repositories are essentially code projects, and they are commonly referred to as a "repo." Once you have an account, log in. We are now going to create a GitHub repo. If you look at the left-hand side of the page, there should be a menu bar. In that menu bar, you will have the option to create a new repository. Click "New."

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/new_git_repo.png)

This will take you to a new page that will prompt you to fill in some information about the repo you are creating. We will name the repo `python_focus_group`. Make the repository public since we are not working with any confidential data. This allows future employers to see the work that you have done. You should also add a `README.md`, which serves as a description of your repository. I like to set up my `README.md` as a table of contents so that if someone else is looking at the repository or if I look at an old repository, I know where I can find what I'm looking for. It is also useful to add a license. Following these steps should look like this:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/create_git_repo.png)

You've created a Git repo! Now, we will clone the repo, which essentially just means that we will create a local copy of the repo and its contents for you to work on. Click on your repo and navigate to the middle to right side of the page. You should see a green button that says "Code." Click on "Code." This will open a drop down menu with the top section being "Clone." In "Clone," there is a link to your repository. Copy that link.

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/git_clone_repo.png)

Open your terminal, and run the following command using **YOUR** link. It should look something like this:

```
git clone https://github.com/vhaghani26/python_focus_group.git python_focus_group
```

Enter your user information when prompted. This command means that we are creating the local directory, `python_focus_group` (which we specify at the end of the command), and cloning the contents of the GitHub repository into this local directory. You don't have anything in your GitHub repo at the moment, but this is important because it connects your local directory to GitHub. 

Please note that in rare instances, you may get an error, such as an [`xcrun` error](https://ma.ttias.be/mac-os-xcrun-error-invalid-active-developer-path-missing-xcrun/). I recommend searching the error verbatim and trying some recommended solutions. Often times, this will fix whatever errors you run into.

## GitHub Personal Access Tokens

As of the most recent update of this document, password usage at the command line has been completely replaced by the use of personal access tokens. Before moving on, let's create a GitHub personal access token. Please follow [these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for the **Classic Token**. Once it has been created, save it and use it in place of a password when you Git push.

Regarding the selected access options that pop up, I use the following and have yet to run into any hiccups:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/token_options.png)

Remember, this will now act as your password when you `git push` (but not when you log into GitHub online). 

## Files

Enter `python_focus_group/`. Remember that we can use the `cd` command to do this. The command should look like this:

```
cd python_focus_group
```

If you are changing directories constantly (which you will very likely do), it seems burdensome to type the directory name out every time. There is a lovely trick to manage this: tab complete. To test it out, leave `python_focus_group` and go back a directory. To do so, you can go to your home directory (if you made this directory in your home directory), like so:

```
cd ~
```

Or you can use the `..` notation to take you back a directory:

```
cd ..
```

Let's try getting back into `python_focus_group/`. Try typing `cd p` and then hitting the tab button on your keyboard. Assuming nothing else in your current directory starts with a p, it will automatically complete the rest of the statement for you. If you have other files or directories beginning with p, you can try adding another letter (`cd py`) and then trying tab complete again.

You should now be in `python_focus_group/`. How can you check? `pwd`! Once you start populating your directory with files, you can also use the `ls` command to list the contents of your current directory. This is extremely helpful when you want to see what's in your directory. Let's fill your directory!

Personally, I like having all my files organized. In this case, I would recommend making a subdirectory called `session_01`.

```
mkdir session_01
```

Now enter the directory (tab complete!).

```
cd session_01
```

There are several ways to create a file at the command line, but some of the easier ones include `touch` and `nano`. 

**(1) The `touch` command**

We are going to create a text file called `foo` at the command line. Note that the file extension for text files is `.txt`. Use the touch command to create the file:

```
touch foo.txt
```

To verify that the file has been made, list your directory contents:

```
ls
```

You should now see `foo.txt` in your directory.

**(2) The `nano` command**

Unlike the touch command, which just creates the file, `nano` gives you the ability to create and edit the file. Nano is a built-in text editor (albeit a terrible one) that you can use to edit your files at the command line. While it is easy for simple changes, it sucks. For this reason, people use their own text editors. We will learn how to download and use our own text editors in a future session, but we will use nano for today. Make a new file called `bar` using nano.

```
nano bar.txt
```

This changes the entire look of your terminal. Now you can change the contents of `bar.txt`. Type some random words or sentences into `bar.txt`. Note that cursors do not work in the command line, so you will need to use your keyboard to navigate. Use the arrow keys to move the cursor around. Add some text by typing. Remove some text with the delete key or backspace. At the bottom, you can see a menu that uses control keys. To save the file you hit the ^O key (command/control and then the letter o). You will then be prompted for the file name, at which point you can overwrite the current file (bar) by clicking "Enter" or make a new file with a different name. To exit nano, hit ^X. Note that you don't need to give nano a file name when you start it up. Also know that in Unix, file names do not have spaces in the names. Spaces are usually represented by underscores. Also, file names always display extensions (file types). 

Once you have some text in `bar.txt`, save and exit. Now we will edit `foo.txt`. Use nano to do so (tab complete!).

```
nano foo.txt
```

Add some text to `foo.txt`, save, and exit.

Since this directory is linked to GitHub, we are going to sync your local changes to your GitHub repository. Go to the main `python_focus_group` directory. If you did not make a `session_01` directory, then you should already be in it. If you did make it, go back a directory (Hint: `cd ..`). To see what is out of sync/what changes we have made, we can use the command:

```
git status
```

This should show that you have the directory `session_01` with `foo.txt` and `bar.txt` inside it. You can do the following to add a change to the GitHub repository:

```
git add --all
```

The `--all` flag syncs all changes, so everything you have done will be synced. Now we will commit the change:

```
git commit -m "initial commit"
```

The `-m` flag indicates a message, and the stuff inside the quotation marks is the message that gets displayed alongside your files so you can document what changes you made.

```
git push
```

This prompts you to enter your username and password, and it will sync all of your changes in your GitHub repository. Use the personal access token you set up earlier as the password. 

Congratulations! You pushed your files to GitHub. 

An alternative to pushing all changes at once is to do it manually with specific commit messages (this can be helpful). You can do it sequentially like so:

```
git add session_01/foo.txt
git commit -m "add foo.txt"
git add session_01/bar.txt
git commit -m "add bar.txt"
git push
```

This will prompt you to input your username and password. Now if you go to your GitHub repository from your internet browser and refresh it, you should see your updated repository and its contents! In general, the order of Git commands goes:

```
git add
git commit
git push
```

If you commit multiple changes, you can git push between everything or once at the end.



## Exit Ticket: `git_test.txt`

Create a file called `git_test.txt` in `session_01/`. You can edit it so it includes text or leave it empty. Once you have created the file, push it to GitHub. Do not read on until you have completed this.

### Solution

You will need to enter `session_01/`. Starting in `python_focus_group/`, the steps go as follows:

```
cd session_01
touch git_test.txt
cd ..
git add session_01/git_test.txt
git commit -m "practice pushing to GitHub"
git push
```

## Unix Cheat Sheet

Made by: Ian Korf

| Token   | Function
|:--------|:-------------------------------------|
| .       | your current directory (see pwd)
| ..      | your parent directory
| ~       | your home directory (also $HOME)
| ^C      | send interrupt signal to current process
| ^D      | send end-of-file character
| tab     | tab-complete names
| *       | wildcard - matches everything
| \|      | pipe output from one command to another
| >       | redirect output to file

| Command   | Example       | Intent                        |
|:----------|:--------------|:------------------------------|
| `cat`     | `cat > f`     | create file f and wait for keyboard (see ^D)
|           | `cat f`       | stream contents of file f to STDOUT
|           | `cat a b > c` | concatenate files a and b into c
| `cd`      | `cd d`        | change to relative directory d
|           | `cd ..`       | go up one directory
|           | `cd /d`       | change to absolute directory d
| `chmod`   | `chmod 644 f` | change file permissions 
|           | `chmod u+x f` | change file permissions
| `cp`      | `cp f1 f2`    | make a copy of file f1 called f2
| `date`    | `date`        | print the current date
| `df`      | `df -h .`     | display free space on file system
| `du`      | `du -h ~`     | display the sizes of your files
| `git`     | `git add f`   | start tracking file f
|           | `git commit -m "message"` | finished edits, ready to upload
|           | `git push`    | put changes into repository
|           | `git pull`    | retrieve latest documents from repository
|           | `git status`  | check on status of repository
| `grep`    | `grep p f`    | print lines with the letter p in file f
| `gzip`    | `gzip f`      | compress file f
| `gunzip`  | `gunzip f.gz` | uncompress file f.gz
| `head`    | `head f`      | display the first 10 lines of file f
|           | `head -2 f`   | display the first 2 lines of file f
| `history` | `history`     | display the recent commands you typed
| `kill`    | `kill 1023`   | kill process with id 1023
| `less`    | `less f`      | page through a file
| `ln`      | `ln -s f1 f2` | make f2 an alias of f1
| `ls`      | `ls`          | list current directory
|           | `ls -l`       | list with file details
|           | `ls -la`      | also show invisible files
|           | `ls -lta`     | sort by time instead of name
|           | `ls -ltaF`    | also show file type symbols
| `man`     | `man ls`      | read the manual page on ls command
| `mkdir`   | `mkdir d`     | make a directory named d
| `more`    | `more f`      | page through file f (see less)
| `mv`      | `mv foo bar`  | rename file foo as bar
|           | `mv foo ..`   | move file foo to parent directory
| `nano`    | `nano`        | use the nano text file editor
| `passwd`  | `passwd`      | change your password
| `pwd`     | `pwd`         | print working directory
| `ps`      | `ps`          | show current processes
|           | `ps -u ian`   | show processes user ian is running
| `rm`      | `rm f1 f2`    | remove files f1 and f2
|           | `rm -r d`     | remove directory d and all files beneath
|           | `rm -rf /`    | destroy your computer
| `rmdir`   | `rmdir d`     | remove directory d
| `sort`    | `sort f`      | sort file f alphabetically by first column
|           | `sort -n f`   | sort file f numerically by first column
|           | `sort -k 2 f` | sort file f alphabetically by column 2
| `tail`    | `tail f`      | display the last 10 lines of file f
|           | `tail -f f`   | as above and keep displaying if file is open
| `tar`     | `tar -cf ...` | create a compressed tar-ball (-z to compress)
|           | `tar -xf ...` | decompress a tar-ball (-z if compressed)
| `time`    | `time ...`    | determine how much time a process takes
| `top`     | `top`         | display processes running on your system
| `touch`   | `touch f`     | update file f modification time (create if needed)
| `wc`      | `wc f`        | count the lines, words, and characters in file f
