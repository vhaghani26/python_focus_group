# Session 2: File and Directory Manipulation in UNIX and First Python Script

By: Viktoria Haghani

Session Date: TBD
Last Updated: 2021-12-16

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## File and Directory Manipulation

A common occurence you will experience is reorganization. Here, we will explore how to handle different types of file and directory manipulation techniques at the command line.

### Renaming a Directory

First, we will create a new directory for `session_02/` in `python_focus_group`. Let's make a new directory:

```
mkdir sessin_02
```

Oh no! You typed too quickly and have a typo. Now you have a directory called `sessin_02/` instead of `session_02/`. Luckily, UNIX has an extremely useful command: `mv`. The `mv` command allows us to **m**o**v**e and rename files. Typically, the `mv` function looks something like this:

```
mv <source> <target>
```

Where `source` represents the thing that currently exists in your directory (this can be a file or directory) and `target` represents what you are renaming or moving a file/directory to. Make sure you are in the parent directory containing whatever file or directory you want to rename. In our case, the parent directory we should be in is `python_focus_group/`. Now, we can rename our directory. First, let's see what `python_focus_group/` contains. Remember that you can do this using the `ls` command. Once you verify that you can see `sessin_02/`, carry out the following command:

```
mv sessin_02 session_02
```

If you use `ls` again, you will now see that `sessin_02/` has been renamed `session_02`.

## Renaming a File

Here, we will practice renaming a file. Enter `session_02/`.

```
cd session_02
```

Create a file called `first_python_script.py`. You can do this using either `touch` or `nano`. Since we are not editing the file yet, `touch` will be your simpler option. 

```
touch first_python_script.py
```

In hindsight, we realize we should make the file name represent what the code does. Using the `mv` command, we can rename the file:

```
mv first_python_script.py hello_world.py
```

Using `ls`, you can see that the file has been successfully renamed! We will come back to this file later.

## Moving Files

