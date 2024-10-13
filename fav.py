from bs4 import BeautifulSoup
import requests


fav_url = "https://myanimelist.net/topanime.php?type=favorite"
fav_html_content = requests.get(fav_url).text

soup = BeautifulSoup(fav_html_content, 'lxml')
fav_table_rows = soup.find_all('div', class_='information di-ib mt4')
name_fav_table_rows = soup.find_all('a', class_='hoverinfo_trigger')

strip_fav_names = [0] * 100
no_wsp_strip_fav_names = [0] * 100
i = 0

for name_rows in name_fav_table_rows:
    strip_fav_names[i] = name_rows.text.strip()
    i = i + 1
    
other_counter = 0

for x in range(100):
    if x % 2 == 1:
        no_wsp_strip_fav_names[other_counter] = strip_fav_names[x]
        other_counter = other_counter + 1
    
fav_amounts = [0] * 101
counter = 0

for rows in fav_table_rows:
    split_fav_rows = rows.text.strip().rsplit(" ")
    if counter == 1:
        fav_amounts[counter] = split_fav_rows[21]
    else:
        fav_amounts[counter] = split_fav_rows[22]
    counter = counter + 1  


dict_fav = dict(zip(no_wsp_strip_fav_names, fav_amounts))


##

