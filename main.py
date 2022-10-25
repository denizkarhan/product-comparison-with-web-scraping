import find, bs4, lxml, pymongo, requests, urllib.request, shutil, threading, xlwt, random, openpyxl
from os import link
from bs4 import BeautifulSoup
import pandas as pd
from xlwt import Workbook

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["deneme"]

Trendyol = "https://www.trendyol.com/laptop-x-c103108?pi={0}"
T = "https://www.trendyol.com"
vatan = "https://www.vatanbilgisayar.com/notebook/?page={0}"
V = "https://www.vatanbilgisayar.com"
teknosa = "https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page={0}"
tekno = "https://www.teknosa.com"
n11 = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg={0}"
evkur = "https://www.evkur.com.tr/dizustu-bilgisayarlar?ajax=true&pageNumber={0}"
evkur_site = "https://www.evkur.com.tr"
ciceksepeti = "https://www.ciceksepeti.com/dizustu-bilgisayar-laptop?qt=diz%C3%BCst%C3%BC%20bilgisayar%20(laptop)&qcat=kategori-diz%C3%BCst%C3%BC%20bilgisayar%20(laptop)&suggest=1%7Claptop&page={0}"
C = "https://www.ciceksepeti.com"

OS = "null"
cpuType = "null"
cpuStatus = "null"
ram = "null"
Disk = "null"
DiskType = "null"
screen = "null"
row = 1
computer_count = 0

Ozellik_adi2 = []
Ozellik_aciklamasi2 = []
Link_two = []
full_points = []
Uniq_Computer_of_n11 = []
Uniq_Computer_of_evkur = []
Uniq_Computer_of_vatan = []
Uniq_Computer_of_teknosa = []
Uniq_Computer_of_trendyol = []
Uniq_Computer_of_ciceksepeti = []
Global_Computer_Data = []
End_computer_data = []
image_computer_links = []

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
  computer_count = 0
  for s_s in range(1, 3):
    Link_one = get_soup(teknosa.format(s_s))
    x = Link_one.find_all("div",{"id":"product-item"})
    for s in x:
        Link_two.append(tekno + s.a['href'])
    for link_site in Link_two:
      computer = get_soup(link_site)
      _aciklama = computer.find("div", {"class":"pdp-base"}).h1.text.strip(" \n\r")
      try:
        Title = computer.find("div", {"class":"rch-brand"}).text.strip(" \n").split(" ")
      except:
        Title = "null null".split(" ")
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
      mydict = { "Marka": Marka, "ModelAdi": Model_adi, "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus, "Ram": ram,
                "DiskBoyutu": Disk, "DiskTürü": DiskType, "EkranBoyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Siteİsmi": "teknosa", "SiteLinki": link_site, "Title": _aciklama }
      Uniq_Computer_of_teknosa.append(mydict)
      computer_count += 1
      print(str(computer_count) + ". Teknosa")
    print(str(s_s) + ". Sayfa verileri alındı (Teknosa) ✏️")

def _vatan():
    computer_count = 0
    for s_s in range(1, 6): 
      page = get_soup(vatan.format(s_s)).find_all("div", {"class":"product-list product-list--list-page"})
      for i in page:
          link_site = V + i.a['href']
          page2 = get_soup(V + i.a['href'])
          _aciklama = page2.find("div", {"class":"product-list__content product-detail-big-price"}).h1.text.strip(" \n\r")
          try:
            puan = str(page2.find("div", {"class":"rank-star"}))
            puan = puan[puan.find("width:") + 6:puan.find("%")].strip(" \n\r")
            puan = str(int(puan) / 20)
          except:
            puan = "0.0"
          Full_Title = page2.find("div", {"class":"product-list__content product-detail-big-price"})
          fiyat = Full_Title.find("div", {"class":"product-list__cost product-list__description"}).span.text.strip(" \n")
          try:
            Title = Full_Title.h1.text.strip(" \n").strip(" \n").split(" ")
          except:
            Title = "null null".split(" ")
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
                  Disk = ""
                  for j in range(len(value[i])):
                        Disk += value[i][j]
                        if (value[i][j] == 'B'):
                            break
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
          mydict = { "Marka": Marka, "ModelAdi": Model_adi, "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus,
                    "Ram": ram, "DiskBoyutu": Disk, "DiskTürü": DiskType, "EkranBoyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Siteİsmi": "vatan", "SiteLinki": link_site, "Title": _aciklama }
          Uniq_Computer_of_vatan.append(mydict)
          computer_count += 1
          print(str(computer_count) + ". Vatan")
      print(str(s_s) + ". Sayfa verileri alındı (Vatan) ✏️")

