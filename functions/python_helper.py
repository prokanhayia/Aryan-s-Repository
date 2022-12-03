from customtkinter import *



def search():
    value = entry1.get()
    value.replace("()","")

    with open(f"func\{value}.txt","r") as f:
        help_value = f.read()

    outtext.configure(state="normal")
    outtext.delete("0.0","end")
    outtext.insert("0.0",f"{help_value}")
    outtext.configure(state="disabled")

root = CTk()
root.geometry("605x600")
root.title("Python Helper")


f1 = CTkFrame(root)
f1.pack(side=TOP,fill=BOTH)

f2 = CTkFrame(root)
f2.pack(side=TOP,pady=4,fill=BOTH)


entry1=CTkEntry(f1,font=("Agency FB",33,"bold"),width=440,height=40,text_color="#ffffff")
entry1.pack(side=LEFT,padx=5,pady=5,fill=BOTH)


search_button=CTkButton(f1,text="Search",height=44,command=search)
search_button.pack(pady=5,padx=5)


outtext = CTkTextbox(f2,height=520,width=589,text_color="#ffffff",font=("BaskerVille Old Face Regular",14))
outtext.configure(state="disabled")
outtext.pack(side=BOTTOM,anchor=SW,padx=4,pady=4,fill=BOTH)



root.mainloop()