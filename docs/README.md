
# FIFA 22 Ultimate Team Recommender

## Overview

This is project using Python to scrap FIFA player data from an open
source website [SoFIFA](https://sofifa.com/) and apply automated
non-interacitve scripts to process crawled data, then fit models to
player statistics to setup a recommender (With UI) of players in FIFA22
given user inputs as constraints eg. budget, potential, attribute and
etc.

## Authors:

**Chloe Zhang**:

-   [GitHub](https://github.com/ZiyueChloeZhang)

**Jinghan Xu**:
- <jh0220x@gmail.com>

**Minting Fu**

- <mminting@student.ubc.ca>

**Muke Wang**

- <shaodwaaron@gmail.com>


**Shiyang Zhang**

- <harryzhang957@gmail.com>

**Tony Liang**:

-   <chunqingliang@gmail.com>

-   [GitHub](https://github.com/tonyliang19)

## Usage of the project (Instructions)

#### 1. Without using Docker

To replicate this project, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
command at the command line/terminal from the root directory of this
project:

    make all

To reset the repo to a clean state, with no intermediate or results
files, run the following command at the command line/terminal from the
root directory of this project:

    make clean

#### 2. Using Docker to run on Jupyter lab

1)  Clone this GitHub repository and run the following code in the
    terminal

`git clone https://github.com/FIFA22-UT-Recommender/fifa22-ultimate-team-recommender`

2)  Run this firstly in your terminal to pull latest docker image

`docker pull tonyliang19/fifa22-ultimate-team-recommender`

3)  Run the following command to run the container based on the latest
    image

`docker run -it --rm -v /$(pwd):/opt/notebooks/ -p 8888:8888 tonyliang19/fifa22-ultimate-team-recommender`

4)  After the command runs, copy the last link in your terminal similar
    to the following:

`http://127.0.0.1:8888/lab?token=f4eef0c11762e60a7974f3ea3eb352a4913e70755433398b`
and open it on any browser like Google Chrome or Mozilla Firefox.

Then you should be able to run and explore the project interactively!

## Dependencies

-   Python 3.9.5 and Python packages:
    -   aiohttp=3.8.1
    -   awscli=1.25.2
    -   beautifulsoup4=4.11.1
    -   bs4=0.0.1
    -   certifi=2021.10.8
    -   chardet=4.0.0
    -   charset-normalizer=2.0.12
    -   idna==3.3
    -   fifa-pack=0.0.3
    -   numpy=1.22.3
    -   pandas=1.4.2
    -   pathlib=1.0.1
    -   python-dateutil=2.8.2
    -   pytz=2022.1
    -   requests=2.27.1
    -   six=1.16.0
    -   soupsieve=2.3.2.post1
    -   urllib3=1.26.9
-   R version 4.1.1 and R packages:
    -   bookdown=0.25
    -   docopt=0.7.1
    -   devtools=2.4.3
    -   knitr=1.38
    -   rfifa=1.0.0
    -   rlang=1.0.2
    -   tidyverse=1.3.1
    -   tinytex=0.38
    -   vctrs=0.4.1
-   GNU make 4.3

## License

The underlying source code used to format and display the content of
this project is licensed under the [MIT License](LICENSE)
