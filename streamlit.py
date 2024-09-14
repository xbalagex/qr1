import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Streamlit app
st.title("QR Code Generator")

# Input for URL
url = st.text_input("Enter the URL to generate QR code")

if url:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Display the QR code image
    st.image(img, caption="Generated QR Code", use_column_width=True)
    
    # Save QR code to buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    
    # Download QR code
    st.download_button(
        label="Download QR Code",
        data=buffer.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
