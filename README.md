# tagtog2df
 
JSON Parser
A python module for parsing .json files into dataframes.

General Functionalities
Parsing .json files into entities and relations dataframes
Merging entities and relations dataframes for multiple .json files into one dataframe
Option to get one dataframe for each .json file or a list of dataframes for multiple .json files
Option to get one dataframe for one .json file or a concatenated dataframe for multiple .json files
How to use
Clone the repository to your local machine

Import the module into your project with the following code:

python
Copy code
from pathlib import Path
import json
import pandas as pd
import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
Use the following functions to parse the .json files:
For parsing one .json file into one dataframe:
scss
Copy code
onefile_onedataframe(pathfile)
For parsing multiple .json files into one dataframe:
```
allfiles_onedataframe(path)
```
For parsing multiple .json files into a list of dataframes:
scss
Copy code
allfiles_listdataframe(path)
Example
Parsing one .json file into one dataframe
scss
Copy code
data = onefile_onedataframe('path/to/json/file')
print(data)
Parsing multiple .json files into one dataframe
scss
Copy code
data = allfiles_onedataframe('path/to/json/folder')
print(data)
Parsing multiple .json files into a list of dataframes
scss
Copy code
data = allfiles_listdataframe('path/to/json/folder')
print(data)
Note: Replace 'path/to/json/file' or 'path/to/json/folder' with the actual path to the .json file or folder.




