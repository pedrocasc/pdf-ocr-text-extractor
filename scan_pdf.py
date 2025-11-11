import pytesseract
from pdf2image import convert_from_path
import os

# Set Tesseract path for Windows (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set poppler path for Windows
POPPLER_PATH = r'C:\poppler\Library\bin'  # Adjust to where you extracted poppler

# Set OCR language
# Options: 'eng' (English), 'por' (Portuguese), 'eng+por' (both)
OCR_LANGUAGE = 'eng'

def extract_text_from_pdf(pdf_path, output_path=None):
    """Extract text from a scanned PDF."""
    try:
        # Check if file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Convert PDF to images with poppler path
        pages = convert_from_path(pdf_path, dpi=300, poppler_path=POPPLER_PATH)
        
        text = ""
        for i, page in enumerate(pages):
            print(f"Processing page {i+1}/{len(pages)}...")
            text += pytesseract.image_to_string(page, lang=OCR_LANGUAGE)
            text += "\n\n--- Page Break ---\n\n"
        
        # Save to file if output path provided
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text saved to {output_path}")
        
        return text
    
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    text = extract_text_from_pdf("scanned.pdf", "output.txt")
    if text:
        print("Extraction completed successfully!")
