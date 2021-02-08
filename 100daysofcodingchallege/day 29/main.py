from tkinter import *
from random import choice,randint,shuffle
from tkinter import messagebox
import pyperclip
#-------------------------------------------------------------------------- PASSWORD MANAGER ----------#


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(2, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbol + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert("1.0",password)
    pyperclip.copy(password)
#-------------------------------------------------------------------------------- SAVE PASSWORD ----------#


def save():

    website = web_name.get('1.0',"end-1c")
    email = email_input.get('1.0',"end-1c")
    password = pass_input.get('1.0',"end-1c")

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure You haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered \nEmail: {email}"
                                                          f"\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} |\n")
                web_name.delete('0',"end")
                pass_input.delete('0',"end")

#------------------------------------------------------------------------------------- UI SETUP ----------#


window= Tk()
window.config(height=300, width=300, bg="#091833",padx=40, pady=50)
window.title("Password Manager")

canvas= Canvas(width=150,height=150,bg="#091833",highlightthickness=0)
lock_img=PhotoImage(file="lock5.png")
canvas.create_image(97, 80, image=lock_img)
canvas.grid(row=1,column=2,columnspan=2)

website_label=Label(text="Website:", bg="#091833" ,fg="white" ,font=("arial",10,"bold"))
website_label.grid(row=2,column=1)

web_name=Text(height=1,width=35, bg="white")
web_name.grid(row=2,column=2,columnspan=2)
web_name.focus()

email_label=Label(text="Email/Username:",pady=5, bg="#091833" ,fg="white" ,font=("arial",10,"bold"))
email_label.grid(row=3,column=1)

email_input=Text(height=1,width=35)
email_input.grid(row=3,column=2,columnspan=2)
email_input.insert(END,"@gmail.com")

pass_label=Label(text="Password:", bg="#091833" ,fg="white" ,font=("arial",10,"bold"))
pass_label.grid(row=4,column=1)

pass_input=Text(height=1,width=18)
pass_input.grid(row=4,column=2)

generate_button=Button(text="Generate Password",command=generate_password,pady=-2,bg="#122c63",
                       fg="white" ,font=("arial",10,"bold"))
generate_button.grid(row=4,column=3)

add_button=Button(text="Add",height=1,width=35,command=save ,bg="#f2a343" ,fg="white" ,font=("arial",10,"bold"))
add_button.grid(row=6,column=2,columnspan=2)

window.mainloop()
