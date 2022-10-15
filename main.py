import find, bs4, lxml, pymongo, requests
from os import link
from bs4 import BeautifulSoup
import pandas as pd
import xlwt, random, openpyxl
from xlwt import Workbook

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["Deneme4"]

Trendyol = "https://www.trendyol.com/laptop-x-c103108?pi={0}"
vatan = "https://www.vatanbilgisayar.com/notebook/?page={0}"
V = "https://www.vatanbilgisayar.com"
teknosa = "https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page={0}"
tekno = "https://www.teknosa.com"
n11 = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg={0}"
evkur = "https://www.evkur.com.tr/dizustu-bilgisayarlar?ajax=true&pageNumber={0}"
evkur_site = "https://www.evkur.com.tr"

Ozellik_adi2 = []
Ozellik_aciklamasi2 = []
Link_two = []
full_points = []
OS = "null"
cpuType = "null"
cpuStatus = "null"
ram = "null"
Disk = "null"
DiskType = "null"
screen = "null"
success_data = 0
row = 1

Uniq_Computer_of_n11 = []
Uniq_Computer_of_evkur = []
Uniq_Computer_of_vatan = []
Uniq_Computer_of_teknosa = []
Uniq_Computer_of_trendyol = []

Global_Computer_Data = []

def get_soup(Url):
    return BeautifulSoup(requests.get(Url).text, 'html.parser')

def my_atoi(str):
    resultant = 0
    for i in range(len(str)):
        if (str[i] == ','):
          break
        elif ((str[i] >= '0' and str[i] <= '9')):
          resultant = resultant * 10 + (ord(str[i]) - ord('0'))
    return (resultant)

def _teknosa():
  for s_s in range(1,10):
    Link_one = get_soup(teknosa.format(s_s))
    x = Link_one.find_all("div",{"id":"product-item"})
    for s in x:
        Link_two.append(tekno + s.a['href'])
    for link_site in Link_two:
      computer = get_soup(link_site)
      Title = computer.find("div", {"class":"rch-brand"}).text.strip(" \n").split(" ")
      Marka = Title[0].strip(" \n")
      Model_adi = " ".join(Title[1:3]).strip(" \n")
      try:
        fiyat = computer.find("div", {"class":"prd-prc2"}).text.strip(" \n")
      except:
        fiyat = "Fiyat Bilgisi Yok"
      puan = '0'

      Page_urun = computer.find("div", {"class":"pdp-acc-body"}).find("div", {"class":"ptf-body"})
      Ozellikler1 = Page_urun.find_all("table")
      for ozellik in Ozellikler1:
          Ozellikler2 = ozellik.find_all("tr")
          Ozellik_adi = Ozellikler2[0].find_all("th")
          Ozellik_aciklamasi = Ozellikler2[1].find_all("td")
          for i in Ozellik_adi:
              Ozellik_adi2.append(i.text)
          for j in Ozellik_aciklamasi:
              Ozellik_aciklamasi2.append(j.text)

      for k in range(len(Ozellik_aciklamasi2)):
          if (Ozellik_adi2[k].find("Model Kodu") != -1):
            Model_no = Ozellik_aciklamasi2[k].strip(" \n").upper()
          elif (Ozellik_adi2[k].find("İşletim Sistemi") != -1):
            OS = Ozellik_aciklamasi2[k].strip(" \n")
          elif (Ozellik_adi2[k].find("İşlemci Nesli") != -1):
            cpuStatus = Ozellik_aciklamasi2[k].strip(" \n")
          elif (Ozellik_adi2[k].find("İşlemci") != -1):
            cpuType = Ozellik_aciklamasi2[k].strip(" \n")
          elif (Ozellik_adi2[k].find("Ram") != -1):
            ram = Ozellik_aciklamasi2[k].strip(" \n")
            if (ram.find("GB") == -1):
             ram += " GB"
          elif (Ozellik_adi2[k].find("SSD Kapasitesi") != -1):
            Disk = Ozellik_aciklamasi2[k].strip(" \n")
          elif (Ozellik_adi2[k].find("Disk Türü") != -1):
            DiskType = Ozellik_aciklamasi2[k].strip(" \n")
          elif (Ozellik_adi2[k].find("Ekran Boyutu") != -1):
            screen = Ozellik_aciklamasi2[k].strip(" \n")
      
      mydict = { "Marka": Marka, "Model Adı": Model_adi, "Model No": Model_no, "İşletim Sistemi": OS, "İşlemci Tipi": cpuType, "İslemci Nesli": cpuStatus, "Ram": ram,
                "Disk Boyutu": Disk, "Disk Türü": DiskType, "Ekran Boyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Site İsmi": "teknosa", "Site Linki": link_site }
      
      Uniq_Computer_of_teknosa.append(mydict)
    
    print("Sayfa verileri alındı ✏️")

