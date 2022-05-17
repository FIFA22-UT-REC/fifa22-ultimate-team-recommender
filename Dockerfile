# Docker file for fifa 22 ultimate team recommender
# Author : Tony Liang, Chloe Zhang
# Date : May, 2022

# docker run -it --rm -v /$(pwd):/opt/notebooks/ -p 8888:8888 tonyliang19/fifa22-ultimate-team-recommender

# docker build -t <image-name> .   <- this dot means everything 
# docker run -it  <image-name> <- means run interactive 
# docker run -it --rm <image-name> runs interactively and remove it after <exit>
# docker run -it --rm -v /$(pwd): <path-to-store> <img>
# docker run -it --rm -v /$(pwd):/home/folder_name hello-w 

FROM ubcdsci/jupyterlab

RUN conda install --quiet --yes -c conda-forge\
  r-bookdown=0.25 \
  r-docopt=0.7.1  \
  r-devtools=2.4.3 \
  r-knitr=1.38 \
  r-rlang=1.0.2 \
  r-tidyverse=1.3.1 \
  r-tinytex=0.38 \
  r-vctrs=0.4.1
  
# install R packages
RUN Rscript -e "devtools::install_github('FIFA22-UT-Recommender/rfifa', force = TRUE)"

# install dependencies of python 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

