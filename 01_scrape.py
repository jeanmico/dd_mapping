import requests
from bs4 import BeautifulSoup

url = 'https://locations.dunkindonuts.com/en/ma'
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'html.parser')

links = [x.get('href') for x in soup.find_all('a', href=True)]
links = [l for l in links if l.startswith('..')]
links = [url + i[8:] for i in links[1:]]

my_adds = []
for i,j in enumerate(links):
    r = requests.get(links[i])
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')
    adds = soup.find_all('div', class_='text-base-mobile font-secondary')
    addresses = [x.get_text() for x in adds]
    my_adds += addresses
print(my_adds)
with open('/mnt/c/Users/jeanmico/projects/misc/dunks/data/addresses_raw.txt', 'w') as outfile:
    outfile.write('\n'.join(str(i) for i in my_adds))


