Employee Data Processing Script

Overview:
This Python script reads employee data from a CSV file, calculates salary statistics, and writes the results to a text file. The script performs the following tasks:
1. Reads employee data from `emp_data_v2.csv`
2. Calculates the average salary, highest-paid employee, and the number of employees per department
3. Saves the results to `results.txt`
4. Prints the highest-paid employee's details to the console

Prerequisites:
- Python 3.x
- A CSV file named `emp_data_v2.csv` with the following columns:
  - `id` (Employee ID)
  - `name` (Employee Name)
  - `department` (Department Name)
  - `salary` (Employee Salary)

Installation:
1. Clone or download this repository.
2. Ensure Python 3 is installed on your system.
3. Place the `emp_data_v2.csv` file in the same directory as the script.

Usage:
Run the script using the command:
```sh
python script.py
```

Output:
- The script prints the highest-paid employee's details to the console.
- The results are saved in `results.txt` with the following format:
  ```
  Average Salary: <value>
  Highest Salary: <value> (Employee Name)
  Employees per Department:
  <Department>: <Count>
  ```

Error Handling:
- If the CSV file is missing, the script displays an error message.
- If any salary values are invalid, they are skipped.
- If no valid employee records are found, the script exits with an appropriate message.

License
This project is open-source and available for modification and distribution.

