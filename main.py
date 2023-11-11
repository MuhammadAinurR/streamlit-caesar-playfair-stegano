import streamlit as st
from stegano import lsb
import playfair_cipher_decrypt as pcd
import playfair_cipher_encrypt as pce
import caesar_cipher as cc
import numpy as np
import cv2
from PIL import Image
import hybrid as ed

# Set the title and subtitle of the app
st.title("Image Encryption and Decryption")

# Create a sidebar for input text and upload image
sidebar = st.sidebar

# Input text
input_text = sidebar.text_input("Enter text to encrypt:")

# Upload image
uploaded_image = sidebar.file_uploader("Upload image:")

if uploaded_image is not None:
    # Convert the uploaded image to a PIL Image object
    uploaded_image = Image.open(uploaded_image)

    # Save the image to a local file
    uploaded_image.save("rahasia1.png")


# Create a button for encrypt and decrypt image
encrypt_button = sidebar.button("Encrypt Image")
decrypt_button = sidebar.button("Decrypt Image")

# Define a function to encrypt image
def encrypt_image(image, text):
    encrypted_image = lsb.hide(image, text)
    return encrypted_image

# Define a function to decrypt image
def decrypt_image(image):
    decrypted_text = lsb.reveal(image)
    return decrypted_text

def download_encrypted_image(encrypted_image_path):

  with open(encrypted_image_path, "rb") as f:
    encrypted_image_bytes = f.read()

  st.download_button(
    label="Download Encrypted Image",
    data=encrypted_image_bytes,
    file_name="encrypted_image.png",
  )

# Input text
caesar_cipher_key = 3
playfair_cipher_key = "violence"
# If the user clicks on the encrypt button
if encrypt_button:

    # Check if the uploaded image is not empty
    if uploaded_image is not None:
      

        st.write("input text : ", input_text)
        st.write("caesar cipher key : ", caesar_cipher_key)
        st.write("playfair cipher key : ", playfair_cipher_key)

        caesar_encrypted = str(cc.enc(caesar_cipher_key, input_text))
        st.write("encrypted as caesar : ", caesar_encrypted)

        playfair_encrypted = pce.final(playfair_cipher_key, str(caesar_encrypted))
        st.write("encrypted as playfair : ", playfair_encrypted)



        def compare_mse(img1, img2):
            
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            # Calculate the MSE between the two images.
            mse = np.mean((img1 - img2) ** 2)
            return mse



        # Encrypt the image
        encrypted_image = encrypt_image(uploaded_image, playfair_encrypted)

        # save the encrypted image
        encrypted_image.save("./rahasia2.png")

        # Display the encrypted image
        st.image(encrypted_image, caption="Encrypted Image")

        original_image = cv2.imread('rahasia1.png')
        processed_image = cv2.imread('rahasia2.png')
        st.write("MSE Evaluation : ", compare_mse(original_image, processed_image))

        encrypted_image_path = "./rahasia2.png"

        with open(encrypted_image_path, "rb") as f:
            image_data = f.read()
        # Display the download button
        st.download_button(
            label="Download Image",
            data=image_data,
            file_name="image.jpg",
            mime="image/jpeg",
            )
        


# If the user clicks on the decrypt button
if decrypt_button:

    # Check if the uploaded image is not empty
    if uploaded_image is not None:

        # Decrypt the image
        decrypted_text = decrypt_image(uploaded_image)
        decrypted_text = ed.final_dcr(caesar_cipher_key, playfair_cipher_key, decrypted_text)

        # Display the decrypted text
        st.write("Decrypted Text:", decrypted_text)

