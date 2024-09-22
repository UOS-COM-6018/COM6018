# COM6018 Data Science with Python

*Copyright © Jon Barker, 2023, 2024 University of Sheffield. All rights reserved*

## Welcome

This repository contains the teaching materials and other resources for the module COM6018 Data Science with Python, taught at the University of Sheffield.

If you are taking this module please see the [module website](https://vle.shef.ac.uk/ultra/courses/_108012_1/cl/outline) for more information and please use `git` to clone this repository to your own computer. The repository will be updated throughout the module and you will need to `git pull` regularly to get the latest materials.

The materials in this repository are also available in Jupyter book format at [https://uos-com-6018.github.io/COM6018/](https://uos-com-6018.github.io/COM6018/).

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
