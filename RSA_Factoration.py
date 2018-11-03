import base64
import binascii
from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
from binascii import hexlify,unhexlify

asciikey = """-----BEGIN PUBLIC KEY-----
MGQwDQYJKoZIhvcNAQEBBQADUwAwUAJJAMLLsk/b+SO2Emjj8Ro4lt5FdLO6WHMM
vWUpOIZOIiPu63BKF8/QjRa0aJGmFHR1mTnG5Jqv5/JZVUjHTB1/uNJM0VyyO0zQ
owIDAQAB
-----END PUBLIC KEY-----"""

key = RSA.importKey(asciikey)
n = int(key.n)

p=398075086424064937397125500550386491199064362342526708406385189575946388957261768583317

q=472772146107435302536223071973048224632914695302097116459852171130520711256363590397527

M=(p-1)*(q-1)

e=65537

d=inverse(e,M)

msg = base64.b64decode("e8oQDihsmkvjT3sZe+EE8lwNvBEsFegYF6+OOFOiR6gMtMZxxba/bIgLUD8pV3yEf0gOOfHuB5bC3vQmo7bE4PcIKfpFGZBA")
cipher = int(hexlify(msg),16)

plaintext = pow(cipher,d,n)
original = hex(plaintext)[2:].strip("L")
if len(original)%2:
	original="0"+original

print(unhexlify(original))

# the flag is :up2l6DnaIhZgxA
