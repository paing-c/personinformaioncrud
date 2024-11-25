import tkinter as tk  # Import tkinter with alias 'tk'
from tkinter import ttk, messagebox
import mysql.connector
import pandas as pd

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # default XAMPP MySQL user
    password="",  # default XAMPP MySQL password is empty
    database="person_db"
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS persons (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name_myanmar VARCHAR(255),
        name_english VARCHAR(255),
        age INT,
        gender VARCHAR(10),
        dob DATE,
        nrc_number VARCHAR(255)
    )
''')
conn.commit()

# GUI Application
class PersonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Person Information CRUD")

        self.create_widgets()
        self.populate_treeview()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name (Myanmar)', 'Name (English)', 'Age', 'Gender', 'DOB', 'NRC Number'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name (Myanmar)', text='Name (Myanmar)')
        self.tree.heading('Name (English)', text='Name (English)')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Gender', text='Gender')
        self.tree.heading('DOB', text='Date of Birth')
        self.tree.heading('NRC Number', text='NRC Number')
        self.tree.pack(fill=tk.BOTH, expand=True)

        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name (Myanmar)").grid(row=0, column=0)
        tk.Label(form_frame, text="Name (English)").grid(row=0, column=1)
        tk.Label(form_frame, text="Age").grid(row=0, column=2)
        tk.Label(form_frame, text="Gender").grid(row=0, column=3)
        tk.Label(form_frame, text="DOB (yyyy-mm-dd)").grid(row=0, column=4)
        tk.Label(form_frame, text="NRC Number").grid(row=0, column=5)

        self.name_myanmar_entry = tk.Entry(form_frame)
        self.name_english_entry = tk.Entry(form_frame)
        self.age_entry = tk.Entry(form_frame)
        self.gender_entry = tk.Entry(form_frame)
        self.dob_entry = tk.Entry(form_frame)
        self.nrc_number_entry = tk.Entry(form_frame)

        self.name_myanmar_entry.grid(row=1, column=0)
        self.name_english_entry.grid(row=1, column=1)
        self.age_entry.grid(row=1, column=2)
        self.gender_entry.grid(row=1, column=3)
        self.dob_entry.grid(row=1, column=4)
        self.nrc_number_entry.grid(row=1, column=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Add", command=self.add_person).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Update", command=self.update_person).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Delete", command=self.delete_person).pack(side=tk.LEFT)
        tk.Button(btn_frame, text="Execute", command=self.export_to_excel).pack(side=tk.LEFT)

    def populate_treeview(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        cursor.execute("SELECT * FROM persons")
        for row in cursor.fetchall():
            self.tree.insert('', 'end', values=row)

    def add_person(self):
        data = (
            self.name_myanmar_entry.get(),
            self.name_english_entry.get(),
            self.age_entry.get(),
            self.gender_entry.get(),
            self.dob_entry.get(),
            self.nrc_number_entry.get()
        )
        cursor.execute('''
            INSERT INTO persons (name_myanmar, name_english, age, gender, dob, nrc_number)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', data)
        conn.commit()
        self.populate_treeview()
        messagebox.showinfo("Success", "Person added successfully")

    def update_person(self):
        selected_item = self.tree.selection()[0]
        person_id = self.tree.item(selected_item)['values'][0]

        data = (
            self.name_myanmar_entry.get(),
            self.name_english_entry.get(),
            self.age_entry.get(),
            self.gender_entry.get(),
            self.dob_entry.get(),
            self.nrc_number_entry.get(),
            person_id
        )
        cursor.execute('''
            UPDATE persons
            SET name_myanmar=%s, name_english=%s, age=%s, gender=%s, dob=%s, nrc_number=%s
            WHERE id=%s
        ''', data)
        conn.commit()
        self.populate_treeview()
        messagebox.showinfo("Success", "Person updated successfully")

    def delete_person(self):
        selected_item = self.tree.selection()[0]
        person_id = self.tree.item(selected_item)['values'][0]

        cursor.execute('DELETE FROM persons WHERE id=%s', (person_id,))
        conn.commit()
        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "Person deleted successfully")

    def export_to_excel(self):
        cursor.execute("SELECT * FROM persons")
        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=['ID', 'Name (Myanmar)', 'Name (English)', 'Age', 'Gender', 'DOB', 'NRC Number'])
        df.to_excel('persons.xlsx', index=False)
        messagebox.showinfo("Success", "Data exported to persons.xlsx")

if __name__ == "__main__":
    root = tk.Tk()
    app = PersonApp(root)
    root.mainloop()
