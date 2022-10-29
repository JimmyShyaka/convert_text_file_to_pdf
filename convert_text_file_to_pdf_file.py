# This is a Python program to convert
# a text file to a pdf file

# import the module that is used for this pdf conversion operation

from fpdf import FPDF

import os # import the os module used to create/get directory paths

current_directory=os.getcwd()  # variable to get current working directory

# save this imported FPDF() class
# into a variable called pdf

pdf = FPDF()

# Adding a page

pdf.add_page()

# set style and size of font
# that you want in the pdf

pdf.set_font("Times", size=15)

# open the text file in read mode
# place the text file into the current working directory or
# provide the path to the text file if located in another location

file = open(f"{current_directory}/my_text_file.txt", "r")

# for loop to insert the texts in pdf

for text in file:

# check this website for details explanation for all
# those settings below in the multi_cell method below
# https://pyfpdf.readthedocs.io/en/latest/reference/multi_cell/index.html
    pdf.multi_cell(190, 8, txt=text, border=0, align='L', fill=False )

# output to the pdf with name of your choice with .pdf extension
pdf.output(f"{current_directory}/my_new_pdf_file.pdf")
