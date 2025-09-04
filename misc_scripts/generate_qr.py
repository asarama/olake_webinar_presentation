import qrcode
import sys

def generate_qr_code(url, filename):
    """
    Generates a QR code for the given URL and saves it to a file.
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        # Add data to the QR code
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(filename)
        print(f"Successfully generated QR code and saved it as {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_qr.py <url> <filename.png>")
    else:
        url_to_encode = sys.argv[1]
        output_filename = sys.argv[2]
        if not output_filename.endswith('.png'):
            output_filename += '.png'
        generate_qr_code(url_to_encode, output_filename)
