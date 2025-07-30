import pandas as pd
import numpy as np
from datetime import datetime
import os

# Load data - path is relative to repo root
birds = pd.read_csv("bird_list.csv")

# Show unique categories (optional - can remove)
print("Unique categories:", birds['category'].unique())

# Filter datasets
bird_species = birds[(birds['category'] == 'species') & 
                    (~birds['category'].isna()) & 
                    (birds['category'] != '')]

# Set seed based on current week
current_week = datetime.now().isocalendar()[1]
np.random.seed(current_week)

# Select random bird
weekly_bird = bird_species.sample(n=1).iloc[0]

# Generate description
range_text = ("its range is unknown" 
             if pd.isna(weekly_bird['range']) or weekly_bird['range'] == "" 
             else f"native to: {weekly_bird['range']}")

status_text = ("Extant" 
              if pd.isna(weekly_bird['extinct']) 
              else f"Extinct ({weekly_bird['extinct.year']})")

bird_sentence = (
    f"This week's bird of the week is the {weekly_bird['common.name']} "
    f"({weekly_bird['scientific.name']}), a "
    f"{weekly_bird['order'].lower()} from the "
    f"{weekly_bird['family'].lower()} family. "
    f"{range_text}. "
    f"Conservation status: {status_text}."
)

# Write to file
with open("bird_of_the_week.txt", "w") as f:
    f.write(bird_sentence)

print("Successfully generated bird_of_the_week.txt")
