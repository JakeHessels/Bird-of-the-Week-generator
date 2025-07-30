library(tidyverse)

#Change file path
birds <- read.csv("/bird_list.csv")
#showing all unique categoires in category
unique(birds$category)

#filtering to smaller data sets
bird_family <- birds %>%
  filter(category == 'family' & !is.na(category) & category != '')
bird_species <- birds %>%
  filter(category == 'species' & !is.na(category) & category != '')
bird_subspecies <- birds %>%
  filter(category == 'subspecies' & !is.na(category) & category != '')

#set seed based on current week
current_week <- as.numeric(strftime(Sys.Date(), format = "%V"))
set.seed(current_week)

weekly_birds <- bird_species %>% 
  sample_n(1)

#Short term information bird of the week write up
## Handle range (blank/NA becomes "unknown")
range_text <- ifelse(is.na(weekly_bird$range) | weekly_bird$range == "", 
                     "its range is unknown", 
                     paste0("native to: ", weekly_bird$range))

## Determining status
status_text <- ifelse(is.na(weekly_bird$extinct),
                      "Extant",
                      paste0("Extinct (", weekly_bird$extinct.year, ")"))

##full sentance
bird_sentence <- paste0(
  "This week's bird of the week is the ", weekly_bird$common.name, 
  " (", weekly_bird$scientific.name, "), a ", 
  tolower(weekly_bird$order), " from the ", 
  tolower(weekly_bird$family), " family. ",
  range_text, ". ",
  "Conservation status: ", status_text, "."
)

bird_sentence

writeLines(bird_sentence, "bird_of_the_week.txt")
