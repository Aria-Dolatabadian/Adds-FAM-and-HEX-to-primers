#Generates random primers 

import pandas as pd
import random
import string

# Function to generate a random DNA sequence of a given length
def generate_random_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

# Function to generate a DataFrame with random primer data
def generate_primer_data(num_entries):
    data = {
        'Forward_A1_Name': [f'Forward_A1_{i}' for i in range(1, num_entries + 1)],
        'Forward_A1_Sequence': [generate_random_sequence(20) for _ in range(num_entries)],
        'Forward_A2_Name': [f'Forward_A2_{i}' for i in range(1, num_entries + 1)],
        'Forward_A2_Sequence': [generate_random_sequence(20) for _ in range(num_entries)],
        'Common_Reverse_Name': [f'Common_Reverse_{i}' for i in range(1, num_entries + 1)],
        'Common_Reverse_Sequence': [generate_random_sequence(20) for _ in range(num_entries)]
    }
    return pd.DataFrame(data)

# Generate primer data with 10 entries (you can change this number)
primer_data = generate_primer_data(10)

# Export the DataFrame to CSV
primer_data.to_csv('primer_data.csv', index=False)



#Adds FAM and HEX sequences to the beginning of each primer sequence


import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

# Read the CSV file
primer_data = pd.read_csv('primer_data.csv')

# Add FAM and HEX sequences to the beginning of each primer sequence
fam_sequence = 'GAAGGTGACCAAGTTCATGCT'
hex_sequence = 'GAAGGTCGGAGTCAACGGATT'

primer_data['Forward_A1_Sequence'] = fam_sequence + primer_data['Forward_A1_Sequence']
primer_data['Forward_A2_Sequence'] = hex_sequence + primer_data['Forward_A2_Sequence']

# Create a new Excel workbook
wb = Workbook()

# Create a new sheet in the workbook
ws = wb.active

# Write header row to the sheet
ws.append(primer_data.columns.tolist())

# Write data to the sheet
for r_idx, row in primer_data.iterrows():
    ws.append(row.tolist())  # Convert Series to list before appending


# Save the workbook to an Excel file
wb.save('modified_primer_data.xlsx')
