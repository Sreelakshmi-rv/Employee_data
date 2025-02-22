Data Cleaning Script

Overview:
This Python script loads a dataset, performs data cleaning operations such as handling missing values, validating email addresses and phone numbers, removing duplicates, and filtering out outliers. The cleaned dataset is then saved as a CSV file.

Prerequisites:
Ensure you have the following installed on your system:
- Python 3.x
- Pandas library (`pip install pandas`)
- NumPy library (`pip install numpy`)

Setup Instructions:
1. Download the dataset: Place your `customers.csv` file in a known directory (e.g., `D:\Downloads\customers.csv`).
2. Update the file paths: In the script, update the `file_path` and `final_cleaned_file_path` variables to match the location of your dataset and where you want to save the cleaned data.

Running the Script:
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved using `cd` command.
3. Run the script using:
   ```sh
   python script_name.py
   ```
   (Replace `script_name.py` with your actual script filename.)

Expected Output:
- The script will print information about the dataset, such as missing values, duplicate counts, and invalid emails/phone numbers.
- After processing, a cleaned CSV file will be saved at the specified path (`D:\Downloads\customers_final.csv`).
- The script will output:
  - Initial dataset information
  - Count of missing values before and after cleaning
  - Number of duplicate records removed
  - Count of invalid emails and phone numbers
  - Number of outliers removed
  - Confirmation message that the cleaned dataset has been saved.

Troubleshooting:
- ModuleNotFoundError: If you get an error about missing modules, install the required libraries using:
  ```sh
  pip install pandas numpy
  ```
- FileNotFoundError: Ensure the dataset path is correct and the file exists.
- PermissionError: If the script fails to save the file, try running Python as an administrator or change the save location.

Notes:
- The script assumes phone numbers are 10 digits long and standardizes them to a format like `+1-XXXXXXXXXX`.
- Invalid email addresses are marked as "Invalid".
- The script filters out purchase amounts that are extreme outliers based on the IQR method.
- You can modify the `standardize_phone` function if phone numbers follow different country formats.

License:
This script is free to use and modify for personal or educational purposes.
