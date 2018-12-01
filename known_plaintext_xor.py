import time,re


def find_key():
	key=""
	HEADER_FILE="\x24\x2c\x9a\xe3\x62\x6e\x66\x61\x6c\x6c\x53\x6e\x66\x61"  # le header de notre fichier bmp encrypt
	HEADER_AVANT_ENC="\x42\x4d\xF6\x8F\x07\x00\x00\x00\x00\x00\x36\x00\x00\x00" # c'est le header du fichier avant encryption='BM'+taille+00+offset
	for a,b in zip(HEADER_AVANT_ENC,HEADER_FILE):
		key+=chr(ord(a)^ord(b))
	return  key
  
key=find_key()[:6]  #return fallenfallenfa
cipher=""
i=0
for line in open('image.bmp'):
	for x in line:
		cipher+=chr(ord(x)^ord(key[i%6]))
		i+=1
			
f=open('generate.bmp','wb')
f.write(cipher)
f.close()
		
# lorsque vous ouvrer le fichier : generate.bmp vous trouver:
# le mot de pass est: ICONOCLASTE