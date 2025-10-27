# Text extraction from image
This repository helps to extract text from images using YOLOv8 and PyTesseract.

To try this project, 
- Clone the repository
```
git clone https://github.com/joshwat33/Text_extraction_from_image.git
cd Text_extraction_from_image
```
- Install the dependencies 
```
pip install -r requirements.txt
```
You need to install [Google Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki), if not already done. 
If Tesseract is not added to your system’s PATH, you must specify its full installation path in your code:
```
pytesseract.pytesseract.tesseract_cmd = r"<full_path_to_your_tesseract_executable>"
```
If Tesseract is already added to your PATH, you can comment out or remove this line.
