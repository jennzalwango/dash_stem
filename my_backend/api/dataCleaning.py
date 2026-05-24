import pandas as pd
import os
import numpy as np

#access the dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    'data',
    'women_in_stem.csv'
)

#load the dataset
df=pd.read_csv(csv_path)

#read, display the first rows in the dataset
print(df.head()) # get the first rows
print(df.info()) # understand data columns and types

# Clean column names (remove any extra spaces)
df.columns = df.columns.str.strip()

print("\ncleaned column names:")
print(df.columns.tolist())

# Check for duplicate rows
print("Duplicate rows found:", df.duplicated().sum())

# Store row count before dropping duplicates
before_drop = df.shape[0]

# Drop duplicates and save back to df
df = df.drop_duplicates()

# Store row count after dropping duplicates
after_drop = df.shape[0]

