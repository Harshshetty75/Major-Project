from cryptography.fernet import Fernet
import os

# Load the encryption key
with open("keyfile.key", "rb") as kf:
    key = kf.read()
cipher = Fernet(key)

# Decrypt files
folder_path = "test_files"
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            encrypted = file.read()
        decrypted = cipher.decrypt(encrypted)
        with open(file_path, "wb") as file:
            file.write(decrypted)

print(f"Files in {folder_path} have been decrypted successfully.")
