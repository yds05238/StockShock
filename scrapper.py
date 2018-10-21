'''
from bs4 import BeautifulSoup
import urllib.request


CREATE A JSON FILE OF NASDAQ 100 COMPANIES + DATA

#FIGURE OUT WHY SSL ERROR IS FORMING
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

testlink = 'https://pythonprogramming.net/parsememcparseface/'
top100 = 'https://www.suredividend.com/nasdaq-100-stocks-list/'
source = urllib.request.urlopen(top100, context=ctx)

soup = BeautifulSoup(source, 'lxml')
#print(soup)
table = soup.table
table = soup.find('table')
#print(table)

#find all the table rows
row_list = []
table_rows = table.find_all('tr')[1:-1]
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
    #print(row)
#print(row_list)

#put data into a dictionary
#key is company name, value is list of data
dict = {}
for row in row_list:
    dict[row[1]] = [row[0], row[2], row[3], row[4], row[5], row[6]]
#print(dict)

import json
d = [{'Company':key,"Ticker":value[0],"Price":value[1],
"Dividend Yield":value[2],"Market Cap ($M)":value[3],"P/E Ratio":value[4],
"Payout Ratio":value[5]} for key,value in dict.items()]
j = json.dumps(d, indent=4)

f = open("companies.json", 'w')
#print(j, file=f)
f.close()

#user_input = input("input company name: ")
#values = dict[user_input]
#print("Price: " + values[1])
#print("Dividend Yield: " + values[2])
#print("Market Cap ($M): " + values[3])
#print("P/E Ratio: " + values[4])
#print("Payout Ratio: " + values[5])
'''
import bs4 as bs
import urllib.request
import sys

testlink = 'https://pythonprogramming.net/parsememcparseface/'
top100 = 'https://www.suredividend.com/nasdaq-100-stocks-list/'
source = urllib.request.urlopen(top100).read()
soup = bs.BeautifulSoup(source, 'lxml')
#print(soup)
#table = soup.table
table = soup.find('table')
#print(table)

#find all the table rows
row_list = []
table_rows = table.find_all('tr')[1:-1]
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
#print(row_list)

row_list = [[s.replace(",","") for s in element] for element in row_list]

#put data into a dictionary
#key is company name, value is list of data
dict = {}
for row in row_list:
    dict[row[1]] = [row[0], row[2], row[3], row[4], row[5], row[6]]
for i in dict:
    dict[i] = [dict[i][0]] + [0.0 if x == '' else float(x) for x in dict[i][1:]]

#print(dict)

import json
d = [{'Company':key,"Ticker":value[0],"Price":value[1],
"Dividend Yield":value[2],"Market Cap ($M)":value[3],"P/E Ratio":value[4],
"Payout Ratio":value[5]} for key,value in dict.items()]
j = json.dumps(d, indent=4)
f = open('companies.json', 'w')
print(j, file=f)
f.close()


#user_input = input("input company name: ")
#values = dict[user_input]
#print("Price: " + values[1])
#print("Dividend Yield: " + values[2])
#print("Market Cap ($M): " + values[3])
#print("P/E Ratio: " + values[4])
#print("Payout Ratio: " + values[5])
