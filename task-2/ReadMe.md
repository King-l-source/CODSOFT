# Simple Calculator

A basic calculator application built using Python and the Tkinter library. It allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- Perform addition, subtraction, multiplication, and division.
- Handle division by zero error.
- Validate numeric input.
- Display result dynamically after calculation.

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python installations)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.
3. Tkinter should come pre-installed with Python. If not, install it using your package manager.

## Usage

1. Run the Python script.
2. The application window will appear with two input fields for numbers and a dropdown to select an operation.
3. Enter two numbers and choose an operation (Addition, Subtraction, Multiplication, or Division).
4. Press the **Calculate** button to see the result displayed below.

### Example

- **Enter first number:** 10
- **Enter second number:** 5
- **Select Operation:** Addition
- **Result:** 15.0

## Error Handling

- **Invalid Input:** If a non-numeric value is entered, an error message will appear.
- **Division by Zero:** If you try to divide by zero, an error message will be shown.

## Code Overview

### `perform_calculation()` function:
- Retrieves input values from the user.
- Performs the selected arithmetic operation.
- Displays the result or shows an error message if necessary.

### Tkinter UI:
- The application window is created using Tkinter widgets such as `Entry`, `Label`, `Button`, and `OptionMenu`.
- User input is validated and the result is dynamically updated in the interface.

## License
This project is open-source and available under the MIT License.
