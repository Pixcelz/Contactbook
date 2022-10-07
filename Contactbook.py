#Python Program for Contactbook by Anag Devnani XII-A

# Importing the Modules
from tkinter import *
import tkinter.messagebox as mb
import pymysql

# Connecting and Initializing the Database where we will store all the data
connector = pymysql.connect(host='localhost',user='root',password='Birla@123',database='Contacts')
cursor = connector.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CONTACT_BOOK (NAME char(20), PHONE_NUMBER int(10), ADDRESS varchar(50))")

# Creating the StringVar variables
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
search_strvar = StringVar()

# Initializing the GUI window
root = Tk()
root.title("Anag's Contact Book")
root.geometry('700x550')
root.resizable(0, 0)

# Creating the Frames
frame_font = ("Roboto", 14)
Label(root, text='CONTACT BOOK', font=("Roboto Mono", 15, "bold"), bg='Black', fg='White').pack(side=TOP, fill=X) # Topmost Bar
option_frame = Frame(root, bg='Gray20')                            # Buttons Frame
option_frame.place(relx=0, relwidth=0.3, relheight=1, y=30)
contact_frame = Frame(root, bg='Gray35')                           # Contacts Frame
contact_frame.place(relx=0.3, relwidth=0.7, relheight=1, y=30)

# Options Frame
search_entry = Entry(option_frame, width=18, font=("Arial", 12), textvariable = search_strvar).place(relx=0.1, rely=0.025)
Button(option_frame, text='Search Record', font=frame_font, width=15, command = record_search).place(relx=0.075, rely=0.1) #command not working
Button(option_frame, text='Add Record', font=frame_font, width=15, command = add_record).place(relx=0.075, rely=0.2)    #command not working
Button(option_frame, text='Delete Record', font=frame_font, width=15, command = delete_record).place(relx=0.075, rely=0.3)  #command not working

# Contacts Frame
Label(contact_frame, text='Saved Contacts', font=("Roboto Mono", 14), bg='Gray35').place(relx=0.5, rely=0.05)

# Defining the functions
def list_contacts():
#Should give a list of all the contacts present

def add_record():
#should add a record using INSERT statement and update using list_contacts()

def delete_record():
#should delete selected record with a confirmation and update

def record_search():
#should search by all columns and undate the Label accordingly