Another useful thing to do at the command line is to move files. This is especially helpful if you decide to reorganize your directories. Starting from `python_focus_group/`, **m**a**k**e a new sub-**dir**ectory called `practice`. You should now be familiar with how to make a directory, but please let Viki know if you need a refresher or see the [notes](https://github.com/vhaghani26/python_focus_group/blob/main/Session_01/session1.md) from Session 1. Enter `practice/` and make two more directories within practice: `dir1` and `dir2`.

We will practice moving files between directories. Enter `dir1/` and create a file called `file1.txt`. Exit the directory (i.e. return to `practice/`). Using the `mv` command, we can move the file to `dir2/`. This uses the same `source` and `target` formatting I introduced earlier:

```
mv dir1/file1.txt dir2/file1.txt
```

Now if you enter `dir1/` and check the directory contents, it will be empty. On the other hand, `dir2/` will contain `file1.txt`. 

**Exercise**: Create a file called `file2.txt` in `dir2/`, then move that file from `dir2/` to `dir1/`. Do not move on until you have succesfully completed this.

## Moving Directories

Moving directories is slightly more complicated than moving files since directories often contain other files and subdirectories. The main difference here is that we need to use a command line option (aka flag). The command we will use will look like this:

```
mv -r <source> <target>
```

The `-r` flag represents "**r**ecursively." Essentially, we are telling our terminal to recursively move a directory somewhere else. The "recursive" part of this means that we are moving the contents within the directory along with the directory we are moving.

In `practice/`, create a subdirectory called `dir1A`. Within `dir1A/`, create the following files: `samp1.txt`, `samp2.txt`, `samp3.txt`. 

Now we will move `dir1A/` and its contents into `dir1/`. To do so, we run this command while in `practice/`:

```
mv -r dir1A/ dir1/dir1A
```

If you enter `dir1`, and check the directory contents (hint: `ls`), then you should see `dir1A/` within `dir1`. Enter `dir1A/` and check the directory contents. You should see your sample text files here.

## Copying Files

Copying files can be convenient for a number of reasons, including wanting to manipulate a file but keeping the original version for reference. There are a few ways this can be done. In this example, we will be using the `cp` command, which stands for "**c**o**p**y."

Enter `dir2/` and create a subdirectory `dir2A/`. We are going to copy all of the text files from `dir1A/` into `dir2A/`. Remember that when you are manipulating files and directories, you need to be in the parent directory that contains all of the contents you are moving and their desired locations. In our case, this means we can be in `practice/`. Enter `practice/` and carry out these commands:

```
cp dir1/dir1A/samp1.txt dir2/dir2A/samp1.txt
cp dir1/dir1A/samp2.txt dir2/dir2A/samp2.txt
cp dir1/dir1A/samp3.txt dir2/dir2A/samp3.txt
```

### Wildcards at the Command Line

Notice that this is tedious. You don't want to do this manually for several files. To address this issue, we can use wildcards. At the command line, `*` is the wildcard symbol. Since all of the files we want to copy are text files, we can represent the prefix of the text files using `*`. This would look like:

```
cp dir1/dir1A/*.txt dir2/dir2A/
```

Since the "samp" part is the same, you can alternatively use:

```
cp dir1/dir1A/samp*.txt dir2/dir2A/
```

As I mentioned earlier, there are multiple ways you can do this. You can also do something similar to the `mv -r` command for `cp`, where you copy files and directories recursively: `cp -r`. These commands are helpful to know, but recall that Google is your best friend with Unix commands. If you forget how to do something or want to figure out how to do something, Google it! I often find myself Googling things like: "how to move directory and its contents unix," and that's totally okay! 

## Deleting Files

Deleting files is another helpful thing that we can do. We went through this in Session 1 briefly, but we will review it again here. We can **r**e**m**ove files using `rm`. 

Enter `dir1A/` and delete the file `samp1.txt`.

```
rm samp1.txt
```

If you check the directory contents, you will now only see `samp2.txt` and `samp3.txt` left. You can also use the wildcard symbol to delete multiple files:

```
rm *.txt
```

Now `dir1A/` should be empty.

## Deleting Directories

Since all of the content in `practice/` was just for UNIX practice, but it does not have anything useful to look at, we will delete the directory. We can use the `-r` option to delete a directory and all its contents. Remember that we need to be in the parent directory containing `practice/` to carry out this command:

```
rm -rf practice/
```

Now if you check the contents of `python_focus_group`, you will no longer have `practice/`.

Note: Be VERY careful when removing files and directories, as you will not be able to undo this operation once it has been carried out.








## Linking Files & Directories

## File Permissions










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

## Verify Python Installation

Once you have installed Python, verify that you have installed it by running the command:

```
python --version
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

```
print("My name is Viki")
print("I have many pets")
print("I enjoy learning Python!"
print('Here I am using single quotation marks')
```

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

Congratulations! You wrote your first Python script! Go back to the `python_focus_group` directory, then push it to GitHub.

```
git add session_01/hello_world.py
git commit -m "prints hello world"
git push
```

## Exit Ticket: Update `README.md`

In your main `python_focus_group` directory, you should have a file called `README.md`. Your assignment is to navigate to the file and edit it to reflect the content in your repository, then Git push it. An example of the text you can include is:

```
This repository is for the LaSalle Lab Python Focus Group, where we are learning how to code using Python.

# Session_01
foo.txt: A file containing random phrases that was created using `touch`
bar.txt: A file containing random phases that was created using `nano`
git_test.txt: An empty file created to practice pushing files to GitHub

# Session _02
hello_world.py: A Python script that prints "Hello, World!" when run
```

Note that since the file extension is `.md`, a markdown file, it is written in markdown language. For the most part, you can just use text. However, if you want to make it fancy, you can include things like bolded text, headings, and code blocks. This document is actually written in [markdown](https://www.markdownguide.org/basic-syntax/). In the above example, the `#` in front of `Session_01` indicates that that line is a heading. This is not necessary, but it does look organized. If you do not want to have `Session_01` as a heading, simply remove the `#` in front of it.

### Solution

Assuming you start in `session_02`, you can carry out the following:

```
cd ..
nano README.md
# Edit and save the file
git add --all
git commit -m "finish session 2 work"
git push
```

Congratulations! You finished Session 2!