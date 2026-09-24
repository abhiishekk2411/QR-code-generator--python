QR Code Generator
A simple and interactive command-line Python application that generates custom QR codes. You can turn any URL or text into a QR code, customize the foreground and background colors, and save it with a custom or auto-generated timestamped filename.

Features
Interactive CLI: Prompts the user for data, colors, and filenames step-by-step.
Color Customization: Choose any standard color for the QR code and its background (e.g., navy on white, black on yellow).
Smart File Naming: Specify a custom name or let the script auto-generate a unique timestamped filename (e.g., qr_20260924_153139.png).
Instant Preview: Automatically opens the generated QR code image on your computer using Pillow.

Prerequisites
Python 3.x installed on your system.

Installation
Clone the repository (or download the files):

Bash
git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
Create and activate a virtual environment (optional but recommended):

Bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
Install the required libraries:

Bash
pip install "qrcode[pil]"
Usage
Run the script from your terminal:

Bash
python app.py
Example Session
Plaintext
Enter the URL or text for the QR code: https://github.com
Enter output filename (press Enter for default): my_github
Enter QR color (e.g. black, navy, darkgreen) [default: black]: navy
Enter background color (e.g. white, yellow, cyan) [default: white]: white
Success! Saved as 'my_github.png'

Technologies Used---
qrcode: Core library for QR code matrix generation.
Pillow (PIL): Image processing engine to render and save the .png files
qrcode: Core library for QR code matrix generation.

Pillow (PIL): Image processing engine to render and save the .png files.
