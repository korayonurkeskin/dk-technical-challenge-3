Overview
  - This script processes the Excel file that contains metadata about course book audio files to generate a structured JSON file.

Features
  - Reads metadata from the Excel file.
  - Sorts data by the 'sortOrder' column.
  - Concatenates file paths and file names to generate a complete url for each row.
  - Excludes empty columns to produce a clean JSON output
  - Outputs a structured JSON file within the local folder.

Requirements
  - Python 3.7 or higher
  - Required Library: 'pandas'
  - No need to install 'json' as it's part of Python's standard library
  - Download the Course Book Audios Excel File : https://docs.google.com/spreadsheets/d/1eYDa2h6ZOUA0aOZL38EoXSeXD-FC5Tpr_ghcH7iY2HU/edit?usp=sharing

Installation
  - Install Python: https://www.python.org/downloads/
  - Install the required library: ```pip install pandas```

Usage
  - Place the Excel file in the same directory as the script.
  - Ensure the Excel file path is 'Course Books - Audios.xlsx'
  - Run the script: ```python main.py```
  - The JSON file will be saved in the same directory as the script with the name 'Course_Books_Audios_Adjusted.json'
