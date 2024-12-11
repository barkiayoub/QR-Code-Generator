import qrcode

def generate_qr_code(data: str, file_name: str):
    """
    Generates a QR code from provided data and saves it as an image file.

    Args:
        data (str): The text or URL to encode into the QR code.
        file_name (str): The name of the file to save the QR code image (e.g., 'qrcode.png').

    Returns:
        None
    """
    # Create a QRCode instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the data to the QRCode
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QRCode instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)

if __name__ == "__main__":
    # Example usage: Generate a QR code for any data
    sample_data = "https://www.example.com" # Replace with your link
    output_file_name = "example_qrcode.png" # Define your output file name

    generate_qr_code(sample_data, output_file_name)
    print(f"QR code saved as {output_file_name}")
