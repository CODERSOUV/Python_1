from cryptography.fernet import Fernet

key=Fernet.generate_key()

obj=Fernet(key)

msg="hello world".encode()

enc=obj.encrypt(msg)
print(enc)

drc=obj.decrypt(enc)
print(drc.decode())