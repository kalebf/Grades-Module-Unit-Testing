# Grades Module and Unit Testing
## Description:
This project contains two main files: Grades.py, which implements functions to calculate the total, average, and median of a list of numbers, and test_grades.py, which contains unit tests to ensure the correctness of those functions. The program handles typical scenarios such as calculating values for lists with numbers, handling empty lists gracefully, and providing precise floating-point results where necessary.

## Grades Module Functions:
1. **total(values: list) -> float**  
   Returns the sum of all elements in the `values` list. If the list is empty, it returns 0.
   
2. **average(values: list) -> float**  
   Returns the arithmetic mean (average) of the elements in the `values` list. If the list is empty, it returns `math.nan`.
   
3. **median(values: list) -> float**  
   Returns the median of the elements in the `values` list. If the list is empty, it raises a `ValueError`. For an even number of elements, it returns the average of the two middle values.

## Unit Testing (test_grades.py):
The `test_grades.py` module contains unit tests to verify the functionality of the `Grades.py` functions:
1. **Total Function Tests**:
   - Verifies that the `total` function correctly sums a list of numbers.
   - Ensures the function returns 0 when given an empty list.
   
2. **Average Function Tests**:
   - Verifies the average function calculates the correct mean of a list.
   - Ensures precision by checking up to 5 decimal places.
   - Checks that the function returns `math.nan` when given an empty list.
   
3. **Median Function Tests**:
   - Checks that the median function works for both odd and even-length lists.
   - Verifies that a `ValueError` is raised when given an empty list.

## How to Run the Program
1. Clone or download this repository to your local machine.
2. Ensure Python 3.x is installed on your machine.
3. To run the unit tests, make sure `unittest` is available (it comes with Python by default).
4. Run the tests and you should get an output with the tests ran and the time it took to run them. 

