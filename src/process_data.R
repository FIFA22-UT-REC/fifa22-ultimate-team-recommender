# Author : Tony Liang
# Date : 05-06-2022

"This script process the raw data and filter them to different csv files. It 
takes data file path as argument, and another out directory to store processed
data.

Usage: src/process_data.R --file_path=<file_path> --out_path=<>

Options:
    --file_path=<file_path> Path to the raw data
    --out_path=<out_path> Path to store processed data
" -> doc
install.packages("docopt", repos = "http://cran.us.r-project.org")
library(tidyverse)
library(docopt)
library(rlang)
source("src/filter_pos.R")

opt <- docopt(doc)
main <- function(file_path, out_path) {
  
  # value = 0 means "system created player (not real)"
  # best_position from 12 : 21 means legacy players
  
  df <- read_csv(file_path) %>% as.data.frame() %>%
        filter(value != 0, !best_position %in% c("12","13", "14","15","16","17",
                                                 "18","19","20","21")) %>%
        rename(pos = best_position) 

  if (!dir.exists(out_path)) {
  dir.create(out_path,recursive = TRUE)
  }
  st <- filter_pos(df,"ST") %>%  write.csv(paste0(out_path, "/ST.csv"))
  cf <- filter_pos(df,"CF") %>%  write.csv(paste0(out_path, "/CF.csv"))
  cam <- filter_pos(df,"CAM") %>%  write.csv(paste0(out_path, "/CAM.csv"))
  cm <- filter_pos(df,"CM") %>% write.csv(paste0(out_path, "/CM.csv"))
  cdm <- filter_pos(df,"CDM") %>%  write.csv(paste0(out_path, "/CDM.csv"))
  lm <- filter_pos(df,"LM") %>%  write.csv(paste0(out_path, "/LM.csv"))
  rm <- filter_pos(df,"RM") %>%  write.csv(paste0(out_path, "/RM.csv"))
  lw <- filter_pos(df,"LW") %>%  write.csv(paste0(out_path, "/LW.csv"))
  rw <- filter_pos(df,"RW") %>%  write.csv(paste0(out_path, "/RW.csv"))
  lwb <- filter_pos(df,"LWB") %>%  write.csv(paste0(out_path, "/LWB.csv"))
  rwb <- filter_pos(df,"RWB") %>%  write.csv(paste0(out_path, "/RWB.csv"))
  lb <- filter_pos(df,"LB") %>%  write.csv(paste0(out_path, "/LB.csv"))
  rb <- filter_pos(df,"RB") %>%  write.csv(paste0(out_path, "/RB.csv"))
  cb <- filter_pos(df,"CB") %>%  write.csv(paste0(out_path, "/CB.csv"))
  gk <- filter_pos(df,"GK") %>%  write.csv(paste0(out_path, "/GK.csv"))

}

main(opt[["--file_path"]], opt[["--out_path"]])

