from bs4 import BeautifulSoup
import requests 
#import openpyxl
import pandas as pd

filename = "workopolis.csv"
f = open(filename,"w")

headers = "Role, Company, Location, Description, Salary\n"
f.write(headers)
f.close()
#excelf = openpyxl.Workbook()
#print(excel.sheetnames)

try:
    source = requests.get('https://www.workopolis.com/jobsearch/find-jobs?ak=film+industry&l=Calgary%2C+AB&job=2bl4QrssMt9cmZI7ibACIncLrAPy7U42ZyeDkXv859empQEt2o-yEw')
    source.raise_for_status()

    soup = BeautifulSoup(source.text,'html.parser')
    
    jlist = soup.find('main', id="job-list", class_="jobs").find_all('article', class_="JobCard")
    
    for job in jlist:

        role = job.find('h2', class_="JobCard-title").a.get_text(strip=True).replace(",",";")
        company = job.find('div', class_="JobCard-property JobCard-company").span.get_text(strip=True)
        location = job.find('span', class_="JobCard-property JobCard-location").get_text(strip=True).split('—')[1].replace(", ","-")
        desc = job.find('div', class_="JobCard-snippet").get_text(strip=True).replace(",",";")
        sal = job.find('span', class_="Salary").get_text(strip=True).replace(",",";")
        
        print(role + "  ---  " + company + "  ---  " + location + "  ---  " + desc + "  ---  " + sal + " \n ")
        # print(company)
        # print(location)
        # print(desc)
        # print(sal)
        # print("\n")

        f = open(filename,"a")

        f.write(role + "," + company + "," + location + "," + desc + "," + sal + "\n")
        f.close()

        

except Exception as e:
    print(e)







 
