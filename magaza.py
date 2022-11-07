import find, bs4, lxml, pymongo, requests, urllib.request, xlwt
from os import link
from bs4 import BeautifulSoup
from xlwt import Workbook

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["magaza_magaza"]

total_data = []
my_data = []

data = open("a.txt")

a = data.read().split("\n")

for i in a:
    try:
        total_data.append(i[i.find(":") + 1:].strip(" \n\r"))
    except:
        pass

for i in range(int(len(total_data)/16)):
    my_data.append({"id": i + 1, "Marka":total_data[0 + i * 16], "ModelAdi":total_data[1 + i * 16], "Modelno":total_data[2 + i * 16],
                    "İşletimSistemi":total_data[3 + i * 16], "İslemciTipi":total_data[4 + i * 16], "İslemciNesli":total_data[5 + i * 16],
                    "Ram":total_data[6 + i * 16], "DiskBoyutu":total_data[7 + i * 16], "DiskTürü":total_data[8 + i * 16], "EkranBoyutu":total_data[9 + i * 16],
                    "Puanı":total_data[10 + i * 16], "Fiyat":total_data[11 + i * 16].split(".")[0], "Siteİsmi":total_data[12 + i * 16],
                    "SiteLinki":total_data[13 + i * 16], "Title":total_data[14 + i * 16], "İmageLink": total_data[15 + i * 16]})
    x = mycol.insert_one(my_data[i])
