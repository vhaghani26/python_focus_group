# Session 15: Conda and Mamba

By: Viktoria Haghani

Session Date: TBD

Last Updated: 2026-01-07

Reference materials include teaching material from Dr. Ian Korf and Dr. C. Titus Brown.


## Why should you use Conda?

Software installation is difficult. It's a confusing ecosystem of operating systems (Mac OS X, many versions of Linux, Windows), and many software has many dependencies (e.g. just consider base language -- C++, Java, Python, R, and their different versions).


![isolation](https://github.com/ngs-docs/2021-GGG298/raw/latest/Week3-conda_for_software_installation/conda-isolation.png)


This leads to confusing situations where different versions of underlying software are needed to run two different programs. What if you wanted to run Macs14 and sourmash both, but one wanted 'python' to mean python2 and the other wanted 'python' to mean python3?

![versions](https://github.com/ngs-docs/2021-GGG298/raw/latest/Week3-conda_for_software_installation/versions.png)

Decoupling user-focused software from underlying operating systems is a Big Deal - imagine, otherwise you'd have to rebuild software for every OS! (This is kind of what conda does for you, actually - it's just centralized!)

Also, lot of software installation currently requires (or at least is much easier with) sysadmin privileges, which is inherently dangerous.

**Why do you need isolated software install environments? Some specific reasons:**

* Your work relies on a bunch of specific versions (perhaps old versions?)
* Working with a collaborator who really likes a particular feature!
* Experiment with new packages without messing up current workflow (reproducibility!)
* Publication ("here's what I used for software", repeatability!)
* Sometimes workflows rely on incompatible software packages! see [Titus' Twitter question](https://twitter.com/ctitusbrown/status/1218252506335080449)

Conda tries to solve all of these problems, and (in my experience) largely succeeds. That's what we'll explore today.

Conda is a solution that seems to work pretty well, and can be used by any user. Downsides are that it can get big to have everyone install their own software system, but it's not that big... (The farm admins like it, too!)

![conda image](https://angus.readthedocs.io/en/2019/_static/conda2.png)

Note that conda emerged from the Python world but is now much broader and works for many more software packages, including R!

## Installing Conda

If you remember from [Session 3](https://github.com/vhaghani26/python_focus_group/blob/main/Session_03/session3.md#installing-python-via-conda), we have already installed Conda. If you have not installed it yet or are using a new device without it, please refer back to the session 3 notes and reinstall Conda.

## Mamba

The default package resolver has been known to have some issues and be on the slow side. As such, we can switch to install Mamba. You can install Mamba with the following command:

```
conda install mamba -n base -c conda-forge
```

From this point forward, just use `mamba` instead of `conda` with your Conda commands. 

## Creating Environments

In the next session, we will be working with actual data. To prepare, we will create an environment and install software into it. First, let's make an environment:

```
mamba create --name data_analysis
```

This will ask you to confirm that you want to create the environment. Confirm it and it will take a moment to finalize.

## Activating an Environment

Once you have created the environment, you will need to activate it.

```
mamba activate data_analysis
```

You should see the `(base)` next to your name become `(data_analysis)`. This indicates that you are now using the software installed in that environment. By default, Conda installs several base packages for use, but there will still be many we need to install. 

## Installing Packages

We need to install the following packages:

- Jupyter
- Numpy
- Polars
- Plotnine

You can install multiple packages at once or one at a time. Personally, I prefer installing one at a time in case dependency issues or errors arise. If you just search "conda install {package you want to install}" it should show what command you need to run. Remember that since we have Mamba, we can use that instead. For example, [this](https://anaconda.org/channels/anaconda/packages/jupyter/overview) is how to install Jupyter: `conda install anaconda::jupyter`. The `anaconda::` part is the channel. It's not strictly necessary unless you want it from a particular source. Here, we see the package is `jupyter` (package installation is usually all lowercase), so we can run:

```
mamba install jupyter
```

And then it will ask for confirmation to install. To install the remaining packages, run:

```
mamba install numpy
mamba install polars
mamba install plotnine
```

## Deactivating an Environment

Now that we have installed the packages we need, we are done using our environment for today. We can run:

```
mamba deactivate
```

And you will exit the environment and return to `(base)`. You can alternatively just exit the terminal; it will always open in `(base)`

## Advanced Conda Documentation

From this point forward, I recommend looking at the [Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for how to create environments, activate them, deactivate them, and more. The following specific sections are particularly helpful and relevant:

- [Creating Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
- [Activating an Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
- [Installing Packages](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#installing-packages)
- [Deactivating an Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#deactivating-an-environment)
- [Cloning an Environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#cloning-an-environment)
