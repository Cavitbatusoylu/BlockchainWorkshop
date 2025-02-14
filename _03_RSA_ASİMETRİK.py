# pip --vesion
# pip install pycrptodome  # AES KÜTÜPHANESİ
#pip install colorama #Color

# Eğer paket yüklenmezse
# pip uninstall pycrptodome
# pip install pycryptodome --no--cache-dir

#CBC(Cipher Block Chaining)
#Simetrik: Aynı anahtar hem şifreleme hemde çözme işlemleri için kullanılır.
#Asimetrik: İki farklı anahtar kullanılır(public, private)

# 3.RSA (Rivest Shamir Adleman) - Asimetrik Şifreleme
# 8 Bit = 1 Bayt

"""
RSA (Rivest Shamir Adleman) - Asimetrik Şifreleme:
1977 yılında geliştirilmiştir
İki farklı anahatar kullanılır: Public, Private
Anahtar uzunluğu: 1024-bit, 2048-bit, 4096-bit kullanılır ancak biz genelde 2048-bit kullanırız.
AES, DES'e göre çok daha yavaştır.

SSL/TLS(HTTPS)
Digital İmza
Kripto Para cüzdanlarında

Anahtar Üretme: Büyük asal sayılar kullanılır. 2,3,5,7,11,13,17,19,23 ....
public key: Veriyi şifrelemek
private key: Veriyi çözmek için gereken anahtar
"""

####################################################################
from Crypto.PublicKey import RSA # RSA ŞİFRELEME KÜTÜPHANESİ
from Crypto.Cipher import PKCS1_OAEP # RSA Anahtar Üretme Kütüphanesi
#import os # Rastgele anahatar üretmek için kullanılan kütüphane
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
# RSA Anahtar üretmek
#key = os.urandom(8) # 256-bit DES anahtarı güvenli ve rastgele sayılar için(2.Yol) AES
#key = b"8bytekey1" # 8 byte uzunluğunda bir anahtar (1.Yol) DES
key = RSA.generate(2048) # 2048-bit uzunluğunda bir RSA anahtarı üret
public_key = key.publickey().export_key()
private_key = key.export_key()

print(f"{YELLOW}Genel Anahtar (RSA): ", public_key.decode()+"\n")
print(f"{BLUE}Özel Anahtar (RSA): ", private_key.decode()+"\n")

#Şifrelenecek veriyi tamamladık(Ör: Cavit Batu Soylu)
data =  "Cavit Batu Soylu" .encode() # string veriyi byte formatına çevirir

rsa_public_key = RSA.import_key(public_key)

# Şifreleme (Public Key kullanarak)
cipher = PKCS1_OAEP.new(rsa_public_key) # RSA nesnesini oluştur

# Veriyi DES şifreleme bloğu boyutuna uygun hale getirmek için pad() kullanıyoruz.
# DES boyutu 8 byte olduğu için eksik kalan kısımları uygun bir şemada dolduralım.
ciphertext = cipher.encrypt(data)

#Şifrelenmiş verileri hexadecimal formatında ekrana yazdırıyoruz.
# print(f"{CYAN}Şifrelenmiş Veri (RSA):  {RESET} {ciphertext.hex()}" )
print(f"{CYAN}Şifrelenmiş Veri (RSA):  {RESET}" , ciphertext.hex()+"\n")

# RSA şifre çözme (private key kullanarak)
rsa_private_key = RSA.import_key(private_key)
decipher = PKCS1_OAEP.new(rsa_private_key)
decrpyted_data = decipher.decrypt(ciphertext)

# Şifre çözülmüş veriyi ekrana yazdırıyoruz.
print(f"{CYAN}Çözülmüş İlk Veri: (DES): {RESET}" , decrpyted_data.decode())