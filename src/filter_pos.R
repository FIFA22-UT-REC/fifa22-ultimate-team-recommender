#' filter_pos , function that filters the raw data and select those players
#' of tha position only, and sort them from largest to minimum in terms of 
#' overall rating.It accepts an unquoted position name eg. CAM or ST, and the 
#' pre loaded df 
#' 
#' @param df pre loaded data from process_data.R
#' @param position unquoted string that represents the position interested in filter
#'
#' @return
#' @export
#'
#' @examples

library(tidyverse)
library(rlang)
library(stringr)
filter_pos <- function(df,position) {
  df %>% filter(pos == position) %>% arrange(desc(overall))
}
