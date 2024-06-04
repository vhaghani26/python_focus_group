# Session 14: `screen`

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2024-06-04

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. 

## Introduction to `screen`

Up to now, we have learned a mixture of tools to use Python and the Python language itself. Today, we'll be learning about another tool that will help with our use of Python. Let's say you write a Python script and it takes a few hours to run. Do you leave your terminal open, computer on, and desperately hope your internet doesn't cut out and kill your entire job? No! You use `screen`.

`screen` is a tool that allows you to manage multiple terminal sessions from a single window. This can be particularly useful when working on remote servers or running long processes, as you can disconnect and reconnect without losing your work.

## Installation

Most of the time, your computer will already have `screen` installed. To try it out, run:

```
screen -ls
```

If it says that no sockets are found, that's great because it means you have `screen` installed! If it says `screen` is not found, you will need to install it. Run the following to install it

```
sudo apt-get install screen
```

## Using `screen`

Once it's installed, screen is actually fairly straightforward to use. Just imagine that you are using the command line to switch between different tabs/windows. While there are many more advanced uses than the ones I present here today, I only plan to teach you the practical everyday type of usage you'll likely need. However, you are welcome to browse the `screen` [documentation](https://www.gnu.org/software/screen/manual/screen) as you feel fit.

For now, let's try starting a new `screen` session. Usually, you would type the commands listed. In this case, the `screen` commands include a combination of actual commands to run and buttons you will physically press on your keyboard.

First, we are going to create a `screen`. Run the following command to create a `screen`:

```
screen -S test_screen
```

The `-S` is used to start a new `screen` session. The `test_screen` portion is the name of the screen. Feel free to name it any name you'd like. I prefer to name mine based on what job I'm doing in that screen so that I can easily switch between tasks and projects. The above command should open a blank screen with some job information at the top. Try running:

```
screen -ls
```

You should see that you are now attached to `test_screen`. Imagine you are running something quite intensive and long and want to now leave the screen. You can do so by clicking `ctrl-a` (i.e. `ctrl` and `a` at the same time), then clicking `d` afterwards. It should detach you from the screen. Now, run the following again:

```
screen -ls
```

You should see that you are detached from your `screen` session. Feel free to open and close your terminal and check your `screen` session. It gets preserved! Now, let's say hours have gone by and you are interested in checking in on your job. You can reattach to your `screen` by running:

```
screen -r test_screen
```

Now you'll be loaded back into your `screen`. Maybe lots of things have been output to standard error and you'd like to scroll through to investigate. Click `ctrl-a` then the `esc` button. It should tell you that copy mode has been initiated. You can use the up and down arrows on your keyboard to navigate. Once you're content, just click `enter` once or twice and it should abort copy mode and take you back to the bottom of the screen.

Finally, assuming your job has finished and you no longer need your session, we can kill the `screen`. To do so, click `ctrl-a` and then `k`. It will ask you to confirm. You can click `enter` to confirm and your session will be terminated.

Overall, this is an extremely powerful tool that will allow you to multitask more effectively or ensure that jobs are able to run to completion without being interrupted. Congratulations on learning how to use this new computational tool!

## `screen` Cheat Sheet

| Action | Command |
| :----: | :-----: |
| Start a screen session | `screen -S {name}` |
| Reattach to a screen session | `screen -r {name} |
| List your screens | `screen -ls` |
| Detach from a screen | ctrl-a, d |
| Terminate a screen | ctrl-a, k |
| Scroll through a screen | ctrl-a, esc |
