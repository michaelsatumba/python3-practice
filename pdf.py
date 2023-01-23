import PyPDF2
import os

os.chdir('/Users/michaelsatumba/Desktop')
'''
# print(os.getcwd())
pdfFile = open('TPR Code of Business Conduct and Ethics May 2021.pdf', 'rb')
reader = PyPDF2.PdfReader(pdfFile)
pageNum = len(reader.pages)
# print(len(reader.pages))

page = reader.pages[0]
# print(page.extract_text())
for i in range(pageNum):
    print(reader.pages[i].extract_text())
'''
pdf1File = open('TPR Code of Business Conduct and Ethics May 2021.pdf', 'rb')
pdf2File = open('TPR Social Media Policy 2021-6-2 final.pdf', 'rb')

reader1 = PyPDF2.PdfReader(pdf1File)
reader2 = PyPDF2.PdfReader(pdf2File)

writer = PyPDF2.PdfWriter()
pageNum1 = len(reader1.pages)
pageNum2 = len(reader2.pages)

for i in range(pageNum1):
    page = reader1.pages[i]
    writer.add_page(page)
    
for i in range(pageNum2):
    page = reader2.pages[i]
    writer.add_page(page)

outputFile = open('combined.pdf', 'wb')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
