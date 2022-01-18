# Session 2: File and Directory Manipulation in UNIX and First Python Script

By: Viktoria Haghani

Session Date: 2022-01-11

Last Updated: 2022-01-18

Session Recording: https://www.youtube.com/watch?v=OItmKM8uuyI

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## A Brief Note: Months of Mistakes

Before we begin this session, I'd like to note that although this is the *Python* Focus Group, there are many housekeeping things that we can or need to do to effectively program. When I began learing Python, I used very basic tools with little understanding of the tools I had at my disposable. I used `nano` for months (disgusting!) and did all of my directory setup incorrectly. This meant that when I finally realized my big error, it was a conglomeration of several smaller mistakes, forcing me to delete all my work and start my setup from scratch. My goal here is to make your learning experience better. I want you to be aware of the tools you can utilize as well as understanding how incrediblly helpful some of these tools are. Therefore, the first few sessions may not be the *most* interesting or *most* helpful with learning Python coding directly, but it is a necessary step to get to the point of efficient coding. Your setup and organization is as instrumental as the code you will write one day.

## File and Directory Manipulation

A common occurence you will experience is reorganization. Today, we will explore how to handle different types of file and directory manipulation techniques at the command line.

## Renaming a Directory

First, we will create a new directory for `session_02/` in `python_focus_group`. Let's make a new directory:

```
mkdir sessin_02
```

Oh no! You typed too quickly and have a typo. Now you have a directory called `sessin_02/` instead of `session_02/`. Luckily, UNIX has an extremely useful command: `mv`. The `mv` command allows us to **m**o**v**e and rename files. Typically, the `mv` function looks something like this:

```
mv <source> <target>
```

Where `source` represents the thing that currently exists in your directory (this can be a file or directory) and `target` represents what you are renaming or moving a file/directory to. Make sure you are in the parent directory containing whatever file or directory you want to rename (note that you can avoid this using `..` in your paths, but we will use these steps for simplification). In our case, the parent directory we should be in is `python_focus_group/`. Now, we can rename our directory. First, let's see what `python_focus_group/` contains. Remember that you can do this using the `ls` command. Once you verify that you can see `sessin_02/`, carry out the following command:

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

Moving directories is similar to moving files. We will use the `mv` command. In `practice/`, create a subdirectory called `dir1A`. Within `dir1A/`, create the following files: `samp1.txt`, `samp2.txt`, `samp3.txt`. Now we will move `dir1A/` and its contents into `dir1/`. To do so, we run this command while in `practice/`:

```
mv dir1A/ dir1/dir1A
```

If you enter `dir1`, and check the directory contents (hint: `ls`), then you should see `dir1A/` within `dir1`. Enter `dir1A/` and check the directory contents. You should see your sample text files here.

## Copying Files

Copying files can be convenient for a number of reasons, including wanting to manipulate a file but keeping the original version for reference. There are a few ways this can be done. In this example, we will be using the `cp` command, which stands for "**c**o**p**y."

Enter `dir2/` and create a subdirectory `dir2A/`. We are going to copy all of the text files from `dir1A/` into `dir2A/`. Remember that when you are manipulating files and directories, it is helpful to be in the parent directory that contains all of the contents you are moving and their desired locations. In our case, this means we can be in `practice/`. Enter `practice/` and carry out these commands:

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

Since the "samp" part is the same, you can alternatively use the following to be a little more conservative:

```
cp dir1/dir1A/samp*.txt dir2/dir2A/
```

As I mentioned earlier, there are multiple ways you can do this. Recall that Google is your best friend with Unix commands. If you forget how to do something or want to figure out how to do something, Google it! I often find myself Googling things like: "how to move directory and its contents unix," and that's totally okay! 

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

Note: Be **VERY** careful when removing files and directories, as you will not be able to undo this operation once it has been carried out.

## Linking Files & Directories

Linking (aka aliasing) files or directories is an extremely powerful tool. Let's say I downloaded and processed the entire human genome as a reference file on epigenerate and now someone else wants to use it. Instead of copying the whole file into their directory to work with, they can create a symbolic link to the file within their own directory. This allows them to use/access the file or directory without taking up any extra space - especially for such a large file! The **l**i**n**k command, `ln`, allows us to do this. Before we get started, there are a few things that may be helpful to explain. First, when we use the command, it will generally look like this:

