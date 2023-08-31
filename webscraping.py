import requests
import pandas
from bs4 import beautifulsoup

response =requests.get("flipkart.com/automotive-accessories/helmets-and-riding-gear/helmet-and-accessories/biker-helmets/pr?sid=1mt%2Cztf%2Civ8%2Ctih&marketplace=FLIPKART&hpid=8c7ftGcyG0cjQM1vrbGcgap7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIDY5OSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6IkhMTUdSRE1DTks0RUhaM1ciLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJSaWRlciBIZWxtZXRzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_59ca6fe8-3931-4317-a54b-24c4b5c241d3_7.V5VSIKF9EZSQ&ppt=None&ppn=None&ssid=ol50ulu10w0000001692368616035&otracker=hp_omu_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_1_7.dealCard.OMU_V5VSIKF9EZSQ_5&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Beauty%252C%2BFood%252C%2BToys%2B%2526%2Bmore_NA_dealCard_cc_1_NA_view-all_5&cid=V5VSIKF9EZSQ")
print(response)  #after run we have to get output "200 "means they give access to scrap the data
soup=beautifulsoup(response.content) # this soup function is used to scrap the data from the website
print(soup)
names=soup.findall('div',class_='_khbsbj')  # this used to convert unstructed data into structred data
for  i in names[20]: # we want only 20 mobiles data so we have to given range
    d= i.text     #we want it in text format and the data is in append mode
    name.append(d)
    print (name)