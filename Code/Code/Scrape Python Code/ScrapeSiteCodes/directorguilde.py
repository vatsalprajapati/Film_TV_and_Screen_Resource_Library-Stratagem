from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests  
#import openpyxl
import pandas as pd

filename = "DGCv6.csv"
f = open(filename,"w", encoding="utf-8")

headers = "Name, Email, Contact, Title, Currently Working, Availibility\n"
f.write(headers)
f.close()

#excelf = openpyxl.Workbook()
#print(excel.sheetnames)

try:

    #webpage = requests.get('https://www.dgc.ca/en/ontario/avails-and-production-lists/availability-list/AdvancedSearchForm?district=2&department=&jc%5B%5D=24&advancedSearch=&Submit=Submit#search-results-start')
    #webpage.raise_for_status()


    #req = Request('https://www.dgc.ca/en/ontario/avails-and-production-lists/availability-list/AdvancedSearchForm?district=2&department=&jc%5B%5D=24&advancedSearch=&Submit=Submit#search-results-start')
    #webpage = urlopen(req).read()

    print(" Check Point #1  ")
    url="https://www.dgc.ca/en/ontario/avails-and-production-lists/availability-list/generatePrintableOtherResult?advancedSearch=&district=2&onlyDirector=0&department=&jc%5B0%5D=&onlyAvailable=0&pdf=0&Submit=Submit"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')

    print(" Check Point #2 ")


    soup = BeautifulSoup(webpage,'html.parser')
    
    jlist = soup.find('tbody').find_all('tr')
    #pn = jlist.get_text()
    print(len(jlist))
    #print(pn)
    cnt=0
    chk=0
    cdk=3
    
    for job in jlist:

       
        try:

            innerrow = job.find('div', class_="row nomargin").find_all('div',class_="col-sm-3")

            # try:
                #     rr = ro.find_all('br')
                    
                #     for xx in rr:

                #         xy = xx.get_text(strip=True).replace(",",";")
                #         yyz=xy.get_text()

                #         sp = yyz.split("(")
                #         num = ("("+sp[1])
                #         print(num + " 202 ")
                        
                #         sp2 = sp[0].split(",")
                #         mail = sp2[1]
                #         print(mail + " 202 ")



                #         # if fy in xx:
                #         #     xx.replace(fy,'')
                        
                #         # print(xx)
                #         f.write(","+ num + "," + mail )
                    
                #     #print("     $$    " + rr)
                    
                # except:
                #     unwanted = ro.find('strong')
                #     unwanted.extract()
                #     cy = ro.get_text(strip=True)
                #     #cnt=cnt+1
                #     print(cy + "  303  ")
                #     f.write(","+ cy)
                
                # f.write( "\n" )
                # f.close()

          
            for ro in innerrow:
                
                f = open(filename,"a", encoding="utf-8")

                cy = ro.get_text(strip=True).replace("/ ","&")

                if cnt==chk:

                    fy = ro.find('strong').get_text(strip=True).replace(",",";")
                    print( "  #1 Name - " + fy)
                    f.write(fy)

                    sent = str(ro)
                    #sent=sent.replaceAll("</div>","")
                    se = sent.split("<br/>")
                    chk=chk+4
                    #print(len(se))

                    if (len(se)>=3):
                        print("  #2 Mail - " +se[1].strip())
                        f.write(","+se[1].strip())

                        ttt = se[2].replace("</div>"," ")
                        print( "  #3 Cell - " + ttt.strip())
                        f.write(","+ttt.strip())
                    
                    if (len(se)==2):

                        yyy = se[1].replace("</div>"," ")
                        print( "  #2 Mail - " +yyy.strip())
                        f.write(","+yyy.strip())
                        f.write(", ")

                    if (len(se)<2):
                        f.write(", ")
                        f.write(", ")


                else:

                    print( " #4 Others - " + cy +  "   count = " + str(cnt) )
                    f.write(","+ cy)
                    #f.write( "\n" )
                    #f.close()
                    if cnt==cdk:
                        f.write("\n")
                        cdk=cdk+4
                    
                    f.close()

                
                cnt=cnt+1


        except:
                continue

        

except Exception as e:
    print(e)
 
