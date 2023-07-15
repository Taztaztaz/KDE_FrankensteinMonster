import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askdirectory

#1111
def get_linux_distribution():
    command = "lsb_release -a"
    output = subprocess.check_output(command.split()).decode("utf-8")
    return output

def get_desktop_environment():
    command = "echo $XDG_CURRENT_DESKTOP"
    output = subprocess.check_output(command, shell=True).decode("utf-8")
    return output.strip()

#222
def save_folder():
    folder_path = askdirectory()
    selected_folder_label.configure(text=folder_path)


#333 Function to display selected check buttons' values
def save_selected_values():
    selected_values = []
    for check_button in check_buttons:
        if check_button.get():
            selected_values.append(check_button["text"])
    messagebox.showinfo("Selected Values", "Selected Check Buttons:\n" + "\n".join(selected_values))

# Function to handle check button selection
def handle_checkbutton():
    print("Check button selected")
######################################################################################################
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
#
# Create a frame to hold progress bar, save folder button, and output field
frame = tk.Frame(window)
frame.grid(row=0, column=1, sticky=tk.W, padx=1, pady=1)

## Create a button to select and save a folder path
select_folder_button = ttk.Button(frame, text="Save Folder", command=save_folder)
select_folder_button.grid(row=0, column=0, padx=1, pady=1, sticky=tk.W)

## Create a label to display the selected folder path
selected_folder_label = ttk.Label(frame, text="No folder selected")
selected_folder_label.grid(row=0, column=0, padx=1, pady=1, sticky=tk.E)

# Create a progress bar
progress_bar = ttk.Progressbar(frame, mode="determinate", length=400)
progress_bar.grid(row=1, column=0, padx=1, pady=1)

# Create a program output field
output_field = tk.Text(frame, height=5, width=50)
output_field.grid(row=3, column=0, padx=1, pady=1)

#333
#
# Create a tabbed layout
tab_control = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Save Current System Settings")


# Create check buttons on Tab 1
setting_checkbutton_tab1 = tk.Checkbutton(tab1, text="Settings", command=handle_checkbutton)
setting_checkbutton_tab1.grid(pady=10)

shortcut_checkbutton_tab1 = tk.Checkbutton(tab1, text="Shortcuts", command=handle_checkbutton)
shortcut_checkbutton_tab1.grid(pady=10)

# Tab 2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Invoke Old Config")

# Create check buttons on Tab 2
setting_checkbutton_tab2 = tk.Checkbutton(tab2, text="Settings", command=handle_checkbutton)
setting_checkbutton_tab2.grid(pady=10)

shortcut_checkbutton_tab2 = tk.Checkbutton(tab2, text="Shortcuts", command=handle_checkbutton)
shortcut_checkbutton_tab2.grid(pady=10)


# Add the tabbed layout to the window
tab_control.grid(row=1, column=0, rowspan=5, padx=10, pady=10, sticky=tk.W)

# Create a button to show selected values
button = tk.Button(window, text="SAVE Selected Values", command=save_selected_values)
button.grid(row=1, column=1, padx=10, pady=10)


#
#
# Run the Tkinter event loop
window.mainloop()
