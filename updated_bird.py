import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Load data - path is relative to repo root
birds = pd.read_csv("bird_list.csv")

# Filter datasets
bird_species = birds[(birds['category'] == 'species') & 
                    (~birds['category'].isna()) & 
                    (birds['category'] != '')]

# Setting current bird of the week
today = datetime.now()
current_week = today.isocalendar()[1]
current_year = today.year
current_seed = int(f'{current_year}{current_week}')
np.random.seed(current_seed)

# generating current bird
current_bird = bird_species.sample(n=1).iloc[0]

# Generating current bird of the week descriptions
range_text = ("its range is unknown"
              if pd.isna(current_bird['range']) or current_bird['range'] == ""
              else f"native to: {current_bird['range']}")

status_text = ("Extant"
               if pd.isna(current_bird['extinct'])
               else f"Extinct ({current_bird['extinct.year']})")
# final description for current
current_bird_sentence = (
    f" Bird of Week {current_week}, {current_year} \n"
    f"The bird of the week is the {current_bird['English name']} "
    f"({current_bird['scientific name']}), a "
    f"{current_bird['order'].lower()} from the "
    f"{current_bird['family'].lower()} family.\n"
    f"{range_text}.\n"
    f"Conservation status: {status_text}.\n\n"
)

# Next weeks bird of the week
next_week_date = today + timedelta(weeks=1)
next_week = next_week_date.isocalendar()[1]
next_year = next_week_date.year
next_seed = int(f"{next_year}{next_week}")
np.random.seed(next_seed)
# Generating next weeks bird of the week
next_bird = bird_species.sample(n=1).iloc[0]

# Generating next weeks bird of the week descriptions
next_range_text = ("its range is unknown"
                   if pd.isna(next_bird['range']) or next_bird['range'] == ""
                   else f"native to: {next_bird['range']}")

next_status_text = ("Extant"
                    if pd.isna(next_bird['extinct'])
                    else f"Extinct ({next_bird['extinct.year']})")
# final description for next weeks bird of the week
next_bird_sentence = (
    f" Preview – Bird of Week {next_week}, {next_year} \n"
    f"The upcoming bird of the week will be the {next_bird['English name']} "
    f"({next_bird['scientific name']}), a "
    f"{next_bird['order'].lower()} from the "
    f"{next_bird['family'].lower()} family.\n"
    f"{next_range_text}.\n"
    f"Conservation status: {next_status_text}.\n"
)
# Write to file
with open("bird_of_the_week.txt", "w") as f:
    f.write(current_bird_sentence)
    f.write(next_bird_sentence)
