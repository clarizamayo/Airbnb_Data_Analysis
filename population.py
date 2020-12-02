from bs4 import BeautifulSoup
import requests

def world_pop_2005(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.findAll("table")[1]
    rows = table.find_all('tr')[1:]
    th_td_list = []
    for row in rows[:-1]:
        th = row.findAll('th')
        tds = row.findAll('td')[1:-1]
        th_td_data_row = []
        for td in tds:
            td_text = td.text.strip()            
            th_td_data_row.append(td_text)              
        th_td_list.append(th_td_data_row)
    sorted_list = sorted(th_td_list)
    sorted_list.insert(0, ["Country", "Year"])
    return sorted_list