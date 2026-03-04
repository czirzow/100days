# day 45
from bs4 import BeautifulSoup
from pprint import pprint
#import lxml


file = "data/website.html"
with open(file, 'r') as fh:
    html = fh.read()
soup = BeautifulSoup(html, "html.parser")

if False:
    for tag in soup.find_all(name='a'):
        print(tag.getText(), ':', tag.get('href'))

h1 = soup.find(name="h1", id="name")
print(h1.getText())

h3 = soup.find(name="h3", class_="heading")
print(h3.getText())

company_url = soup.select_one(selector='p a')
print(company_url)

angela = soup.select_one('#name')
print(angela)

headings = soup.select('.heading')
pprint(headings)






