import pandas as pd
import json

# constants
file_path = 'Course Books - Audios.xlsx'
output_json_path = 'Course_Books_Audios_Adjusted.json'
base_url = 'https://d2hmvvndovjpc2.cloudfront.net/efe'

def read_excel_file(file_path):
    # Read the Excel file -> return a dataframe
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path} was not found.")
        exit(1)

def clean_data(df):
    # Drop fully empty columns and sort by 'levelColor'
    df = df.dropna(axis=1, how='all')
    return df.sort_values(by='levelColor', ascending=True)

def generate_url(df):
    # Add 'url' column to the df
    # Concatenate file path and file name to generate a complete url for each row
    df['url'] = base_url + df['filepath'].astype(str) + df['filename'].astype(str)
    return df

def convert_to_json_and_save(df, output_json_path):
    # Convert the DataFrame to JSON and save the file
    output_json = df.to_dict(orient='records')
    with open(output_json_path, 'w') as json_file:
        json.dump(output_json, json_file, indent=4)

def main():
    df = read_excel_file(file_path)
    df = clean_data(df)
    df = generate_url(df)
    convert_to_json_and_save(df, output_json_path)

if __name__ == "__main__":
    main()