def _vatan():
    for s_s in range(1, 15): 
      page = get_soup(vatan.format(s_s)).find_all("div", {"class":"product-list product-list--list-page"})
      for i in page:
          link_site = V + i.a['href']
          page2 = get_soup(V + i.a['href'])
          puan = str(page2.find("div", {"class":"rank-star"}))
          puan = puan[puan.find("width:") + 6:puan.find("%")]
          points = str(int(puan) / 20)
          Full_Title = page2.find("div", {"class":"product-list__content product-detail-big-price"})
          fiyat = Full_Title.find("div", {"class":"product-list__cost product-list__description"}).span.text.strip(" \n")
          Title = Full_Title.h1.text.strip(" \n").strip(" \n").split(" ")
          Marka = Title[0].strip(" \n")
          Model_adi = " ".join(Title[1:3]).strip(" \n")
          Ozellikler = page2.find_all("div", {"class":"product-feature"})
          key = []
          value = []
          for s in Ozellikler:
              ozellik_adlari = s.find_all("tr")
              for i in ozellik_adlari:
                  k1 = i.find_all("td")
                  key.append(k1[0].text.strip(" \n"))
                  value.append(k1[1].text.strip(" \n"))
          for i in range(len(key)):
              if (key[i].find("İşlemci Teknolojisi") != -1):
                  cpuType = value[i].strip(" \n")
              elif (key[i].find("İşlemci Nesli") != -1):
                  cpuStatus = value[i].strip(" \n")
              elif (key[i].find("Ram (Sistem Belleği)") != -1):
                  if (value[i].find("(") != -1):
                      r = value[i].find("(")
                      ram = value[i][:r].strip(" \n")
                  else:
                      ram = value[i].strip(" \n")
              elif (key[i].find("Ekran Boyutu") != -1):
                  screen = value[i].strip(" \n")
              elif (key[i].find("Disk Kapasitesi") != -1):
                  Disk = value[i][:5].strip(" \n")
              elif (key[i].find("Disk Türü") != -1):
                  k = 0
                  if (value[i].find("NVMe") != -1):
                      k = 4
                  DiskType = value[i][k:].strip(" \n")
              elif (key[i].find("İşlemci Numarası") != -1):
                  cpuStatus = value[i].strip(" \n")
              elif (key[i].find("İşletim Sistemi") != -1):
                  OS = value[i].strip(" \n")
              elif (key[i].find("Üretici Part Numarası") != -1):
                  Model_no = value[i].strip(" \n").upper()
                  
          mydict = { "Marka": Marka, "Model Adı": Model_adi, "Model No": Model_no, "İşletim Sistemi": OS, "İşlemci Tipi": cpuType, "İslemci Nesli": cpuStatus,
                    "Ram": ram, "Disk Boyutu": Disk, "Disk Türü": DiskType, "Ekran Boyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Site İsmi": "vatan", "Site Linki": link_site }
          
          Uniq_Computer_of_vatan.append(mydict)
      print("Sayfa verileri alındı ✏️")

