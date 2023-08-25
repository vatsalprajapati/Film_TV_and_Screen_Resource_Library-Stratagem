from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import warnings



warnings.filterwarnings("ignore")

site= "https://cmpa.ca/resource-library/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page,"lxml")

filename="Scrape.csv"
f=open(filename,"w")
f.write("Title,Description,Pdf Link\n")
f.close()




Data=soup.find("div",{"class":"resource-library-item-wrapper"})

for post in Data.find_all("div",{"class":"resource-library-body"}):
    Title=post.find("div",{"class":"custom-1 cmpa-resource-library-name col-1"}).text
    print(Title)
    try:
        Desc=post.find("div",{"class":"custom-1 cmpa-resource-library-description col-3"})
        Desc1=Desc.p.text.strip()
        Description=Desc1


    except:
        Description="NA"
    LinkPdf=post.find("div",{"class":"cmpa-resource-library-button col-4"})
    site=LinkPdf.a["href"]
    print(site)
    try:
        f2=open(filename,"a")
        f2.write(Title.replace(","," ") + "," + Description.replace(","," ") + "," + site + "\n")
        f2.close()
    except:
        continue







