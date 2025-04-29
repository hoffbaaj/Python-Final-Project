Simple Password Manager (With GUI)

A beginner-friendly password manager with a graphical interface, built using Python and Tkinter.
It stores credentials locally in a CSV file with no encryption.


Features

Add new site credentials
Retrieve and display stored credentials
Update existing site details
Delete site credentials
List all stored sites
Generate random secure passwords
Password input field is hidden (masked)
Simple and clean Tkinter GUI
Auto-creates passwords.csv on first run


Getting Started

Requirements
Python 3.x
Tkinter (comes pre-installed with Python)
No external libraries needed!


Installation

Just download the Python script, then run:
bash
Copy
Edit
python3 password_manager_gui.py
(Rename the file if needed)


How To Use

Add: Fill in Site, Email, Password fields → Click "Add"
Get: Enter Site name → Click "Get" to retrieve credentials
Update: Enter Site name, new Email or new Password → Click "Update"
Delete: Enter Site name → Click "Delete"
List Sites: Click "List Sites" to display all saved sites
Generate Password: Click "Generate Password" to fill a random password into the Password field
All actions update the passwords.csv file automatically.


Important Notes

Credentials are stored as plain text inside passwords.csv.
This tool is intended for local, personal use only — it is not secure for sensitive data.
No encryption or authentication is implemented.
