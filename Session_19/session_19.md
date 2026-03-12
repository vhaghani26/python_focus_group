# Session 19: Introduction to Snakemake

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2026-03-12

## Table of Contents

* [Introduction to Snakemake](#introduction-to-snakemake)
* [Background](#background)
* [Installation](#installation)
* [Rule Structure](#rule-structure)
* [Inputs and Outputs](#inputs-and-outputs)
	* [`temp()`](#temp)
	* [Depencency Mapping](#dependency-mapping)
	* [Snakemake's "Memory"](#snakemakes-memory)
	* [Error Handling](#error-handling)
	* [Improving the Rule](#improving-the-rule)
* [Directory Organization](#directory-organization)
* [Constructing the Workflow](#constructing-the-workflow)
* [Rule All](#rule-all)
* [Running the Workflow](#running-the-workflow)
* [Resources](#resources)

## Introduction to Snakemake

Snakemake is a powerful workflow management system written in Python that enables users to create reproducible and scalable data analyses. Snakemake does a great job of handling input/output (I/O) processes, many of which happen to be related to biological data analyses. However, I think there's a lot more flexibility than that. Here are some benefits of using Snakemake:

* The syntax is very straightforward
* You can integrate Python code in or out of the rule blocks
* You can execute shell commands
* It can manage all associated dependencies and ensure tasks are executed in the correct order
* One of its biggest strengths is parallelization
* It can manage and track SLURM submissions 

I can keep going on, but generally speaking, Snakemake is a very powerful tool that doesn't take too long to get the hang of if you're already familiar with Python.

## Background

As I mentioned, a lot of Snakemake use cases have to do with bioinformatics workflows. However, I was recently working on submitting a paper for peer review and realized that the figures were not allowed to be PDFs. They said their system handles TIFFs (tagged image file format) the best. I had several figures and supplementary figures I needed to convert. Once I tried converting one, I also realized that the image size exceeds the size limits for submission. This posed a problem I needed to answer:

*What's the best way to convert all my PDFs to TIFF images and compress them without losing quality?*

Then, even after that point, I had generated a heatmap for another project that was so big, the PDF took several minutes just to render fully. I figured an image file would be MUCH quicker to open. The problem this time was that I had 100+ figures I was working with, so I wanted to automate the process. This turned my question into:

*What's the best way to quickly and automatically convert all my PDFs to TIFF images and compress them without losing quality?*

Turns out, (unsurprisingly) that there's software for the image conversion and compression (ImageMagick), and Snakemake stepped in for the automation process. Today, I will be discussing how I used Snakemake to answer this question.

## Installation

If you are looking to install Snakemake, I recommend installing `snakemake-minimal`. It's a more minimal version of Snakemake, but speaking from personal experience, I've done everything I've ever needed to using the minimal version without issue (including large scale workflows with 10+ steps, running over 2000 jobs using a script, submitting jobs via SLURM, etc.). The fastest and easiest installation is using conda/mamba:

```
conda install bioconda::snakemake-minimal
```

## Rule Structure

A "rule" in Snakemake refers to a command/code block to execute. Here, let's take a look at an example rule structure:

```
rule rule_name:
	input: "your_input.file"
	output: "your_output.file"
	shell: "some command you want to run"
```

* `input` - this specifies the input file that is required to run whatever shell command you need
* `output` - this is the name of the output file that you are generating. Snakemake looks for this file when the shell command is executed to determine if the rule was successfully run/completed
* `shell` - this is the shell command that gets run with the rule

This is a bare bones version of a Snakemake rule, but you have a lot more power than just basic inputs, output, and shell commands. Here is a more complicated version:

```
rule rule_name:
	message: "A message that gets printed when the rule is executed"
	input: "your_input.file"
	output: "your_output.file"
	log: "standard_error_log.log"
	benchmark: "program_time.log"
	shell: "some command you want to run"
```

* `message` - this is a message that gets printed every time the job is run. It's descriptive and adds to the verbosity of your workflow runs
* `log` - this contains the standard error generated from whatever you are running. This is especially helpful if you are troubleshooting a new pipeline or running several samples at once since it allows for easily viewing the error
* `benchmark` - this documents how much time your program ran for, which is helpful if you are constructing a workflow with recommended resources for SLURM submission

## Inputs and Outputs

Now, let's look at a real life example. 

```
rule pdf_to_tiff:
    input: "{sample}.pdf"
    output: temp("{sample}_uncompressed.tiff")
    shell: "magick -background white -density 600 -quality 90 {input} {output}"
```

I am calling the rule `pdf_to_tiff`, which is descriptive - it says that this rule functions to convert PDF files to TIFF files. The input is a PDF file, the output is an uncompressed TIFF file. The shell command that needs to run specifies the background is white, the density (DPI) is 600 (which is required by almost all journals), the quality is 90, and it specifies my input and output files. There are a few things I'd like to discuss here.

### `temp()`

For the output, we use a `temp()` function. This is because I don't actually need to uncompressed TIFF at the end of the workflow, but it's a necessary intermediate file. The `temp()` function helps with this. After the output is used in whatever downstream rules it's neeeded for, it is deleted.

### Dependency Mapping

Also, see that instead of putting the inputs and outputs directly in the shell command, we use `{input}` and `{output}`. 

In Snakemake, input and output file specifications are necessary for dependency mapping. This ensures that rules are executed in the correct order based on the availability of required files (inputs). By explicitly defining inputs and outputs, Snakemake can automatically determine which rules need to be run and in what order, allowing for efficient workflow execution. Essentially, when a rule's output is specified as an input for another rule, Snakemake recognizes this relationship and will only execute the downstream rule once the upstream rule has successfully completed and generated the necessary output files. 

There are some workflows where one output is used as an input in multiple rules. Specifying inputs and outputs also helps with managing resources and parallelization since Snakemake recognizes that those tasks are independent of each other and can be run in parallel. 

### Snakemake's "Memory"

Another reason that specifying inputs and outputs like this is important is because Snakemkae performs a check on the output files specified in each rule. If Snakemake detects that the output file already exists and is up to date (i.e. it has not been modified since the last run), it will skip the execution of that rule, meaning if your workflow runs into an error halfway through, you only need to run it from that point forward after debugging, not rerunning the entire thing.

### Error Handling

Specifying outputs is also recommended because Snakemake includes effective error handling that automatically removes any output files generated by a rule if it encounters an error during execution. This prevents the use of potentially corrupt or incomplete data in downstream analyses. 

### Improving the Rule

I have mentioned error handling a few times now. Here, I will incorporate a log file and message to improve up on the rule:

```
rule pdf_to_tiff:
	message: "Converting PDF to TIFF..."
    input: "{sample}.pdf"
    output: temp("{sample}_uncompressed.tiff")
	log: "{sample}_pdf_to_tiff_conversion.log"
    shell: "magick -background white -density 600 -quality 90 {input} {output} 2> {log}"
```

If you are generating log files for standard error, you need to make sure log file names are unique if you have multiple samples. I typically name it the sample followed by the rule name. You should also pipe the standard error into the log file using the `2> {log}` code snippet at the end of your command.

## Directory Organization

Snakemake handles making directories automatically. let's say I want my log files stored in a separate directory. I can specify that like so:

```
rule pdf_to_tiff:
	message: "Converting PDF to TIFF..."
    input: "{sample}.pdf"
    output: temp("{sample}_uncompressed.tiff")
	log: "00_std_err_logs/{sample}_pdf_to_tiff_conversion.log"
    shell: "magick -background white -density 600 -quality 90 {input} {output} 2> {log}"
```

Now, every log file generated will go into `00_std_err_logs/`, which keeps my current working directory clean. You can do the same for your inputs and outputs. The only directory that needs to be created is the initial directory containing your first input or any inputs you already have. Other than that, Snakemake takes care of the rest!

## Constructing the Workflow

Now that we understand how to make a rule, let's continue constructing our workflow. We have already converted PDF to TIFF files, but now we want to compress it, so we will add the next rule:

```
rule compress_tiff:
    input: "{sample}_uncompressed.tiff"
    output: "{sample}.tiff"
    shell: "magick -compress LZW {input} {output}"
```

This uses the `LZW` compression method, which is a lossless compression type (i.e. it preserves the image quality, but decreases the file size). Notice that our previous output, `{sample}_uncompressed.tiff` is our input here. That tells Snakemake that this rule needs to be run after the previous one. 

## Rule All

While Snakemake is very flexible and powerful, that does lend itself to some strange behavior sometimes. For instance, Snakemake only runs the first rule of a workflow unless a rule name is specified at the command line. Generally, there's a convention that's used that allows us to run the entire workflow at once. We call the first rule `rule all` and specify the final output(s) as the inputs required for the rule. Essentially, when Snakemake looks at the first rule, it realizes that in order to run that rule, it needs the required inputs. Since the inputs are generated as outputs in the other rules, it realizes it needs to run the other rules to complete rule all. Because I want to generate TIFFs as my final output, I specify that in my `rule all`:

```
rule all:
    input:
        expand("{sample}.tiff", sample=SAMPLES)
```

Now, notice that I use `expand()` instead of just `{sample}.tiff`. The `expand()` function combined with the `sample=SAMPLES` is essentially just a for-loop. It's saying that for `sample` in `SAMPLES`, you should have a `{sample}.tiff` output. That means that the only way that `rule all` finishes is if every sample has a `{sample}.tiff` file generated. 

This is different notation than our other inputs. Here, we are also specifying the samples. Snakemake is Python-based, which means that we can run Python code in the file. Snakemake supports configuration files like YAML or JSON files that allow you to list your samples explicitly. However, I wanted this to be very fast and automatic without me having to constantly generate sample names, so I specified that my samples are the names of the PDF files in the current working directory stripped of the `.pdf` file extension:

```
import glob
import os

# Get the current working directory
current_directory = os.getcwd()

# List of sample names (all PDFs in the current working directory)
SAMPLES = [os.path.basename(f)[:-4] for f in glob.glob(os.path.join(current_directory, "*.pdf"))]
```

## Running the Workflow

We have seen our sample lists and rules at this point, so now we have a complete workflow:

```
import glob
import os

# Get the current working directory
current_directory = os.getcwd()

# List of sample names (all PDFs in the current working directory)
SAMPLES = [os.path.basename(f)[:-4] for f in glob.glob(os.path.join(current_directory, "*.pdf"))]

rule all:
    input:
        expand("{sample}.tiff", sample=SAMPLES)

rule pdf_to_tiff:
    input: "{sample}.pdf"
    output: temp("{sample}_uncompressed.tiff")
    shell: "magick -background white -density 600 -quality 90 {input} {output}"

rule compress_tiff:
    input: "{sample}_uncompressed.tiff"
    output: "{sample}.tiff"
    shell: "magick -compress LZW {input} {output}"
```

This is very short and relatively simple (no logs, benchmarks, conda dependencies, etc.) in comparison to some other ones, but in 22 lines, we are able to convert hundreds of PDF files to compressed TIFF files automatically. This is extremely powerful (and cool!). 

Personally, I like to actually name my Snakemake files (Snakefiles). If you create a file just called `Snakefile`, you can run Snakemake without specifying the file name and it will run automatically. However, in my work, I typically label my scripts and outputs in order of execution. For instance `02_process_data`, where `01_raw_data/` contains raw data, then I run the Snakefile second, hence the `02`. This is entirely a personal preference. I have named my Snakefile here `pdf_to_compressed_tiff`. This is a succinct and descriptive name that tells me everything I need to know if I want to run/look for the file. There are MANY command line options, but the ones I default to are:

```
snakemake -s pdf_to_compressed_tiff -j 5 -n
```

* `-s` - this is the name of the snakefile; the `-s` is only needed if your Snakefile is not named `Snakefile`
* `-j` - this is the number of jobs you'd like to run at once 
* `-n` - this is a dry run to make sure your dependencies are properly mapped 


If your Snakefile is named `Snakefile`, this simplifies to:

```
snakemake -j 5 -n
```

Once the dry run succeeds, remove the `-n` and you can run your workflow:

```
snakemake -s pdf_to_compressed_tiff -j 5
```

or

```
snakemake -j 5 
```

## Resources

Snakemake is far more powerful than what we went through today. You can read the documentation and see more about the command line options [here](https://snakemake.readthedocs.io/en/stable/executing/cli.html) if you would like to dive more deeply into Snakemake.

Here is an example workflow that is used in LaSalle lab to analyze whole-genome bisulfite sequencing data: https://github.com/vhaghani26/epigenerator/blob/main/02_CpG_Me2_PE. Notice that there are messages, multiple inputs, multiple outputs, logs, benchmarking files, resource allocations for SLURM submisisons, and multi-line shell commands. Wildcard usage and sample read in is also more complicated in this workflow compared to what we saw today, so feel free to explore and enjoy the power of Snakemake! Please feel free to reach out to me (vhaghani@ucdavis.edu) if you have any questions. I am happy to help!
