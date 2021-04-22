from tkinter import *
import base64

root = Tk()
root.geometry('500x400')
root.resizable(0,0)
root.title("Message Encode Decode with Python")

Label(root,text="Encode & Decode",font="arial 17 bold").pack()

#variables for encode and decode
Text = StringVar()
private_key = StringVar()
mode = StringVar()
result = StringVar()

#function to encode the messaege
def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
 
#fucntion to decode the messaeg
def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)

#fucntion to set the mode
def Mode():
    if(mode.get() == 'e'):
        result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        result.set(Decode(private_key.get(), Text.get()))
    else:
        result.set("Invalid Mode Selected")
#exit the window
def Exit():
    root.destroy()
    
#function to reset the window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    result.set("")
    
#creating Labels and Entries
#Label and entry for messages
Label(root, text="Message",font="arial 14 bold").place(x=60,y=60)
Entry(root,textvariable=Text,bg = "Ghost White",font = "arial 10").place(x=250,y=60)

#label for key
Label(root,text="Key",font="arial 14 bold").place(x=60,y=90)
Entry(root,textvariable=private_key,bg="ghost white",font="arial 10").place(x=250,y=90)

#label for mode
Label(root,text="Mode(e-encode,d-decode)",font="arial 14 bold").place(x=60,y=120)
Entry(root,textvariable=mode,bg="Ghost White",font="arial 10").place(x=310,y=120)

Entry(root,textvariable=result,bg="Ghost White",font="arial 10").place(x=250,y=150)

Button(root,text="Result",font="arial 10 bold",padx=2,bg="Gray",command=Mode).place(x=60,y=150)

Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

    
root.mainloop()