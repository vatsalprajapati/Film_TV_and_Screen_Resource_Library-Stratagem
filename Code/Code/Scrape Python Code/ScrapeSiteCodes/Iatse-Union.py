from bs4 import BeautifulSoup
import requests

filename="Scrape.csv"
f=open(filename,"w")
headers="UnionName,Craftname,Jurisdication,Phone,Fax,Website\n"
f.write(headers)
f.close()



def insideparser(url):
    f1=open(filename,"a")

    source1=requests.get(url).text
    soup1=BeautifulSoup(source1,"lxml")

    UnionName=soup1.find('div',{"data-id":"cc05e15"}).text.strip()
    CraftName=soup1.find('div',{"data-id":"cb60e26"}).text.strip()
    Juri=soup1.find('div',{"data-id":"358e08f"}).text.strip()
    Localphone=soup1.find('div',{"data-id":"0a6115f"}).text.strip()
    try:
        Localfax=soup1.find('div',{"data-id":"aeb3e2a"}).text.strip()
    except AttributeError:
         Localfax="No Fax Phone"
    try:
        site=soup1.find('div',{"data-id":"df4d78d"}).text.strip()
    except AttributeError:
        site="No Site Found"

    print(UnionName + "," + CraftName + "," + Juri.replace(","," |") + "," + Localphone + "," + Localfax + "," + site )
    f1.write(UnionName + "," + CraftName + "," + Juri.replace(","," |") + "," + Localphone + "," + Localfax + "," + site +"\n")
    f1.close()

def mainparser(url1):

    source = requests.get(url1).text
    soup = BeautifulSoup(source,"lxml")
    articles = soup.findAll("article")
    for info in articles:
        href = info.a['href']
        insideparser(href.strip())



for i in range(1,5):
    Sourceurl="https://iatse.net/local-union-directory/?_sfm_country=Canada&sf_paged="+"i"
    mainparser(Sourceurl)












