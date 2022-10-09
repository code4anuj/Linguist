# importing required modules
import PyPDF2
	
class pdf2txt:
    def pdf2txt (ref, pdfpath):
        # creating a pdf file object
        pdfFileObj = open(pdfpath, 'rb')
        # creating a pdf reader object
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # printing number of pages in pdf file
        # print("Number of Pages = ",pdfReader.numPages)
        # creating a page object
        pageObj = pdfReader.getPage(0)
        # extracting text from page
        text = pageObj.extractText()
        print(text)
        return text
        # closing the pdf file object
        # pdfFileObj.close()

	
# pdfpath = "Problem_Statements.pdf"
# pdf = pdf2txt()
# cf = pdf.pdf2txt(pdfpath)








	

	

