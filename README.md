Overview
This script processes the Excel file that contains metadata about course book audio files to generate a structured JSON file.

Features
  - Reads metadata from the Excel file.
  - Sorts data by the 'sortOrder' column.
  - Concatenates file paths and file names to generate a complete url for each row.
  - Excludes empty columns to produce a clean JSON output
  - Outputs a structured JSON file within the local folder.
