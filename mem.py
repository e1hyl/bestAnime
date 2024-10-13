from bs4 import BeautifulSoup
import requests

mem_url = "https://myanimelist.net/topanime.php?type=bypopularity"
mem_html_content = requests.get(mem_url).text


soupM = BeautifulSoup(mem_html_content, 'lxml')
mem_table_rows = soupM.find_all('div', class_='information di-ib mt4')
name_mem_table_rows = soupM.find_all('a', class_='hoverinfo_trigger')


strip_mem_names = [0] * 100
no_wsp_strip_mem_names = [0] * 50
j = 0


for name_rowsM in name_mem_table_rows:
    strip_mem_names[j] = name_rowsM.text.strip()
    j = j + 1
    # print(name_rowsM.text.strip())

other_counterM = 0

for y in range(100):
    if y % 2 == 1:
        no_wsp_strip_mem_names[other_counterM] = strip_mem_names[y]
        other_counterM = other_counterM + 1

mem_amounts = [0] * 50
Mcounter = 0

for rows in mem_table_rows:
    split_mem_rows = rows.text.strip().rsplit(" ")
    # print(split_mem_rows[22])
    if Mcounter == 18:
        mem_amounts[Mcounter] = split_mem_rows[21]
    else:
        mem_amounts[Mcounter] = split_mem_rows[22]
    Mcounter = Mcounter + 1 

dict_mem = dict(zip(no_wsp_strip_mem_names, mem_amounts))
