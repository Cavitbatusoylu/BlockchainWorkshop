# pip --vesion
# pip install pycrptodome  # AES KÜTÜPHANESİ
#pip install colorama #Color

# Eğer paket yüklenmezse
# pip uninstall pycrptodome
# pip install pycryptodome --no--cache-dir

#BC(Cipher Block Chaining)
#Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
#Asimetrik: İki farklı anahtar kullanılır(public, private)

# 2.DES (Data Encryption Standard) - Simetrik Şifreleme
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
DES:
IBM tarafından 1977 NIST NIST (National Institute of Standards and Technology)
Simetrik blok şifreleme
Günümüzde güvenlik açısından çokça tercih edlimiyor
Anahtar uzunluğu 56-bit
Blok boyutu 64-bit
Düşük Hız, Güçlü, Brute force dayanıklı değil
ATM pin şifreleme
Eski güvenlik sistemlerinde
"""

####################################################################
from Crypto.Cipher import DES  # DES ŞİFRELEME KÜTÜPHANESİ
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
# DES için 8 byte (64 bit) anahtar uzunluğunda
#key = os.urandom(8) # 256-bit DES anahtarı güvenli ve rastgele sayılar için(2.Yol)
key = b"8bytekey1" # 8 byte uzunluğunda bir anahtar (1.Yol)

#DES için 8 byte olarak rastgele bir değer oluşturur
iv = os.urandom(8) # DES için Initialization Vector

#Şifrelenecek veriyi tamamladık(Ör: Cavit Batu Soylu)
data =  "Cavit Batu Soylu" .encode() # string veriyi byte formatına çevirir

#AES şifreleme (CBC Modu)
cipher = DES.new(key, DES.MODE_CBC, iv) # DES nesnesini oluştur(CBC Modu ve IV)

# Veriyi DES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanıyoruz.
# DES boyutu 8 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext = cipher.encrypt(pad(data, DES.block_size))

#Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
print(f"{CYAN}AES:İlk Veri Şifrelenemeden Önce: {RESET} {data.decode()}", data)
# print(f"{BLUE}Şifrelenmiş Veri (DES,CBC Modu):  {RESET} {ciphertext.hex()}" )
print(f"{BLUE}Şifrelenmiş Veri (DES,CBC Modu):  {RESET}" , ciphertext.hex())

# DES şifre çözme (CBC Modu)
# DES şifre çözme işlemi için aynı anahtar ve IV ile yeni bir AES nesnesi oluşturuyoruz.
decipher = DES.new(key, DES.MODE_CBC, iv)

# Şifrelenmiş verileri AES şifre çözme bloğuna uygun hale getirmek için unpad() kullanıyoruz.
decipher_date = unpad(decipher.decrypt(ciphertext), DES.block_size)

# Şifre çözülmüş veriyi ekrana yazdırıyoruz.
print(f"{RED}Çözülmüş İlk Veri: (DES): {RESET}" , decipher_date.decode())