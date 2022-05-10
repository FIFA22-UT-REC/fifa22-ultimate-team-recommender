# Author : Tony Liang
# Date : 05-06-2022

"This script process the raw data and filter them to different csv files. It 
takes data file path as argument, and another out directory to store processed
data.

Usage: src/R/process_data.R --file_path=<file_path> --out_path=<>

Options:
    --file_path=<file_path> Path to the raw data
    --out_path=<out_path> Path to store processed data
" -> doc

suppressWarnings(library(tidyverse))
suppressWarnings(library(docopt))
suppressWarnings(library(rfifa))

opt <- docopt(doc)
main <- function(file_path, out_path) {
  
  # value = 0 means "system created player (not real)"
  # best_position from 12 : 21 means legacy players
  
  df <- read_csv(file_path, locale = locale(encoding = "UTF-8")) %>% as.data.frame() %>%
        filter(value != 0, !best_position %in% c("12","13", "14","15","16","17",
                                                 "18","19","20","21")) %>%
        rename(pos = best_position) 
  
  pos_vec<- c("GK","CB","LB","RB","LWB", "RWB",
                "LM","RM","CM","CDM","CAM","CF","LW","RW","ST")

  if (!dir.exists(out_path)) {
  dir.create(out_path,recursive = TRUE)
  }
  invisible(sapply(pos_vec, save_dat, df = df, out_path = out_path))

}

main(opt[["--file_path"]], opt[["--out_path"]])








