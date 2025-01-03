#File Organizer Application

This is a simple Python-based tool to help organize files in a directory based on their file types (e.g., Images, Documents, Videos, Music). The application uses tkinter for the graphical user interface (GUI) and shutil for moving files into designated subdirectories.

Features:
Automatically organize files by their extensions (e.g., .jpg, .pdf, .mp4, etc...)
Move files into user-defined categories.
Display logs of the files moved during the process.
Progress bar to show the progress of file organization.
Summary report of files moved into each category.
Option to add custom file types and extensions.

Requirements:
Python 3.x
Tkinter (usually included with Python installations)
The logging and shutil libraries (built-in Python libraries)

Installation:
Clone or download this repository.
Make sure you have Python 3.x installed.
Run the application by executing the file_organizer.py script.

Installing Dependencies:
If Tkinter is not installed, you can install it using:

For Windows:

bash
Copy code
pip install tk
For Linux:

bash
Copy code
sudo apt-get install python3-tk
For macOS:

bash
Copy code
brew install python-tk

How to Use:
Select a Directory:

Click the Browse button to select the folder that contains the files you want to organize.
Organize Files:

The application will move files into subdirectories based on their file types (e.g., Images, Documents, Videos, Music).
Add New File Types:

If needed, you can click the Add File Type button to create new categories and assign file extensions to them.
View Logs and Progress:

The logs will show the paths of files being moved. A progress bar will update as files are organized.
View a Report:

After organizing, you can click the Report button to see a summary of how many files were moved into each category.

Key Functions:
setup_logging: Sets up logging to capture and display events during the process.
organize_files: Moves files into the appropriate subdirectories based on their extensions. Updates the progress bar and logs each move.
select_directory: Opens a file dialog to let you choose a directory to organize.
display_summary: Displays a summary of the files moved into each folder.
add_file_type_entry: Allows you to define new file types by specifying a folder and the corresponding file extensions.
Notes:
Files are organized into subdirectories according to their file extensions (e.g., .jpg, .pdf, .mp3).
You can add new file categories (e.g., .xlsx, .mkv) by specifying the folder name and a list of extensions.
If a subdirectory for a file type doesn’t exist, the application will create it automatically
