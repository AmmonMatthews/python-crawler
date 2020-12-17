import requests

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=Boise__2C-ID'
page = requests.get(URL)