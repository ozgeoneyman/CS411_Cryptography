

from Crypto.Hash import SHAKE128

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    if a < 0:
        a = a+m
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


q = 1274928665248456750459255476142268320222010991943
p = 94399082877738640356344835093633851742226810946548058167594106609599304101483376198601628644645578978665867743371516213549559017509270013785262825124888169738692088560919995075509146379802866347021353299579995280712578946802331952341703103059527013530389111994085951544456654086033481582042901134498773988127
g = 74757613048887093209741634228228425902948572222965683892966782829654298800791789084861356704346371244921201938818880899647348974925451953450279300514594642896343751389085838466583384452902564477981127117505259585303938871436241327714244689153971542398500058515599232922200606171788427214873986464441516423273
publickeybeta =9391078822012222264248483853957955450074521847096866533459681369546944886235023857738438187102424298184377435789154539420500484576343932422250732759800837979336463896251863203597988162906413924736488554239908614170057127399588501615428907239954984946982024571938034476806841633488050802767414373595444261997

(message1, r1, s1) = ( b'Erkay hoca wish that you did learn a lot in the Cryptography course',780456265196245442017019073827244628033034896446,214154189471546244965139202160125045302874348377)
(message2, r2, s2) = ( b'Who will win the 2021 F1 championship, Max or Lewis?',927294142715241205623350780659879368622965215767,151110642214296558517943730901561426792280910589)

shake1 = SHAKE128.new(message1)
h1 = int.from_bytes(shake1.read( q.bit_length() // 8), byteorder='big')

shake2 = SHAKE128.new(message2)
h2 = int.from_bytes(shake2.read( q.bit_length() // 8), byteorder='big')

for i in range(1000):
    
  a = (( s2 * r1 * i - s1 * r2) % q)
  b = modinv(a,q)
  key = ((( s1 * h2 - s2 * h1 * i) * b) % q)

  if  pow(g,key,p) == publickeybeta:

    print('Private key:', key)    ## The private key is: 66568624500090235129890566130399211243633217014

    break