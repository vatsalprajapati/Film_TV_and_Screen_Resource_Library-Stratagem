from bs4 import BeautifulSoup
import requests

import warnings

from pdfrw import PdfReader

warnings.filterwarnings("ignore")

url = "https://ontariocreates.ca/research/statistics"
source2 = requests.get(url).text
soup2 = BeautifulSoup(source2, "lxml")

souplist = soup2.findAll("li", {"class": "list-unstyled"})

filename="Scrape.csv"
f=open(filename,"w")
f.write("Title,PDF Keyword ,PDFLink \n")
f.close()


for elements in souplist:
    #count += 1
    Year = elements.a.text.strip()
    Title_Report= "Report - Ontario Film and Televsion " + Year[0:4]
    Pdflink = elements.a['href'].strip()
    print(Title_Report + Pdflink)
    response = requests.get(Pdflink)
    rawcontent = response.content

    with open("Pdf.pdf", "wb") as new_data:
        new_data.write(rawcontent)

    try:
        Keyword=PdfReader("Pdf.pdf").Info.Title
        Keyword.strip()
    except AttributeError:
        Keyword=Title_Report

    f1 = open(filename, "a")
    f1.write(Title_Report + "," + Keyword + "," + Pdflink +  "\n")
    f1.close()



    #pdftitle -p Pdf.pdf
    #tab = tabula.read_pdf("Pdf.pdf")

    #tabula.convert_into("Pdf.pdf", "Crawler" + str(count) + ".csv", output_format="csv", pages="all")

    # df=tabula.read_pdf("Pdf.pdf",pages="all")
    # tabula.convert_into("Pdf.pdf", "PDF.csv", output_format="csv",  all=True)


