# Docker file for fifa 22 ultimate team recommender
# Author : Tony Liang, Chloe Zhang
# Date : May, 2022

# docker run -it --rm -v /$(pwd):/opt/notebooks/fifa -p 8888:8888 fifa22-ultimate-team-recommender

# docker build -t <image-name> .   <- this dot means everything 
# docker run -it  <image-name> <- means run interactive 
# docker run -it --rm <image-name> runs interactively and remove it after <exit>
# docker run -it --rm -v /$(pwd): <path-to-store> <img>
# docker run -it --rm -v /$(pwd):/home/folder_name hello-w  

FROM ubcdsci/jupyterlab

#RUN conda install --quiet --yes -c conda-forge\
#    python \
#    pip \
#    r r r-essentials
    
# install R packages
Run R -e "install.packages('docopt', repos = 'http://cran.us.r-project.org')"

# install dependencies of python 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

