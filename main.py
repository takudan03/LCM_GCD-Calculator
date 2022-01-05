#GCD and LCM calculator in tkinter GUI
#Also adds every entry to a MongoDB database

import tkinter as tk
from pymongo import MongoClient
from pprint import pprint
from tkinter import messagebox

client = MongoClient(port=27017)
db = client.gcddb

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=420, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='FIND THE GCD of two numbers')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type num1:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 120, window=entry1)

label3 = tk.Label(root, text='Type num2:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 200, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(200, 220, window=entry2)


def buttonPress():
    db = client.gcddb

    x1 = entry1.get()
    x2 = entry2.get()

    if int(x1) == 0 or int(x2) == 0:
        ##IF EITHER OF THE NJUMBERS ARE 0
        messagebox.showerror("Math Error", "Please ensure you enter non-zero numbers")
    else:
        label3 = tk.Label(root, text='The GCD of ' + x1 + ' and ' + x2 + ' is:', font=('helvetica', 10))
        canvas1.create_window(200, 320, window=label3)

        label4 = tk.Label(root, text=getGCD(int(x1), int(x2)), font=('helvetica', 12, 'bold'))
        canvas1.create_window(200, 350, window=label4)

        label5 = tk.Label(root, text='The LCM of ' + x1 + ' and ' + x2 + ' is:', font=('helvetica', 10))
        canvas1.create_window(200, 375, window=label5)

        label6 = tk.Label(root, text=getLCM(int(x1), int(x2)), font=('helvetica', 12, 'bold'))
        canvas1.create_window(200, 400, window=label6)

        # adding every entry to the test database
        gcdentry = {
            'num1': x1,
            'num2': x2,
            'gcd': str(getGCD(int(x1), int(x2))),
            'lcm': str(getLCM(int(x1), int(x2)))
        }

        # Step 3: Insert entry object directly into MongoDB via isnert_one
        # result=db.insert_one(gcdentry)  #DID NOT WORK
        result = db.entries.insert_one(gcdentry)

        # Step 4: Print to the console the ObjectID of the new document
        print('Created new entry for nums {0} and {1}: entryid: {2}'.format(x1, x2, result.inserted_id))


def getGCD(a, b):
    a1 = a
    b1 = b

    ###for small numbers, you can use the following. Not advised as has too many iterations
    # while a1!=b1:
    #    if a1>b1: a1=a1-b1
    #    if b1>a1: b1=b1-a1
    # return a1
    while b1 != 0:
        a1, b1 = b1, a1 % b1
    return a1


def getLCM(a, b):
    lcm = (a * b) / getGCD(a, b)
    return lcm


button1 = tk.Button(text='Get the GCD', command=buttonPress, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 275, window=button1)

root.mainloop()