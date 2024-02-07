from tkinter import *
from tkinter import messagebox
import base64
screen = Tk()
screen.geometry("420x420")
screen.title("Cryptography GUI")
screen.configure(bg="gainsboro")
def encrypt() :
  password=code.get()
  if password=="12345":
    screen1=Toplevel(screen)
    screen1.title("Encription")
    screen1.geometry("400x250")
    screen1.configure(bg="indigo")
    message=Text1.get(1.0,END)
    encode_message = message.encode("ascii")
    base64_bytes = base64.b64encode(encode_message)
    encrypt = base64_bytes.decode("ascii")
    Label(screen1, text=" Code is Encrypted",font="Roboto 10 bold").place(x=5,y=6)
    Text2 = Text(screen1, font="30",bd=4, wrap=WORD)
    Text2.place(x=2, y=30, width=390, height=180)
    Text2.insert(END,encrypt)
  elif(password==""):
    messagebox.showerror("Error", "Please Enter the secret key")
  elif(password!="12345"):
    messagebox.showerror("Oops", "Invailad secret key")
    #Decryption
def decrypt() :
  password=code.get()
  if password=="12345":
    screen2=Toplevel(screen)
    screen2.title("Decription")
    screen2.geometry("400x250")
    screen2.configure(bg="indigo")
    message=Text1.get(1.0,END)
    encode_message = message.encode("ascii")
    base64_bytes = base64.b64decode(encode_message)
    encrypt = base64_bytes.decode("ascii")
    Label(screen2, text=" Code is Decrypted",font="Roboto 10 bold").place(x=5,y=6)
    Text2 = Text(screen2, font="30",bd=4, wrap=WORD)
    Text2.place(x=2, y=30, width=390, height=180)
    Text2.insert(END,encrypt)
  elif(password==""):
    messagebox.showerror("Error", "Please Enter the secret key")
  elif(password!="12345"):
    messagebox.showerror("Oops", "Invailad secret key")
    #rest 
def reset():
      Text1.delete(1.0, END)
      code.set("")
  
#label
Label(screen, text="Enter the Text For Encryption and Decryption", font="Roboto 14 bold" ).place(x=5 , y=6)
# text
Text1=Text(screen, font="20")
Text1.place(x=5,y=45 ,width=410, height=120 )
#label
Label(screen, text="Enter Secret Key" , font="Roboto 13 bold").place(x= 138, y=185)
#entry
code=StringVar()
Entry( textvariable=code,bd=4, font="20",show="*").place(x=110 , y=220)
#Button
Button(screen, text="Encryption",font="arial 15 bold", bg="red", fg="white", command= encrypt).place(x=15 , y=280, width=180)
Button(screen, text="Decryption",font="arial 15 bold", bg="green", fg="white", command= decrypt).place(x=220 , y=280, width=180)
Button(screen, text="Reset",font="arial 15 bold", bg="blue", fg="white",command=reset).place(x=60 , y=350, width=280)

mainloop()
