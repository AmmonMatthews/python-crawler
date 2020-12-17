import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=Boise__2C-ID'
URL_ONE = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
job_elems = results.find_all('section', class_='card-content')

for job in job_elems:
  title_elem = job.find('h2', class_='title')
  company_elem = job.find('div', class_='company')
  location_elem = job.find('div', class_='location')
  if None in (title_elem, company_elem, location_elem):
    continue
  print(title_elem.text.strip())
  print(company_elem.text.strip())
  print(location_elem.text.strip())
  print()


# Search for a specific job by title and find the anchor tag to go a long with it. 
  python_jobs = results.find_all('h2',
                               string=lambda text: "software" in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

# print(results.prettify())