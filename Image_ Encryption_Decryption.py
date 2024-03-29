import io
from cryptography.fernet import Fernet
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Generate a random key for encryption
key = Fernet.generate_key()


# Function to encrypt an image
def encrypt_image():
    # Open image file
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if not filename:
        return

    # Read image
    with open(filename, "rb") as f:
        image_bytes = f.read()

    # Initialize Fernet with the generated key
    fernet = Fernet(key)

    # Encrypt image bytes
    encrypted_image_bytes = fernet.encrypt(image_bytes)

    # Save encrypted image to a file
    encrypted_filename = "encrypted_image.jpg"
    with open(encrypted_filename, "wb") as f:
        f.write(encrypted_image_bytes)

    messagebox.showinfo("Success", "Image encrypted successfully.")


# Function to decrypt an image
def decrypt_image():
    # Open encrypted image file
    encrypted_filename = "encrypted_image.jpg"
    if not os.path.exists(encrypted_filename):
        messagebox.showerror("Error", "Encrypted image not found.")
        return

    # Read encrypted image bytes
    with open(encrypted_filename, "rb") as f:
        encrypted_image_bytes = f.read()

    # Initialize Fernet with the same key used for encryption
    fernet = Fernet(key)

    # Decrypt image bytes
    decrypted_image_bytes = fernet.decrypt(encrypted_image_bytes)

    # Create decrypted image from bytes
    image = Image.open(io.BytesIO(decrypted_image_bytes))
    image.show()


# Create GUI
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Buttons for encryption and decryption
encrypt_button = tk.Button(root, text="Encrypt Image", command=encrypt_image)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=decrypt_image)
decrypt_button.pack(pady=10)

root.mainloop()
