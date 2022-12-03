from cryptography.fernet import Fernet

with open("key.txt",'rb') as f:
    key = f.read()

with open("text.txt",'rb') as f:
    encmsg_f = f.read()

fernet=Fernet(key)

decmsg_f = fernet.decrypt(encmsg_f)
with open("text.txt",'wb') as f:
    f.write(decmsg_f)