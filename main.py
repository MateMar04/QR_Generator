import qrcode

# Creates a QR code instance
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Adds data to the QR code
data = "www.google.com"  # Your link
qr.add_data(data)

# Makes the QR code
qr.make(fit=True)

# Creates an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# save the image
img.save("example.png")  # Your filename