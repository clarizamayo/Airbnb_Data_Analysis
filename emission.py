from bs4 import BeautifulSoup
import requests

def co2_emissions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.find("table", attrs = {"class":["wikitable", "sortable", "jquery-tablesorter"]}) 
    rows = table.find_all('tr')
    th_td_list = []
    for row in rows[1:]:
        th = row.findAll('th')
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
        th_td_list[0] = ["Country", "1990", "2005", "2017", "Percentage of world Emissions", "2017 vs 1990 Percentage Change", "Per Land Area", "Per Capita"]
    return th_td_list