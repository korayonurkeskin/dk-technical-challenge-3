import pandas as pd
import json

# constants
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

# -------------------------------
# Unit Tests
# -------------------------------
import unittest
import sys
class TestCourseBooks(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        self.sample_data = {
            'levelColor': ['red', 'blue', 'green'],
            'filepath': ['/folder1/', '/folder2/', '/folder3/'],
            'filename': ['file1.mp3', 'file2.mp3', 'file3.mp3'],
            'other_column': [1, 2, 3]
        }
        self.df = pd.DataFrame(self.sample_data)

    def test_clean_data(self):
        # Create a dummy DataFrame with a fully empty column to test cleaning.
        df_dummy = pd.DataFrame({
            'levelColor': ['red', 'blue', 'green'],
            'empty_col': [None, None, None],
            'other_column': [1, 2, 3]
        })
        cleaned = clean_data(df_dummy)
        self.assertNotIn('empty_col', cleaned.columns)

        sorted_levels = list(cleaned['levelColor'])
        self.assertEqual(sorted_levels, sorted(sorted_levels))

    def test_generate_url(self):
        # Test that the 'url' column is added correctly.
        df_with_url = generate_url(self.df.copy())
        self.assertIn('url', df_with_url.columns)
        expected_url = BASE_URL + self.sample_data['filepath'][0] + self.sample_data['filename'][0]
        self.assertEqual(df_with_url.loc[0, 'url'], expected_url)

if __name__ == '__main__':
    # If the script is run with the argument 'test', run unit tests.
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        sys.argv.pop(1)
        unittest.main()
    else:
        main()