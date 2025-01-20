# To-Do List Application

This project is a feature-rich To-Do List application built using Python, SQLite, and a graphical user interface (GUI) powered by `tkinter`. It helps users manage, organize, and track their tasks efficiently.

## Features
- Add new tasks with title, description, and due date.
- View all tasks in a tabular format.
- Update task details, such as marking them as completed or pending.
- Delete tasks from the database.
- Task status management: differentiate between completed and pending tasks.
- Persistent storage of tasks using SQLite.

## File Structure
- **todo_list_gui.py**: Main script that contains the application code.
- **todo_list.db**: SQLite database file automatically created to store tasks.

## How to Use
1. **Add a Task**:
   - Enter the task title, description, and due date in the provided fields.
   - Click the "Add Task" button to save the task.

2. **View Tasks**:
   - All tasks are displayed in a table format with columns for ID, Title, Description, Due Date, and Status.

3. **Delete a Task**:
   - Select a task from the table and click the "Delete Task" button to remove it.

4. **Mark as Completed**:
   - Select a task and click "Mark as Completed" to update its status.

5. **Mark as Pending**:
   - Select a task and click "Mark as Pending" to revert its status.

## Database Schema
The SQLite database contains a single table `tasks` with the following columns:
- `id` (INTEGER, Primary Key): Unique identifier for each task.
- `title` (TEXT): Title of the task.
- `description` (TEXT): Description of the task.
- `due_date` (TEXT): Due date of the task.
- `completed` (INTEGER): Status of the task (0 for pending, 1 for completed).

## Screenshots
- **Main Interface**: Displays the task input fields and task table.
- **Task Actions**: Buttons for adding, deleting, and updating task statuses.

## Future Enhancements
- Add search and filter functionality.
- Add priority levels to tasks.
- Implement notification reminders for due tasks.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or new features.

## License
This project is open-source and available under the MIT License.


