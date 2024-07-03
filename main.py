import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import logging
from tkinter.ttk import Progressbar, Style

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(directory, log_widget, progress, file_types):
    report = {folder: 0 for folder in file_types.keys()}  # Initialize a report dictionary to count moved files
    total_files = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])  # Count total files to be organized
    processed_files = 0  # Initialize processed files count

    # Create subdirectories for file types if they don't exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Scan the directory and move files to their subdirectories
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    destination = os.path.join(directory, folder, filename)
                    shutil.move(file_path, destination)
                    log_message = f"Moved: {file_path} to {destination}"
                    logging.info(log_message)
                    log_widget.insert(tk.END, log_message + "\n")
                    log_widget.yview(tk.END)
                    report[folder] += 1
                    processed_files += 1
                    progress['value'] = (processed_files / total_files) * 100
                    progress.update()
                    break

    global report_summary
    report_summary = "Organization Report\n===================\n"
    for folder, count in report.items():
        report_summary += f"{folder}: {count} files moved\n"
    log_widget.insert(tk.END, "Report generated\n")
    log_widget.yview(tk.END)
    messagebox.showinfo("Success", "Files organized! Check the log and report for details.")

def select_directory(log_widget, progress, file_types):
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory, log_widget, progress, file_types)

def display_summary(report):
    summary_window = tk.Toplevel()
    summary_window.title("Summary Report")
    text = tk.Text(summary_window, wrap=tk.WORD, bg='white', fg='black')
    text.pack(padx=10, pady=10)
    text.insert(tk.END, report)

def add_file_type_entry():
    new_window = tk.Toplevel(app)
    new_window.title("Add File Type")

    def add_entry():
        folder = folder_entry.get()
        extensions = extensions_entry.get().split(',')
        if folder and extensions:
            file_types[folder] = [ext.strip() for ext in extensions]
            new_window.destroy()

    tk.Label(new_window, text="Folder Name:").pack(pady=5)
    folder_entry = tk.Entry(new_window)
    folder_entry.pack(pady=5)
    tk.Label(new_window, text="Extensions (comma separated):").pack(pady=5)
    extensions_entry = tk.Entry(new_window)
    extensions_entry.pack(pady=5)
    tk.Button(new_window, text="Add", command=add_entry).pack(pady=10)

# Initialize report_summary variable
report_summary = ""

# Main application setup
app = tk.Tk()
app.title("File Organizer")

style = Style(app)
style.theme_use("default")

frame = tk.Frame(app, padx=10, pady=10, bg='white')
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Choose a folder:", bg='white', fg='black')
label.pack(pady=5)

button = tk.Button(frame, text="Browse", command=lambda: select_directory(log_widget, progress, file_types), bg='white', fg='black')
button.pack(pady=5)

progress = Progressbar(frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.pack(pady=5)

log_label = tk.Label(frame, text="Logs:", bg='white', fg='black')
log_label.pack(pady=5)

log_widget = scrolledtext.ScrolledText(frame, width=50, height=10, wrap=tk.WORD, bg='white', fg='black')
log_widget.pack(pady=5)

file_types_button = tk.Button(frame, text="Add File Type", command=add_file_type_entry, bg='white', fg='black')
file_types_button.pack(pady=5)

summary_button = tk.Button(frame, text="Report", borderwidth=1.5, command=lambda: display_summary(report_summary), bg='white', fg='black')
summary_button.pack(pady=5)

if __name__ == "__main__":
    setup_logging()
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.avi', '.mov'],
        'Music': ['.mp3', '.wav']
    }
    app.mainloop()
