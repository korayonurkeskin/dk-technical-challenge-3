import pandas as pd
import json

file_path = 'Course Books - Audios.xlsx'

# Read the Excel file
sheet_df = pd.read_excel(file_path)

# Sort the data by 'sortOrder'
sorted_df = sheet_df.sort_values(by='sortOrder', ascending=True)

# Add 'url' field to each row by combining 'filepath' and 'filename'
sorted_df['url'] = 'https://d2hmvvndovjpc2.cloudfront.net/efe' + sorted_df['filepath'].astype(str) + sorted_df['filename'].astype(str)

# Convert the DataFrame to JSON
output_json = sorted_df.to_dict(orient='records')

# Save the JSON data into a file
output_json_path = 'Course_Books_Audios_Adjusted.json'
with open(output_json_path, 'w') as json_file:
    json.dump(output_json, json_file, indent=4)