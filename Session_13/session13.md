# Session 13: Argparse

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2024-05-14

Reference materials include Dr. Ian Korf's [MCB 185 material](https://github.com/vhaghani26/Learning_Python/tree/master/MCB%20185%20(Korf%20Course)) and [Python Basics for Data Science](https://www.edx.org/course/python-basics-for-data-science?index=product&queryID=4d4d882866dc3e8628ed7728b4662847&position=1) course by IBM hosted on edX. 

## Argparse

What do command-line programs like `ls`, `grep`, and `python` have in common? They all use arguments! When you run these programs, you often provide inputs or options to modify their behavior. In Python, we use the `argparse` module to handle these command-line arguments. Up to this point, we've been writing Python scripts that run from start to finish without needing any input from the command line. However, many useful scripts need to accept user input directly from the command line to function correctly. `argparse` helps us define what arguments our script requires, processes those arguments, and makes our script more flexible and user-friendly. `argparse` is especially helpful for configurable (i.e. parameterized) code, where you only give your arguments at the command line, but do not edit the script once it has been made. 

The following is a script I wrote that downloads and processes full copies of genomes for whenever I want to do a project using a different genome. The code may look difficult to interpret upfront, but you should have close to everything in your tool box to understand the script, including functions, conditionals, dictionaries, string operations, etc. The one thing that may look the most foreign to you is the `argparse` section. By the end of this lesson, you should be able to return to this script and understand how it is written and why it is written the way it is.

```
#!/usr/bin/env python3

import argparse
import os

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Download and process a genome to create a GENOME.fa file')

parser.add_argument('--genome', required=True, type=str,
    metavar='<str>', help='Abbreviated UCSC Genome Browser genome name (e.g. dm6, hg19, hg38, mm9, mm10, rn6, ce11, sacCer3, danRer11)')
    
parser.add_argument('--out_dir', required=True, type=str,
    metavar='<str>', help='Where to output GENOME/GENOME.fa file to')  
    
# Finalization of argparse
arg = parser.parse_args()

#####################
## Define Function ##
#####################

def download_genome(genome, out_dir):
    genome_links = {
        'dm6': 'https://hgdownload.soe.ucsc.edu/goldenPath/dm6/bigZips/dm6.fa.gz',
        'hg19': 'https://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz',
        'hg38': 'https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.chromFa.tar.gz',
        'mm9': 'https://hgdownload.soe.ucsc.edu/goldenPath/mm9/bigZips/chromFa.tar.gz',
        'mm10': 'https://hgdownload.cse.ucsc.edu/goldenPath/mm10/bigZips/chromFa.tar.gz',
        'rn6': 'https://hgdownload.cse.ucsc.edu/goldenPath/rn6/bigZips/rn6.fa.gz',
        'ce11': 'https://hgdownload.soe.ucsc.edu/goldenPath/ce11/bigZips/chromFa.tar.gz',
        'sacCer3': 'https://hgdownload.cse.ucsc.edu/goldenPath/sacCer3/bigZips/chromFa.tar.gz',
        'danRer11': 'https://hgdownload.cse.ucsc.edu/goldenPath/danRer11/bigZips/danRer11.fa.gz'
    }
    
    link = genome_links[genome]
    output_directory = os.path.join(out_dir, genome)
    os.makedirs(output_directory, exist_ok=True)
    
    os.system(f'wget {link} -P {output_directory}')
    
    if link.endswith(f'{genome}/bigZips/{genome}.fa.gz'):
        output_file = os.path.join(output_directory, f'{genome}.fa.gz')
        os.system(f'gunzip -f {output_file}')
        
    if link.endswith(f'{genome}/bigZips/chromFa.tar.gz'):
        output_file = os.path.join(output_directory, 'chromFa.tar.gz')
        os.system(f'tar -xzf {output_file} -C {output_directory}')
        os.system(f'cat {output_directory}/*.fa > {output_directory}/{genome}.fa')
        os.system(f'rm -f {output_directory}/chr*.fa')
        
    if link.endswith('hg38.chromFa.tar.gz'):
        output_file = os.path.join(output_directory, 'chromFa.tar.gz')
        os.system(f'tar -xzf {output_file} -C {output_directory}')
        os.system(f'cat {output_directory}/chroms/*.fa > {output_directory}/{genome}.fa')
        os.system(f'rm -rf {output_directory}/chroms/')
        
#####################
## Download Genome ##
#####################

download_genome(arg.genome, arg.out_dir)
```

