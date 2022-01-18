# Session 4: Text Editors

By: Viktoria Haghani

Session Date: 2022-01-11

Last Updated: 2022-01-10

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Text Editors

### Introduction to Text Editors

A text editor is a type of computer program/software application that allows you to edit code as plain text files. It acts similar to editing a Word document, but for code. Rather than using `nano`, which requires the use of the keyboard only, text editors allow you to navigate with your mouse, copy and paste easily, and move code around in a much more human friendly way. Therefore, it's time for us to stop using `nano`. 

### Choosing a Text Editor

All of the files you have been editing with `nano` up to this point could have been edited with a text editor, such as: Atom, BBEdit, Geany, Gedit, Jedit, Notepad++, Sublime, VS Code, etc. So which programming/text editor should you use? It depends. According to Ian Korf, "Whatever is installed by default in your Linux distribution should be fine. I use Geany on Linux, BBEdit on Mac, and Notepad++ on Windows." As a Windows user myself, I'm a big fan of Notepad++. Since most (if not all) of you are Mac users, BBedit is a great option. 

### Installing Your Text Editor

As much as I'd love to provide more concrete instructions here, your text editor choice may be different. For the purposes of this tutorial, I am going to run through setting up BBEdit. I'd like to quickly note that I am not at all familiar with the use of BBEdit and Mac-based text editors. I will try my best to give you straightforward instructions, but I am relying heavily on external resources for guidance. 

If you have chosen to proceed with a different text editor, please carry out the installation and set up on your own at this time. If you have any questions, please feel free to ask and we can explore or troubleshoot together.

#### Setting Up BBEdit

[BBEdit](https://www.barebones.com/products/bbedit/download.html) is one of the leading text editors for MacOS. Although there is a paid version, the free version is sufficient for most (and probably all) of what you will need to do. First, you will need to go to your browser and search "BBEdit" and click on the first link. As of the day I am making this, the first link should be "BBEdit 14 - Bare Bones Software." Click on the link, and then navigate to the right hand side of the page where there is a "Free Download" button. Wait for the file to download, and then open the file. Once opened, you should get a screen that instructs you to drag the BBEdit icon into the Applications folder. Do so. 

Once you have downloaded BBedit, you can create or open files. [Here](https://itservices.usc.edu/files/2013/11/bbedit.pdf) are some instructions from USC on the use of BBedit. Essentially, you will navigate to the "File" menu to carry out most of these tasks.

## Comments in Python

Now that you have a text editor and the majority of set-up is complete, we can get to the meat of the coding! Begin by creating your session directory, `session04/`. Then, create a new file called `comments.py`. 

```
mkdir session_04
cd session_04/
touch comments.py
```

Here, you will learn how to use different comment styles in your code. Comments are useful for a number of reasons, but primarily because (1) it helps someone else read and understand your code and (2) it helps the future *you* understand the code you wrote. Organization is key when coding, so comments are a really easy way to facilitate this.

### Inline Comments

One type of comment you can write is an inline comment. This is a comment that occurs in the same line as code that is being run. To add a comment, we use the `#` symbol. Everything after the `#` is interpreted as a comment in Python, so it does not get run. Although you do not have to understand the Python code here, I'd like you to see what an inline comment looks like. This is what our code looks like:

```
for i in range(1,5):
	print(f'I am in for-loop iteration: {i}')
	print("Notice the comments do not print")

```

And this is what it looks like when we add inline comments (add this code block to `comments.py`)

```
for i in range(1,5):
	print(f'I am in for-loop iteration: {i}') # Print the number in the current iteration
	print("Notice the comments do not print") # Here is another inline comment that does not print
```

### Single Line Comments

While inline comments are helpful, I personally have a preference for single line comments. This acts almost like a header, saying something like:

```
# The following code carries out function X
def function_x()
	print("This function only prints this statement")
```

It seems more organized, keeping a nice separation between commentary and functional code.

### Multi-Line Comments


