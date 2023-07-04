# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-10
# Topic  :-
# 1) Implement the tkinter and webbrowser module
# 2) create a gui for taking input from the user and create a button to navigate to a browser site.
# 3) Also display the user entered text in the command prompt with message of navigating to "..." whichever site you chooses
# Note:
# [you cannot use Google search]
# you can use YouTube, etc.
# Date   : 04-07-2023

# Program:-
import tkinter as tk
import webbrowser

def navigate_to_website():
    site_url = entry.get()
    print("Navigating to", site_url)
    webbrowser.open(site_url)

root = tk.Tk()
root.title("Website Navigator")

label = tk.Label(root, text="Enter a website URL:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Navigate", command=navigate_to_website)
button.pack()

prompt_label = tk.Label(root, text="Command Prompt:")
prompt_label.pack()

text_area = tk.Text(root, width=50, height=10)
text_area.pack()

def print_command_prompt():
    command = entry.get()
    text_area.insert(tk.END, "Navigating to " + command + "\n")

print_button = tk.Button(root, text="Print Command Prompt", command=print_command_prompt)
print_button.pack()

root.mainloop()

