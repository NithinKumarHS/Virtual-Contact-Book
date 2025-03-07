#PythonGeeks - import library
from tkinter import *
from tkinter import messagebox


#PythonGeeks - Initialize window
root = Tk()
root.geometry('700x550') #it denotes the dimensions of the screen 
root.config(bg = '#d3f3f5') #it will give the color for the background of the gui screen
root.title('PythonGeeks Contact Book') #it will display the title for gui screen
root.resizable(0,0) #it allow the user to resize the screen but here it is restricted
contactlist = [
    ['Siddharth Nigam','369854712'],
    ['Gaurav Patil', '521155222'],
    ['Abhishek Nikam', '78945614'],    #it is the some of the list of contacts that have been already present in book
    ['Sakshi Gaikwad', '58745246'],
    ['Mohit Paul', '5846975'],                  
    ['Karan Patel', '5647892'],
    ['Sam Sharma', '89685320'],
    ['John Maheshwari', '98564785'],
    ['Ganesh Pawar','85967412']
    ]

Name = StringVar
Number = StringVar()


#PythonGeeks - create frame
frame = Frame(root)  #it will apply the root specification to frame 
frame.pack(side = RIGHT) #it allocate a list in right  side of the screen

scroll = Scrollbar(frame, orient=VERTICAL) #it will display the scroolbar from top to bottom
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief=RAISED)
scroll.config (command=select.yview) #user can scrool the list vertically in the left side of the name list
scroll.pack(side=RIGHT, fill=Y) #it is used to style the scroolbar icon 
select.pack(side=LEFT,  fill=BOTH, expand=1)


#PythonGeeks - function to get select value

def Selected():
	#print("hello",len(select.curselection())) #this line doesn't affect the code if it is not present also
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
    
#PythonGeeks -function to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="":    #this line check the name and number block if its not empty it add new contact at end of the list
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set() #entered items are selected to move to the contactlist
        EntryReset() #it is used to reset the column of the list to enter next name and number
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error","Please fill the information")
        
def EntryReset():
	Name.set('')
	Number.set('')



# fun to edit existing contact

def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
    

		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		EntryReset()
		Select_set()

	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)


#PythonGeeks- function to delete selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
# func to view contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
        

#PythonGeeks- function to exit game window   
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


#PythonGeeks - define buttons labels and entry widget 
Label(root, text = 'Name', font=("Times new roman",25,"bold"), bg = '#d3f3f5').place(x= 30, y=20)
Entry(root, textvariable = Name, width=30, highlightbackground="black",highlightcolor="black",highlightthickness=2).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",22,"bold"),bg = '#d3f3f5').place(x= 30, y=70)
Entry(root, textvariable = Number, width=30, highlightbackground="black",highlightcolor="black",highlightthickness=2).place(x= 200, y=80)

Button(root,text=" ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = AddContact, padx=20,width=23). place(x= 40, y=140)
Button(root,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = UpdateDetail, padx=20,width=23).place(x= 40, y=200)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = Delete_Entry, padx=20,width=23).place(x= 40, y=260)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = VIEW,width=25).place(x= 40, y=325)
Button(root,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = EntryReset,width=25).place(x= 40, y=390)
Button(root,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = EXIT).place(x= 250, y=470)

root.mainloop()
  
