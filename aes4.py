### To install the pycryptodome library ####
# sudo apt install python3-pip
# sudo pip3 install pycryptodomex

from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Cryptodome.Cipher import AES
######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes)
key = b'Sixteen byte key'

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
cipherText = encCipher.encrypt(b'hello12345678s0d1111111111111111')
paddedCipherText = pad(cipherText.encode(), 16) 	# Pads the text to be a multiple of 16 bytes

print("Cipher text: ", paddedCipherText)

########### BASIC DECRYPTION ##############

# Set up the AES encryption class
decCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes
plainText = decCipher.decrypt(cipherText)

print("Decrypted text: ", plainText)
