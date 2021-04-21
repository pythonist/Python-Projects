import tkinter as tk
import string
import random
def gen_pwd():
    password=[]
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbols = random.choice(string.punctuation)
        numbers = random.choice(string.digits)
        password.append(alpha)
        password.append(numbers)
        password.append(symbols)
        passwords = "".join(str(x)for x in password)
        label.config(text=passwords)

root = tk.Tk()
root.geometry("400x300")
button = tk.Button(root,text="Generate Password",command=gen_pwd)
button.grid(row=1,column=1)
label = tk.Label(root,font=("times",15,"bold"))
label.grid(row=4,column=2)
root.mainloop()
        