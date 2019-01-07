from Crypto.Util.number import inverse,GCD
from Crypto.PublicKey import RSA
from binascii import hexlify,unhexlify
#import gmpy2

msg1='''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtbdQAzdaO7GHXxUsVZ+FmcddA
Hrugq+azkVdfgnHu6teK3hDQlk0BdNz9LlQT3BoHXg5/g9FDv3bBwaulpQEQPlGM
UXEUnQAJ69KSVaLxHb5Wmb0vqX/qySKc8Hseqt5wbXklOrnZeHJ3Hm3mUeIplpWP
f19C6goN3bUGrrniwwIDAQAB
-----END PUBLIC KEY-----'''
msg2='''-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCtbdQAzdaO7GHXxUsVZ+FmcddA
Hrugq+azkVdfgnHu6teK3hDQlk0BdNz9LlQT3BoHXg5/g9FDv3bBwaulpQEQPlGM
UXEUnQAJ69KSVaLxHb5Wmb0vqX/qySKc8Hseqt5wbXklOrnZeHJ3Hm3mUeIplpWP
f19C6goN3bUGrrniwwIDBTy3
-----END PUBLIC KEY-----'''

message0=5050983197907648139720782448847677677343236446273586870502111273113384857588837608900494692102715861436825279596563904392832518247929761994240007673498974877828278590361242528762459283022987952424770766975922016521475963712698089809426428406068793291250622593222599407825968002220906973019105007856539702124
message1=99993713982446651581396992055360571139557381122865583938229634474666415937105325664345678113405954865343401854091338680448775405253508255042453184099961570780032181898606546389573694481401653361757628850127420072609555997892925890632116852740542002226555293049123266123721696951805937683483979653786235824108

key1 = RSA.importKey(msg1)
n0= int(key1.n)
e1=int(key1.e)
key2 = RSA.importKey(msg2)
e2=int(key2.e)
n1= int(key2.n)
# for a in range(133000,140000):
# 	for b in range(-26000,200):
# 		if (e1*a+e2*b == GCD(e1,e2)):
# 			print a,b
# 			break

a,b=133132 ,-25421
i=inverse(message1,n0)

valeur=(pow(message0,a,n0)*pow(i,-b,n0))%n0
original = hex(valeur)[2:].strip("L")
if len(original)%2:
	original="0"+original

print(unhexlify(original))
# Yeah man, you got the message. The flag is W311D0n3! and 
# this is a padding to have a long text, 
# else it will be easy to decrypt.