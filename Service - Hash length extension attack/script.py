import hlextend
import base64,pwn

host="challenge01.root-me.org"
port=51022
s=pwn.remote(host,port)
print s.recv()
s.sendline('1')
print s.recv()
sha = hlextend.new('sha256')
re=sha.extend('fsfsfdsfs:admin', 'a:guest', 16, '6ac698be1cfd53cd71b42d91b73fa79d2d2676daf775c2c719b4a912e2e58b9d',raw=True)
print re 
tr=base64.b64encode(re)
tok2=base64.b64encode(sha.hexdigest())
token=tr+':'+tok2
s.sendline(token)
print s.recv()
#####################################################
# Welcome back! Flag to validate is u$3_HMAC_l4m3rZ! #
#####################################################
