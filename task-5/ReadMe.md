# Contact Book Application

A simple contact management application built using Python and Tkinter, with SQLite for database storage. It allows users to add, update, delete, search, and view contacts in a contact book.

## Features
- Add new contacts with Name, Phone, Email, and Address.
- Update existing contacts.
- Delete contacts.
- Search contacts by Name or Phone.
- Display contacts in a user-friendly table format.
- Store contacts in an SQLite database for persistence.

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python installations)
- SQLite (comes with Python by default)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3.x installed on your system.
3. Tkinter and SQLite are included with Python, so no additional installation is needed.

## Usage

1. Run the Python script to launch the Contact Book application.
2. The main window will appear with fields to input Name, Phone, Email, and Address for contacts.
3. Use the **Add Contact** button to add new contacts to the database.
4. To update or delete a contact, select a contact from the contact list displayed in the table, make necessary changes in the fields, and click the **Update Contact** or **Delete Contact** button.
5. Use the **Search** field to search for contacts by Name or Phone.
6. Use the **Clear Fields** button to clear the input fields.
7. View contacts in the table, with columns for ID, Name, and Phone.

### Example
- **Add a Contact:** Enter name "John Doe", phone "123-456-7890", and click "Add Contact".
- **Search for a Contact:** Enter a query like "John" and click "Search".
- **Delete a Contact:** Select a contact from the list and click "Delete Contact".

## Code Overview

### `initialize_database()` function:
- Creates an SQLite database and a `contacts` table if it doesn't already exist.

### `add_contact()` function:
- Adds a new contact to the SQLite database with the provided name, phone, email, and address.

### `view_contacts()` function:
- Fetches and displays all contacts in the contacts table with columns: ID, Name, and Phone.

### `search_contact()` function:
- Allows users to search for contacts by name or phone number.

### `update_contact()` function:
- Updates the selected contact with the values from the input fields.

### `delete_contact()` function:
- Deletes the selected contact from the database.

### Tkinter UI:
- The user interface is created using Tkinter widgets such as `Label`, `Entry`, `Button`, `Treeview`, and `Frame`.
- Contacts are displayed in a `Treeview` widget, and contact details are updated through the input fields.

## License
This project is open-source and available under the MIT License.
