from cryptography.fernet import Fernet
key=Fernet.generate_key()

with open("TheKey.txt", "wb") as file:
	file.write(key)

theFile = input("Enter the name of file you want to encrypt it: ")

try:
    with open(theFile, "rb") as file:
	    content = file.read()
    encrypted_content = Fernet(key).encrypt(content)

    with open(theFile, "wb") as file:
	file.write(encrypted_content)
	
    print("File Encrypted")
    print(f"The key used to encrypt: {key}")

except:
    print("ERROR: SYSNTAX OR LOGIC")
