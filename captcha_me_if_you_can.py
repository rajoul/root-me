import requests,base64,re
import pytesseract
import subprocess,Image,string,time

url="http://challenge01.root-me.org/programmation/ch8/"


r=requests.get(url)

print r.cookies
cook=r.cookies
i=0

while(1):
	data=re.findall('data:image/png;base64,(.*) /><br>',r.text)

	sd=base64.b64decode(data[0])
	f=open('img.png','wb')
	f.write(sd)
	f.close()


	tet=pytesseract.image_to_string(Image.open('img.png'))
	r=requests.post(url,data={'cametu':tet},cookies=cook)
	if r.text.find('retente ta chance')!=-1:
		print 'waiting.....',i
	else:
		print r.text
		break;
	i+=1

#Congratz, le flag est dtePZJgVAfaU




