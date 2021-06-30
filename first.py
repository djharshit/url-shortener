'''Python Program - URL Shortener by DJ Harshit'''

# Importing the modules
from tkinter import *
from back import Short_Url

# Functions
def retrive():
	global short_url
	surl = Short_Url(url.get())
	surl.check()
	surl.generate()
	short_url = surl.send_url()

def home():
	l3.config(text='Enter long URL')
	url.set('')

def copy():
	wind.clipboard_clear()
	wind.clipboard_append(short_url)

def short():
	retrive()
	url.set(short_url)
	l3.config(text='Shorten URL   ')

def short_enter(n):
	retrive()
	url.set(short_url)
	l3.config(text='Shorten URL   ')

# Main program 
wind = Tk()
wind.geometry('500x200')
wind.resizable(0,0)
wind.title('URL Shortener')

# Url variable
url = StringVar()

l1 = Label(wind, text='URL Shortener', font=('SugarFont Bold', 30, 'bold'))
l1.grid(row=0, column=0, columnspan=3, padx=5)
l2 = Label(wind, text='By Harshit', font=('Arial Rounded MT Bold', 15))
l2.grid(row=0, column=4)

l3 = Label(wind, text='Enter long URL')
l3.grid(row=1, column=0, padx=5)
e1 = Entry(wind, textvariable=url, width=60)
e1.grid(row=1, column=2, columnspan=3, pady=20)

b1 = Button(wind, text='Short', command=short)
b1.grid(row=3, column=2)
b2 = Button(wind, text='Copy', command=copy)
b2.grid(row=3, column=3)
b3 = Button(wind, text='One More', command=home)
b3.grid(row=3, column=4)

wind.bind('<Return>', short_enter)

wind.mainloop()