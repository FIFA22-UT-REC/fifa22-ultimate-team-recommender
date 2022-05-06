# Docker file for fifa 22 ultimate team recommender
# Tony Liang, May, 2022

# use rocker/tidyverse as the base image
FROM rocker/tidyverse

# install python packages
RUN apt-get update && apt-get install -y --no-install-recommends r-base python3.9 python3-pip

# install R packages
Run R -e "install.packages('docopt')"

# install dependencies of python
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt