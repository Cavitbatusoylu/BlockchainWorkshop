# pip --vesion
# pip install pycrptodome  # AES KÜTÜPHANESİ
#pip install colorama #Color

# Eğer paket yüklenmezse
# pip uninstall pycrptodome
# pip install pycryptodome --no--cache-dir

#CBC(Cipher Block Chaining)
#Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
#Asimetrik: İki farklı anahtar kullanılır(public, private)

# 1.AES (Advanced Encryption Standard) - Simetrik Şifreleme
# AES için Pyhton'da pycryptodome kütüphanesini kullanabiliriz.
# AES 128-bit blok boyutunda çalışır ve CBC (Cipher Block Chaining) gibi modlarla güvenliği artırabiliriz.

# 8 Bit = 1 Bayt

"""
AES,DES şifreleme algoritmalarında kulllanılır:
Şifrelemede öncesinde PAD
Şifre çözümlemede UNPAD

pad, unpad bu fonksiyonlar AES,DES blok şifrelemede algoritmalarında
veriyi istediğimizi formda kullanmak için bu fonksiyonunu çağırız.

1-pad: Doldurma: veriyi belirli bir blok boyutuna tamamlamak içindir
Sabit blok şifrelme algoritmalarıya çalışırız örneğin: 16 byte Eüer veriyi tam blok haline getirmezseni şifreleme çalışmaz.

2-unpad: Kaldırma: şifrelenmiş verinin tamamına ulaşana kadar bırakılan paddingı kaldırır.
pad tarafından eklenen fazlalıkları kaldırarak veriyi original haline getirmek
"""
"""
AES, simetrik anahtarlı şifreleme algoritmasıdır.
2001 yılında NIST (National Intitute of Standarts and Technology)
Rijndael algorithm dayanır
128-bit, 192-bit, 256-bit
Günümüz şartlarında DES'e göre daha güvenlidir.
Yüksek Hız Verimliliği, Güçlü ,Brute force dayanıklıdır.
Veri Şifreleme
WPA2, WPA3
VPN
"""

####################################################################
from Crypto.Cipher import AES  # AES ŞİFRELEME KÜTÜPHANESİ
from Crypto.Util.Padding import pad, unpad # Veri bloklarını tamamlamak ve kaldırma fonksiyonu
import os # Rastgele anahatar üretmek için kullanılan kütüphane
from colorama import Fore, Style #Renkli çıktı için

####################################################################
#Renkleriçin kısayollar
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL #Renkleri sıfırlamak için kullanılır
####################################################################

# 8 bit = 1 byte
# AES için 256-bit(32byte) uzunluğunda rastgele bir anahtar oluşturur
key = os.urandom(32) # 256-bit AES anahtarı güvenli ve rastgele sayılar için

#AES için initialization vector(IV) olarak 16 byte olarak rastgele bir değer oluşturur
iv = os.urandom(16) # AES için Initialization Vector

#Şifrelenecek veriyi tamamladık(Ör: Cavit Batu Soylu)
data =  "Cavit Batu Soylu" .encode() # string veriyi byte formatına çevirir

#AES şifreleme (CBC Modu)
cipher = AES.new(key, AES.MODE_CBC, iv) # AES nesnesini oluştur(CBC Modu ve IV)

# Veriyi AES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanıyoruz.
# AES boyutu 16 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext = cipher.encrypt(pad(data, AES.block_size))

#Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
print(f"{CYAN}AES:İlk Veri Şifrelenemeden Önce: {RESET} {data.decode()}", data)
# print(f"{BLUE}Şifrelenmiş Veri (AES,CBC Modu):  {RESET} {ciphertext.hex()}" )
print(f"{BLUE}Şifrelenmiş Veri (AES,CBC Modu):  {RESET}" , ciphertext.hex())

# AES şifre çözme (CBC Modu)
# AES şifre çözme işlemi için aynı anahtar ve IV ile yeni bir AES nesnesi oluşturuyoruz.
decipher = AES.new(key, AES.MODE_CBC, iv)

# Şifrelenmiş verileri AES şifre çözme bloğuna uygun hale getirmek için unpad() kullanıyoruz.
decipher_date = unpad(decipher.decrypt(ciphertext), AES.block_size)

# Şifre çözülmüş veriyi ekrana yazdırıyoruz.
print(f"{RED}Çözülmüş İlk Veri: (AES): {RESET}" , decipher_date.decode())