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

Installation
  - Install Python: https://www.python.org/downloads/
  - Install the required library: ```pip install pandas```

Usage
  - Place the Excel file in the same directory as the script.
  - Ensure the Excel file path is 'Course Books - Audios.xlsx'
