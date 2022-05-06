# Docker file for fifa 22 ultimate team recommender
# Tony Liang, May, 2022

# use rocker/tidyverse as the base image
FROM jupyter/scipy-notebook:8f0a73e76d17

USER root
RUN conda install --quiet --yes -c conda-forge\
    pip \
    r r r-essentials
    
# install R packages
Run R -e "install.packages('docopt', repos = 'http://cran.us.r-project.org')"

# install dependencies of python
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt