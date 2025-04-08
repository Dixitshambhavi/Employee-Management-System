
from customtkinter import *
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get() == 'shambhavi' and passwordEntry.get() =='1234567':
        messagebox.showinfo('Success', 'Login is successful')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong credentials')

# Create the root window
root = CTk()
root.geometry('930x478')  # Correct geometry syntax
root.title('Login page')

# Load the image and resize it
image = CTkImage(Image.open('coverpage.png'), size=(930, 478))

# Optional: You can add an image to a widget like a label or a canvas
label = CTkLabel(root, image=image)
label.pack(fill="both", expand=True)

# Create a frame for the login form
frame = CTkFrame(root, width=400, height=300, fg_color="white")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Heading label with correct background color usage
headinglabel = CTkLabel(frame, text='Employee Management System', fg_color='#FAFAFA', font=('Goudy Old Style', 20, 'bold'), text_color='#00008B')
headinglabel.grid(row=0, column=0, pady=20)

# Username Entry with placeholder text and width defined during widget creation
usernameEntry = CTkEntry(frame, placeholder_text='Enter your username', width=180, fg_color='white')
usernameEntry.grid(row=1, column=0, pady=10)

# Password Entry with placeholder text and width defined during widget creation
passwordEntry = CTkEntry(frame, placeholder_text='Enter Your Password', width=180, fg_color='white', show="*")
passwordEntry.grid(row=2, column=0, pady=10)

# Login Button
loginButton = CTkButton(frame, text='Login', cursor='hand2', command=login)
loginButton.grid(row=3, column=0, pady=20)

# Run the application
root.mainloop()
