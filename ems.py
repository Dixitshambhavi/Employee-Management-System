from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database

# Functions

def delete_all():
    result = messagebox.askyesno('Confirm', 'Do you really want to delete all the records?')
    if result:
        try:
            database.deleteall_records()
            treeview_data()
            clear()
            messagebox.showinfo('Success', 'All records have been deleted')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete all records: {e}')

def show_all():
    treeview_data()
    searchEntry.delete(0, END)
    searchBox.set('Search By')

def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error', 'Please select an option')
    else:
        try:
            searched_data = database.search(searchBox.get(), searchEntry.get())
            tree.delete(*tree.get_children())
            for employee in searched_data:
                tree.insert('', END, values=employee)
        except Exception as e:
            messagebox.showerror('Error', f'Search failed: {e}')

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        try:
            database.delete(idEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo('Success', 'Data is deleted')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete: {e}')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update')
    else:
        try:
            database.update(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo('Success', 'Data is updated')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to update: {e}')

def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item[0])['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0, END)

def treeview_data():
    try:
        employees = database.fetch_employees()
        tree.delete(*tree.get_children())
        for employee in employees:
            tree.insert('', END, values=employee)
    except Exception as e:
        messagebox.showerror('Error', f'Failed to load data: {e}')

def add_employee():
    if idEntry.get() == '' or phoneEntry.get() == '' or nameEntry.get() == '' or salaryEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error', 'Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error', "Invalid ID format. Use 'EMP' followed by a number (e.g., 'EMP1').")
    else:
        try:
            database.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleBox.get(), genderBox.get(), salaryEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo('Success', 'Data is added')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to add employee: {e}')

# Window Setup
window = CTk()
window.geometry('1250x600+100+100')
window.resizable(False, False)
window.title('Employee Management System')
window.configure(fg_color='#161C30')

# Images Row
logo_paths = ['bg1.jpg', 'bg2.jpg', 'bg3.jpg', 'happy-character-winning-prize-with-flat-design_23-2147890299.jpg', 'bg4.png', 'coverpage.png']
image_frame = CTkFrame(window, fg_color='#161C30')
image_frame.grid(row=0, column=0, columnspan=6, pady=5)

for i, path in enumerate(logo_paths):
    img = CTkImage(Image.open(path), size=(200, 120))
    label = CTkLabel(image_frame, image=img, text='')
    label.grid(row=0, column=i, padx=2)

# Left Frame
leftFrame = CTkFrame(window, fg_color='#161C30')
leftFrame.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky='nsew')

idLabel = CTkLabel(leftFrame, text='Id', font=('arial', 18, 'bold'))
idLabel.grid(row=0, column=0, padx=20, pady=15, sticky='w')
idEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
idEntry.grid(row=0, column=1)

nameLabel = CTkLabel(leftFrame, text='Name', font=('arial', 18, 'bold'))
nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky='w')
nameEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
nameEntry.grid(row=1, column=1)

phoneLabel = CTkLabel(leftFrame, text='Phone', font=('arial', 18, 'bold'))
phoneLabel.grid(row=2, column=0, padx=20, pady=15, sticky='w')
phoneEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
phoneEntry.grid(row=2, column=1)

roleLabel = CTkLabel(leftFrame, text='Role', font=('arial', 18, 'bold'))
roleLabel.grid(row=3, column=0, padx=20, pady=15, sticky='w')
role_options = ['Web Developer', 'Cloud Architect', 'Technical Writer', 'Network Engineer', 'Data Analyst', 'Data Scientist', 'Business Analyst', 'IT Consultant', 'UX/UI Designer']
roleBox = CTkComboBox(leftFrame, values=role_options, width=180, font=('arial', 15, 'bold'), state='readonly')
roleBox.grid(row=3, column=1)
roleBox.set('Web Developer')

genderLabel = CTkLabel(leftFrame, text='Gender', font=('arial', 18, 'bold'))
genderLabel.grid(row=4, column=0, padx=20, pady=15, sticky='w')
gender_options = ['Male', 'Female']
genderBox = CTkComboBox(leftFrame, values=gender_options, width=180, font=('arial', 15, 'bold'), state='readonly')
genderBox.grid(row=4, column=1)
genderBox.set('Male')

salaryLabel = CTkLabel(leftFrame, text='Salary', font=('arial', 18, 'bold'))
salaryLabel.grid(row=5, column=0, padx=20, pady=15, sticky='w')
salaryEntry = CTkEntry(leftFrame, font=('arial', 15, 'bold'), width=180)
salaryEntry.grid(row=5, column=1)

# Right Frame for Treeview & Search
rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=3, columnspan=3, padx=30, pady=25, sticky='nsew')

search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchBox = CTkComboBox(rightFrame, values=search_options, width=180, font=('arial', 15, 'bold'), state='readonly')
searchBox.grid(row=0, column=0)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0, column=1)

searchButton = CTkButton(rightFrame, text='Search', width=100, command=search_employee)
searchButton.grid(row=0, column=2)

showallButton = CTkButton(rightFrame, text='Show All', width=100, command=show_all)
showallButton.grid(row=0, column=3, pady=5)


# Treeview
tree = ttk.Treeview(rightFrame, height=17, selectmode='browse')
tree.grid(row=1, column=0, columnspan=4, sticky='nsew', pady=(10, 0))

# Scrollbar
scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1, column=4, sticky='ns',pady=(10,0))


scrollbar.config(command=tree.yview)



tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')
tree.config(show='headings')

tree.column('Id', width=100)
tree.column('Name', width=160)
tree.column('Phone', width=160)
tree.column('Role', width=200)
tree.column('Gender', width=100)
tree.column('Salary', width=140)

style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 18, 'bold'))
style.configure('Treeview', font=('arial', 15, 'bold'), rowheight=30, background='#161C30', foreground='white')

scrollbar.config(command=tree.yview)

# Button Frame
buttonFrame = CTkFrame(window, fg_color='#161C30')
buttonFrame.grid(row=2, column=0, columnspan=6,pady=10)

CTkButton(buttonFrame, text='New Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=lambda: clear(True)).grid(row=0, column=0, pady=5)
CTkButton(buttonFrame, text='Add Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=add_employee).grid(row=0, column=1, pady=5, padx=5)
CTkButton(buttonFrame, text='Update Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=update_employee).grid(row=0, column=2, pady=5, padx=5)
CTkButton(buttonFrame, text='Delete Employee', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=delete_employee).grid(row=0, column=3, pady=5, padx=5)
CTkButton(buttonFrame, text='Delete All', font=('arial', 15, 'bold'), width=160, corner_radius=15, command=delete_all).grid(row=0, column=4, pady=5, padx=5)

# Grid Configuration
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(3, weight=1)

treeview_data()
window.bind('<ButtonRelease>', selection)
window.mainloop()

