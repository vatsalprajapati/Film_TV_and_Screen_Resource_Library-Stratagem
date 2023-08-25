from bs4 import BeautifulSoup
import requests
import warnings

warnings.filterwarnings("ignore")



filename="Scrape.csv"
f=open(filename,"w")
f.write("Title,Description,link \n")
f.close()



#for elements in list2:
 #   print(elements.find("li",{"class":"mrgn-bttm-md"}))



def parser(baseurl):
    source = requests.get(baseurl).text
    soup = BeautifulSoup(source, "lxml")
    list = soup.find("div", {"id": "results"})
    list2 = list.find("div", {"id": "wb-tables-id-0"})

    for elements in list2.findAll("li", {"class": "mrgn-bttm-md"}):
        Title = elements.a.text.strip()
        print(Title)
        link = elements.a['href'].strip()
        print(link)
        Description = elements.find("span", {"data-name": "summary"}).text.strip()
        print(Description.replace(",","|"))
        f1 = open(filename, "a")
        f1.write(Title.replace(",","|") + "," + Description.replace(",","|") + "," + link +  "\n")
        f1.close()

state=1
i=0
while(state==1):
    baseurl = "https://www120.statcan.gc.ca/stcsr/en/sr1/srs?start=" + str(i) + "&showSum=hide&fq=&enableElevation=true&fq=stclac%3A2&q=film&sort=score+desc#"
    print(baseurl)
    i += 25
    parser(baseurl)
    source1 = requests.get(baseurl).text
    soup1 = BeautifulSoup(source1, "lxml")
    next=soup1.find("a",{"class":"paginate_button next btn-sm"})
    try:
        text=next.text
        state=1
    except:
        state=0



