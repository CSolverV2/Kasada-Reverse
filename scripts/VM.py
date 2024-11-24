import random
import json
from log import Logger
import requests
import time

def IPS(ips):
    ips = requests.get(ips, headers={
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,de;q=0.9',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Avast Secure Browser";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Avast/126.0.0.0',
    }).text
    A = ips.split('A="')[1].split('",T')[0]
    log.info(f"VM String --> {A[:50]}...")
    encstr = ips.split('l(A,"')[1].split('",50')[0]
    log.info(f"Decoder String --> {encstr} ")
    
    return A, encstr

log = Logger('CSolver')

def VM(ips=None):
    if not ips:
        # Replace this url with the url of ur target ips.js
        ips = 'https://accounts.nike.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/ips.js?KP_UIDz=0bzlQM8Zd58VEZEwc7CXIcUScVQiwwBjdvaj8Y0PYP4xDIVzhSSMnJR3yP6foqg53RbfGyipWiuIaKWjqXt8u9siM8vPuSetWg74FREbSEcmKyP1zTsM9WYS78PveGj1ZG32RvqQFZnqAmVixnAfz6azNzFYj2bcdjVtT7G&x-kpsdk-v=j-0.0.0&x-kpsdk-im=CiRiYmEyYjc1Ni0wOTI5LTRjOGUtODYxYS1jODVlZjA1MjRlZWY'
    
    A, encstr = IPS(ips)
    
    def l(v, u, f):
        a = len(u)
        r = a - f
        t = []
        M = 0
        while M < len(v):
            h = 0
            l = 1
            while True:
                x = u.index(v[M])
                M += 1
                h += l * (x % f)
                if x < f:
                    t.append(int(h))
                    break
                h += f * l
                l *= r
        return t

    with open('./window.json', 'r', encoding='utf-8') as f:
        window = json.load(f)

    def L():
        r = [1, {
            'n': window,
            'T': None,
            'o': [],
            'K': [0],
            'S': None
        }, None]
        return {
            'K': r,
            'h': None
        }

    def R(v, u, a=None):
        u[0] += 1
        if a is not None and hasattr(a, 't'):
            return a.t(v[u[0]], v[u[0] + 1])
        t = ""
        M = v[u[0]]
        u[0] += 1
        for h in range(M):
            l = v[u[0]]
            u[0] += 1
            t += chr((l & 4294967232) | (l * 59 & 63))
            #print(t)
        return t
        
    bytecode = l(A, encstr, 50)

    bytelen = len(bytecode)

    bytestr = ""
    c = bytelen + len(bytestr + str(True))
    E = {
        'e': ""
    }
    for v in range(28):
        bytestr += chr(97 + random.randint(0, 25))

    o = L()

    P = bytecode[bytelen + -1] ^ c  
    O = bytecode[P:P + bytecode[P + o['K'][0]] + 2] 

    vm = R(O, o['K'][1]['K'])
    return vm

ips = 'https://api.nike.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/ips.js'
#IPS(ips)
s = time.time()
#vm = VM(ips)
while True:
    try:
        s = time.time()
        log.success(f"Decrypted Kasada VM --> {VM(ips)[:50]}... | {round(time.time()-s,2)}")
    except:
        continue
