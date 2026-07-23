# Session 13: Working on Hive: `SLURM`, `srun`, and `screen`

By: Viktoria Haghani

Last Updated: 2026-07-23

This material was adapted from [Dr. C. Titus Brown's material](https://github.com/ngs-docs/2021-GGG298/tree/latest/Week9-Slurm_and_Farm_cluster_for_doing_analysis) and the [UC Davis Bioinformatics Core's SLURM workshop](https://ucdavis-bioinformatics-training.github.io/2023-October-Slurm-Seminar/cluster_training/intro).

**Note**: If you are not affiliated with UC Davis, then request an account on a cluster environment at your organization (if applicable) or skip to the `screen` section, as much of this session is relevant to UC Davis Hive users.

## Accessing Hive

### Requesting a Hive Account

If you are affiliated with UC Davis, you will need to request a Hive account. **Please do this before we meet for the session.**

1. Go to this webpage: https://hippo.ucdavis.edu/clusters
2. Select "HIVE" for the cluster
3. Select "kdfinkgrp" as the group
4. Write "Julian Halmai" for the PI
5. Make your SSH key
	- To make an SSH key, you will need to run the following on a Unix based terminal (which is the native terminal for macOS and Linux, but for Windows may be something like Ubuntu):

```
ssh-keygen
ls -al ~/.ssh
cat ~/.ssh/*.pub
```

6. Copy and paste the ENTIRE key into the prompt 
7. Submit your profile request for approval. Once approved, it may take a few hours for your account to become active

### Using the OnDemand Interface

The most straightforward way to use Hive is to access it through your browser by logging in here: https://ondemand.hive.hpc.ucdavis.edu. This will allow you to launch an RStudio Server, a Linux Desktop, JupyterLab, or VSCode Server, which are all interactive. They also make it easier to request resources compared to command line requests.

### Using the CLI Interface

I may be a little more old school here, but I prefer the CLI interface. In part, it may be because of my familiarity with the old cluster, which didn't have the OnDemand option. Because not all clusters will have an "easy" option for you to use them, I'm going to teach the old school computer science way of doing things so that you can carry the skill with you moving forward. To access Hive from the command line, run:

```
ssh {username}@hive.hpc.ucdavis.edu
```

Note that your **username** will be emailed to you once your account is live. You will need to log in using the device you generated the SSH key on. Enter your **Kerberos password** when prompted to log in.

## Requesting Resources on Hive

If you use OnDemand, you will be asked to request resources before you initiate your session. Using the CLI, however, you have to be more careful about your resource usage. There are two main ways that you can request resources. If you are submitting a job to run in the background that's hands-off, you can use [**SLURM**](https://slurm.schedmd.com/documentation.html) (**S**imple **L**inux **U**tility for **R**esource **M**anagement), which is an open source workload manager that is commonly used on compute clusters. It handles allocating resources requested by batch scripts. If you are doing something more interactive, like troubleshooting, you can use `srun`.

### Interactive SRUN Sessions

Interactive sessions allow you to work on computers that aren't the login/head node. Essentially you can do everything you've done at the command line interface on the cluster.  To request and launch a basic interactive session that will last for two hours use the following:

```
srun --time=02:00:00 --pty /bin/bash
```

Pay close attention to the time you give to yourself using `srun`! SLURM will terminate the session immediately at the end of the allotted time. It, sadly, doesn't care if you are 99.99% of the way through your analysis :(

Also, you can request more/different resources by using to following flags:
* `--mem=<number>Gb` - request a certain amount of memory
* `-c <number>` - request a certain number of CPUs
* `--pty R` - request an interactive R session
* `--account` - specifies the account; (e.g. `publicgrp`)

Please note that resources available to you will be listed upon log in, so you may request accordingly. Any of the options you add should come before the `--pty` argument:

```
srun --time=00:05:00 --mem=4Gb --account publicgrp --partition low --pty /bin/bash
```

Once you are done your `srun` session, type `exit` so that the resources can be used by someone else since you are no longer using them. This is the nice thing to do!

### SBATCH Scripts (SLURM Submissions)

Batch job scripts (also known as job scripts) are scripts that contain `#!/bin/bash` at the beginning of each script and are submitted to the SLURM workload manager by using `sbatch`. They are scripts that contain code usually written in `bash`. We can use most commands (and a few more) that we would use at the command line within our `sbatch` scripts:

- The **partition** we would like to use for our job (this will also entail the _priority_ in which our job is submitted). We can request a partition by using the following flag: `-p {name_of_partition}`
- The **memory** required to run our job. We can request a specified amount of time with the following flag: `--mem={number}Gb`
- We can have SLURM **mail** us updates about our job, such as when it starts(`BEGIN`), ends(`END`), if it fails(`FAIL`) or all of the above (`ALL`). There are many other mail-type arguments: REQUEUE, ALL, TIME_LIMIT, TIME_LIMIT_90 (reached 90 percent of time limit), TIME_LIMIT_80 (reached 80 percent of time limit), TIME_LIMIT_50 (reached 50 percent of time limit) and ARRAY_TASKS. We can request SLURM emails us with the following flags: `--mail-user={your_email} --mail-type={argument}`
- We can also give jobs specific **names**. To name your job use: `-J {job_name}` Be careful, as there is a limit to the number of characters your job name can be.
- SLURM automatically generates **output scripts** where all of the output from commands run from the script are printed to. These will take the form as `slurm-12345.out` where 12345 is an identifying number (the job ID, by default!) SLURM assigns to the file. We can change this to any output file name we want. To specify the name of your output file use `-o {file_name}.out`
- SLURM can generate **error files**, where all of the errors from the script are printed to. We can ask SLURM to create err files and name them with `-e {file_name}.err`

When we submit a script to SLURM it is considered a _job_ and gets a unique `job_ID` assigned to it. Jobs can be submitted to SLURM with the `sbatch` command:

```
sbatch {your_script}.slurm
```

You will see your job was successfully submitted and will be given an associated Job ID number: `Submitted batch job {job_id}`. To submit the job, you can write a SLURM script and submit it.

#### SLURM Script Template

```
#!/bin/bash
#
#SBATCH -J job_name		                                            # Name for job
#SBATCH --mail-user=vhaghani@health.ucdavis.edu                     # User email to receive updates
#SBATCH --mail-type=ALL                                             # Get an email when the job begins, ends, or if it fails
#SBATCH -p low		                                                # Partition, or queue, to assign to
#SBATCH -o job_name.j%j.out              		                    # File to write STDOUT to
#SBATCH -e job_name.j%j.err                  		                # File to write error output to
#SBATCH -N 1                                                        # Number of nodes/computers
#SBATCH -n 1                                                        # Number of cores
#SBATCH -c 8                                                        # Eight cores per task
#SBATCH -t 72:00:00                                                 # Ask for no more than 72 hours
#SBATCH --mem=6gb                                                   # Ask for no more than 6 GB of memory
#SBATCH --chdir=/quobyte/kdfinkgrp/Viki/my_project_directory	    # Directory I want the job to run in

##############################
# Activate Conda Environment #
##############################

# Load conda
module load conda

#  Source the Conda shell function loader
source /cvmfs/hpc.ucdavis.edu/sw/conda/root/etc/profile.d/conda.sh

# Activate your conda environment
conda activate {path to environment}

#################
# Your Commands #
#################

# Run your commands
{your_commands_go_here}

###################
## Documentation ##
###################

# Print out various information about the job
env | grep SLURM                                               # Print out values of the current jobs SLURM environment variables

scontrol show job ${SLURM_JOB_ID}                              # Print out final statistics about resource uses before job exits

sstat --format 'JobID,MaxRSS,AveCPU' -P ${SLURM_JOB_ID}.batch
```
 
Depending on your text editor, you may get an error about DOS line breaks. If so, run `dos2unix {filename}`.
 
## Managing Jobs

### Monitor Jobs with `squeue`

We can look at the status of any job SLURM is handling by using `squeue`. This will output a list of **ALL** the jobs currently submitted to SLURM. Often we won't be able to scroll through the list to find our job(s). So, in order to only see your own job(s) we can specify a **username**:

If you don't know your username, you can find it in a couple of ways: `whoami` or `echo $USER`.

We can use the output of this to see the status of the jobs associated with a particular username (yours or another user's can be displayed):

```
squeue -u {username}
```

If you don't care about other people's jobs, you can also just use the `--me` flag instead of `-u {username}` like so:

```
squeue --me
```

We can also expand our view to show the full rule name (the default is 8 characters long, which is too short for my uses at times). It also displays how long a job has been running next to the time limit. As such, I find this more informative than the above command:

```
squeue --format="%.18i %.9P %.30j %.8u %.8T %.10M %.9l %.6D %.10a %.10R" --me
```

**Tip**: You can add the following to your `~/.profile`:

```
alias squeue_me='squeue --format="%.18i %.9P %.30j %.8u %.8T %.10M %.9l %.6D %.10a %.10R" --me'
```

Then if you just run `squeue_me` it will be beautifully tailored to your own jobs.

### Cancel Jobs with `scancel`

To cancel a single job you can specify the `JOBID`

```
scancel {job_ID}
```

To cancel all of the jobs that belong to you, use the `-u`flag.

```
scancel -u {username}
```

## Introduction to `screen`

Now that you're somewhat familiar with Hive, let's say you write a Python script and it takes a few hours to run. Do you leave your terminal open, computer on, and desperately hope your internet doesn't cut out and kill your entire job? No! You use `screen`.

`screen` is a tool that allows you to manage multiple terminal sessions from a single window. This can be particularly useful when working on remote servers or running long processes, as you can disconnect and reconnect without losing your work.

### Installation

Most of the time, your computer will already have `screen` installed. To try it out, run:

```
screen -ls
```

If it says that no sockets are found, that's great because it means you have `screen` installed! If it says `screen` is not found, you will need to install it. Run the following to install it

```
sudo apt-get install screen
```

### Using `screen`

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

### `screen` Cheat Sheet

| Action | Command |
| :----: | :-----: |
| Start a screen session | `screen -S {name}` |
| Reattach to a screen session | `screen -r {name} |
| List your screens | `screen -ls` |
| Detach from a screen | ctrl-a, d |
| Terminate a screen | ctrl-a, k |
| Scroll through a screen | ctrl-a, esc |
