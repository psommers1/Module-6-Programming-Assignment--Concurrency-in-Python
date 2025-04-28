# Module 6 Programming Assignment - Concurrency in Python

This assignment implements solutions for problems related to file handling, date parsing, and multiprocessing in Python.

## Problems Implemented

### File Handling (Problems 13.1, 13.2, 13.3)
- **13.1**: Write the current date as a string to the text file `today.txt`
- **13.2**: Read the text file `today.txt` into the string `today_string`
- **13.3**: Parse the date from `today_string`

### Multiprocessing (Problem 15.1)
- **15.1**: Use multiprocessing to create three separate processes. Each process waits a random number of seconds between zero and one, prints the current time, and then exits.

## Files Included

- `module6_assignment.ipynb`: Jupyter notebook containing the solutions with explanations
- `module6_assignment.py`: Python script implementing the same solutions

## How to Run

### Running the Python Script

```bash
python module6_assignment.py
```

This will execute all the problems in sequence and display the output in the console.

### Running the Jupyter Notebook

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `module6_assignment.ipynb` in the Jupyter interface
3. Run each cell sequentially to see the output for each problem

## Expected Output

When running the code, you should see:

1. The current date being written to `today.txt`
2. The contents of `today.txt` being read into a string
3. The date being parsed from the string
4. Three separate processes running concurrently, each waiting a random time and printing the current time

## Notes

- The multiprocessing implementation uses Python's `multiprocessing` module to create separate processes
- Each process runs independently with its own memory space
- The random wait time demonstrates how processes can execute concurrently