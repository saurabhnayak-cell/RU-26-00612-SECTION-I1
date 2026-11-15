"""
Project Title : Class Marks Analyzer
PS No.        : 18
Language      : Python 3
Description   : Validates class marks and calculates descriptive statistics using NumPy.
"""

import numpy as np


PASS_MARK = 40
MIN_MARK = 0
MAX_MARK = 100


def get_marks():
    """Read and validate marks entered on one line; return a NumPy array."""
    raw_input = input("Enter marks separated by spaces: ").strip()

    if not raw_input:
        raise ValueError("Please enter at least one student's mark.")

    marks = []
    for item in raw_input.split():
        try:
            mark = float(item)
        except ValueError:
            raise ValueError(f"Invalid marks '{item}'. Enter numbers only.")

        if not MIN_MARK <= mark <= MAX_MARK:
            raise ValueError("Marks must be between 0 and 100.")

        marks.append(mark)

    return np.array(marks, dtype=float)


def analyze_marks(marks):
    """Calculate the required statistics and student counts."""
    if not isinstance(marks, np.ndarray):
        marks = np.array(marks, dtype=float)

    if marks.size == 0:
        raise ValueError("At least one mark is required.")

    mean = np.mean(marks)
    median = np.median(marks)
    highest = np.max(marks)
    lowest = np.min(marks)
    std_dev = np.std(marks)  # Population standard deviation (NumPy default)

    passed = int(np.count_nonzero(marks >= PASS_MARK))
    failed = int(marks.size - passed)
    above_average = int(np.count_nonzero(marks > mean))
    pass_percentage = (passed / marks.size) * 100

    return {
        "mean": mean,
        "median": median,
        "highest": highest,
        "lowest": lowest,
        "std_dev": std_dev,
        "passed": passed,
        "failed": failed,
        "total": int(marks.size),
        "pass_percentage": pass_percentage,
        "above_average": above_average,
    }


def display_results(result):
    """Print the analysis in a clear format."""
    print("\n========== CLASS MARKS ANALYSIS ==========")
    print(f"Mean             : {result['mean']:.2f}")
    print(f"Median           : {result['median']:.2f}")
    print(f"Highest mark     : {result['highest']:g}")
    print(f"Lowest mark      : {result['lowest']:g}")
    print(f"Standard deviation: {result['std_dev']:.2f}")
    print(f"Passed           : {result['passed']} of {result['total']}")
    print(f"Failed           : {result['failed']} of {result['total']}")
    print(f"Pass percentage  : {result['pass_percentage']:.2f}%")
    print(f"Above average    : {result['above_average']}")
    print("==========================================")


def main():
    """Program entry point."""
    try:
        marks = get_marks()
        result = analyze_marks(marks)
        display_results(result)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
