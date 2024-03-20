import os
import pandas as pd
import glob

inputDataLocation = '/Users/rich/git/pythonScripts/dataAnalysis/inputData'

joinedFiles = os.path.join(inputDataLocation, '*.csv')

joinedList = glob.glob(joinedFiles)

df = pd.concat(map(pd.read_csv, joinedList), ignore_index=True)
df.to_csv('/Users/rich/git/pythonScripts/dataAnalysis/mergeCSV/merged.csv', index=False)

print(f'{len(joinedList)} Files Merged')