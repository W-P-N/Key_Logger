# Imports
from cryptography.fernet import Fernet

# Creating a list of keys.
with open(r"files/log.txt", "r") as file:
    key_list = file.readlines()

# Converting key from string to bytes using encode function.
key = key_list[0].encode("utf-8")

# Fernet object with valid key as an argument.
f = Fernet(key)

# Putting decoded strings in file:
with open(r"files/decoded.txt", "a") as file_:
    
    for key_ in key_list[1:]:  # Looping from second line (first line is the key).    
        dec_key = f.decrypt(key_)  # Decrypting...
        file_.write(str(dec_key)[2:-1] + "\n")  # Converting the datatype from bytes to string and removing ambiguities.