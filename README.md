
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

## How it works

The principle of our recommended system is that: According to what player the user is looking for, find the player with the lowest price.

##### For example:
Imagine if a user wants to find a substitution of L.messi in his team. After he input the data of L.messi into our system, we would
recommend the slightly cheaper players that is most similar to L.messi(in terms of skills)

### 1 Train our model

#### 1.1 Label players by their value(price)



##### example:
| Player      | Price  | Label |
| ----------- | ------ | ----- |
| L.Messi     | €69.5M	    | 1     |
| D.Malen     | €28.5M	     | 2     |
| E.Ferguson  | €3.6M	     | 3     |


#### 1.2 Using Quadratic Discriminant Analysis (QDA) model to find decision boundary.
![This is an image](https://yintingchou.com/posts/2017-03-13-lda-and-qda/ldaqda_2.png)

### 2 Predict the label of player that the user want

#### 2.1 Ask user input

- [x] Postion of the player (eg: LB, ST, CAM)
- [x] Age of the player
- [x] Height of the player
- [x] Different Skill of the player

#### 2.2 Using Quadratic Discriminant Analysis (QDA) model to label the player.

### 3 Recommend a list of players to user
##### example:
If label of the player that the user want to find is labeled as 2 by the QDA model, we would recommend the nearest player that labeled as 3

![This is an image](https://raw.githubusercontent.com/FIFA22-UT-REC/fifa22-ultimate-team-recommender/main/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220601203157.png)



![This is an image](https://github.com/FIFA22-UT-REC/fifa22-ultimate-team-recommender/blob/main/pics/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220601203408.png)
## Dependencies

-   Python 3.9.5 and Python packages:
    -   beautifulsoup4=4.11.1
    -   bs4=0.0.1
    -   certifi=2021.10.8
    -   chardet=4.0.0
    -   charset-normalizer=2.0.12
    -   idna==3.3
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
