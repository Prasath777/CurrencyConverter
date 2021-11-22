from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests
root=Tk()
root.title("Currency Converter")
root.iconbitmap('C:/Users/PRASATH/PycharmProjects/CurrencyConverter/currency.py')
root.geometry("500x500")

# Create tabs
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=5)

# Create Two Frames
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

my_notebook.add(currency_frame, text = "Currencies")
my_notebook.add(conversion_frame , text = "Conversion")


#Disable the 2nd tab
my_notebook.tab(1, state='disabled')

###########
# Currency Stuff
###########
def lock():
    if not convert_from.get() or not convert_to.get():
        messagebox.showwarning("WARNING","You didn't fill out all the fields")

    elif convert_from.get()==convert_to.get():
        messagebox.showwarning("WARNING", "You have chosen the same currency!")
    else:
        # Disable entry boxes
        #convert_from.config(state='disabled')
        #conversion_entry.config(state='disabled')
        #rate_entry.config(state='disabled')
        home_entry.configure(state='disabled')
        conversion_entry.configure(state='disabled')
        my_notebook.tab(1, state='normal')
        converted_entry.delete(0,END)
        amount_entry.delete(0,END)
        #Change Tab Field
        amount_label.config(text=f'Amount of {convert_from.get()} To Convert To {convert_to.get()}')
        converted_label.config(text=f'Equals This Many {convert_to.get()}')
        convert_button.config(text=f'Convert from {convert_from.get()} to {convert_to.get()}')


def unlock():
    # enable entry boxes
    # convert_from.config(state='normal')
    # conversion_entry.config(state='normal')
    #rate_entry.config(state='normal')
    home_entry.configure(state='normal')
    conversion_entry.configure(state='normal')
    my_notebook.tab(1, state='disabled')

home = LabelFrame(currency_frame, text= " Your Home Currency")
home.pack(pady=20)

#Home currency entry box
convert_from=StringVar()
convert_from.set("INR")

home_entry = OptionMenu(home, convert_from, "INR", "USD", "CAD", "EUR", "GBP")
# home_entry= Entry(home, font=("Helvetica", 24))
home_entry.pack(pady=10,padx=10)

#Conversion Currency Frame
conversion = LabelFrame(currency_frame, text=" Conversion Currency")
conversion.pack(pady=20)

#convert to Label
# conversion_label= Label(conversion, text=" Currency To Convert To")
# conversion_label.pack(pady=10)

#Convert to Entry

convert_to=StringVar()
convert_to.set("CAD")


conversion_entry=OptionMenu(conversion, convert_to, "INR", "USD", "CAD", "EUR", "GBP")
# conversion_entry = Entry(conversion, font=("Helvetica", 24))
conversion_entry.pack(pady=10,padx=10)


#Rate Label
# rate_label= Label(conversion, text=" Current Conversion Rate")
# rate_label.pack(pady=10)

#Rate Entry
# rate_entry = Entry(conversion, font=("Helvetica", 24))
# rate_entry.pack(pady=10,padx=10)

#Button Frame
button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

#create buttons
lock_button = Button(button_frame, text="Lock", command =lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text="Unlock", command =unlock)
unlock_button.grid(row=0, column=1, padx=10)

###########
# Conversion Stuff
###########

def convert():
    #clear converted entry box
    converted_entry.delete(0,END)

    # response = requests.get(f'http://api.exchangeratesapi.io/v1/latest? access_key =b5f21b387f279b6435dabfa8edc4a533& base = {convert_from}& symbols = {convert_to}')
    # data=response.json()
    # exchange_rate = data['rates'][convert_to]
    try:
        float(amount_entry.get())
    except ValueError:
        messagebox.showwarning("WARNING", "Input is not a number")
        quit()
    currency_values={
        'INR': {'CAD':0.017, 'USD':0.014, 'GBP':0.0099, 'EUR':0.012},
        'CAD': {'INR': 58.12, 'USD': 0.80, 'GBP': 0.58, 'EUR':0.67},
        'USD': {'CAD': 1.26, 'INR': 73.05, 'GBP': 0.72, 'EUR':0.84},
        'GBP': {'CAD': 1.74, 'USD': 1.38, 'INR': 100.99, 'EUR':1.17},
        'EUR': {'CAD': 1.49, 'USD': 1.19, 'INR': 86.64, 'GBP': 0.86}
    }
    exchange_rate=currency_values[convert_from.get()][convert_to.get()]
    #Convert
    converted_value = exchange_rate * float(amount_entry.get())
    #have 2 decimal places
    converted_value=round(converted_value,2)
    #add commas
    converted_value='{:,}'.format(converted_value)
    #update entry box
    converted_entry.insert(0,converted_value)


def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text = " Amount to Convert")
amount_label.pack(pady=20)

#Entry Box for amount

amount_entry = Entry(amount_label, font=("Helvetica", 24))
amount_entry.pack(pady=10, padx=10)

#Convert button
convert_button = Button(amount_label, text="Convert",command = convert)
convert_button.pack(pady=20)

#Equals frame

converted_label = LabelFrame(conversion_frame, text="Converted Currency")
converted_label.pack(pady=20)

#converted entry

converted_entry = Entry(converted_label, font=("Helvetica",24 ), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

#Clear button

clear_button = Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

#Fake label for spacing

spacer = Label(conversion_frame,text="",width=68)
spacer.pack()






root.mainloop()