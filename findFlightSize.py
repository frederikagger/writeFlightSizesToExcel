from bs4 import BeautifulSoup
import requests

source = requests.get('http://www.airlinecodes.co.uk/arctypes.asp').text
soup = BeautifulSoup(source, 'html.parser')
html = soup.find('html')


# def that return a size when given a flightnumber
def findSize(flightNumber):
    found = False
    #loop through the html and
    for row in html.find_all_next(string=True):
        if flightNumber in row:
            found = True
        if found:
            if row.strip() == 'L':
                return 'L'
            if row.strip() == 'M':
                return 'M'
            if row.strip() == 'H':
                return 'H'
