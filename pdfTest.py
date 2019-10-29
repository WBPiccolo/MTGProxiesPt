#File di test per la creazione di pdf
#Uso PyMuPDF https://pymupdf.readthedocs.io/en/latest/tutorial/
import fitz
import os
from shutil import copyfile
from fpdf import FPDF
filename = 'output.pdf'
dirpath =os.path.dirname(__file__)
filepath = os.path.join(dirpath, filename)

# Creo il file pdf
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.output(filepath)

black_image_file = dirpath+'/Black.png'
blue_image_file = dirpath+'/Blue.png'
#Aggiungo le immagini al file pdf
#https://github.com/pymupdf/PyMuPDF/wiki/How-to-Insert-new-PDF-Pages,-Images-and-Text
# define the position (upper-right corner)
image_rectangle = fitz.Rect(450, 20, 550, 120)
# retrieve the first page of the PDF
file_handle = fitz.open(filepath)
first_page = file_handle[0]
# add the image
pix = fitz.Pixmap(black_image_file)
first_page.insertImage(image_rectangle, pixmap=pix, overlay=True)
#Se cambio il nome dell'output funziona
file_handle.save(filepath,incremental=True)
