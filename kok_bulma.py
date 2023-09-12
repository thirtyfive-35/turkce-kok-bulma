import codecs
import os
import chardet
from unidecode import unidecode

        
class kok_ayir_cl():

  def __init__(self):
    self.ekler = [
    'el', 'siz', 'sız', 'suz', 'süz', 'ci', 'cı', 'cu', 'cü', 'çı', 'çi', 'çu',
    'çü', 'sı', 'si', 'su', 'sü', 'ce', 'ca', 'daş', 'taş', 'deş', 'teş', 'inci',
    'ıncı', 'uncu', 'üncü', 'lik', 'lık', 'lük', 'luk', 'li', 'lı', 'lu', 'lü',
    'de', 'da', 'er', 'ki', 'kü', 'msi', 'msı', 'cil', 'çil', 'cıl', 'çıl',
    'çul', 'cul', 'cül', 'şın', 'çın', 'sal', 'sel', 'ıt', 'cağız', 'ceğiz',
    'cik', 'cık', 'cük', 'çık', 'ti', 'tı', 'tu', 'z', 'ce', 'ecek', 'acak',
    'ak', 'aç', 'ge', 'gi', 'gı', 'kı', 'ki', 'giç', 'gıç', 'gin', 'gın', 'kin',
    'kın', 'gun', 'i', 'ı', 'u', 'ü', 'ici', 'ucu', 'ücü', 'ıcı', 'ik', 'ık',
    'ük', 'im', 'ım', 'üm', 'um', 'in', 'ın', 'ün', 'inç', 'ünç', 'geç', 'gaç',
    'inti', 'ıntı', 'üntü', 'untu', 'ir', 'ur', 'er', 'ar', 'iş', 'ış', 'uş',
    'üş', 'it', 'ıt', 'üt', 'kan', 'ken', 'gan', 'gen', 'ma', 'mek', 'mak',
    'maç', 'mbaç', 'ti', 'tı', 'maca', 'mece', 'sel', 'sal', 'anak', 'enek',
    'ler', 'lar', 'i', 'ı', 'u', 'ü', 'e', 'a', 'de', 'da', 'te', 'ta', 'den',
    'dan', 'ten', 'tan', 'ce', 'ca', 'çe', 'ça', 'm', 'n', 'si', 'miz', 'niz',
    'leri', 'ları', 'ın', 'in', 'un', 'ün'
    'ma', 'me', 'mı', 'mi', 'mu', 'mü', 'm', 'im', 'ım', 'um', 'üm', 'n', 'in',
    'ın', 'un', 'ün', 'sin', 'sın', 'sun', 'sün', 'k', 'ız', 'iz', 'uz', 'üz',
    'niz', 'nız', 'nuz', 'nüz', 'iniz', 'ınız', 'unuz', 'ünüz', 'siniz', 'sınız',
    'sunuz', 'sünüz', 'ler', 'lar', 'sinler', 'sınlar', 'sunlar', 'sünler',
    'dır', 'dir', 'dur', 'dür', 'tır', 'tir', 'tur', 'tür', 'dı', 'di', 'du',
    'dü', 'tı', 'ti', 'tu', 'tü', 'mış', 'miş', 'muş', 'müş', 'sa', 'se', 'r',
    'ar', 'er', 'ır', 'ir', 'ur', 'ür', 'yor', 'acak', 'ecek', 'üt', 'aş', 'eş',
    'i', 'ı', 'kır', 'kir', 'kur', 'kür', 'l', 'le', 'la', 'len', 'lan', 'msa',
    'mse', 'r', 'rga', 'rge', 'se', 'sa', 'da', 'de', 'ta', 'te', 'e', 'a', 'el',
    'al', 'an', 'en', 'at', 'et', 'ut', 'malı', 'meli', 'leş', 'laş', 't', 'ş',
    'ele', 'ala', 'ik'
    ]
    self.kelime = ''
    self.my_kelime_list = []
    self.user_input()
    
  def kok_bul(self,kelime): 
    while len(kelime) > 3:
      kelime = kelime.lower()       #karakterleri kucuk harfe cevirir
      if kelime[-6:] in self.ekler:
        kelime = kelime[:-6]
        self.kelime = kelime
        continue

      elif kelime[-5:] in self.ekler:
        kelime = kelime[:-5]
        self.kelime = kelime
        continue

      elif kelime[-4:] in self.ekler:
        kelime = kelime[:-4]
        self.kelime = kelime
        continue

      elif kelime[-3:] in self.ekler:
        kelime = kelime[:-3]
        self.kelime = kelime
        continue

      elif kelime[-2:] in self.ekler:
        kelime = kelime[:-2]
        self.kelime = kelime
        continue

      elif kelime[-1:] in self.ekler:
        kelime = kelime[:-1]
        self.kelime = kelime
        continue

      else:
        break

  def dosya_oku(self,path):
    with open(path, "rb") as dosya:
      dosya_encoding = chardet.detect(dosya.read())['encoding']
    with codecs.open(path, "rb",dosya_encoding,errors='ignore') as dosya:
      for satir in dosya:
          row = []
          satir = satir.replace('\uFFFD', '')
          kelimeler_satir = satir.split()
          print('okuyor..')
          for i in kelimeler_satir:
            if self.asi == 'y' :
              i = unidecode(i)
            if i[-1:] in '.;:,?!%':
              i = i[:-1]
            self.kok_bul(i)
            row.append(self.kelime)
          self.my_kelime_list.append(row)
  def dosya_yaz(self,path):
    with codecs.open(path, "w", encoding="utf-8") as dosya:
      
      for i in range(len(self.my_kelime_list)):
        for j in range(len(self.my_kelime_list[i])):
          dosya.write(self.my_kelime_list[i][j] + ' ')
          
  def calistir(self):
    ana_klasor_yolu = self.path
    for klasor_yolu, alt_klasorlar, dosyalar in os.walk(ana_klasor_yolu):
        for dosya in dosyalar:
            if dosya.endswith('.txt'):
                # dosya yolunu oluşturur
                dosya_yolu = os.path.join(klasor_yolu, dosya)

                # dosyayı okur
                self.dosya_oku(dosya_yolu)

                # yeni dosya ismini ve klasörü oluşturur
                yeni_klasor_yolu = klasor_yolu + '_kok'
                os.makedirs(yeni_klasor_yolu, exist_ok=True)
                yeni_dosya_isim = dosya.split('.')[0] + '_kok.txt'
                yeni_dosya_yolu = os.path.join(yeni_klasor_yolu, yeni_dosya_isim)

                # dosyayı yazar
                self.dosya_yaz(yeni_dosya_yolu)
                self.my_kelime_list = []

    print('Tüm dosyalar başarıyla degistirildi.')
  def user_input(self):
    print('Orn "C:\\Users\\batur\\Desktop\\Bonus_Ekler_Ara_Sınav_30_Puan_Eklenecek\\Bonus_Ekler_Ara_Sınav_30_Puan_Eklenecek" ')
    self.path = input('Dosya yolunu belirtiniz:  ')
    self.asi = input('ascii formatiyla kok bulunsun mu(y/n): ')

dd = kok_ayir_cl()

dd.calistir()


       