def _n11():
  for s_s in range(1,15):
    Link_one = get_soup(n11.format(s_s)).find_all("div", {"class":"pro"})
    for i in Link_one:
      link_site = i.a['href']
      Page_urun = get_soup(i.a['href'])
      ozellikler = Page_urun.find_all("li", {"class":"unf-prop-list-item"})
      fiyat = Page_urun.find("div", {"class":"unf-p-summary-price"}).text.strip(" \n")
      puan = Page_urun.find("div", {"class":"proRatingHolder"}).find("div", {"class":"ratingCont"}).strong.text.strip(" \n")
      Title = Page_urun.find("div", {"class":"nameHolder"}).find("h1").text.strip(" \n").split(" ")
      Marka = Title[0].strip(" \n")
      Model_adi = Title[3].strip(" \n")
      for i in ozellikler:
          str = i.text.strip(" \n")
          if (i.find("p", {"class":"unf-prop-list-title"}).text.find("Model") != -1 and len(i.find("p", {"class":"unf-prop-list-title"}).text) <= 6):
            ss = i.text[6:].strip(" \n").split(" ")
            if (len(ss) > 1):
              Model_adi = " ".join(ss[:len(ss) - 1]).strip(" \n")
            Model_no = (ss[len(ss) - 1]).strip(" \n").upper()
          elif (str.find("İşletim Sistemi") != -1):
            OS = str[17:].strip(" \n")
          elif (str.find("İşlemci Modeli") != -1):
            cpuStatus = str[16:].strip(" \n")
          elif (str.find("İşlemci") != -1):
            cpuType = str[9:].strip(" \n")
          elif (str.find("Bellek Kapasitesi") != -1 and len(str) < 27):
            ram = str[19:].strip(" \n")
          elif (str.find("Disk Kapasitesi") != -1):
            Disk = str[17:].strip(" \n")
          elif (str.find("Disk Türü") != -1):
            DiskType = str[11:].strip(" \n")
          elif (str.find("Ekran Boyutu") != -1):
            screen = str[14:].strip(" \n")
            
      mydict = { "Marka": Marka, "Model Adı": Model_adi, "Model No": Model_no, "İşletim Sistemi": OS, "İşlemci Tipi": cpuType, "İslemci Nesli": cpuStatus,
                    "Ram": ram, "Disk Boyutu": Disk, "Disk Türü": DiskType, "Ekran Boyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Site İsmi": "n11", "Site Linki": link_site }  
      Uniq_Computer_of_n11.append(mydict)
    print("Sayfa verileri alındı ✏️")


def _trendyol():
  row = 1
  for s_s in range(1,20):
    Link_one = get_soup(Trendyol.format(s_s))
    computers = Link_one.find_all("div", {"class":"p-card-wrppr with-campaign-view"})
    Links_points = Link_one.find_all("div", {"class":"product-down"})
    for s in Links_points:
      try:
        rrr = s.find("div", {"class":"ratings"})
        pp = rrr.find_all("div", {"class":"star-w"})
        points = 0
        for p in pp:
          points += my_atoi(str(p)[str(p).find("style") + 13:])
        full_points.append(points)
      except:
        full_points.append(0)
    for i in computers:
      row += 1
      link_site = "https://www.trendyol.com" + i.a['href']
      Page_urun = get_soup("https://www.trendyol.com" + i.a['href'])
      try:
        Marka = Page_urun.find("div", {"class":"pr-in-cn"}).h1.a.text.strip(" \n")
      except:
        Marka = Page_urun.find("div", {"class":"pr-in-cn"}).h1.text.strip(" \n").split(" ")[0]
      Model = []
      Model = Page_urun.find("h1", {"class":"pr-new-br"}).span.text.strip(" \n").split(" ")
      Model_adi = (Model[1] + " " + Model[2]).strip(" \n")
      fiyat = Page_urun.find("span", {"class":"prc-dsc"}).text.strip(" \n")
      ozellikler = Page_urun.find("ul", {"class":"detail-attr-container"}).find_all("li")
      flag = 1

      for i in ozellikler:
        str = i.text.strip(" \n")
        if (str.find("İşletim Sistemi") != -1):
          OS = str[16:].strip(" \n")
        elif (str.find("İşlemci Tipi") != -1):
          cpuType = str[13:].strip(" \n")
        elif (str.find("İşlemci Nesli") != -1):
          cpuStatus = str[14:].strip(" \n")
        elif (str.find("Ram (Sistem Belleği)") != -1 and len(str) < 27):
          ram = str[20:].strip(" \n")
        elif (str.find("SSD") != -1):
          Disk = str[14:].strip(" \n")
          DiskType = "SSD"
          flag = 0
        elif (str.find("HDD") != -1 and flag == 1):
          Disk = str[20:].strip(" \n")
          DiskType = "HDD"
        elif (str.find("Ekran Boyutu") != -1):
          screen = str[13:].strip(" \n")

      Model_no = " ".join(Model).strip(" \n").upper()

      mydict = { "Marka": Marka, "Model Adı": Model_adi, "Model No": Model_no, "İşletim Sistemi": OS, "İşlemci Tipi": cpuType, "İslemci Nesli": cpuStatus,
                "Ram": ram, "Disk Boyutu": Disk, "Disk Türü": DiskType, "Ekran Boyutu": screen, "Puanı": full_points[row%23] / 100, "Fiyat": fiyat, "Site İsmi": "Trendyol", "Site Linki": link_site }
      
      Uniq_Computer_of_trendyol.append(mydict)
    print("Sayfa verileri alındı ✏️")


