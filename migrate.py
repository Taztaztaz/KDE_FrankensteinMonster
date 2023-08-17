import os
import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory
from os.path import abspath

######################## DEF PART ######################################################################

# Absolute paths to the files
shortcut_path = "~/.config/kglobalshortcutsrc"


#111 Linux distro
def get_linux_distribution():
    command = "lsb_release -a"
    output = subprocess.check_output(command.split()).decode("utf-8")
    return output

def get_desktop_environment():
    command = "echo $XDG_CURRENT_DESKTOP"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    return output.strip()

#222 Folders and Save
def choose_path():
    global save_path
    save_path = askdirectory()
    selected_folder_label.configure(text=save_path)

def copy_home_folder():
    global save_path
    if save_path:
        home_folder = os.path.expanduser("~")
        try:
            shutil.copytree(home_folder, os.path.join(save_path, "Home_Copy"))
            messagebox.showinfo("Copy Complete", "Home folder copied successfully!")
        except Exception as e:
            messagebox.showerror("Copy Error", f"An error occurred: {e}")
    else:
        messagebox.showerror("Path Error", "Please select a destination path first.")


#333 Function to check selected check buttons' values
def save_selected_values():
    selected_files = []
    if checkbox_file1_var.get():
        selected_files.append("shortcut_path")
    if checkbox_file2_var.get():
        selected_files.append(os.path.expanduser("~/file1.txt"))

    if selected_files and save_path:
        try:
            for file in selected_files:
                shutil.copy(file, os.path.join(save_path, os.path.basename(file)))
            messagebox.showinfo("Files Saved", "Selected files saved in the specified path!")
        except Exception as e:
            messagebox.showerror("Copy Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Incomplete Selection", "Please select files and a save path.")

# Function to handle check button selection
def handle_checkbutton():
    print("Check button selected")

###################### OS INF ###########################################################################

# Create a Tkinter window
window = tk.Tk()
window.title("MIGRATE")

#111
#
# Create a text field to display system information
text_field = tk.Text(window, height=10, width=50)
text_field.grid(row=0, column=0, padx=1, pady=1)

# Get system information
distro_info = get_linux_distribution()
desktop_env = get_desktop_environment()

# Display system information in the text field
text_field.insert(tk.END, f"Linux Distribution:\n{distro_info}\n\nDesktop Environment:\n{desktop_env}")
text_field.config(state=tk.DISABLED)

#222
###################### HOME FOLDER SAVE ################################################################
# Create a frame to hold progress bar, save folder button, and output field etc
frame = tk.Frame(window)
frame.grid(row=0, column=1, sticky=tk.W, padx=1, pady=1)

## Create a button to select and save a folder path
select_folder_button = ttk.Button(frame, text="Save Folder Path", command=choose_path)
select_folder_button.grid(row=0, column=0, padx=1, pady=1, sticky=tk.W)

## Create a label to display the selected folder path
selected_folder_label = ttk.Label(frame, text="No folder selected")
selected_folder_label.grid(row=0, column=0, padx=1, pady=1, sticky=tk.E)

## Create a button to copy the home folder
copy_button = ttk.Button(frame, text="Copy Home Folder", command=copy_home_folder)
copy_button.grid(row=1, column=0, padx=1, pady=1, sticky=tk.W)

# Create a progress bar
progress_bar = ttk.Progressbar(frame, mode="determinate", length=400)
progress_bar.grid(row=2, column=0, padx=1, pady=1)

# Create a program output field
output_field = tk.Text(frame, height=5, width=50)
output_field.grid(row=3, column=0, padx=1, pady=1)

#333
####################### TAB LAYOUT ################################################################
# Create a tabbed layout
tab_control = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Tab 1")

# Create checkboxes for selecting files in Tab 1
checkbox_file1_var = tk.BooleanVar()
checkbox_file1 = tk.Checkbutton(tab1, text="System Shortcuts", variable=checkbox_file1_var)
checkbox_file1.pack(pady=5)


# Tab 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Tab 2")

# Create checkboxes for selecting files in Tab 2
checkbox_file2_var = tk.BooleanVar()
checkbox_file2 = tk.Checkbutton(tab2, text="File 2", variable=checkbox_file2_var)
checkbox_file2.pack(pady=5)


# Add the tabbed layout to the window
tab_control.grid(row=1, column=0, rowspan=5, padx=10, pady=10, sticky=tk.W)

#444
################### SAVE BUTTON TO SAVE CHECKBOXES ######################################################
# Create a button to show selected values
button = tk.Button(window, text="SAVE Selected Values", command=save_selected_values)
button.grid(row=2, column=1, padx=10, pady=10)


#
#
# Run the Tkinter event loop
window.mainloop()
