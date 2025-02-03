# -------------------------------
# Unit Tests
# -------------------------------

import unittest
import pandas as pd
from main import clean_data, generate_url, BASE_URL

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
        # Verify that the empty column is dropped.
        self.assertNotIn('empty_col', cleaned.columns)
        # Verify the DataFrame is sorted by 'levelColor' in ascending order.
        sorted_levels = list(cleaned['levelColor'])
        self.assertEqual(sorted_levels, sorted(sorted_levels))

    def test_generate_url(self):
        # Test that the 'url' column is added correctly.
        df_with_url = generate_url(self.df.copy())
        self.assertIn('url', df_with_url.columns)
        expected_url = BASE_URL + self.sample_data['filepath'][0] + self.sample_data['filename'][0]
        self.assertEqual(df_with_url.loc[0, 'url'], expected_url)

if __name__ == '__main__':
    unittest.main()