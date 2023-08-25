from bs4 import BeautifulSoup
import requests
import warnings
import sys
warnings.filterwarnings("ignore")

url="https://cionorth.ca/film-tv/hotlist"

source=requests.get(url).text
soup=BeautifulSoup(source,"lxml")

filename="Scrape.csv"
f=open(filename,"w")
f.write("Title,Type,Production House,Description \n")
f.close()

stuff=soup.findAll("div",{"class":"listing__box"})

for item in stuff:
    Post=item.find("div",{"class":"listing__header"})
    Title=Post.span.text.strip()
    print(Title)
    Type=Post.h5.text.strip()
    print(Type)
    try:
        Production= Post.p.text.strip()
        ProdText=""
        for prod in Production:
            ProdText+=prod.strip()

    except AttributeError:
        ProdText="NA"

    Meta= item.find("div", {"class": "listing__meta"})
    try:
        Description=Meta.p.text
        Single=""
        for Words  in Description:
            Single += Words.strip()


        Description=Single.replace(")",") : ")
        Description=Description.replace(","," ")
    except:
        Description="NA"

    f1=open(filename,"a")
    f1.write(Title +"," + Type + "," + ProdText + "," + Description + "\n" )
    f1.close()

