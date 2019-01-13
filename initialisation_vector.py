from Crypto.Cipher import AES
import base64

plaintext='''Marvin: "I am at a rough estimate thirty billion times more intelligent than you. Let me give you an example. Think of a number, any number."
Zem: "Er, five."
Marvin: "Wrong. You see?"'''

ciphertext='''cY1Y1VPXbhUqzYLIOVR0RhUXD5l+dmymBfr1vIKlyqD8KqHUUp2I3dhFXgASdGWzRhOdTj8WWFTJ
PK0k/GDEVUBDCk1MiB8rCmTZluVHImczlOXEwJSUEgwDHA6AbiCwyAU58e9j9QbN+HwEm1TPKHQ6
JrIOpdFWoYjS+cUCZfo/85Lqi26Gj7JJxCDF8PrBp/EtHLmmTmaAVWS0ID2cJpdmNDl54N7tg5TF
TrdtcIplc1tDvoCLFPEomNa5booC'''

key='AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRqrHB0eHyA='

key=base64.b64decode(key)
ciphertext=base64.b64decode(ciphertext)
def padding(message,taille_block):
	return message+'?'*(taille_block-len(message)%taille_block)
def xor(str1,str2):
	cipher=""
	for i in range(len(str1)):
		cipher+=chr(ord(str1[i])^ord(str2[i]))
	return cipher

def decrypt_ECB(payload):
    obj = AES.new(key, AES.MODE_ECB)
    
    ciphertext=""
    ciphertext+=obj.decrypt(payload)
    return ciphertext


initialisation_vector=xor(decrypt_ECB(ciphertext[:16]),plaintext[:16])
print "the VI =",initialisation_vector
# the flag is = I_l0v3_Crypt0_:)