def _n11():
  computer_count = 0
  for s_s in range(1, 6):
    Link_one = get_soup(n11.format(s_s)).find_all("div", {"class":"pro"})
    for i in Link_one:
      link_site = i.a['href']
      Page_urun = get_soup(link_site)
      ozellikler = Page_urun.find_all("li", {"class":"unf-prop-list-item"})
      try:
        fiyat = Page_urun.find("div", {"class":"unf-p-summary-price"}).text.strip(" \n")
        puan = Page_urun.find("div", {"class":"proRatingHolder"}).find("div", {"class":"ratingCont"}).strong.text.strip(" \n")
        Title = Page_urun.find("div", {"class":"nameHolder"}).find("h1").text.strip(" \n").split(" ")
      except:
        fiyat = "Belirtilmemiş"
        puan = "0.0"
        Title = "null null null null null"
      Marka = Title[0].strip(" \n")
      Model_adi = Title[3].strip(" \n")
      _aciklama = " ".join(Title)
      for i in ozellikler:
          key = i.text.strip(" \n")
          if (i.find("p", {"class":"unf-prop-list-title"}).text.find("Model") != -1 and len(i.find("p", {"class":"unf-prop-list-title"}).text) <= 6):
            ss = i.text[6:].strip(" \n").split(" ")
            if (len(ss) > 1):
              Model_adi = " ".join(ss[:len(ss) - 1]).strip(" \n")
            Model_no = i.text[6:].strip(" \n").upper()
          elif (key.find("İşletim Sistemi") != -1):
            OS = key[17:].strip(" \n")
          elif (key.find("İşlemci Modeli") != -1):
            cpuStatus = key[16:].strip(" \n")
          elif (key.find("İşlemci") != -1):
            cpuType = key[9:].strip(" \n")
          elif (key.find("Bellek Kapasitesi") != -1 and len(key) < 27):
            ram = key[19:].strip(" \n")
          elif (key.find("Disk Kapasitesi") != -1):
            Disk = key[17:].strip(" \n")
          elif (key.find("Disk Türü") != -1):
            DiskType = key[11:].strip(" \n")
          elif (key.find("Ekran Boyutu") != -1):
            screen = key[14:].strip(" \n")  
      mydict = { "Marka": Marka, "ModelAdi": Model_adi, "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus,
                    "Ram": ram, "DiskBoyutu": Disk, "DiskTürü": DiskType, "EkranBoyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Siteİsmi": "n11", "SiteLinki": link_site, "Title": _aciklama }  
      Uniq_Computer_of_n11.append(mydict)
      computer_count += 1
      print(str(computer_count) + ". N11")
    print(str(s_s) + ". Sayfa verileri alındı (N11) ✏️")

def _trendyol():
  computer_count = 0
  row = 1
  for s_s in range(1, 6):
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
        points = (points - (points % 10000)) / 100000
        full_points.append(points)
      except:
        full_points.append(0)
    for i in computers:
      row += 1
      link_site = T + i.a['href']
      Page_urun = get_soup(link_site)
      _aciklama = Page_urun.find("div", {"class":"pr-in-cn"}).span.text.strip(" \n\r")
      try:
        Marka = Page_urun.find("div", {"class":"pr-in-cn"}).h1.a.text.strip(" \n")
      except:
        Marka = Page_urun.find("div", {"class":"pr-in-cn"}).h1.text.strip(" \n").split(" ")[0]
      Model = []
      Model = Page_urun.find("h1", {"class":"pr-new-br"}).span.text.strip(" \n").split(" ")
      Model_adi = (Model[1] + " " + Model[2]).strip(" \n")
      fiyat = Page_urun.find("span", {"class":"prc-dsc"}).text.strip(" \n")
      try:
          ozellikler = Page_urun.find("ul", {"class":"detail-attr-container"}).find_all("li")
      except:
          ozellikler = ["NULL", "NULL","NULL","NULL"]
      flag = 1
      for i in ozellikler:
        try:
          key = i.text.strip(" \n")
        except:
          key = "NULL"
        if (key.find("İşletim Sistemi") != -1):
          OS = key[16:].strip(" \n")
        elif (key.find("İşlemci Tipi") != -1):
          cpuType = key[13:].strip(" \n")
        elif (key.find("İşlemci Nesli") != -1):
          cpuStatus = key[14:].strip(" \n")
        elif (key.find("Ram (Sistem Belleği)") != -1 and len(key) < 27):
          ram = key[20:].strip(" \n")
        elif (key.find("SSD") != -1):
          Disk = key[14:].strip(" \n")
          DiskType = "SSD"
          flag = 0
        elif (key.find("HDD") != -1 and flag == 1):
          Disk = key[20:].strip(" \n")
          DiskType = "HDD"
        elif (key.find("Ekran Boyutu") != -1):
          screen = key[13:].strip(" \n")
      Model_no = " ".join(Model).strip(" \n").upper()
      mydict = { "Marka": Marka, "ModelAdi": Model_adi, "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus,
                "Ram": ram, "DiskBoyutu": Disk, "DiskTürü": DiskType, "EkranBoyutu": screen, "Puanı": str(full_points[row%23]), "Fiyat": fiyat, "Siteİsmi": "Trendyol", "SiteLinki": link_site, "Title": _aciklama }
      Uniq_Computer_of_trendyol.append(mydict)
      computer_count += 1
      print(str(computer_count) + ". Trendyol")
    print(str(s_s) + ". Sayfa verileri alındı (Trendyol) ✏️")

def _evkur():
    computer_count = 0
    index_data = 0
    OS = "null"
    cpuType = "null"
    cpuStatus = "null"
    ram = "null"
    Disk = "null"
    DiskType = "null"
    screen = "null"
    for s_s in range(1, 3):
      main_page = get_soup(evkur.format(s_s)).find("div", {"class":"products"}).find_all("div", {"class":"product-mobile-wrapper"})
      for s in main_page:
        link_site = evkur_site + s.a['href']
        computer = get_soup(link_site)
        _aciklama = computer.find("div", {"class":"product-info"}).h1.span.text.strip(" \n\r")
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
        mydict = { "Marka": Marka, "ModelAdi": Model_adi, "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus,
            "Ram": ram, "DiskBoyutu": Disk, "DiskTürü": DiskType, "EkranBoyutu": screen, "Puanı": puan, "Fiyat": fiyat, "Siteİsmi": "evkur", "SiteLinki": link_site, "Title": _aciklama }
        Uniq_Computer_of_evkur.append(mydict)
        computer_count += 1
        print(str(computer_count) + ". Evkur")
      print(str(s_s) + ". Sayfa verileri alındı (Evkur) ✏️")

def _ciceksepeti():
    computer_count = 0
    OS = "null"
    cpuType = "null"
    cpuStatus = "null"
    ram = "null"
    Disk = "null"
    DiskType = "null"
    screen = "null"
    for s_s in range(1, 6):
        page = get_soup(ciceksepeti.format(s_s)).find("div", {"class":"products products--category js-ajax-category-products"})
        pages = page.find_all("div",{"class":"products__item js-category-item-hover js-product-item-for-countdown js-product-item"})
        for x in pages[:30]:
            link_site = C + x.a['href']
            products = get_soup(link_site)
            _aciklama = products.find("div", {"class":"product__info-wrapper--left"}).text.strip(" \n\r")
            try:
              Title = products.find("div", {"class":"product__info-wrapper--left"}).text.strip(" \n\r").split(" ")
            except:
              Title = "null null".split(" ")
            Marka = Title[0]
            Model_no = " ".join(Title).strip(" \n\r")
            try:
                fiyat = products.find("div", {"class":"product__info__new-price__integer js-price-integer"}).text
            except:
                fiyat = "Belirtilmemiş"
            ozellikler = products.find_all("div", {"class":"product__specifications__table-row"})
            for i in ozellikler:
                key = i.find_all("div", {"class":"product__specifications__table-cell"})[0].text.strip(" \n\r")
                value = i.find_all("div", {"class":"product__specifications__table-cell"})[1].text.strip(" \n\r")
                if (key == "SSD Kapasitesi" or key == "Kapasite"):
                    Disk = value
                elif (key == "İşletim Sistemi"):
                    OS = value
                elif (key == "İşlemci Tipi"):
                    cpuType = value
                elif (key == "İşlemci Nesli"):
                    cpuStatus = value
                elif (key == "Ram (Sistem Belleği)"):
                    ram = value
                elif (key == "Ekran Boyutu"):
                    screen = value
            mydict = { "Marka": Marka, "ModelAdi": "Belirtilmemiş", "Modelno": Model_no, "İşletimSistemi": OS, "İslemciTipi": cpuType, "İslemciNesli": cpuStatus,
            "Ram": ram, "DiskBoyutu": Disk, "DiskTürü": "SSD", "EkranBoyutu": screen, "Puanı": "0.0", "Fiyat": fiyat, "Siteİsmi": "ciceksepeti", "SiteLinki": link_site, "Title": _aciklama }
            Uniq_Computer_of_ciceksepeti.append(mydict)
            computer_count += 1
            print(str(computer_count) + ". Ciceksepeti")
        print(str(s_s) + ". Sayfa verileri alındı (Ciceksepeti) ✏️")

