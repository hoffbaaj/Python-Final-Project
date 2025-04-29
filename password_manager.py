import tkinter as tk
from tkinter import messagebox
import csv
import os
import secrets
import string

CSV_FILE = os.path.join(os.path.dirname(__file__), "passwords.csv")

def ensure_csv_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["site", "email", "password"])


def add_entry(site, email, password):
    ensure_csv_exists()
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([site, email, password])
    messagebox.showinfo("Success", f"Added entry for {site}.")


def get_entry(site):
    ensure_csv_exists()
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['site'] == site:
                return f"Site: {row['site']}\nEmail: {row['email']}\nPassword: {row['password']}"
    return "Entry not found."


def update_entry(site, new_email, new_password):
    ensure_csv_exists()
    updated = False
    rows = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['site'] == site:
                if new_email:
                    row['email'] = new_email
                if new_password:
                    row['password'] = new_password
                updated = True
            rows.append(row)

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["site", "email", "password"])
        writer.writeheader()
        writer.writerows(rows)

    if updated:
        messagebox.showinfo("Success", f"Updated entry for {site}.")
    else:
        messagebox.showwarning("Warning", "Entry not found.")


def delete_entry(site):
    ensure_csv_exists()
    deleted = False
    rows = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['site'] != site:
                rows.append(row)
            else:
                deleted = True

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["site", "email", "password"])
        writer.writeheader()
        writer.writerows(rows)

    if deleted:
        messagebox.showinfo("Success", f"Deleted entry for {site}.")
    else:
        messagebox.showwarning("Warning", "Entry not found.")


def list_sites():
    ensure_csv_exists()
    sites = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sites.append(row['site'])
    return sites if sites else ["No sites found."]


def generate_password(length=12):
    charset = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(charset) for _ in range(length))


def gui_add():
    add_entry(site_entry.get(), email_entry.get(), password_entry.get())


def gui_get():
    result = get_entry(site_entry.get())
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)


def gui_update():
    update_entry(site_entry.get(), email_entry.get(), password_entry.get())


def gui_delete():
    delete_entry(site_entry.get())


def gui_list():
    sites = list_sites()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "\n".join(sites))


def gui_generate():
    generated = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated)

# GUI setup
root = tk.Tk()
root.title("Simple Password Manager")
root.geometry("450x500")
root.configure(bg="#f0f2f5")

font_large = ("Helvetica", 14)
font_small = ("Helvetica", 12)


# Fields
site_label = tk.Label(root, text="Site:", font=font_large, bg="#f0f2f5")
site_label.grid(row=0, column=0, pady=5, sticky="e")
site_entry = tk.Entry(root, font=font_small)
site_entry.grid(row=0, column=1, pady=5)

email_label = tk.Label(root, text="Email:", font=font_large, bg="#f0f2f5")
email_label.grid(row=1, column=0, pady=5, sticky="e")
email_entry = tk.Entry(root, font=font_small)
email_entry.grid(row=1, column=1, pady=5)

password_label = tk.Label(root, text="Password:", font=font_large, bg="#f0f2f5")
password_label.grid(row=2, column=0, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*", font=font_small)
password_entry.grid(row=2, column=1, pady=5)

tk.Button(root, text="Add", command=gui_add, font=font_small, bg="#d1e7dd").grid(row=3, column=0, pady=5)
tk.Button(root, text="Get", command=gui_get, font=font_small, bg="#d1e7dd").grid(row=3, column=1, pady=5)
tk.Button(root, text="Update", command=gui_update, font=font_small, bg="#ffe5b4").grid(row=4, column=0, pady=5)
tk.Button(root, text="Delete", command=gui_delete, font=font_small, bg="#ffe5b4").grid(row=4, column=1, pady=5)
tk.Button(root, text="List Sites", command=gui_list, font=font_small, bg="#f8d7da").grid(row=5, column=0, pady=5)
tk.Button(root, text="Generate Password", command=gui_generate, font=font_small, bg="#cfe2ff").grid(row=5, column=1, pady=5)

# Output box
output_text = tk.Text(root, height=10, width=50, font=font_small, bg="#ffffff")
output_text.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
