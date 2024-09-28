# COM6018 Data Science with Python

*Copyright © Jon Barker, 2023, 2024 University of Sheffield. All rights reserved*

## Welcome

This repository contains the teaching materials and other resources for the module COM6018 Data Science with Python, taught at the University of Sheffield. If you are taking this module please see the [module website](https://vle.shef.ac.uk/ultra/courses/_108012_1/cl/outline) for more information

You can install the materials on your laptop use by 'cloning' this repository. If you have not used git before then please see the instructions below in the section [Using Git](#using-git) below.

The materials in this repository are also available in Jupyter book format at [https://uos-com-6018.github.io/COM6018/](https://uos-com-6018.github.io/COM6018/). The Jupyter book is updated automatically when this repository is updated and so will show the latest version of the materials.

## Contents

The main contents of repository can be found in the `materials` directory. This contains the following subdirectories:

* `lectures` - the markdown source for the lecture slides
* `tutorials` - a set of jupyter notebooks covering the lecture material
* `labs` - the Jupyter notebooks used for the lab classes
* `solutions` - the solutions to the lab classes

## Using Git

If you have not used `git` before you may need to install it on your computer. The instructions depend on your operating system:

* **Linux**: For Debian/Ubuntu run `sudo apt-get install git` and for Fedora run `sudo dnf install git`.
* **MacOS** (e.g., MacBooks): Install the latest version from [this list](https://sourceforge.net/projects/git-osx-installer/files/) by clicking on the link.
* **Windows**: Follow the instructions at <https://gitforwindows.org/>

## Setting up your local environment

First clone the repositry to your local machine:

```bash
git clone https://github.com/UOS-COM-6018/COM6018.git
```

Then make a conda environment from the `com6018.environment.yml` file and activate it,

```bash
cd COM6018
conda env create -n com6018 -f com6018.environment.yml
conda activate com6018
```

You should now be able to open the `ipynb` files. For example, to open the first lab class run:

```bash
jupyter notebook  materials/labs/010_python_intro.ipynb
```

Note, this repository will be updated with new materials regularly throughout the semester. To synchronise your local copy with the master repository run the command:

```bash
git pull
```

If you have changed any of the files you may need to `commit` your changes before you can pull the new files. If you are not sure how to do this please ask for help.
