import cv2
import os

# Load the image
img = cv2.imread("react_logo.jpg")  # Ensure the file exists

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message (ASCII only): ")
password = input("Enter a password: ")

# Character-to-value mapping (0-255)
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape  # Get image dimensions

n, m, z = 0, 0, 0  # Pixel indices

# Encryption
for char in msg:
    if n >= height or m >= width:
        print("Error: Message is too long for this image!")
        exit()

    img[n, m, z] = d[char]  # Encode character into pixel
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= width:
            m = 0
            n += 1

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens image on Windows

# Decryption
message = ""
n, m, z = 0, 0, 0  # Reset indices

pas = input("Enter password for decryption: ")
if password == pas:
    for _ in range(len(msg)):
        if n >= height or m >= width:
            break  # Stop if we reach image boundary

        message += c[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= width:
                m = 0
                n += 1

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT THE CORRECT PERSON")
