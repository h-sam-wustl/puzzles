import pandas as pd
import os

file_dict={}

for filename in os.listdir('mimic-iii'):
    f = os.path.join('mimic-iii', filename)
    # checking if it is a file
    if f[-3:]=='csv':
        file_dict[filename]=pd.read_csv(f)