#------------------SEARCH MODEL NUMBER ON SITES-------------------
def Site_Model_No_Find(Uniq_Computer):
    index = 0
    for i in Uniq_Computer:
        Model_No = i.get("Modelno")
        ctrl = 1
        if (ctrl == 1):
            for j in Uniq_Computer_of_vatan:
              if (Model_No.find(j.get("Modelno")) != -1):
                  Uniq_Computer[index].update({"Modelno": j.get("Modelno")})
                  Uniq_Computer[index].update({"ModelAdi": j.get("ModelAdi")})
                  print(i.get("Siteİsmi") + " Model Numarası vatan ile değiştirildi ✨")
                  ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_evkur:
                if (Model_No.find(j.get("Modelno")) != -1):
                    Uniq_Computer[index].update({"Modelno": j.get("Modelno")})
                    Uniq_Computer[index].update({"ModelAdi": j.get("ModelAdi")})
                    print(i.get("Siteİsmi") + " Model Numarası evkur ile değiştirildi ✨")
                    ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_teknosa:
                if (Model_No.find(j.get("Modelno")) != -1):
                    Uniq_Computer[index].update({"Modelno": j.get("Modelno")})
                    Uniq_Computer[index].update({"ModelAdi": j.get("ModelAdi")})
                    print(i.get("Siteİsmi") + " Model Numarası teknosa ile değiştirildi ✨")
                    ctrl = 0
        if (ctrl == 1):
            for j in Uniq_Computer_of_n11:
                if (Model_No.find(j.get("Modelno")) != -1):
                    Uniq_Computer[index].update({"Modelno": j.get("Modelno")})
                    Uniq_Computer[index].update({"ModelAdi": j.get("ModelAdi")})
                    print(i.get("Siteİsmi") + " Model Numarası n11 ile değiştirildi ✨")
                    ctrl = 0
        if (i.get("Siteİsmi") == "n11"):
            str_count = len(i.get("Modelno").split(" "))
            if (str_count > 1):
                Uniq_Computer[index].update({"Modelno": "NULL"})
        index += 1
    return Uniq_Computer

#------------------BLOCK SAME DATA-------------------
def data_in_list(liste, data):
    for i in liste:
        if (i.get("Modelno") == data.get("Modelno")):
            print("Duplicate ürün silindi!")
            return (1)
    return (0)

#------------------BLOCK SAME DATA-------------------
def Uniq_computer_Converter(Computer_data):
    New_uniq_computer_data = []
    index = 0
    flag = 1
    print("Duplicate kontrolü yapılıyor 🔧🔧")
    for i in Computer_data:
        flag = 1
        for j in Computer_data[index:]:
            if (flag == 1 and i.get("Modelno") == j.get("Modelno")):
                if (data_in_list(New_uniq_computer_data, i) == 0):
                    New_uniq_computer_data.append(j)
                    flag = 0
        index += 1
    print("Duplicate kontrolü bitti.")
    return New_uniq_computer_data

#------------------COLLECT SITE DATA-------------------
def Global_data_create():
      Global_Computer_Data = Uniq_Computer_of_ciceksepeti + Uniq_Computer_of_evkur + Uniq_Computer_of_n11 + Uniq_Computer_of_vatan + Uniq_Computer_of_teknosa + Uniq_Computer_of_trendyol
      return Global_Computer_Data

