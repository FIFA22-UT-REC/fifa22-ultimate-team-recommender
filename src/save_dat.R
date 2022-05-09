#' save_dat , function that filters the raw data and select those players
#' of tha position only, and sort them from largest to minimum in terms of 
#' overall rating, then save them to csv from user input filepath
#' It accepts an unquoted position name eg. CAM or ST, and the  pre loaded df
#' 
#' @param df pre loaded data from process_data.R
#' @param position unquoted string that represents the position interested in filter
#' @param out_path path to store the processed csvs, arg passed from another function
#'
#' @return
#' @export
#'
#' @examples

library(tidyverse)
library(rlang)
library(stringr)
save_dat <- function(df,position,out_path) {
  df %>% filter(pos == position) %>% arrange(desc(overall)) %>%
    write.csv(paste0(out_path, "/", position, ".csv"), fileEncoding = "UTF-8") 
  
  print(paste0(position , " data generated"))
}
