# Password Generator

A simple password generator built with Python and Tkinter. This application allows users to generate random, secure passwords of a specified length and copy them to the clipboard.

## Features
- Generate random passwords using a mix of letters (uppercase and lowercase), digits, and punctuation symbols.
- Choose the desired length for the generated password.
- Copy the generated password to the clipboard for easy use.
- Handle invalid input (e.g., non-numeric or invalid password length).

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python installations)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.
3. Tkinter should come pre-installed with Python. If not, install it using your package manager.

## Usage

1. Run the Python script to launch the password generator application.
2. Enter the desired password length in the input field.
3. Click the **Generate Password** button to create a random password.
4. The generated password will be displayed below the button.
5. To copy the password to the clipboard, click the **Copy to Clipboard** button.

### Example

- **Enter password length:** 12
- **Generated Password:** `aF9#lY2!3kG9`
- **Copy to Clipboard:** Copies the generated password to your clipboard.

## Error Handling

- **Invalid Length:** If you enter a non-numeric or invalid password length (less than 1), an error message will appear.
- **Empty Password:** If you attempt to copy an empty password (before generating one), an error message will appear.

## Code Overview

### `generate_password()` function:
- Retrieves the length of the password from the user.
- Validates the length input.
- Generates a random password using uppercase letters, lowercase letters, digits, and punctuation.

### `copy_to_clipboard()` function:
- Copies the generated password to the clipboard.
- Shows an error message if no password has been generated yet.

### Tkinter UI:
- The user interface is built using Tkinter widgets such as `Entry`, `Button`, and `Label`.
- The application allows users to generate and copy passwords in a few simple steps.

## License
This project is open-source and available under the MIT License.

