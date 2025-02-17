Employee Salary Analysis Script

Overview
This Python script processes employee data from a CSV file, computes salary statistics, and outputs the results to a text file. The script performs the following tasks:
1. Reads employee data from `emp_data_v2.csv`.
2. Calculates:
   - The average salary.
   - The highest-paid employee.
   - The number of employees per department.
3. Saves the results to `results.txt`.
4. Displays the highest-paid employee's details in the console.

Prerequisites
- Python 3.x
- A CSV file named `emp_data_v2.csv` containing the following columns:
  - `id` (Employee ID)
  - `name` (Employee Name)
  - `department` (Department Name)
  - `salary` (Employee Salary, numerical value)

Installation
1. Clone or download this repository.
2. Ensure Python 3 is installed on your system.
3. Place `emp_data_v2.csv` in the same directory as the script.

Usage
Run the script using the command:
```sh
python script.py
```

Output
- The highest-paid employee's details will be printed in the console.
- The results will be saved in `results.txt` in the following format:
  ```
  Average Salary: <value>
  Highest Salary: <value> (Employee Name)
  Employees per Department:
  <Department>: <Count>
  ```

Error Handling
- If the CSV file is missing, an error message is displayed.
- Invalid salary values are skipped.
- If no valid employee records are found, the script exits with an appropriate message.

License
This project is open-source and available for modification and distribution.

