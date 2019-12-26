import os
import PyPDF2


def extract_data_from_pdf(fullPath):

    path = (fullPath.rsplit('\\', 1))

    os.chdir(path[0])
    print(os.listdir("."))
    for file in os.listdir("."):
        if file.endswith(".pdf"):
            print(file)
            pp = PyPDF2.PdfFileReader(open(file, "rb"))
    return pp.pages[0].extractText()


extract_data_from_pdf('E:\\RajTestReport\\RajTestMedicalReport.pdf')
