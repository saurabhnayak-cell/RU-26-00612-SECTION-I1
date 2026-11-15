# Class Marks Analyzer

**PS No.:** 18  
**Language:** Python 3  
**Library:** NumPy

## Objective
Create a console program that accepts a class's marks, validates the input, and calculates the mean, median, highest mark, lowest mark, population standard deviation, pass count, fail count, pass percentage, and number of students scoring above the average.

## Requirements
- Python 3.8 or later
- NumPy

## Installation
```bash
python -m pip install -r requirements.txt
```

## Run
```bash
python class_marks_analyzer.py
```
Enter all marks on one line, separated by spaces. Each mark must be numeric and in the inclusive range 0–100.

## Rules
- Pass mark: **40** (a score of 40 is a pass).
- Valid marks: **0 to 100**, inclusive.
- Standard deviation: population standard deviation, calculated using `numpy.std()` (NumPy's default `ddof=0`).
- Above average: counts marks strictly greater than the class mean.
- At least one mark is required.

## Program structure
- `get_marks()` reads and validates the input and returns a NumPy array.
- `analyze_marks(marks)` calculates all statistics and counts.
- `display_results(result)` prints the results.
- `main()` controls execution and handles validation errors.

## Test cases
See [sample_outputs.txt](sample_outputs.txt) for the four test cases and their expected results.
