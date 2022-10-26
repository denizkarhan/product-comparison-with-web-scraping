import find, bs4, lxml, pymongo, requests, urllib.request, shutil, threading, xlwt, random, openpyxl
from os import link
from bs4 import BeautifulSoup
import pandas as pd
from xlwt import Workbook

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["magaza_magaza"]

data = open("a.txt")

a = data.read().split("\n")

total_data = []
my_data = []

for i in a:
    total_data.append(i)

for i in range(len(total_data)):
    try:
        my_data.append({"id": i + 1, "Marka":total_data[0 + i * 15].split(":")[1].strip(" "), "ModelAdi":total_data[1 + i * 15].split(":")[1].strip(" "), "Modelno":total_data[2 + i * 15].split(":")[1].strip(" "),
                    "İşletimSistemi":total_data[3 + i * 15].split(":")[1].strip(" "), "İslemciTipi":total_data[4 + i * 15].split(":")[1].strip(" "), "İslemciNesli":total_data[5 + i * 15].split(":")[1].strip(" "),
                    "Ram":total_data[6 + i * 15].split(":")[1].strip(" "), "DiskBoyutu":total_data[7 + i * 15].split(":")[1].strip(" "), "DiskTürü":total_data[8 + i * 15].split(":")[1].strip(" "), "EkranBoyutu":total_data[9 + i * 15].split(":")[1].strip(" "),
                    "Puanı":total_data[10 + i * 15].split(":")[1].strip(" "), "Fiyat":total_data[11 + i * 15].split(":")[1].strip(" ").split(".")[0], "Siteİsmi":total_data[12 + i * 15].split(":")[1].strip(" "), "SiteLinki":total_data[13 + i * 15].split(":")[1].strip(" "), "Title":total_data[14 + i * 15].split(":")[1]})
        x = mycol.insert_one(my_data[i])
        print(my_data[i])
    except:
        pass
    i += 15

