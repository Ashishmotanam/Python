import requests
from  bs4 import BeautifulSoup
import os
l=[]
link_1="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
link=requests.get(link_1) # getting access to the link

obj=BeautifulSoup(link.content,"html.parser") #Calling the beautiful soup function for the link
print( obj.title)
l.append(obj.find_all('a')) # appending all a's in list

for i in obj.find_all('a'):
    print(  i.get('href')) # printing the links with respect to a using for loops

table = obj.find("table", { "class" : "wikitable sortable plainrowheaders" }) # finding table using class
for row in table.findAll("tr"): # finding table rows
    t_data = row.findAll("td") # finding table data
    t_heading=row.findAll("th") # finding table headers
    print(t_data)
    print(t_heading)