def _evkur():
    index_data = 0
    for s_s in range(1, 3):
      main_page = get_soup(evkur.format(s_s)).find("div", {"class":"products"}).find_all("div", {"class":"product-mobile-wrapper"})
      for s in main_page:
        link_site = evkur_site + s.a['href']
        computer = get_soup(link_site)
        ozellikler = computer.find("table", {"class":"product-detail-specifications"}).find_all("tr")
        puan = computer.find("div", {"class":"stars"})['data-rating']
        fiyat_baslik = computer.find("h2", {"class":"price-option"}).text.strip(" \n\r")
        fiyat = ""
        r = 1
        for i in range(len(fiyat_baslik)):
              if (fiyat_baslik[i] >= '0' and fiyat_baslik[i] <= '9'):
                    fiyat += fiyat_baslik[i]
              elif (fiyat_baslik[i] == ',' and r == 1):
                    fiyat += '.'
                    r = 0
              elif (fiyat_baslik[i] == ',' and r == 0):
                    fiyat += ','
        for i in ozellikler:
          key_value = i.find_all("td")
          key = key_value[0].text.strip(" \n\r")
          value = key_value[1].text.strip(" \n\r")
          
          if (key.find("Marka") != -1):
                Marka = value.strip(" \n\r")
          elif (key.find("Model") != -1):
                Model_no = value.strip(" \n\r")
          elif (key.find("Ürün Çeşidi") != -1):
                Model_adi = value.strip(" \n\r")
          elif (key.find("İşletim Sistemi") != -1):
                OS = value.strip(" \n\r")
          elif (key.find("İşlemci Tipi") != -1):
                cpuType = value.strip(" \n\r")
          elif (key.find("İşlemci Numarası") != -1):
                cpuStatus = value.strip(" \n\r")
          elif (key.find("Bellek (RAM)") != -1):
               ram = value.strip(" \n\r")
          elif (key.find("Depolama") != -1):
               Full_disk = value.split("-")
               Disk = Full_disk[0].strip(" \n\r")
               DiskType = Full_disk[1].strip(" \n\r")
          elif (key.find("Ekran Boyutu") != -1):
                screen = value.strip(" \n\r")
          
        mydict = { "Marka": Marka, "Model Adı": Model_adi, "Model No": Model_no, "İşletim Sistemi": OS, "İşlemci Tipi": cpuType, "İslemci Nesli": cpuStatus,
            "Ram": ram, "Disk Boyutu": Disk, "Disk Türü": DiskType, "Ekran Boyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Site İsmi": "evkur", "Site Linki": link_site }
        
        Uniq_Computer_of_evkur.append(mydict)
      print("Sayfa verileri alındı ✏️")

def Trendyol_Model_No_Find():
    index = 0
    for i in Uniq_Computer_of_trendyol:
        Model_no_trendyol = i.get("Model No")
        ctrl = 1
        if (ctrl == 1):
            for j in Uniq_Computer_of_evkur:
                if (Model_no_trendyol.find(j.get("Model No")) != -1):
                    Uniq_Computer_of_trendyol[index].update({"Model No": j.get("Model No")})
                    print("Trendyol Model Numarası evkur ile değiştirildi ✨")
                    ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_vatan:
                if (Model_no_trendyol.find(j.get("Model No")) != -1):
                    Uniq_Computer_of_trendyol[index].update({"Model No": j.get("Model No")})
                    print("Trendyol Model Numarası vatan ile değiştirildi ✨")
                    ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_teknosa:
                if (Model_no_trendyol.find(j.get("Model No")) != -1):
                    Uniq_Computer_of_trendyol[index].update({"Model No": j.get("Model No")})
                    print("Trendyol Model Numarası teknosa ile değiştirildi ✨")
                    ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_n11:
                if (Model_no_trendyol.find(j.get("Model No")) != -1):
                    Uniq_Computer_of_trendyol[index].update({"Model No": j.get("Model No")})
                    print("Trendyol Model Numarası n11 ile değiştirildi ✨")
                    ctrl = 0
        index += 1

def data_in_list(liste, data):
    for i in liste:
        if (i.get("Model No") == data.get("Model No")):
            print("Duplicate ürün silindi!")
            return (1)
    return (0)

def Uniq_computer_Converter(Computer_data):
    New_uniq_computer_data = []
    index = 0
    flag = 1
    print("Duplicate kontrolü yapılıyor...")
    for i in Computer_data:
        flag = 1
        for j in Computer_data[index:]:
            if (flag == 1 and i.get("Model No") == j.get("Model No")):
                if (data_in_list(New_uniq_computer_data, i) == 0):
                    New_uniq_computer_data.append(j)
                    flag = 0
        index += 1
    print("Duplicate kontrolü bitti.")
    return New_uniq_computer_data

def Global_data_create():
      for i in Uniq_Computer_of_evkur:
          Global_Computer_Data.append(i)
      for i in Uniq_Computer_of_n11:
          Global_Computer_Data.append(i)
      for i in Uniq_Computer_of_vatan:
          Global_Computer_Data.append(i)
      for i in Uniq_Computer_of_teknosa:
          Global_Computer_Data.append(i)
      for i in Uniq_Computer_of_trendyol:
          Global_Computer_Data.append(i)

def Global_data_to_MongoDB():
    for i in Global_Computer_Data:
        x = mycol.insert_one(i)

def view_success_data():
  for i in Global_Computer_Data:
      Model_no_i = i.get("Model No")
      for j in Global_Computer_Data:
          if (Model_no_i == j.get("Model No")):
              print("Eşleşen sonuç var 🔥")
              success_data += 1

print("📌 Evkur verileri alınıyor...")
_evkur()
print("Evkur verileri alındı ☑️")
# Uniq_Computer_of_evkur = Uniq_computer_Converter(Uniq_Computer_of_evkur)

print("📌 N11 verileri alınıyor...")
_n11()
print("N11 verileri alındı ☑️")
# Uniq_Computer_of_n11 = Uniq_computer_Converter(Uniq_Computer_of_n11)

print("📌 Teknosa verileri alınıyor...")
_teknosa()
print("Teknosa verileri alındı ☑️")
# Uniq_Computer_of_teknosa = Uniq_computer_Converter(Uniq_Computer_of_teknosa)

print("📌 Trendyol verileri alınıyor...")
_trendyol()
print("Trendyol verileri alındı ☑️")

print("📌 Vatan Bilgisayar verileri alınıyor...")
_vatan()
print("Vatan Bilgisayar verileri alındı ☑️")
# Uniq_Computer_of_vatan = Uniq_computer_Converter(Uniq_Computer_of_vatan)


print("Trendyol verileri için Model Numarası aranıyor 🔍")
Trendyol_Model_No_Find()
Uniq_Computer_of_trendyol = Uniq_computer_Converter(Uniq_Computer_of_trendyol)

print("Veriseti oluşturuluyor 🔧")
Global_data_create()

print("Veriler MongoDB'ye aktarılıyor 📝")
Global_data_to_MongoDB()

print("Veriler başarılı bir şekilde veritabanına aktarıldı ✅")

view_success_data()
print("- Eşleşen veri miktarı -")
print(success_data)


''' def Uniq_Computer_Converter(Uniq_Computers, dict):
      idx = 0
      for i in Uniq_Computers:
        Model_Nolar = i.get("Model No")
        if (Model_Nolar == dict.get("Model No") and my_atoi(i.get("Fiyat")) > my_atoi(dict.get("Fiyat"))):
              print("Duplicate önlendi ve veriler değiştirildi.")
              print("Eski: " + Model_Nolar + " | Yeni: " + dict.get("Model No"))
              print(str(my_atoi(i.get("Fiyat"))) + " " + str(my_atoi(dict.get("Fiyat"))))
              Uniq_Computers.pop(idx)
              Uniq_Computers.insert(idx, dict)
              return (0)
        idx += 1
      Uniq_Computers.append(dict) '''