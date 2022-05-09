# Docker file for fifa 22 ultimate team recommender
# Tony Liang, May, 2022


# docker build -t <image-name> .   <- this dot means everything 
# docker run -it  <image-name> <- means run interactive 
# docker run -it --rm <image-name> runs interactively and remove it after <exit>
# docker run -it --rm -v /$(pwd): <path-to-store> <img>
# docker run -it --rm -v /$(pwd):/home/folder_name hello-w  

#FROM jupyter/scipy-notebook:8f0a73e76d17
FROM ubcdsci/jupyterlab:v0.9.0
#FROM continuumio/miniconda3
#RUN conda install --quiet --yes -c conda-forge\
#    python \
#    pip \
#    r r r-essentials
    
# install R packages
#Run R -e "install.packages('docopt', repos = 'http://cran.us.r-project.org')"

# install dependencies of python
COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt