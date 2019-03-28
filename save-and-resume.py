"""
Code that checks to see if a mid-execution save exists. If not, it will create one after each iteration of the
relevant loop. If so, it will pick up where it left off rather than starting over from the top of the file/dataframe
in question. After the final entry, it will delete the .sav file.
"""

import pandas as pd
import os

# set filename to .sav version, else original
filename = 'filename.csv.sav' \
    if os.path.isfile('filename.csv.sav') \
    else 'filename.csv'


df_from_file = pd.read_csv(filename, header=0, index_col=0)

# If you want to filter an incoming file using a filtering function, this is how you'd do it


def filtering_func(col):
    pass


filtered_df = df_from_file.loc[filtering_func(df_from_file['col_we_care_about'])]  \
    if filename == 'filename.csv.sav' \
    else df_from_file


def audit_value(row):
    return "new value"


for index, row in filtered_df.iterrows():
    df_from_file.loc[index, 'col_we_care_about'] = audit_value(row)
    df_from_file.to_csv('filename.csv.sav')


df_from_file.to_csv('filename.csv')

if os.path.isfile('filename.csv.sav'):
    os.remove('filename.csv.sav')


