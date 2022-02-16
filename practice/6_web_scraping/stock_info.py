"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


def youngestceo():
    url = 'https://finance.yahoo.com/most-active'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    }
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')
    liststock = []
    listname = []
    for item in soup.select('.simpTblRow'):
        liststock.append(item.select('[aria-label=Symbol]')[0].get_text())
        listname.append(item.select('[aria-label=Name]')[0].get_text())

    b = 0
    output = {"Code": [], "Name": [], "Country": [], "Employees": [], "CEO": [], "Age": []}
    out = []

    while b <= (len(liststock) - 1):

        output["Code"].append(liststock[b])
        output["Name"].append(listname[b])
        url = 'https://finance.yahoo.com/quote/' + liststock[b] + '/profile?p=' + liststock[b]
        response = requests.get(url, headers=header)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        first = html_soup.find_all('div', class_='Mb(25px)')
        fo = html_soup.find_all('p', class_='D(ib) W(47.727%) Pend(40px)')
        for i in fo:
            output["Country"].append(i.contents[4])
        fo = html_soup.find_all('p', class_='D(ib) Va(t)')
        for i in fo:
            output["Employees"].append(i.contents[10].get_text())
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.content, 'lxml')
        output["CEO"].append(soup.select('[class="Ta(start)"]')[0].get_text())
        output["Age"].append(soup.select('[class="Ta(end)"]')[2].get_text())
        out.append(output.copy())
        output = {"Code": [], "Name": [], "Country": [], "Employees": [], "CEO": [], "Age": []}
        b = b + 1
    newout = sorted(out, key=lambda d: d['Age'])
    i = 0
    while i < (len(out) - 5):
        del newout[0]
        i = i + 1
    print("==================================== 5 stocks with most youngest CEOs ===================================")

    t = PrettyTable(['Name', 'Code', 'Country', 'Employees', 'CEO', 'Age'])
    for i in newout:
        t.add_row(
            [str(i['Name']), str(i['Code']), str(i['Country']), str(i['Employees']), str(i['CEO']), str(i['Age'])])
    print(t)
def bestchange():
    pass
# 5 stocks with most youngest CEOs
# youngestceo()
# 10 stocks with best 52-Week Change
bestchange()