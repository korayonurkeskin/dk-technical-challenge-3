# Course Book Audios Processing Script

## Overview

This Python script processes metadata from the Course Book Audios Excel file. It performs the following tasks:

- **Reads** metadata from the Excel file.
- **Cleans** the data by excluding fully empty columns.
- **Sorts** the data by the 'levelColor' column.
- **Generates URLs:** Concatenates file paths and file names to produce a complete URL for each row.
- **Exports** the processed data into a structured JSON file, saved in the same directory as the script.

## Features

- **Data Reading:** Retrieves metadata from the provided Excel file.
- **Data Cleaning:** Drops fully empty columns to produce a clean DataFrame.
- **Data Sorting:** Sorts the data by the 'levelColor' column.
- **URL Generation:** Creates a new 'url' field by concatenating a base URL with the 'filepath' and 'filename' columns.
- **JSON Export:** Converts the DataFrame into a structured JSON file, preserving the original column order.

## Requirements

- **Python:** Version 3.7 or higher
- **Dependencies:**
  - pandas  
    (Note: The `json` module is part of Python’s standard library)
- **Input File:** The Course Book Audios Excel file (named `Course Books - Audios.xlsx`)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

## Step-by-Step Instructions to Run the Script

1. **Activate Your Virtual Environment (if not already active):**

   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - After activation, your terminal prompt should display `(venv)`.

2. **Install Dependencies:**

   - Run the following command to install required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Place the Excel File:**

   - Ensure that the Excel file, named `Course Books - Audios.xlsx`, is in the same directory as the script.

4. **Run the Script:**

   - Execute the script using:
     ```bash
     python main.py
     ```

5. **Verify the Output:**

   - After the script finishes running, check the project directory for the output JSON file named `Course_Books_Audios_Adjusted.json`.

6. **(Optional) Unit Testing**
   - Includes tests (using Python’s built-in unittest framework) to validate filtering and price updating functionality.
   - Execute:
   ```bash
   python -m unittest test_main.py
   ```
