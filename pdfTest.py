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


black_image_file = 'Black.png'
blue_image_file = 'Blue.png'
#doc = fitz.open(filename)
