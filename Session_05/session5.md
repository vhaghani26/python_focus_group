# Session 5: 

By: Viktoria Haghani

Session Date: TBD
Last Updated: 2021-12-16

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. More specific references can be found in the text.

## Aliasing (in .bashrc/.profile)

A bash alias is an extremely helpful thing to take advantage of. It is essentially a shortcut or keyboard abbreviation that you can customize to make your life easier at the command line. Typically, the aliases you create get put in a `.bashrc`, `.profile`, or `.zshrc` file depending on how your system is set up/what operating system you use. These files contain configuration information that manage how your profile/terminal work for you. Everything contained in the file your system uses is run upon starting the terminal. When you create an alias and put it in your configuration file, it will run the command upon starting your terminal. This means you are free to use your shortcuts at any time! The alias command takes on the following structure:

```
alias "the shortcut you want to use"="the actual/old command"
```

Note that if the shortcut does not contain any spaces, you do not need quotes around it. Last week, I mentioned that I would discuss how I change my directory by only typing `pfg`. This is because in my `.bashrc`, I put the following:

```
alias pfg="cd /mnt/c/Users/vicky/Documents/GitHub/python_focus_group"
```

In English, this means that if I type `pfg`, the command `cd /mnt/c/Users/vicky/Documents/GitHub/python_focus_group` gets run. My favorite aliases to add to my `.bashrc` or `.profile` are:

```
alias ls="ls -F" # Add one char of */=>@| to enteries to denote type (file, directory, alias)
alias rm="rm -i" # Prompt user before every removal
alias cp="cp -i" # Prompt before overwrite
alias mv="mv -i" # Prompt before overwrite
```

Because the aliases listed above primarily qualify as "make the terminal stop you from doing something stupid," I'd highly recommend adding them into your file. The configuration bash files are ALWAYS located in your home directory. Navigate to your home directory and list the directory contents:

```
cd ~
ls
```

Most Mac users will have a `.zshrc` file. If this is not present, look for `.bashrc` or `.profile` instead. Open the file using your text editor or nano since this will be a quick edit. Find somewhere appropriate to put the aliases (I usually scroll to where I see aliases already listed), and add in the following to your file:

```
alias ls="ls -F" # Add one char of */=>@| to enteries to denote type (file, directory, alias)
alias rm="rm -i" # Prompt user before every removal
alias cp="cp -i" # Prompt before overwrite
alias mv="mv -i" # Prompt before overwrite
alias pfg="cd your/path/to/python_focus_goup/" # Use pfg to change into python_focus_group
```

To get your path to `python_focus_group/`, you can navigate to the directory and use `pwd`. Save your file and close it. Then, restart your terminal (close it and open a new one) so that the commands get executed when it restats. 

## Data Types

## Type Casting