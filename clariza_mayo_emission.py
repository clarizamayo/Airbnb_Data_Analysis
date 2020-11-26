from bs4 import BeautifulSoup
import requests
import csv
url = "https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions"

def co2_emissions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.find("table", attrs = {"class":["wikitable", "sortable", "jquery-tablesorter"]}) 
    rows = table.find_all('tr')
    th_td_list = []
    for row in rows[2:]:
        tds = row.findAll('td')
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()
            td_text = td_text.replace(',',"")
            if td_text == 'n/a':
                td_text = None      
            else:
                td_text = td_text              
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row)
    return th_td_list

def data_to_csv(url):
    with open("clariza_mayo_emissions.csv", "w") as csvfile:
        file = csv.writer(csvfile)
        file.writerow(["Country","1990","2005","2017","Percentage of world Emmisions","2017 vs 1990 Percentage Change", "Per Land Area", "Per Capita"])
        file.writerows(co2_emissions(url))
        
data_to_csv(url)