import tkinter as tk
from tkinter import ttk

# create a window 
window = tk.Tk()
window.title('Fasting')
window.geometry('200x200')

# widgets 
label = ttk.Label(master = window, text = '')
label.pack()


entry = ttk.Entry(master = window,width=5,font=('Arial',40),justify='center',)
entry.pack()
entry.bind('<FocusOut>', lambda event: calculate_hours(entry.get()))

h=1

entry2 = ttk.Entry(master = window,width=5,font=('Arial',40),justify='center',)
entry2.pack()

def calculate_hours(text):
    res = "15hrs"
    entry2.insert(0, res)

def button_func():
	# get the content of the entry
	entry_text = entry.get()

	# update the label
	# label.configure(text = 'some other text')
	label['text'] = entry_text
	entry['state'] = 'disabled'
	# print(label.configure())
 


button = ttk.Button(master = window, text = 'Comenzar Ayuno', command = button_func)
button.pack()

# run 
window.mainloop()