## Argparse Set-Up

One of the first things you need to do is import and initialize `argparse`. Create a file called `smiley_argparse.py` (I don't know if just `argparse.py` will mess with the native `argparse` or not and I'm too afraid to test it, so do with that what you will). Now, put the following in your script:

```
#!/usr/bin/env python3

import argparse

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Description of program')
```

`argparse.ArgumentParser` is a class in the `argparse` module that is used to create a new argument parser object (we will learn about classes and object-oriented programming later, so you don't need a super deep understanding of classes/objects quite yet; just get an idea of what this is doing). This object holds information about how to parse the command-line arguments. `description=` is an optional argument that provides a brief description of what your program does. Even though it's optional, this is important to include both for your future self and other users. Whenever someone runs `--help` on your program, it will display the description you give the program. Let's change the description so that it matches what our script will be doing:

```
# Initialize argparse
parser = argparse.ArgumentParser(
    description='Print any number of smiley emoticons on the same or a different line')
```

Now, we have imported and initialized `argparse`, so we get to start introducing our command line arguments. There are many different types of arguments with varying degrees of complexity. However, in this lesson, we will just focus on what most daily usage looks like. Of all the times I've used `argparse`, the information in this lesson is all I have needed. 

Also, in order for the stuff downstream to run, we need to finalize `argparse` as well. After the initialization line, add the following:

```
# Finalization of argparse
arg = parser.parse_args()
```

This will always go last in your `argparse` set up (i.e. after you add your arguments). It helps separate your arguments and allows you to call them by name in your script using `arg.{argument_name}`.

## Required Arguments

Required arguments are any arguments at the command line that the script requires before it can run successfully. Here, we will require our smiley face script to be given an integer input so that it can determine how many smiley faces to print:

```
# Required arguments
parser.add_argument('--num', required=True, type=int,
    metavar='<int>', help='Required integer argument to choose number of smiley emoticons to print')
```

Let's break down the components of the required arguments.

1. `parser.add_argument()` 
	* `parser` is the `ArgumentParser` object that we created earlir when we initialized `argparse`
	* `add_argument` is function that allows us to specify what command-line option the script is expecting
2. `--num`
	* The double dashes (`--`) indicate that this is an argument, and `num` is the name we are assigning to the argument
3. `required=True`
	* This indicates that the argument is mandatory, which means the person running the script must provide this argument when they run it, otherwise an error will occur
4. `type=int`
	* The type specifies the data type for the input. Most commonly, it will be something like `int` or `str`. The `int` part here is especially important because `argparse` will convert the argument into an integer for downstream use, preventing any `type` issues that may arise
5. `metavar='<int>'`
	* This provides a name for the argument value in the help message. It acts as a placeholder to indicate what type of value is expected, so the help message will display `--num <int>` for users
6. `help='Required integer argument to choose number of smiley emoticons to print'`
	* This is a description of the argument that will be shown in the help message. It explains what the argument is for, making the usage of the script more understandable
	
Now that you have added this to your script, save your script, and run:

```
python3 smiley_argparse.py --help
```

And you should see a print out of the script description and arguments! Let's populate the script with what we want it to do now:

```
a = ':) '
b = a * arg.num
print(b)
```

In order to use the argument in your script, all you need to do is use the variable `arg.{argument_name}` and it will function as a variable storing the value from the command line. Once you save the script, run:

```
python3 smiley_argparse.py --num 3
```

You should see an output with three smiley emoticons. Try changing the number and rerunning it a few times. You can start to see the power of using `argparse` - no need to edit any code or even open the script for that matter!

## Optional Arguments

Sometimes, there are arguments that you offer for users, but the argument is not necessary for the script to run succesfully. For example, here, we can print whatever number of smiley emoticons we want, but we have given the user power to choose how many smiley emoticons they want. An alternative to requiring the argument is to make it optional and include a default value.

### Default Values

A default value in `argparse` is used when a user does not specify an alternative argument at the command line. Let's remove our required argument and change it to an optional one with a default:

```
# Optional arguments
parser.add_argument('--num', required=False, type=int, default = 5,
    metavar='<int>', help='Integer argument to choose number of smiley emoticons to print, default is [%(default)i]')
```

Notice that compared to the required argument, we have changed `required=True` to `required=False`. This is what explicitly tells `argparse` that the user does not need to give it an argument. In some cases, there is no need for a default value. For demonstration purposes, however, we will use a default value. Here, we tell `argparse` that if `arg.num` is not specified by the user, then use `5` instead. It also helps to put the default in your `help` description. Let's see what has changed in our script now:

```
python3 smiley_argparse.py --help
```

Try running it again with a value:

```
python3 smiley_argparse.py --num 14
```

And now, let's run it without an argument:

```
python3 smiley_argparse.py
```

This is especially powerful because you can decide an appropriate default, but also allow the users of your program flexibility.

## Switches

Another form of an optional argument is a switch. An `argparse` switch, however, acts like more of a Boolean. It is often used to represent a True/False scenario. Let's add a switch into our script in addition to the optional argument we already have:

```
# Switch
parser.add_argument('--same', action="store_true",
   help='If used, the smiley emoticon are printed on the same line instead of different lines')
```

We tell `argparse` that when the argument `--same` is used at the command line, to store the value "True" (`action="store_true"`). We can, therefore, use it as a conditional in our code:

```
if arg.same:
    a = ':) '
    b = a * arg.num
else:
    a = ':) \n'
    b = a * arg.num
print(b)
```

See how we used `arg.same` directly after `if`? This is because we are effectively saying `if True:`, and by using `--same` at the command line, we are saying that the condition is true. You do not need to give it any argument since just using `--same` stores a value for you to use. Let's run the script a few different ways so you can see the arguments at play:

```
# Optional argument used, switch used
python3 smiley_argparse.py --num 10 --same
```

```
# Optional argument not used, switch used
python3 smiley_argparse.py --same
```

```
# Optional argument used, switch not used
python3 smiley_argparse.py --num 10
```

This should show you, even with a simple script, how helpful `argparse` can be! Now, if you haven't already, take a look back at the script towards the beginning of the lesson. Look through it and notice how the arguments are set up and used in the script.

## Argparse Template

Given how powerful `argparse` is, I use it in just about every single script I write. As such, I typically open an old script and just copy and paste the `argparse` set up. Here, I will provide an easy template that includes required arguments, optional arguments, and switches, so they can be added, deleted, and modified as needed.

```
#!/usr/bin/env python3

import argparse

#####################
## Set Up Argparse ##
#####################

# Initialize argparse
parser = argparse.ArgumentParser(
    description='Description of program')

# Required argument(s)
parser.add_argument('--required_argument', required=True, type=str,
    metavar='<str>', help='Description of the argument')
    
# Optional argument(s)
parser.add_argument('--optional_argument', required=False, type=int, default = 5,
    metavar='<int>', help='Some optional argument that uses the default value [%(default)i]')
	
# Switch(es)
parser.add_argument('--switch1', action="store_true",
   help='An argparse switch that stores the value "True"')
   
# Finalization of argparse
arg = parser.parse_args()
```

Congratulations for learning how to use `argparse`, arguably one of the most helpful tools for coding in Python!