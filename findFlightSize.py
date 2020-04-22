from bs4 import BeautifulSoup
import requests

source = requests.get('http://www.airlinecodes.co.uk/arctypes.asp').text
soup = BeautifulSoup(source, 'html.parser')
html = soup.find('html')


def findSize(flightNumber):
    found = False
    for row in html.find_all_next(string=True):
        if flightNumber in row:
            found = True
        if found:
            if row.strip() == 'L':
                print('L')
                return 'L'
            if row.strip() == 'M':
                return 'M'
            if row.strip() == 'H':
                return 'H'
