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
from Crypto.Cipher import AES
import os

from Crypto.Util.Padding import pad, unpad

key = os.urandom(32) # 256-bit AES anahtarı
iv = os.urandom(16) # AES için Initialization Vector

data =  "Cavit Batu Soylu" .encode() #

#AES şifreleme (CBC Modu)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, AES.block_size))
print("İlk Veri AES: " , data)
print("Şifreli Veri AES: " , ciphertext.hex())

# AES şifre çözme (CBC Modu)
decipher = AES.new(key, AES.MODE_CBC, iv)
decipher_date = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Çözülmüş İlk Veri: (AES): " , decipher_date.decode())