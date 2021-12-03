# Session 1: Getting Started

## Terminals
Modern bioinformatics primarily uses Unix or a Unix-based operating system. Navigating a command line requires you to know Unix commands. However, Unix language is used in a shell program, aka a terminal. Depending on a user's operating system (Windows, Mac OS, Linux), different steps must be taken to access a Unix-based terminal. Fortunately, both Mac OS and Linux use Unix-based terminals by default. Windows, on the other hand, requires a few extra steps. The native Windows command prompt (terminal) does not use the Unix language required by most software. This means that Windows users need to install a different terminal capable of using Unix. One of the most common terminals for download is the Linux distribution: Ubuntu. Use of Ubuntu requires enabling WSL1 or WSL2 (Windows Subsystem for Linux). Detailed instructions can be found using a simple search, but these are instructions that I find helpful for the [download of Ubuntu](https://www.windowscentral.com/install-windows-subsystem-linux-windows-10) and [enabling WSL2](https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/). 

## Opening the Terminal
### Mac OS
(1) Click the Launchpad icon in the Dock, type Terminal in the search field, then click Terminal  
(2) In the Finder, open the /Applications/Utilities folder, then double-click Terminal  
[Source](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)

### Linux
This may vary depending on the Linux distribution being used, but at its simplest, you can open the terminal by directly pressing ctrl+alt+T or searching it up by clicking the "Dash" icon, typing "terminal" in the search box, and opening the Terminal application.  
[Source](https://towardsdatascience.com/a-quick-guide-to-using-command-line-terminal-96815b97b955)

### Windows
Open the start menu and type "Ubuntu." Open the application. Using Ubuntu, you will be prompted to create an "account" involving a username and password. The password is required at times for installing or updating software, so it is important to keep note of your password. 

## Using the Terminal
In order to use the terminal, you will need to use Unix-based language. At the end of this document, I will include a Unix cheat sheet for easy reference. For now, we will start with something basic. Try running the `pwd` command:

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

Now try `pwd` again. You will see that we are in the original directory we started in. 

## GitHub
If you plan on doing anything with bioinformatics in your career, you will need to add your GitHub account to your CV, and likely submit the link in job applications. GitHub helps log your code activity (how often you code and what you code) as well as provide a place to work on your code. If you keep your GitHub up to date, then you are able to work on the same code from any computer.

First, make sure that you have a GitHub account. Keep in mind that you will probably have to submit a link to your profile to someone down the line, so choose your username carefully. Please sign up your account [here](https://github.com/join). Choose the free plan and answer whatever questions you are asked about your interests. Also make sure that you verify your email address. 

 Now, we are going to make a GitHub repository for your account. Repositories are essentially code projects, and they are commonly referred to as a "repo." Once you have an account, log in. We are now going to create a GitHub repo.

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/new_git_repo.png)

This will take you to a new page that will prompt you to fill in some information about the repo you are creating. We will name the repo `python_focus_group`. Make the repository public since we are not working with any confidential data. This allows future employers to see the work that you have done. You should also add a `README.md`, which serves as a description of your repository. I like to set up my `README.md` as a table of contents so that if someone else is looking at the repository or if I look at an old repository, I know where I can find what I'm looking for. It is also useful to add a license. Following these steps should look like this:

![github](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/create_git_repo.png)

You've created a Git repo!

## Files







## Tab Complete

## Rerunning Comands













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
