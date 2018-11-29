import socket, sys, time, base64
import math,re
import codecs
import zlib
server = "irc.root-me.org"
port = 6667
channel = "#root-me_challenge"
botnick = "rajoul"
serverbot = "candy"
 
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, port))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :This is a fun bot!\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("JOIN "+ channel +"\n")
 
i = 0
while 1:
        text = irc.recv(2040)
        print text

 
        if text.find('PING') != -1:
                irc.send('PONG ' + text.split() [1] + '\r\n')
        i += 1
        if i == 6:
                break
 
time.sleep(3)
irc.send('PRIVMSG '+serverbot+' :!ep4\r\n')
text = irc.recv(2040)

dec=re.findall('rajoul :(.*)',text)
message=base64.b64decode(dec[0].strip('\r'))
mes=zlib.decompress(message)
irc.send('PRIVMSG '+serverbot+' :!ep4 -rep %s\r\n'%mes)
text = irc.recv(2040)
print text


#:Candy!Candy@root-me.org PRIVMSG rajoul :
#You dit it! You can validate the challenge with the password tumasp0wned










