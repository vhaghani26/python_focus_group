# Session 16: Data Analysis Tools and the JupyterLab Interface

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2026-01-23

Reference materials include teaching material from Dr. Ian Korf, Dr. C. Titus Brown, and Dr. Nick Ulle.

## Packages for Working with Data Frames

Python is general-purpose programming language, so data structures and functions specialized for research computing are not built-in. Instead, the community provides these through packages, which is why we learned about Conda in the last session. Nevertheless, and to the community's credit, Python is a leading language for research computing and data science. This section introduces some of the fundamental packages for research computing. 

For data science, **data frames**, which represent tables of data, are another fundamental data structure. Several competing packages provide data frames and related functions. See some of these below.

### [NumPy](https://numpy.org/)

NumPy provides *n*-dimensional arrays (such as vectors and matrices) and a broad collection of mathematical functions. NumPy is the primary way to do linear algebra efficiently in Python. Many other packages depend on or are compatible with NumPy.

### [Pandas](https://pandas.pydata.org/)

Pandas is the oldest and most widely-used data frame package. It provides a broad set of features but also has many quirks. Pandas is generally less efficient than other packages in terms of compute time and memory usage, but the documentation is quite thorough given how widely used it is. Thus, it can be easier to troubleshoot.

### [DuckDB](https://duckdb.org/)

DuckDB treats data frames as tables in a database. This makes DuckDB extremely efficient and also means all operations on DuckDB data frames must be written in Structured Query Language (SQL) rather than Python. If you're comfortable with SQL or need to work with big data (hundreds of gigabytes or more), DuckDB is a good choice. 

### [Ibis](https://ibis-project.org/)

Ibis provides data frames that can use any of the other packages under-the-hood. Ibis uses DuckDB by default, so it has similar efficiency but a Python programming interface (SQL is also supported).

### [Polars](https://pola.rs/)

Polars is specifically designed to be efficient, prevent bugs, and present a consistent programming interface. Polars is most highly recommended (by me and some other people) because it has great documentation, intuitive functions, is more efficient than Pandas, and provides early warnings for certain kinds of common mistakes.

## Packages for Research Computing in Python

Other notable packages for research computing in Python:

### [Jupyter](https://jupyter.org/)

Jupyter provides interactive notebooks that use **IPython** and **IRkernel**, a more convenient command-line prompt for Python and R, respectively. Fun fact, "Jupyter" is short for "Julia, Python, Text, and R."

### [SciPy](https://scipy.org/)

SciPy provides even more mathematical functions, to supplement NumPy.

### [Matplotlib](https://matplotlib.org/)

Matplotlib provides a rich collection of visualization functions and is the foundation for many data visualization packages.

### [statsmodels](https://www.statsmodels.org/)

statsmodels provides functions to fit statistical models (where the focus is inference and interpretability).

### [scikit-learn](https://scikit-learn.org/)

scikit-learn provides functions to fit machine learning models (where the focus is prediction). The package's excellent documentation also provides a light but practical introduction to the models.

This is by no means an exhaustive list. You're likely to encounter many more packages as you learn and use Python.

## The JupyterLab Interface

There are many different ways to edit and run Python code, but we'll use JupyterLab. JupyterLab is an **integrated development environment** (IDE), which means it's a comprehensive program for writing, editing, searching, and running code. You can do all of these things without JupyterLab, but JupyterLab makes the process easier. In the last session, we created an environment called `data_analysis`. Let's go ahead and activate this since we will be using some of the software we installed:

```
mamba activate data_analysis
```

Now, let's launch JupyterLab:

```
jupyter lab
```

Notice that when you run this command, lots of things will print out at your terminal. You want to copy and paste the link that it sends you into your browser.

![launchjupyter](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/jupyterlab.png)

Upon doing so, your browser should load the JupyterLab interface. Don't worry if the text in the panes isn't exactly the same on your computer; it depends on your operating system and version of JupyterLab.