def Price_list_update(a):
    for i in range(1, 6):
      for j in range(i, 6):
        if (a.get("Fiyat" + str(i)) != "NULL" and a.get("Fiyat" + str(j)) != "NULL"):
          if (int(a.get("Fiyat" + str(i))) > int(a.get("Fiyat" + str(j)))):
              Puanı = a.get("Puanı" + str(j))
              Fiyat = a.get("Fiyat" + str(j))
              Siteİsmi = a.get("Siteİsmi" + str(j))
              SiteLinki = a.get("SiteLinki" + str(j))
              Title = a.get("Title" + str(j))
              
              a.update({"Puanı" + str(j): a.get("Puanı" + str(i))})
              a.update({"Fiyat" + str(j): a.get("Fiyat" + str(i))})
              a.update({"Siteİsmi" + str(j): a.get("Siteİsmi" + str(i))})
              a.update({"SiteLinki" + str(j): a.get("SiteLinki" + str(i))})
              a.update({"Title" + str(j): a.get("Title" + str(i))})
              
              a.update({"Puanı" + str(i): Puanı})
              a.update({"Fiyat" + str(i): Fiyat})
              a.update({"Siteİsmi" + str(i): Siteİsmi})
              a.update({"SiteLinki" + str(i): SiteLinki})
              a.update({"Title" + str(i): Title})
    return (a)

#------------------SEND MATCHİNG DATA TO MONGODB-------------------
def Global_success_data_to_MongoDB():
    mongo_id = 0
    duplicate_control = []
    for i in Global_Computer_Data:
        k = 0
        a = {}
        for j in Global_Computer_Data:
            if (i.get("Modelno") == j.get("Modelno")):
                k += 1
                if (k == 1):
                    a.update(j)
                    a.pop("Puanı")
                    a.pop("Fiyat")
                    a.pop("Siteİsmi")
                    a.pop("SiteLinki")
                    a.pop("Title")
                a.update({"Puanı" + str(k):j.get("Puanı")})
                a.update({"Fiyat" + str(k):str(my_atoi(j.get("Fiyat")))})
                a.update({"Siteİsmi" + str(k):j.get("Siteİsmi")})
                a.update({"SiteLinki" + str(k):j.get("SiteLinki")})
                a.update({"Title" + str(k):j.get("Title")})
        for j in range(k + 1, 6):
            a.update({"Puanı" + str(j):"NULL"})
            a.update({"Fiyat" + str(j):"NULL"})
            a.update({"Siteİsmi" + str(j):"NULL"})
            a.update({"SiteLinki" + str(j):"NULL"})
            a.update({"Title" + str(j):"NULL"})
        if (k >= 2):
            if a.get("Modelno") not in duplicate_control:
              duplicate_control.append(a.get("Modelno"))
              mongo_id += 1
              id_added = {"id": mongo_id}
              a = Price_list_update(a)
              id_added.update(a)
              id_added.update({"İmageLink":get_image_link(id_added)})
              x = mycol.insert_one(id_added)
              End_computer_data.append(id_added)
              print(k * "🔥")
    return End_computer_data

