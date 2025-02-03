import pandas as pd
import json

FILE_NAME = 'Course Books - Audios.xlsx'
OUTPUT_FILE_NAME = 'Course_Books_Audios_Adjusted.json'
BASE_URL = 'https://d2hmvvndovjpc2.cloudfront.net/efe'

def read_excel_file(FILE_NAME):
    """
    Read the Excel file -> return a dataframe
    """
    try:
        return pd.read_excel(FILE_NAME)
    except Exception as e:
        raise RuntimeError(f"Error reading the Excel file: {e}")

def clean_data(df):
    """
    Drop fully empty columns and sort by 'levelColor'
    """
    df = df.dropna(axis=1, how='all')
    return df.sort_values(by='levelColor', ascending=True)

def generate_url(df):
    """
    Add 'url' column to the df
    Concatenate file path and file name to generate a complete url for each row
    """
    df['url'] = BASE_URL + df['filepath'].astype(str) + df['filename'].astype(str)
    return df

def convert_to_json_and_save(df, OUTPUT_FILE_NAME):
    """
    Convert the DataFrame to JSON and save the file
    """
    output_json = df.to_dict(orient='records')
    with open(OUTPUT_FILE_NAME, 'w') as json_file:
        json.dump(output_json, json_file, indent=4)

def main():
    df = read_excel_file(FILE_NAME)
    df = clean_data(df)
    df = generate_url(df)
    convert_to_json_and_save(df, OUTPUT_FILE_NAME)

if __name__ == "__main__":
    main()