import pwn,base64,time,re

host="challenge01.root-me.org"
port=51035
token="IRZjBh6GxjeYI7YZvxwfBPBBe5cpN84jh8o2TWgPhS9K/U//543B0eTr/rOd3oMVPWxQKSHR/j3Q4BHnBbkGK6c7s5KBmolfgf6bMZ2Y6yZ7+vAgN8xdU2yFS0T9ktLh"

for ele in range(53,256):
	token=list(base64.b64decode(token))
	s=pwn.remote(host,port)
	pr=s.recv()
	pr=s.recv()
	s.sendline('2')
	pr=s.recv()
	token[32]=chr(ele)  # we brute force on this char to make it acceptable by the server
	token=''.join(token)
	token=base64.b64encode(token)
	s.sendline(token)
	pr=s.recv()
	pr1=s.recv()
	if pr1.find('INVALID TOKEN')!=-1:

		d=re.findall("Token :(.*)|	 Splitting",pr1)
		print str(ele)+"==>>"+d[0]
	else:
		print '###################################'
		print "GREAT   GREAT    GREAT"
		d=re.findall("Token :(.*)|	 Splitting",pr1)
		print str(ele)+"==>>"+d[0]
		print pr1
		break
	time.sleep(1)



