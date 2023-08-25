from bs4 import BeautifulSoup
import requests 
#import openpyxl
import pandas as pd

filename = "canadamediafund.csv"
f = open(filename,"w", encoding="utf-8")

headers = "Project, Company, Year, Content_Type, Commitment, Broadcaster, Activity, Genre, Delivery Method, Round, Region, Program, Status, Language, Selection Round\n"
f.write(headers)
f.close()

try:

    for z in range(1,155):

        url = "https://cmf-fmc.ca/funded-projects/?_paged="+str(z)+"&_per_page=100"
        source = requests.get(url)
        source.raise_for_status()

        #cnt=1

        soup = BeautifulSoup(source.text,'html.parser')

        #sample = soup.find_all('div', class_="accordion")

        #for s in sample:

            #ss = sample.get_text(strip=True)

            #print("      ++++++++++++++++++        " + ss + "          +++++++++++++++        ")

        plist = soup.find('div', class_="facetwp-template").find_all('article', class_="item")

        for proj in plist:

            #print(" counter =  " + cnt)
            #cnt=cnt+1
            print("\n")
            pname = proj.find('span', class_="h4 mb-0 toggle-header").get_text(strip=True).replace(",",";")
            company = proj.find('span', class_="sub-title").get_text(strip=True).replace(",",";")

            activity = proj.find('div', class_="inner pb-3").find_all('div', class_="detail")

            f = open(filename,"a", encoding="utf-8")
        
            print( pname + " - " + company + " - " )

            f.write(pname + "," + company )

            for ac in activity:

                unwanted = ac.find('div', class_="h6")
                unwanted.extract()
                fy = ac.get_text(strip = True).replace(",",";")

                print( fy + " - " )
                f.write("," + fy )

            f.write( "\n" )
            f.close()
        

except Exception as e:
    print(e)

        
        
        

