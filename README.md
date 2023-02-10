# tagtog2df
This repository provides three main functionalities to convert tagtag JSON files into a pandas dataframe format. The functionalities are:

* `allfiles_onedataframe`: converts all JSON files in a given directory into one big dataframe.
* `allfiles_listdataframe`: converts all JSON files in a given directory into a list of separate dataframes.
* `onefile_onedataframe`: converts a single JSON file into one dataframe.

# Example Usage
Consider a directory data that contains three JSON files: file1.json, file2.json, and file3.json.

```
import logging
import pandas as pd
from pathlib import Path
from json_to_dataframe import allfiles_onedataframe, allfiles_listdataframe, onefile_onedataframe

# Example 1: convert all JSON files in a directory into one big dataframe
path = Path('data')
df = allfiles_onedataframe(path)
print(df)

# Example 2: convert all JSON files in a directory into a list of separate dataframes
df_list = allfiles_listdataframe(path)
for df in df_list:
    print(df)

# Example 3: convert a single JSON file into one dataframe
file = Path('data/file1.json')
df = onefile_onedataframe(file)
print(df)
```
# Note
It is recommended to set the logging level to logging.INFO to see the log messages during execution.