def get_image_link(i):
    link = "NULL"
    try:
      if (i.get("Siteİsmi1") != "ciceksepeti"):
        if (i.get("Siteİsmi1") == "evkur"):      
            link = get_soup(i.get("SiteLinki1")).find("div", {"class":"image"}).img['src']
        elif (i.get("Siteİsmi1") == "n11"):
            link = get_soup(i.get("SiteLinki1")).find("div", {"class":"imgObj"}).a['href']
        elif (i.get("Siteİsmi1") == "vatan"):
            link = get_soup(i.get("SiteLinki1")).find("div", {"class":"swiper-slide"}).a['href']
        elif (i.get("Siteİsmi1") == "teknosa"):
            link = get_soup(i.get("SiteLinki1")).find("div", {"class":"swiper-slide swiper-slide-active"}).a['href']
        elif (i.get("Siteİsmi1") == "Trendyol"):
            link = get_soup(i.get("SiteLinki1")).find("div", {"class":"flex-container"}).img['src']
      else:
        try:
          if (i.get("Siteİsmi2") == "evkur"):      
              link = get_soup(i.get("SiteLinki2")).find("div", {"class":"image"}).img['src']
          elif (i.get("Siteİsmi2") == "n11"):
              link = get_soup(i.get("SiteLinki2")).find("div", {"class":"imgObj"}).a['href']
          elif (i.get("Siteİsmi2") == "vatan"):
              link = get_soup(i.get("SiteLinki2")).find("div", {"class":"swiper-slide"}).a['href']
          elif (i.get("Siteİsmi2") == "teknosa"):
              link = get_soup(i.get("SiteLinki2")).find("div", {"class":"swiper-slide swiper-slide-active"}).a['href']
          elif (i.get("Siteİsmi2") == "Trendyol"):
              link = get_soup(i.get("SiteLinki2")).find("div", {"class":"flex-container"}).img['src']
        except:
          pass
    except:
        if (i.get("Siteİsmi2") == "evkur"):      
            link = get_soup(i.get("SiteLinki2")).find("div", {"class":"image"}).img['src']
        elif (i.get("Siteİsmi2") == "n11"):
            link = get_soup(i.get("SiteLinki2")).find("div", {"class":"imgObj"}).a['href']
        elif (i.get("Siteİsmi2") == "vatan"):
            link = get_soup(i.get("SiteLinki2")).find("div", {"class":"swiper-slide"}).a['href']
        elif (i.get("Siteİsmi2") == "teknosa"):
            link = get_soup(i.get("SiteLinki2")).find("div", {"class":"swiper-slide swiper-slide-active"}).a['href']
        elif (i.get("Siteİsmi2") == "Trendyol"):
            link = get_soup(i.get("SiteLinki2")).find("div", {"class":"flex-container"}).img['src']
    return (link)

#------------------DOWNLOAND İMAGE AND MOVE DİRECTORY-------------------
def Download_images(End_computer_data):
    id = 0
    for i in End_computer_data:
        id += 1
        url = i.get("İmageLink")
        print(url)
        try:
          urllib.request.urlretrieve(url, str(id) + ".jpg")
          shutil.move(str(i.get("id")) + ".jpg", "resimler")
        except:
          print("Resim indirilemedi !!!")

#------------------MULTI THREADING STARTING-------------------
t1 = threading.Thread(target = _ciceksepeti)
t2 = threading.Thread(target = _evkur)
t3 = threading.Thread(target = _trendyol)
t4 = threading.Thread(target = _teknosa)
t5 = threading.Thread(target = _vatan)
t6 = threading.Thread(target = _n11)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()

#------------------MODEL NUMBER FINDER-------------------
print("N11 verileri için Model Numarası aranıyor 🔍")
Uniq_Computer_of_n11 = Site_Model_No_Find(Uniq_Computer_of_n11)
print("Ciceksepeti verileri için Model Numarası aranıyor 🔍")
Uniq_Computer_of_ciceksepeti = Site_Model_No_Find(Uniq_Computer_of_ciceksepeti)
print("Trendyol verileri için Model Numarası aranıyor 🔍")
Uniq_Computer_of_trendyol = Site_Model_No_Find(Uniq_Computer_of_trendyol)


#------------------DUPLICATE CONTROL-------------------
Uniq_Computer_of_ciceksepeti = Uniq_computer_Converter(Uniq_Computer_of_ciceksepeti)
Uniq_Computer_of_trendyol = Uniq_computer_Converter(Uniq_Computer_of_trendyol)
Uniq_Computer_of_teknosa = Uniq_computer_Converter(Uniq_Computer_of_teknosa)
Uniq_Computer_of_evkur = Uniq_computer_Converter(Uniq_Computer_of_evkur)
Uniq_Computer_of_n11 = Uniq_computer_Converter(Uniq_Computer_of_n11)
Uniq_Computer_of_vatan = Uniq_computer_Converter(Uniq_Computer_of_vatan)

#------------------DATASET CREATED-------------------
print("Veriseti oluşturuluyor 🔧")
Global_Computer_Data = Global_data_create()
print("Veriler MongoDB'ye aktarılıyor 📝")
End_computer_data = Global_success_data_to_MongoDB()
print("Veriler başarılı bir şekilde veritabanına aktarıldı ✅✅✅")

#------------------IMAGE DOWNLOAD2-------------------
''' print("Resimler indiriliyor 🔧🔧🔧")
Download_images(End_computer_data)
print("Resimler indirildi ✅✅✅") '''