```
ln -s <original file> <link to file>
```

Second, we will always use the `-s` option when using `ln`. `-s` represents that the link is "symbolic," which means that it creates a soft link rather than a hard link. A **soft link** is equivalent to a shortcut in Windows, or rather a redirection to the original location and file. A **hard link**, on the other hand, associates two files (which may have different names) to the same file information. We don't want hard links; we only want to use soft links, hence our strict use of `ln -s` instead of *just* `ln`.

Now let's practice creating a link. In `session_02/`, create a subdirectory called `linked_file`. In `session_02/`, create a file called `original_copy.txt`. Then, enter `linked_file/` and create a symbolic link to `original_copy.txt` that is called `linked_to_original_copy.txt`. To do so, we can use the following command:

```
ln -s ../original_copy.txt linked_to_original_copy.txt
```

The `..` in the above command tells the terminal to go up a directory. Since we are in `linked_file/` and we want to go back up to `session_02/`, we can use the `..` to accomplish this. The command essentially means we are linking the file `original_copy.txt` found in the directory above ours to a new "file" we are calling `linked_to_original_copy.txt`. Notice that if you use `ls`, the file will have `@` next to it. This tells us that it is a link.

Once you have created a linked file, edit `original_copy.txt` to include some sort of words or phrases and save it. Then, view the contents of `linked_to_original_copy.txt`. Notice that you see the same text you input in `original_copy.txt`. 

Because this is just practice with no content, feel free to remove `linked_file/` and `original_copy.txt`.

## File Permissions

This section is adapted directly from Ian Korf.

While file permissions may not affect daily work, it is still important to know and understand. A file can have 3 kinds of permissions: read, write, and execute. These are abbreviated as `rwx`. Read and write are obvious, but execute is a little weird. Programs and directories need executable permission to access them. Generally, you want read and write access to the files you create. However, if you have some incredibly important data file, you might want to protect it from being edited, so you may want to remove write permission and make it read-only.

In addition to having 3 types of permissions, every file also has 3 types of people that can access it: the owner (you), the group you belong to (e.g. a laboratory), or the public. For the purposes of learning how to program, we can treat these all the same. However, you can imagine that some files should not be readable by others (for example, your private poetry efforts). Navigate into `session_02` and examine the file permissions on `hello_world.py`, the script we will be editing shortly. 

```
ls -lF hello_world.py
```

This will produce something like the following.

```
-rw-r--r--  1 vhaghani  vhaghani     0 Dec 16 13:56 hello_world.py
```

After the leading dash, there are 3 triplets of letters. The first triplet shows user permissions. In the example code above, you should see that I have read and write permissions, but not execute. The next triplets are for group and public. Both have read permission, but not write or execute. Let's first turn on all permissions for everyone using the `chmod` command and then list again.

```
chmod 777 hello_world.py
ls -lF hello_world.py # Remember you can use your up arrow to rerun previously run commands
```

Notice that you can now see `rwx` for owner, group, and public.

```
-rwxrwxrwx  1 vhaghani  vhaghani     0 Dec 16 13:56 hello_world.py*
```

There is also an asterisk after the program name indicating that the file is now executable. The `-F` option in `ls` shows you what kind of file something is with a trailing character. If the file is a directory, there will be a trailing `/`.

You won't need to get complicated with permissions. This is just a helpful tidbit of information that may be useful one day. The following 3 are all you need right now.

* `chmod 444` file is read only
* `chmod 666` file may be read and edited
* `chmod 777` file may be read, edited, and used as Unix command

Furthermore, the `chmod` command has two different syntaxes. The more human readable one looks like this.

```
chmod u-x hello_world.py
ls -lF hello_world.py
```

The above command says: "change the user (u) to remove (-) the execute (x) permission from file hello_world.py". You add permissions with +, like so:

```
chmod u+x hello_world.py
ls -lF hello_world.py
```

The less readable `chmod` format is assigning all parameters in octal format. 4 is the read permission. 2 is the write permission. 1 is the execute permission. Each rwx corresponds to one octal number from 0 to 7. So `chmod 777` turns on all permissions for all types of people and `chmod 000` turns them all off.

You will not use this frequently, but it is here for your reference if need be.

Congratulations! You finished Session 2!