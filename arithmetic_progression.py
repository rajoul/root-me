import requests,time,re



url='http://challenge01.root-me.org/programmation/ch1'


r=requests.get(url)

cookie=r.cookies
mes=r.text[217:260].split()
a=int(mes[0])
b=int(mes[8])
u0=int(re.findall('<sub>0</sub> = (.*)',r.text)[0])
n=int(re.findall('<br />You must find U<sub>(.*)</sub>',r.text)[0])

result=u0+(n)*a+b*((n*(n-1))/2)
print result
url=url+'/ep1_v.php?result='+str(result)
g=requests.get(url,cookies=cookie)
print g.text

#Congratz! The flag is : lFablYE9P1