![jupyterinterface](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/jupyterlabinterface.png)

Start by opening up a Python **console**. In JupyterLab, look for the "Python 3" button in the "Console" section of the pane on the right. If there are multiple Python 3 buttons, click on the one that mentions "IPython" or "ipykernel". The console is a interactive, text-based interface to Python. If you enter a Python expression in the console, Python will compute and display the result. After you open the console, your window should look like this:

![pythonconsole](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/pythonconsole.png)

At the bottom of the console, the text box beginning with `[ ]:` is called the **prompt**. The prompt is where you'll type Python expressions. In our terminal, this is commonly denoted by a `$`. Let's start by asking Python to compute the sum `2 + 2` by typing the code the prompt and then pressing `Shift`-`Enter`. Your code and the result from Python should look like this:

![pythonpromptoutput](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/pythonpromptoutput.png)

The Python console displays your code and the result on separate lines. Both begin with the tag `[1]` to indicate that they are the first expression and result. Python will increment the tag each time you run an expression. The tag numbers will restart from 1 each time you open a new Python console.

Now try typing the code `3 - 1` in the prompt and pressing `Shift`-`Enter`. The tag on the code and result is `[2]`, and once again the result is displayed after the tag.

# Starting a Data Analysis Project

We already know how to run Python scripts at the terminal, but let's try working in Jupyter notebooks now. You are going to create a new GitHub repository called `Terns_Data_Analysis`. You should do so in the browser on GitHub. Once you create your repository, use GitHub Desktop to clone it locally so we can work in the repository.

## Project Organization

Often times when working on a project, you should organize your scripts, inputs, and outputs in a way that someone looking at it fresh for the first time will understand the order things were run in. For my own organization, I like to organize using an ordinal numbering system. For example, my RNA-seq projects typically look something like:

```
.git/
.gitignore
00_slurm/
01_raw_sequences/
02_trimmed/
03_bam_files/
04_multiqc/
05_gene_counts/
05.1_assign_gene_names.py
05.2_DEG_Analysis.ipynb
06_DEG_GO.ipynb
07.1_Visualize_DEG.ipynb
07.2_heatmaps.py
08_WGCNA.ipynb
09_WGCNA_GO.ipynb
10_Visualize_WGCNA.ipynb
LICENSE
README.md
02_snakefile
samples.yaml
```

I use this system because it helps maintain clarity regarding the workflow and the order of operations. The directory labeled **00** contains configuration-related files, ensuring that all settings and parameters are defined from the beginning. Think of these like the necessary context to begin. The **01_raw_sequences** folder is designated for storing raw data, providing a clear starting point for data processing. As the workflow progresses, each subsequent directory numerically reflects the order in which processes are executed, allowing anyone reviewing the project to easily understand the flow. Scripts are also labeled with numerical prefixes; for instance, **05.1_assign_gene_names.py** indicates that this script is executed during the fifth stage of the analysis. This systematic approach not only enhances reproducibility but also facilitates collaboration, making it simpler for others to follow and comprehend the various stages involved in the project. 

## Initializing the Project

We are going to start our own data analysis project using some sample data. In the GitHub repository you created, create a directory called `01_raw_data/`. Now, go to the GitHub repository for the Python Focus Group and download this dataset into `01_raw_data/`: `https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/2000-2023_ca_least_tern.csv`. 

If you look at GitHub desktop now, it should show that you can commit your directory with the CSV file. As a general rule of thumb, **you do not want any data hosted on GitHub**. GitHub is for documenting your code and analysis process. Luckily, we can give GitHub instructions on ignoring this directory. We can do so by creating a file called `.gitignore` and adding the raw data directory into it. The contents of your `.gitignore` file should just be:

```
01_raw_data/
```

Now go back to GitHub desktop. You should see that the raw data directory disappeared, but you have an option to commit the `.gitignore` file. Go ahead and commit and push `.gitignore`.

