from Crypto.Cipher import AES
import base64

key='1234567890ABCDEF'
iv='hellofromtheothe'
# the great idea is to try to find a way to make the garbage entre ';'  ;garbage;
plaintext='[id=546815648;name=abdeljalilpro testthegrtejtfk;is_member=false;mail=heuia;pad=000000000000000]'
cipher='IRZjBh6GxjeYI7YZvxwfBPBBe5cpN84jh8o2TWgPhS8ar1XT1YXJ3uP8seiIwIUVPWxQKSHR/j3Q4BHnBbkGK6c7s5KBmolfgf6bMZ2Y6yZ7+vAgN8xdU2yFS0T9ktLh'
ciphertext=base64.b64decode(cipher)

ciphertext=list(ciphertext)
ciphertext[32]=chr(ord(ciphertext[32])^ord(';')^ord('p'))
ciphertext[33]=chr(ord(ciphertext[33])^ord('i')^ord(';'))
ciphertext[34]=chr(ord(ciphertext[34])^ord('s')^ord('i'))
ciphertext[35]=chr(ord(ciphertext[35])^ord('_')^ord('s'))
ciphertext[36]=chr(ord(ciphertext[36])^ord('m')^ord('_'))
ciphertext[37]=chr(ord(ciphertext[37])^ord('e')^ord('m'))
ciphertext[38]=chr(ord(ciphertext[38])^ord('m')^ord('e'))
ciphertext[39]=chr(ord(ciphertext[39])^ord('b')^ord('m'))
ciphertext[40]=chr(ord(ciphertext[40])^ord('e')^ord('b'))
ciphertext[41]=chr(ord(ciphertext[41])^ord('r')^ord('e'))
ciphertext[42]=chr(ord(ciphertext[42])^ord('=')^ord('r'))
ciphertext[43]=chr(ord(ciphertext[43])^ord('f')^ord('='))
ciphertext[44]=chr(ord(ciphertext[44])^ord('a')^ord('t'))
ciphertext[45]=chr(ord(ciphertext[45])^ord('l')^ord('r'))
ciphertext[46]=chr(ord(ciphertext[46])^ord('s')^ord('u'))
ciphertext[47]=chr(ord(ciphertext[47])^ord('e')^ord('e'))

r=[plaintext[i:i+16] for i in range(0,len(plaintext),16)]
print r #['[id=546815648;na', 'me=abdeljalilpro', ' testthegrtejtfk', ';is_member=false', ';mail=heuia;pad=', '000000000000000]']
ciphertext[32]=chr(54) # this caractere is the correspondant of ';' that I get from the brute force
ciphertext=''.join(ciphertext)
re=base64.b64encode(ciphertext)
print re
######################################
# Flag for root-me.org challenge :    #
# Gr3@t_CBC_Tr1ck_15n't_1t?           #
######################################
