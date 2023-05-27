from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

def foo(file, password):
    pdfwriter = PdfFileWriter()
    pdf = PdfFileReader(fr"{file}")

    for page in range(pdf.numPages):
        pdfwriter.add_page(pdf.pages[page])

    pdfwriter.encrypt(password)


    with open("protectedfile.pdf", 'wb') as file:
        pdfwriter.write(file)

def main():
    password = getpass(prompt="Enter password: ")
    filepath = input("Enter path of the file: ")
    foo(filepath, password)