## Creating a Jupyter Notebook

For data science tasks, it is also common to use a **Jupyter notebook** with extension `.ipynb` to store code. In addition to Python code, Jupyter notebooks have full support for formatted text, images, and code from other programming languages such as Julia and R. The tradeoff is that Jupyter notebooks can only be viewed in a web browser.

Jupyter notebooks are more convenient than Python scripts for **interactive work**, such as data analysis and learning or experimenting with the language. On the other hand, Python scripts are more appropriate for long-running code that does not require user interaction (such as web scrapers or scientific simulations) and for developing packages and software. 

You can create a new Jupyter notebook in JupyterLab with this menu option:

```
File -> New -> Notebook
```

JupyterLab will prompt you to select a **kernel** for the notebook. The kernel is the software used to run code in the notebook. For a notebook that will contain Python code, you should choose a Python kernel.

Now that you have created the notebook, you want to save it. Give it an appropriate name. For now, we will just be inspecting the data. Because this notebook will use the raw data, we can call it `01_inspect_data.ipynb`. Save the script in the main project directory, or alternatively in a scripts directory (this is just more difficult because you will have to navigate back a directory every time you read files in or output any, but it's still fine if you prefer this).

## Using Jupyter Notebooks

While looking at the notebook, you can see that it is subdivided into **cells**. You can create as many cells as you like, but each cell can only contain one kind of content, usually code or text. New cells are code cells by default. You can run a code cell by clicking on the cell and pressing `Shift`-`Enter`. The notebook will display the result and create a new empty code cell below the result. You can also convert a code cell to a text cell by clicking on the cell and selecting the "Markdown" option from the cell type dropdown menu.

It is always recommended to have nicely organized code. Generally, when we import modules, we do so at the top of the script. Let's create a markdown cell with `# Import Modules` as the heading, then insert a code cell where we will import the modules we need, specifically `import polars as pl`.

As a quick aside, Markdown is a simple language you can use to add formatting to your text. For example, surrounding a word with asterisks, as in `Let *sleeping* dogs lie`, makes the surrounded word italic. You can find a short, interactive tutorial about Markdown [here][https://www.markdowntutorial.com/]. If you "run" a text cell by pressing `Shift`-`Enter`, the notebook will display the text with any formatting you added.

Your notebook should now look like this:

![moduleimportnotebook](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/moduleimportnotebook.png)

## Reading Files

As you can imaginme, the first step in most data analyses is loading a data set. In order to know which function to use to load the data, you must first identify the file format.

Most of the time, you can guess the format of a file by looking at its **extension**, the characters (usually three) after the last dot `.` in the filename. For example, the extension `.jpg` or `.jpeg` indicates a JPEG image file. Some operating systems hide extensions by default, but you can find instructions to change this setting online by searching for "show file extensions" and your operating system's name. The extension is just part of the file's name, so it should be taken as a hint about the file's format rather than a guarantee.

The table below shows several formats that are frequently used to distribute data. Polars provides reader functions for many of these, but some can only be read with help from other packages or Python's built-in modules.

| Name                        | Extension            | Function or Package      | Tabular?  | Text?
| :-------------------------- | :--------------      | :------------------      | :-------- | :----
| Comma-separated Values      | `.csv`               | `read_csv`               | Yes       | Yes
| Tab-separated Values        | `.tsv`               | `read_table`             | Yes       | Yes
| Fixed-width File            | `.fwf`               | See [this issue](https://github.com/pola-rs/polars/issues/3151) | Yes       | Yes
| Microsoft Excel             | `.xls`, `.xlsx`      | `read_excel`             | Yes       | No
| Apache Parquet              | `.parquet`           | `read_parquet`           | Yes       | No
| Apache Arrow                | `.arrow`, `.feather` | `read_ipc`               | Yes       | No
| Extensible Markup Language  | `.xml`, `.html`      | [parsel](https://parsel.readthedocs.io/en/latest/) package       | No        | Yes
| JavaScript Object Notation  | `.json`              | `json` module            | No        | Yes
| Arbitrary File              |                      | `open` (built-in)        |           |

A **tabular** data set is one that's structured as a table, with rows and columns. We'll focus on tabular data sets for most of this reader, since they're easier to get started with. Here's an example of a tabular data set:

| Fruit  | Quantity | Price
| :----  | -------: | ----:
| apple  | 32       | 1.49
| banana | 541      | 0.79
| pear   | 10       | 1.99

A **text** file is one that contains human-readable lines of text. You can check this by opening the file with a text editor such as Microsoft Notepad or macOS TextEdit. Many file formats use text in order to make the format easier to work with.

For instance, a **comma-separated values** (CSV) file records tabular data using one line per row, with commas separating columns. If you store the table above in a CSV file and open the file in a text editor, here's what you'll see:

```
Fruit,Quantity,Price
apple,32,1.49
banana,541,0.79
pear,10,1.99
```

A **binary** file is one that's not human-readable. You can't just read off the data if you open a binary file in a text editor, but they have a number of other advantages. Compared to text files, binary files are often faster to read and take up less storage space (bytes).

## Loading the Terns Data

In our first data analysis project, we will be using a dataset about the California least tern. The California least tern is a endangered subspecies of seabird that nests along the coast of California and Mexico. The California Department of Fish and Wildlife (CDFW) monitors least tern nesting sites across the state to estimate breeding pairs, fledglings, and predator activity in each annual breeding season.

The CDFW publishes most of the data it collects to the [California Open Data portal][https://data.ca.gov/]. In this project, we will use a cleaned 2000-2023 version of the California least tern data. 

Let's use Polars to read the California least tern data set. The default file name is `2000-2023_ca_least_tern.csv`, which suggests it's a **CSV file**. The Polars function to read a CSV file is `read_csv`. The function's first and only required argument is the path to the CSV file. The path to the California least tern data set is `01_raw_data/2000-2023_ca_least_tern.csv`, because we stored the file in the `01_raw_data` directory. When we load the data, we will save the result from the `read_csv` function in a variable called `terns`. We can use this variable to access the data in subsequent code. 

In our Jupyter Notebook, add a markdown segment titled "Load Data" and a code cell that reads in the data. If your cell block runs without error, then that means your data is loaded. But how do we *know* the data is properly loaded? We look at it!

When working with a new data set, it usually isn't a good idea to print the whole thing (at least until you know how big it is). Large data sets can take a long time to print, and the output can be difficult to read.

Instead, use the `.head` method to print only the beginning, or `head`, of the data set. Add a markdown cell saying "Inspect Data" and then run the code cell:

```
terns.head()
```

You can check to make sure Polars has indeed created a data frame with the `type` function:

```
type(terns)
```

By now, your notebook should look something like this:

![inspectdata](https://github.com/vhaghani26/python_focus_group/blob/main/Session_16/inspectdata.png)

At the end of this page, you should see some documentation on the dataset. Does what we loaded match what we expect from the data? Yes, everything looks good here!

## Inspecting a Data Frame

There are other ways you can inspect your data. Similar to how the `.head` method shows the first few rows of a data frame, the `.tail` method shows the last few:

```
terns.tail()
```

Both `.head` and `.tail` accept an optional argument that specifies the number of rows to print to screen:

```
terns.head(3)
```

As a heads up, for data frames with many rows or columns, Polars will usually replace some rows or columns with `...` when printing to the screen.

You can control how many rows and columns are printed with the `pl.Config.set_tbl_rows` and `pl.Config.set_tbl_cols` functions, respectively. You can later restore the default settings with the `pl.Config.restore_defaults` function. This is not necessary for us to do, so we will not be doing it. This is just to make you aware that you can change this if you'd like.

One way to get a quick idea of what your data looks like without having to skim through all the columns and rows is by inspecting its **shape**. This is the number of rows and columns in a data frame, and you can access this information with the `.shape` attribute:

```
terns.shape
```

You may recall from earlier in the Python Focus Group that there are functions and attributes. The `.shape` attribute uses the same dot (`.`) syntax as the `.head` and`.tail` methods. The key difference is that because `.shape` is not a method,there are no parentheses `()` at the end. Parentheses are necessary when you want to call a method, but not when you want just want to access the value of an attribute.

How can you tell whether or not an attribute is a method? If its value must be computed (for example, by taking a subset), it's probably a method. If its value is an inherent property of the object, it's probably not. You can always use `help` or `type` to check if you're not sure.

Polars stores the data frame's column names in the `.columns` attribute:

```
terns.columns
```

We have now initialized a project, organized the raw data, and loaded it. This is likely what the beginning of any coding project will look like for you. This concludes this session, but during the next session, we will be diving into data manipulation.

# Documentation for 2000-2023 California Least Tern Data Set

Each row in the data set contains measurements from one year-site combination.

| Column                | Description
| --------------------: | :----------
| `year`                | Year of the breeding season
| `site_name`           | Site name
| `site_name_2013_2018` | Site name from 2013-2018
| `site_name_1988_2001` | Site name from 1988-2001
| `site_abbr`           | Abbreviated site name
| `region_3`            | Region of state: S.F. Bay, Central, or Southern (includes Ventura)
| `region_4`            | Region of state: S.F. Bay, Central, Ventura, or Southern
| `event`               | Climate events
| `bp_min`              | Reported minimum breeding pairs
| `bp_max`              | Reported maximum breeding pairs
| `fl_min`              | Reported minimum fledges
| `fl_max`              | Reported maximum fledges
| `total_nests`         | Total reported nests (maximum if a range was reported)
| `nonpred_eggs`        | Total non-predator-related mortalities of eggs
| `nonpred_chicks`      | Total non-predator-related mortalities of chicks
| `nonpred_fl`          | Total non-predator-related mortalities of fledges
| `nonpred_ad`          | Total non-predator-related mortalities of adults
| `pred_control`        | Site predator control (yes/no)
| `pred_eggs`           | Total predator-related mortalities of eggs
| `pred_chicks`         | Total predator-related mortalities of chicks
| `pred_fl`             | Total predator-related mortalities of fledges
| `pred_ad`             | Total predator-related mortalities of adults
| `pred_pefa`           | Predation by peregrine falcons (yes/no)
| `pred_coy_fox`        | Predation by coyotes or foxes (yes/no)
| `pred_meso`           | Predation by other mesocarnivores: dogs, cats, skunks, opossums, raccoons, weasels, etc. (yes/no)
| `pred_owlspp`         | Predation by owls (yes/no)
| `pred_corvid`         | Predation by corvids: ravens or crows (yes/no)
| `pred_other_raptor`   | Predation by raptors other than peregrine falcons and owls (yes/no)
| `pred_other_avian`    | Predation by birds other than raptors and corvids (yes/no)
| `pred_misc`           | Predation by other animals (yes/no)
| `total_pefa`          | Total mortalities due to peregrine falcons
| `total_coy_fox`       | Total mortalities due to coyotes and foxes
| `total_meso`          | Total mortalities due to other mesocarnivores
| `total_owlspp`        | Total mortalities due to owls
| `total_corvid`        | Total mortalities due to ravens and crows
| `total_other_raptor`  | Total mortalities due to other raptors
| `total_other_avian`   | Total mortalities due to other birds
| `total_misc`          | Total mortalities due to other animals
| `first_observed`      | Date CA least terns first observed at site
| `last_observed`       | Date CA least terns last observed at site
| `first_nest`          | Date first egg observed at site
| `first_chick`         | Date first chick observed at site
| `first_fledge`        | Date first fledge observed at site