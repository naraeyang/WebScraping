import requests
from bs4 import BeautifulSoup

all_data=[]

def scrap_page(url):
    response= requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find_all('div', class_="bjs-jlid_meta")
    
    for job in jobs:
    # Using find within each job to get the first <a> tag with the specified attributes
    title=job.find('h4', class_='bjs-jlid__h').text
    company=job.find('a', class_='bjs-jlid__b').text
    jobdescription=job.find('div', class_='bjs-jlid__description').text
    link=job.find('a')[href]
    all_data={
        'title':title,
        'company':company, 
        'jobdescription':jobdescription,
        'link':link,
    }
    all_data.append(all_data)

#page button numbers

def get_page(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content, 'html.parser')
    buttons=len(soup.find(ul, class_=bsj-nav).find_all('a', class_=page_numbers))+1
    return buttons

total_page=get_page('https://berlinstartupjobs.com/engineering')

for x in range(total_page):
    url=f'https://berlinstartupjobs.com/engineering/page/{x}'
    scrap_page(url)

print(len(all_data))