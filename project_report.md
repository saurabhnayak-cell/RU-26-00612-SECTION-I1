# Project Report – Class Marks Analyzer

## 1. Problem Statement
Create a Python 3 program that takes the marks of a class as a list, validates them, and uses NumPy to calculate the mean, median, highest, lowest, standard deviation, pass count, and number of students above average.

## 2. Concepts Used
- Python lists and NumPy arrays
- Functions and exception handling
- Input validation
- NumPy statistical functions
- Conditional counting

## 3. Algorithm
1. Read marks as space-separated input.
2. Check that at least one mark has been entered.
3. Convert each value to a number.
4. Reject non-numeric values and values outside 0–100.
5. Convert the validated list to a NumPy array.
6. Calculate mean, median, maximum, minimum, and population standard deviation.
7. Count marks greater than or equal to 40 as passed.
8. Count marks below 40 as failed.
9. Count marks strictly greater than the mean as above average.
10. Display the results in a formatted manner.

## 4. NumPy Functions
| Function | Purpose |
|---|---|
| `np.mean()` | Calculates arithmetic mean |
| `np.median()` | Calculates median |
| `np.max()` | Finds highest mark |
| `np.min()` | Finds lowest mark |
| `np.std()` | Calculates population standard deviation by default |
| `np.count_nonzero()` | Counts values meeting a condition |

## 5. Validation
- Only numeric values are accepted.
- Every mark must be between 0 and 100, inclusive.
- Empty input is rejected.
- The program reports a clear error and stops processing invalid input.

## 6. Test Results
All four test cases and their expected outputs are provided in `sample_outputs.txt`.

## 7. Conclusion
The Class Marks Analyzer demonstrates the use of Python functions, lists, NumPy arrays, validation, and statistical calculations to analyze a class's performance.
