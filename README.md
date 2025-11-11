# PDF OCR Text Extractor

A Python script that extracts text from scanned PDFs using Optical Character Recognition (OCR). Supports multiple languages including English and Portuguese.

## Features

- Extract text from scanned PDF documents
- Support for multiple languages (English, Portuguese, or both)
- High-quality OCR using Tesseract
- Save extracted text to a file
- Progress tracking for multi-page PDFs

## Prerequisites

Before running this script, you need to install the following:

### 1. Python Dependencies

```bash
pip install pytesseract pdf2image pillow
```

### 2. Tesseract OCR

**Download and Install:**
- Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
- Install to default location: `C:\Program Files\Tesseract-OCR\`
- During installation, make sure to select the language packs you need

**Install Portuguese Language Data (Optional):**
1. Download `por.traineddata` from: https://github.com/tesseract-ocr/tessdata
2. Place it in: `C:\Program Files\Tesseract-OCR\tessdata\`

### 3. Poppler for Windows

**Download Pre-built Binaries:**
1. Download poppler from: https://github.com/oschwartz10612/poppler-windows/releases/
2. Extract to a folder (e.g., `C:\poppler`)
3. Update the `POPPLER_PATH` in `scan_pdf.py` to match your extraction location

## Configuration

Edit the variables at the top of `scan_pdf.py`:

```python
# Set Tesseract path (adjust if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set poppler path (adjust to your extraction location)
POPPLER_PATH = r'C:\poppler\Library\bin'

# Set OCR language
OCR_LANGUAGE = 'eng'  # Options: 'eng', 'por', 'eng+por'
```

### Language Options

- `'eng'` - English only
- `'por'` - Portuguese only
- `'eng+por'` - Both English and Portuguese

## Usage

### Basic Usage

Place your scanned PDF file in the project folder and run:

```bash
python scan_pdf.py
```

By default, it looks for `scanned.pdf` and saves the output to `output.txt`.

### Custom Usage

Edit the main block in `scan_pdf.py`:

```python
if __name__ == "__main__":
    # Extract text from custom PDF
    text = extract_text_from_pdf("your_document.pdf", "custom_output.txt")
    if text:
        print("Extraction completed successfully!")
```

### Programmatic Usage

You can also import and use the function in your own scripts:

```python
from scan_pdf import extract_text_from_pdf

# Extract text
text = extract_text_from_pdf("document.pdf", "output.txt")

# Or just get the text without saving
text = extract_text_from_pdf("document.pdf")
print(text)
```

## Troubleshooting

### "Tesseract not found" Error
- Make sure Tesseract is installed
- Verify the path in `pytesseract.pytesseract.tesseract_cmd` matches your installation

### "Poppler not found" Error
- Download and extract poppler binaries
- Update `POPPLER_PATH` to point to the `bin` folder inside your poppler installation

### "Language not found" Error
- Download the required language data files from Tesseract's GitHub
- Place them in `C:\Program Files\Tesseract-OCR\tessdata\`

### Poor OCR Quality
- Try increasing the DPI in the code: `convert_from_path(pdf_path, dpi=400)`
- Ensure your PDF has good image quality
- Make sure you're using the correct language setting

## How It Works

1. The script converts each PDF page to an image using `pdf2image`
2. Each image is processed through Tesseract OCR
3. Extracted text is combined with page breaks
4. The final text is saved to an output file
