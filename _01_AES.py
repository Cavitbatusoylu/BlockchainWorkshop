# pip --vesion
# pip install pycrptodome  # AES KÜTÜPHANESİ

# Eğer paket yüklenmezse
# pip uninstall pycrptodome
# pip install pycryptodome --no--cache-dir

# 8 Bit = 1 Bayt

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
##############################
from Crypto.Cipher import AES  # AES ŞİFRELEME KÜTÜPHANESİ
from Crypto.Util.Padding import pad, unpad # Veri bloklarını tamamlamak ve kaldırma fonksiyonu
import os # Rastgele anahatar üretmek için kullanılan küütüphane

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
print("İlk Veri AES: " , data)
print("Şifreli Veri AES: " , ciphertext.hex())

# AES şifre çözme (CBC Modu)
# AES şifre çözme işlemi için aynı anahtar ve IV ile yeni bir AES nesnesi oluşturuyoruz.
decipher = AES.new(key, AES.MODE_CBC, iv)

# Şifrelenmiş verileri AES şifre çözme bloğuna uygun hale getirmek için unpad() kullanıyoruz.
decipher_date = unpad(decipher.decrypt(ciphertext), AES.block_size)

# Şifre çözülmüş veriyi ekrana yazdırıyoruz.
print("Çözülmüş İlk Veri: (AES): " , decipher_date.decode())