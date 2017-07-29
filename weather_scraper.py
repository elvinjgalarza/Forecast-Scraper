print("\n"*70)
#This script scrapes code from the National Weather Service
#and grabs information about the 7 day forecast for Edinburg, Texas (78539)
import requests

#Download web page content
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=26.2976&lon=-98.1796#.WXttuYQrLX4")

#Returned 200, so successful download
#print(page.status_code)

from bs4 import BeautifulSoup

#Create instance of BS to parse the document
soup = BeautifulSoup(page.content, 'html.parser')

#div container with id 'seven-day-forecast' from webpage
seven_day = soup.find(id="seven-day-forecast")

#finds all individual days 
forecast_items = seven_day.find_all(class_="tombstone-container")

#extracts and prints first item and second item since find_all generates a list
afternoon = forecast_items[0]
tonight = forecast_items[1]

#print(afternoon.prettify())
#print("\n")
#print(tonight.prettify())
#print("\n")

#-------------------------------------------
#Extract a name, description of the conditions, short description, and temperature low
period0 = afternoon.find(class_="period-name").get_text()
short_desc0 = afternoon.find(class_="short-desc").get_text()
temp0 = afternoon.find(class_="temp temp-high").get_text()

period1 = tonight.find(class_="period-name").get_text()
short_desc1 = tonight.find(class_="short-desc").get_text()
temp1 = tonight.find(class_="temp").get_text()


print(period0[0:4] + " " + period0[4:13])
print(short_desc0)
print(temp0)
#Extract the title attribute from img tag

img0 = afternoon.find("img")
desc0 = img0['title']
print(desc0)

print("\n")

print(period1)
print(short_desc1)
print(temp1)

#Extract the title attribute from img tag

img1 = tonight.find("img")
desc1 = img1['title']
print(desc1)