from cryptography.fernet import Fernet



key=Fernet.generate_key()
with open("key.txt",'wb') as f:
    f.write(key)


with open("text.txt", 'rb') as f:
    msg_f = f.read()

fernet=Fernet(key)

encmsg = fernet.encrypt(msg_f)

with open("text.txt","wb") as f:
    f.write(encmsg)

with open("text.txt","rb") as f:
    encmsg_f=f.read()


