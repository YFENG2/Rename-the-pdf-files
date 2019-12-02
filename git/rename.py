from io import StringIO
from io import open
import os
import re
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

def read_pdf(pdf):
    #Read the PDF files 
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    #lines = str(content).split("\n")
    return content[:2000]

def re_name(filePath):
    # rename the read PDF files,
    # extract the pubilsh by using Regular expression.
    file_name = os.listdir(filePath)
    for name_ in file_name:
        with open(filePath + name_, "rb") as my_pdf: 
            a = read_pdf(my_pdf)
        r = re.findall('[21][0-9]{3}',a)
        i = 0
        while i <= len(r)-1:
            if int(r[i])>1900 and int(r[i])<2020:
                os.rename(filePath + name_,filePath + r[i]+'_' + name_) 
                print(r[i]+'_'+name_)
                break
            else:
                i = i +1


#please input your file path below.
filePath = '/home/feng/pdf/'         
re_name(filePath)
