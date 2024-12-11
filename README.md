# QR Code Generator

This Python script generates QR codes from any given text or URL and saves them as image files. It uses the `qrcode` library to create the QR codes with customizable options such as box size and border.

## Features

- Generate QR codes from any text or URL.
- Save the QR code as an image file.
- Customize QR code appearance.

## Requirements

- Python 3.6 or higher
- `qrcode` library (Install using `pip install qrcode[pil]`)

## Usage

### Step 1: Clone the repository

```bash
git clone https://github.com/barkiayoub/QR-Code-Generator.git
```

### Step 2: Install dependencies

Make sure you have Python installed, then install the required library:

```bash
pip install qrcode[pil]
```

### Step 3: Run the script

To generate a QR code, run the script and follow the prompts to input the data and file name:

```bash
python QR_Code_Generator.py
```

Alternatively, you can modify the script to hardcode the values of `data` and `file_name` for quicker execution.

### Example Output

The script will generate a QR code for the given text or URL and save it as an image file (e.g., `example_qrcode.png`). You can open this file to view the QR code.

![Main Interface](example_qrcode.png)

## Customization

You can call the `generate_qr_code` function in your own Python script with your desired parameters:

```python
from qr_code_generator import generate_qr_code

generate_qr_code("https://www.example.com", "example_qrcode.png")
```

- **data**: The text or URL to encode.
- **file_name**: The name of the output image file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

