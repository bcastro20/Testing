<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt

# Specify the Excel file path using raw string literal
excel_file = r'C:\Users\Brett\Downloads\MSDS-Orientation-Computer-Survey.xlsx'

# Load data from Excel
df = pd.read_excel(excel_file)

# Extract sixth column
column_sixth = df.iloc[:, 5]  # Assuming zero-based indexing

# Create histogram
plt.hist(column_sixth, bins=10, edgecolor='black')  # Adjust bins as needed

# Add labels and title
plt.xlabel('CPU Number of Cores')
plt.ylabel('Frequency')
plt.title('Distribution of MSDS 2024 Cohort CPU Number of Cores')

# Display the plot
plt.show()
=======
print("hello")
>>>>>>> 4c54aea0adb00a91e0b5ede2ab4c9a9ef2c730ba
