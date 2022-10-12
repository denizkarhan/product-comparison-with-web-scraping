from gettext import find
import requests
from bs4 import BeautifulSoup
import pandas as pd
import xlwt
import openpyxl
from xlwt import Workbook

my_wb = openpyxl.Workbook()
my_sheet = my_wb.active

col = ["Marka", "Model Adı", "Model No", "İşletim Sistemi", "İşlemci Tipi", "İslemci Nesli", "Ram", "Disk Boyutu", "Disk Türü", "Ekran Boyutu", "Puanı", "Fiyat", "Site İsmi", "Site Linki"]
hepsiburada = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa={0}"
OS = " "
cpuType = " "
cpuStatus = " "
ram = " "
Disk = " "
DiskType = " "
screen = " "
row = 1

for i in range(14):
    c1 = my_sheet.cell(row = 1, column = i + 1)
    c1.value = col[i]

def get_soup(Url):
    return BeautifulSoup(requests.get(Url).text, 'lxml')

for s_s in range(1,2):
  Link_one = get_soup(hepsiburada.format(s_s))
  Link_one = Link_one.find("div", {"class" : "wrapper"})
  print(Link_one)
  exit(0)
  for i in Link_two:
    print(i)
    exit(0)
    row += 1
    Marka = i.find("ul", {"class":"productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm"})
    print(Marka)
    exit(0)   
    Model = []
    Model = Page_urun.find("h1", {"class":"pr-new-br"}).span.text.split(" ")
    Model_adi = Model[1] + " " + Model[2]
    
    fiyat = Page_urun.find("span", {"class":"prc-dsc"}).text

    ozellikler = Page_urun.find("ul", {"class":"detail-attr-container"}).find_all("li")

my_wb.save("hepsiburada.xlsx")
