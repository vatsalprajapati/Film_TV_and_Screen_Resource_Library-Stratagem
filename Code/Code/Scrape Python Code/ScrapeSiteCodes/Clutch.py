from bs4 import BeautifulSoup
import requests
import sys

source = "https://clutch.co/ca/agencies/video-production?page="
base = "https://clutch.co"
filename = "Scrape.csv"
f = open(filename, "w")
headers = "Name,MinProjectSize,Wage,Team-Size,Website,location\n"
f.write(headers)
f.close()


def siteparser(insideurl):
    print("Inside nest loop")

    source2 = requests.get(insideurl).text

    soup2 = BeautifulSoup(source2, "lxml")

    try:
        Title = soup2.find("div", {"class": "header-company company_logotype"}).text.strip()
    except:
        Title = "Not Found "
    try:
        Minproject = soup2.find("div", {"data-content": "<i>Min. project size</i>"}).text.strip()
    except:
        Minproject = "Not Found"
    try:
        Price = soup2.find("div", {"data-content": "<i>Avg. hourly rate</i>"}).text.strip()
    except:
        Price = "Not Found"
    try:
        Size = soup2.find("div", {"data-content": "<i>Employees</i>"}).text.strip()
        Size2= "Size : "+Size
    except:
        Size = "N/A"
    try:
        link = soup2.find("li", {"class": "website-link-a"})
        site = link.a["href"]
    except:
        site = "N/A"
    try:
        loc = soup2.find("div", {"class": "field-location"})
        location = loc.span.text.strip()
    except:
        location = "N/A"

    print(
        Title.replace(",", "") + "," + Minproject.replace(",", "") + "," + Price.replace(",", "") + "," + Size.replace(
            ",", "") + "," + site.replace(",", "") + "," + location.replace(",", " ") + "\n")
    f1 = open(filename, "a")
    f1.write(
        Title.replace(",", "") + "," + Minproject.replace(",", "") + "," + Price.replace(",", "") + "," + Size2.replace(
            ",", "") + "," + site.replace(",", "") + "," + location.replace(",", " ") + "\n")
    f1.close()


def mainsiteparser(url):
    source1 = requests.get(url).text
    soup = BeautifulSoup(source1, "lxml")
    List = soup.find("div", {"class": "list_wrap"})
    ##print(List)
    try:
        for divs in List.find_all("div", {"class": "row"}):
            try:
                href = (divs.find("a", {"data-link_text": "Profile Button"})["href"])
                site = base + href + "#summary"
                print(site)
                siteparser(site)
            except:
                continue

    except:
        print("Nothing")


for i in range(0, 10):
    page = source + str(i)
    mainsiteparser(page)

