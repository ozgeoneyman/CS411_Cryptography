#OZGE ONEYMAN 24906
#NAFIYE MELDA TOPALOGLU 25326

#PHASE 3


import math
import time
import random
import sympy
import warnings
from random import randint, seed
import sys
from ecpy.curves import Curve,Point
from Crypto.Hash import SHA3_256, HMAC, SHA256
import requests
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import random
import re
import json

API_URL = 'http://10.92.52.175:5000/'

stuID =  24906  ## Change this to your ID number

E = Curve.get_curve('secp256k1')
n = E.order
P = E.generator

#server's Identitiy public key
IKey_Ser = Point(93223115898197558905062012489877327981787036929201444813217704012422483432813 , 8985629203225767185464920094198364255740987346743912071843303975587695337619, E)
secret_key=84778574918942222088099711187884322731227739255553936013632928681338507626324
public_key=Point(38508038560074577258012458388978946423300349321004633869034054656606480408885,96057604945677386304388018751659479315743419762108708316718984156983297467990,E)

def IKRegReq(h,s,x,y):
    mes = {'ID':stuID, 'H': h, 'S': s, 'IKPUB.X': x, 'IKPUB.Y': y}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "IKRegReq"), json = mes)
    if((response.ok) == False): print(response.json())

#Send the verification code
def IKRegVerify(code):
    mes = {'ID':stuID, 'CODE': code}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "IKRegVerif"), json = mes)
    if((response.ok) == False): raise Exception(response.json())
    print(response.json())

#Send SPK Coordinates and corresponding signature
def SPKReg(h,s,x,y):
    mes = {'ID':stuID, 'H': h, 'S': s, 'SPKPUB.X': x, 'SPKPUB.Y': y}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "SPKReg"), json = mes)
    if((response.ok) == False):
        print(response.json())
    else:
        res = response.json()
        return res['SPKPUB.X'], res['SPKPUB.Y'], res['H'], res['S']

#Send OTK Coordinates and corresponding hmac
def OTKReg(keyID,x,y,hmac):
    mes = {'ID':stuID, 'KEYID': keyID, 'OTKI.X': x, 'OTKI.Y': y, 'HMACI': hmac}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "OTKReg"), json = mes)
    print(response.json())
    if((response.ok) == False): return False
    else: return True

#Send the reset code to delete your Identitiy Key
#Reset Code is sent when you first registered
def ResetIK(rcode):
    mes = {'ID':stuID, 'RCODE': rcode}
    print("Sending message is: ", mes)
    response = requests.delete('{}/{}'.format(API_URL, "ResetIK"), json = mes)
    print(response.json())
    if((response.ok) == False): return False
    else: return True

#Sign your ID  number and send the signature to delete your SPK
def ResetSPK(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.delete('{}/{}'.format(API_URL, "ResetSPK"), json = mes)
    print(response.json())
    if((response.ok) == False): return False
    else: return True

#Send the reset code to delete your Identitiy Key
#Pseudo-client will send you 5 messages to your inbox via server when you call this function
def PseudoSendMsg(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "PseudoSendMsg"), json = mes)
    print(response.json())

#get your messages. server will send 1 message from your inbox
def ReqMsg(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.get('{}/{}'.format(API_URL, "ReqMsg"), json = mes)
    print(response.json())
    if((response.ok) == True):
        res = response.json()
        return res["IDB"], res["OTKID"], res["MSGID"], res["MSG"], res["EK.X"], res["EK.Y"]
print("*******************************************************************************OTK0******************************************************")
print(secret_key)
#secret_key=26976342948598823328591013699338247285993361436327857303375628528398446733146
public_key = secret_key*P
#public_key=Point(35567389869680402551795541665043160581833719528695756461010094243531766778575,15918718625843594182129387409997771297560797564613038181669402622292924010412,E)
print("public_key on curve?", E.is_on_curve(public_key))
print(public_key)
x = public_key.x
y = public_key.y
print("X is :", x)
print("Y is :", y)
k = random.randint(0, E.order-3)
R = k*P
r = (R.x) % n
m= 24906
r = r.to_bytes((r.bit_length()+7)//8, byteorder='big')
m = m.to_bytes((m.bit_length()+7)//8, byteorder='big')
hash = r+ m
h_obj = SHA3_256.new(hash).digest()
h = (int.from_bytes(h_obj, byteorder='big'))% n
s = ( k - ( secret_key*int.from_bytes(h_obj, byteorder='big') ) ) % n
print("H:", h)
print("S:" , s)
def ResetOTK(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.delete('{}/{}'.format(API_URL, "ResetOTK"), json = mes)
    print(response.json())
h= 60544380000576951201106801399621618582580323644753107985569947872488503874552
s= 69717220902829183292447818371601392003027527259097856666632383181250481877922
ResetOTK(h,s)

def Status(stuID, h, s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.get('{}/{}'.format(API_URL, "Status"), json = mes)
    print(response.json())
    if (response.ok == True):
        res = response.json()
        return res['numMSG'], res['numOTK'], res['StatusMSG']

def status_control(h,s):

    sta = Status(stuID, h, s)

    if sta[1] in [0,1]:

        otk_id = sta[2].split(' ')[-1]

        if otk_id == 'None':
            return 0

        else:
            return int(otk_id)

    return None

statu = status_control(h,s)

def session_key(otk_pri, ekx, eky):
    ekb_pub = Point(ekx, eky, E)
    T = otk_pri * ekb_pub
    T_x = T.x
    T_y = T.y
    T_x =  T_x.to_bytes((T_x.bit_length() + 7) // 8, byteorder='big')
    T_y = T_y.to_bytes((T_y.bit_length() + 7) // 8, byteorder='big')
    U = T_x + T_y + b'MadMadWorld'
    KS = SHA3_256.new(U).digest()
    return KS
def sender_session_key(prikey, otk_pub):
    T = prikey * otk_pub
    T_x = T.x
    T_y = T.y
    T_x =  T_x.to_bytes((T_x.bit_length() + 7) // 8, byteorder='big')
    T_y = T_y.to_bytes((T_y.bit_length() + 7) // 8, byteorder='big')
    U = T_x + T_y + b'MadMadWorld'
    KS = SHA3_256.new(U).digest()
    return KS

def keyderivation_function(kdf):
    U = kdf + b'LeaveMeAlone'
    KENC = SHA3_256.new(U).digest()
    U2 = KENC + b'GlovesAndSteeringWheel'
    KHMAC = SHA3_256.new(U2).digest()
    U3 = KHMAC + b'YouWillNotHaveTheDrink'
    KKDF_next = SHA3_256.new(U3).digest()
    return KENC, KHMAC, KKDF_next

spk_secret=34917935707090290631794265147946836748957274720324623488466245132655832717242
server_spk_public= Point(85040781858568445399879179922879835942032506645887434621361669108644661638219,46354559534391251764410704735456214670494836161052287022185178295305851364841, E)


otksecret= []

def OTKS(i):
    otk_secret = random.randint(0, E.order-2)
    otksecret.append(otk_secret)
    otk_public = otk_secret*P
    print(otk_public)
    x = otk_public.x
    y = otk_public.y
    x_b = x.to_bytes(( x.bit_length() +7 ) // 8, byteorder='big')
    y_b = y.to_bytes(( y.bit_length() +7 ) // 8, byteorder='big')
    concay_key = x_b + y_b
    T = spk_secret * server_spk_public
    T_x = T.x
    T_y = T.y
    T_x = T.x.to_bytes((T.x.bit_length() + 7) // 8, byteorder='big')
    T_y = T.y.to_bytes((T.y.bit_length() + 7) // 8, byteorder='big')
    U = T_x + T_y + b'NoNeedToRideAndHide'
    Khmac = SHA3_256.new(U).digest()
    hmac = HMAC.new(key = Khmac, msg = concay_key, digestmod = SHA256).hexdigest()
    OTKReg(i, x, y, hmac)


if statu != None:

    otk0= OTKS(0)
    otk1= OTKS(1)
    otk2= OTKS(2)
    otk3= OTKS(3)
    otk4= OTKS(4)
    otk5= OTKS(5)
    otk6= OTKS(6)
    otk7= OTKS(7)
    otk8= OTKS(8)
    otk9= OTKS(9)

    OTK0_secret = otksecret[0]
    OTK1_secret = otksecret[1]
    OTK2_secret = otksecret[2]
    OTK3_secret = otksecret[3]
    OTK4_secret = otksecret[4]
    OTK5_secret = otksecret[5]
    OTK6_secret = otksecret[6]
    OTK7_secret = otksecret[7]
    OTK8_secret = otksecret[8]
    OTK9_secret = otksecret[9]

def PseudoSendMsgPH3(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "PseudoSendMsgPH3"), json = mes)
    print(response.json())


PseudoSendMsgPH3(h, s)


kenc9 = []
khmac9 = []
kdfnt9 = []
kenc8 = []
khmac8 = []
kdfnt8 = []
kenc7 = []
khmac7 = []
kdfnt7 = []
kenc6 = []
khmac6 = []
kdfnt6 = []
kenc5 = []
khmac5 = []
kdfnt5 = []
kenc4 = []
khmac4 = []
kdfnt4 = []
kenc3= []
khmac3 = []
kdfnt3 = []
kenc2 = []
khmac2 = []
kdfnt2 = []
kenc1 = []
khmac1 = []
kdfnt1 = []
kenc0 = []
khmac0 = []
kdfnt0 = []
message0= []
message1= []
message2= []
message3= []
message4= []
message5= []
message6= []
message7= []
message8= []
message9= []
KENC0= []
KENC1= []
KENC2= []
KENC3= []
KENC4= []
KENC5= []
KENC6= []
KENC7= []
KENC8= []
KENC9= []
KHMAC0 = []
KHMAC1 = []
KHMAC2 = []
KHMAC3 = []
KHMAC4 = []
KHMAC5 = []
KHMAC6 = []
KHMAC7 = []
KHMAC8 = []
KHMAC9 = []
count0 = -1
kdfnext0 = []
count1 = -1
kdfnext1 = []
count2 = -1
kdfnext2 = []
count3 = -1
kdfnext3 = []
count4 = -1
kdfnext4 = []
count5 = -1
kdfnext5 = []
count6 = -1
kdfnext6 = []
count7 = -1
kdfnext7 = []
count8 = -1
kdfnext8 = []
count9 = -1
kdfnext9 = []

while True:
    message = ReqMsg(h,s)
    print("***************************************************")
    print("***************************************************")
    print("***************************************************")

    print("***************************************************")
    if message is None:
        break
    if message[1] == 0:
        if message0 is not None:
            message0.append(message)
        else:
            message0=message
        kdf = session_key(OTK0_secret, message[4], message[5])
        if KENC0 is not None:
            KENC0.append(kdf)
        else:
            KENC0 = kdf
        if count0== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc0.append(kenc)
            khmac0.append(khmac)
            kdfnt0.append(kdfnext)
            kdfnext0.append(kdfnext)
            count0 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext0[-1])
            print(khmac)
            kenc0.append(kenc)
            khmac0.append(khmac)
            kdfnt0.append(kdfnext)
            kdfnext0.append(kdfnext)
        if KHMAC0 is not None:
            KHMAC0.append(khmac)
        else:
            KHMAC0 = khmac
    elif message[1] == 1:
        if message1 is not None:
            message1.append(message)
        else:
            message1=message
        kdf = session_key(OTK1_secret, message[4], message[5])
        if KENC1 is not None:
            KENC1.append(kdf)
        else:
            KENC1 = kdf
        if count1== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc1.append(kenc)
            khmac1.append(khmac)
            kdfnt1.append(kdfnext)
            kdfnext1.append(kdfnext)
            count1 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext1[-1])
            print(khmac)
            kenc1.append(kenc)
            khmac1.append(khmac)
            kdfnt1.append(kdfnext)
            kdfnext1.append(kdfnext)
        if KHMAC1 is not None:
            KHMAC1.append(khmac)
        else:
            KHMAC1 = khmac
    elif message[1] == 2:
        if message2 is not None:
            message2.append(message)
        else:
            message2=message
        kdf = session_key(OTK2_secret, message[4], message[5])
        if KENC2 is not None:
            KENC2.append(kdf)
        else:
            KENC2 = kdf
        if count2== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc2.append(kenc)
            khmac2.append(khmac)
            kdfnt2.append(kdfnext)
            kdfnext2.append(kdfnext)
            count2 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext2[-1])
            print(khmac)
            kenc2.append(kenc)
            khmac2.append(khmac)
            kdfnt2.append(kdfnext)
            kdfnext2.append(kdfnext)
        if KHMAC2 is not None:
            KHMAC2.append(khmac)
        else:
            KHMAC2 = khmac
    elif message[1] == 3:
        if message3 is not None:
            message3.append(message)
        else:
            message3=message
        kdf = session_key(OTK3_secret, message[4], message[5])
        if KENC3 is not None:
            KENC3.append(kdf)
        else:
            KENC9 = kdf
        if count3== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc3.append(kenc)
            khmac3.append(khmac)
            kdfnt3.append(kdfnext)
            kdfnext3.append(kdfnext)
            count3 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext3[-1])
            print(khmac)
            kenc3.append(kenc)
            khmac3.append(khmac)
            kdfnt3.append(kdfnext)
            kdfnext3.append(kdfnext)
        if KHMAC3 is not None:
            KHMAC3.append(khmac)
        else:
            KHMAC3 = khmac
    elif message[1] == 4:
        if message4 is not None:
            message4.append(message)
        else:
            message4=message
        kdf = session_key(OTK4_secret, message[4], message[5])
        if KENC4 is not None:
            KENC4.append(kdf)
        else:
            KENC4 = kdf
        if count4== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc4.append(kenc)
            khmac4.append(khmac)
            kdfnt4.append(kdfnext)
            kdfnext4.append(kdfnext)
            count4 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext4[-1])
            print(khmac)
            kenc4.append(kenc)
            khmac4.append(khmac)
            kdfnt4.append(kdfnext)
            kdfnext4.append(kdfnext)
        if KHMAC4 is not None:
            KHMAC4.append(khmac)
        else:
            KHMAC4 = khmac
    elif message[1] == 5:
        if message5 is not None:
            message5.append(message)
        else:
            message5=message
        kdf = session_key(OTK5_secret, message[4], message[5])
        if KENC5 is not None:
            KENC5.append(kdf)
        else:
            KENC5 = kdf
        if count5== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc5.append(kenc)
            khmac5.append(khmac)
            kdfnt5.append(kdfnext)
            kdfnext5.append(kdfnext)
            count5 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext5[-1])
            print(khmac)
            kenc5.append(kenc)
            khmac5.append(khmac)
            kdfnt5.append(kdfnext)
            kdfnext5.append(kdfnext)
        if KHMAC5 is not None:
            KHMAC5.append(khmac)
        else:
            KHMAC5 = khmac
    elif message[1] == 6:
        if message6 is not None:
            message6.append(message)
        else:
            message6=message
        kdf = session_key(OTK6_secret, message[4], message[5])
        if KENC6 is not None:
            KENC6.append(kdf)
        else:
            KENC6 = kdf
        if count6== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc6.append(kenc)
            khmac6.append(khmac)
            kdfnt6.append(kdfnext)
            kdfnext6.append(kdfnext)
            count6 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext6[-1])
            print(khmac)
            kenc6.append(kenc)
            khmac6.append(khmac)
            kdfnt6.append(kdfnext)
            kdfnext6.append(kdfnext)
        if KHMAC6 is not None:
            KHMAC6.append(khmac)
        else:
            KHMAC6 = khmac
    elif message[1] == 7:
        if message7 is not None:
            message7.append(message)
        else:
            message7=message
        kdf = session_key(OTK7_secret, message[4], message[5])
        if KENC7 is not None:
            KENC7.append(kdf)
        else:
            KENC7 = kdf
        if count7== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc7.append(kenc)
            khmac7.append(khmac)
            kdfnt7.append(kdfnext)
            kdfnext7.append(kdfnext)
            count7 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext7[-1])
            print(khmac)
            kenc7.append(kenc)
            khmac7.append(khmac)
            kdfnt7.append(kdfnext)
            kdfnext7.append(kdfnext)
        if KHMAC7 is not None:
            KHMAC7.append(khmac)
        else:
            KHMAC7 = khmac
    elif message[1] == 8:
        if message8 is not None:
            message8.append(message)
        else:
            message8=message
        kdf = session_key(OTK8_secret, message[4], message[5])
        if KENC8 is not None:
            KENC8.append(kdf)
        else:
            KENC8 = kdf
        if count8== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc8.append(kenc)
            khmac8.append(khmac)
            kdfnt8.append(kdfnext)
            kdfnext8.append(kdfnext)
            count8 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext8[-1])
            print(khmac)
            kenc8.append(kenc)
            khmac8.append(khmac)
            kdfnt8.append(kdfnext)
            kdfnext8.append(kdfnext)
        if KHMAC8 is not None:
            KHMAC8.append(khmac)
        else:
            KHMAC8 = khmac
    elif message[1] == 9:

        if message9 is not None:
            message9.append(message)
        else:
            message9=message
        kdf = session_key(OTK9_secret, message[4], message[5])
        if KENC9 is not None:
            KENC9.append(kdf)
        else:
            KENC9 = kdf
        if count9== -1:
            kenc, khmac ,kdfnext = keyderivation_function(kdf)
            print(khmac)
            kenc9.append(kenc)
            khmac9.append(khmac)
            kdfnt9.append(kdfnext)
            kdfnext9.append(kdfnext)
            count9 += 1
        else:
            kenc, khmac ,kdfnext = keyderivation_function(kdfnext9[-1])
            print(khmac)
            kenc9.append(kenc)
            khmac9.append(khmac)
            kdfnt9.append(kdfnext)
            kdfnext9.append(kdfnext)
        if KHMAC9 is not None:
            KHMAC9.append(khmac)
        else:
            KHMAC9 = khmac

def ctext_mess(key, mes):
    cipher = AES.new(key, AES.MODE_CTR)
    ctext= cipher.encrypt(mes)
    non = cipher.nonce
    return ctext, non


dtext_list_9=[]
dtext_list_8=[]
dtext_list_7=[]
dtext_list_6=[]
dtext_list_5=[]
dtext_list_4=[]
dtext_list_3=[]
dtext_list_2=[]
dtext_list_1=[]
dtext_list_0=[]
PseudoSendMsg(h, s)
i=0

for i in range(5):
    if  message9:
        mes=message9[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac9[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message9[i][2], " has valid MAC values")
            key = kenc9[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_9.append(dtext)
        else:
            print("Mesage id ", message9[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message9[i][0], message9[i][2], dtext)
    elif message8:
        mes=message8[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac8[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message8[i][2], " has valid MAC values")
            key = kenc8[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_8.append(dtext)
        else:
            print("Mesage id ", message8[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message8[i][0], message8[i][2], dtext)
    elif message7:
        mes=message7[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac7[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message7[i][2], " has valid MAC values")
            key = kenc7[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_7.append(dtext)
        else:
            print("Mesage id ", message7[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message7[i][0], message7[i][2], dtext)
    elif message6:
        mes=message6[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac6[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message6[i][2], " has valid MAC values")
            key = kenc6[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_6.append(dtext)
        else:
            print("Mesage id ", message6[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message6[i][0], message6[i][2], dtext)
    elif message5:
        mes=message5[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac5[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message5[i][2], " has valid MAC values")
            key = kenc5[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_5.append(dtext)
        else:
            print("Mesage id ", message5[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message5[i][0], message5[i][2], dtext)
    elif message4:
        mes=message4[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac4[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message4[i][2], " has valid MAC values")
            key = kenc4[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_4.append(dtext)
        else:
            print("Mesage id ", message4[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message4[i][0], message4[i][2], dtext)
    elif message3:
        mes=message3[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac3[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message3[i][2], " has valid MAC values")
            key = kenc3[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_3.append(dtext)
        else:
            print("Mesage id ", message3[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message3[i][0], message3[i][2], dtext)
    elif message2:
        mes=message2[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac2[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message2[i][2], " has valid MAC values")
            key = kenc2[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_2.append(dtext)
        else:
            print("Mesage id ", message2[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message2[i][0], message2[i][2], dtext)
    elif message1:
        mes=message1[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac1[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message1[i][2], " has valid MAC values")
            key = kenc1[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_1.append(dtext)
        else:
            print("Mesage id ", message1[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message1[i][0], message1[i][2], dtext)
    elif message0:
        mes=message0[i][3]
        mes= mes.to_bytes((mes.bit_length() + 7) // 8, byteorder='big')
        nonce= mes[:8]
        ciphertext = mes[8:-32]
        MACv = mes[-32:]
        MAC_val = HMAC.new(key = khmac0[i], msg = ciphertext, digestmod = SHA256).digest()
        if MACv == MAC_val:
            print("Mesage id ", message0[i][2], " has valid MAC values")
            key = kenc0[i]
            cipher = AES.new(key, AES.MODE_CTR, nonce=mes[:8])
            dtext = cipher.decrypt(ciphertext).decode('utf-8')
            print("dtext: ", dtext)
            dtext_list_0.append(dtext)
        else:
            print("Mesage id ", message0[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        #Checker(stuID, message0[i][0], message0[i][2], dtext)



def SendMsg(idA, idB, otkid, msgid, msg, ekx, eky):
    mes = {"IDA":idA, "IDB":idB, "OTKID": int(otkid), "MSGID": msgid, "MSG": msg, "EK.X": ekx, "EK.Y": eky}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "SendMSG"), json = mes)
    print(response.json())

def reqOTKB(stuID, stuIDB, h, s):
    OTK_request_msg = {'IDA': stuID, 'IDB':stuIDB, 'S': s, 'H': h}
    print("Requesting party B's OTK ...")
    response = requests.get('{}/{}'.format(API_URL, "ReqOTK"), json = OTK_request_msg)
    print(response.json())
    if((response.ok) == True):
        print(response.json())
        res = response.json()
        return res['KEYID'], res['OTK.X'], res['OTK.Y']
    else:
        return -1, 0, 0
print("************************************************************************************************************************************")
print("************************************************************************************************************************************")
print("************************************************************************************************************************************")

print("************************************************************************************************************************************")
print("************************************************************************************************************************************")
stuIDB = 18007
def sending_mes(n, P, stuIDB):
    stuIDB_b =  stuIDB.to_bytes((stuIDB.bit_length() + 7) // 8, byteorder='big')
    k = random.randint(0, E.order-3)
    R = k*P
    r = (R.x) % n
    m= 24906
    r = r.to_bytes((r.bit_length()+7)//8, byteorder='big')
    m = m.to_bytes((m.bit_length()+7)//8, byteorder='big')
    hash = r+ stuIDB_b
    h_obj = SHA3_256.new(hash).digest()
    h = (int.from_bytes(h_obj, byteorder='big'))% n
    s = ( k - (secret_key*int.from_bytes(h_obj, byteorder='big') ) ) % n
    key_id, otk_x, otk_y = reqOTKB(stuID, stuIDB, h, s)
    s_key = random.randint(0, E.order-2)
    public_key = s_key * P
    print("Private key is :", s_key)
    print("Secret key is :", public_key)
    ks= session_key(s_key, otk_x, otk_y)

    if dtext_list_0:
        for i in range(len(dtext_list_0)):
            mes = dtext_list_0[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)
    elif dtext_list_1:
        for i in range(len(dtext_list_1)):
            mes = dtext_list_1[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)
    elif dtext_list_2:
        for i in range(len(dtext_list_2)):
            mes = dtext_list_2[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_3:
        for i in range(len(dtext_list_3)):
            mes = dtext_list_3[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_4:
        for i in range(len(dtext_list_4)):
            mes = dtext_list_4[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_5:
        for i in range(len(dtext_list_5)):
            mes = dtext_list_5[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_6:
        for i in range(len(dtext_list_6)):
            mes = dtext_list_6[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)
    elif dtext_list_7:
        for i in range(len(dtext_list_7)):
            mes = dtext_list_7[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_8:
        for i in range(len(dtext_list_8)):
            mes = dtext_list_8[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

    elif dtext_list_9:
        for i in range(len(dtext_list_9)):
            mes = dtext_list_9[i].encode()
            K_enc, khmca, kkdf_next = keyderivation_function(ks)
            mac = HMAC.new(khmca, mes, digestmod = SHA256).digest()
            ctext , nonce = ctext_mess(K_enc, mes)
            m = int.from_bytes(nonce+ctext+mac,byteorder='big')
            SendMsg(stuID, stuIDB,key_id,i,m, public_key.x, public_key.y)

sending_mes(n, P, stuIDB)


'''
Our output is this:


84778574918942222088099711187884322731227739255553936013632928681338507626324
public_key on curve? True
(0x5522c706c784cd75c4a8d8ad53420dafaf616607180eade3b91f9690c74ca135 , 0xd45ead7ed91c71ffd0577ca57260ee8c3554ce0434ce154f5342f421cca26656)
X is : 38508038560074577258012458388978946423300349321004633869034054656606480408885
Y is : 96057604945677386304388018751659479315743419762108708316718984156983297467990
H: 36627351035481154190710303935138079671274177603471192912959924464643423039404
S: 59323167148295896139649525723342566532482245715253304716680814384154998203043
Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
All OTKs deleted !
Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'numMSG': 5, 'numOTK': 0, 'StatusMSG': 'You have 5 unread messages in your mailbox.\n You have 0 OTKs left. The largest key id is None'}
(0x6c9ac58c0a929aa5b90dad63c4d8c6c7ae3e25f94d792a8e96d64741a70761ae , 0x887f99fafba16404a7373e21e1ce2d6749269ddfd9153cfb9a11df09b7e54012)
Sending message is:  {'ID': 24906, 'KEYID': 0, 'OTKI.X': 49123245514504924614976427953151154711316380158830014797207686651422708294062, 'OTKI.Y': 61739999718228586862801575282896985650753737096935132269690618886753897234450, 'HMACI': '092be1399b0201601318a7d21787f39629691fbee6a21f05a311535ac8cd54ba'}
OTK with ID number0 is registered successfully
(0x1e188a4f9b2606f6f847ef0a5588d3ddcf02016b1225007d6d441c74d8df4726 , 0x5a9e2b65fe68ecf2e7f350d87c924d9b2b72f681e9cc93c6e3e05dc19b3cee7a)
Sending message is:  {'ID': 24906, 'KEYID': 1, 'OTKI.X': 13612744374223365371616973766107467775663145955878168258565913595472720643878, 'OTKI.Y': 40987617733568971018559164784770096045680980794494262678347600504482357374586, 'HMACI': 'e769fcaba5a0d2cd6f62cde12cb9fe0558b8b88a07d9e5d269d0ab6b369480b4'}
OTK with ID number1 is registered successfully
(0x62865792c6af3d5c71127adef8955f1bab9c9f78247abbd04c410b3626bc74f , 0xe96e5b12bd7c864dfd94874c68aa86a16135d738e5c1b2a13aac9eb29e3f4a32)
Sending message is:  {'ID': 24906, 'KEYID': 2, 'OTKI.X': 2785251317303044807627284597516016370146553470463279485483588825800956954447, 'OTKI.Y': 105583875461178538303141663073216092218175755260465491169909297162177617021490, 'HMACI': '9bcf9373621e4f219fe90576b885a54a3e8558f92437d425c316e59b63de3951'}
OTK with ID number2 is registered successfully
(0x2bc66b6dd927d9b6b1b883285e4cbe0fd2ec8df4f6feaae24484fb12cd3fb5c8 , 0x9a876adca2b37afb65842bf97dcf24151b56c748ca52d5796413f9b061226331)
Sending message is:  {'ID': 24906, 'KEYID': 3, 'OTKI.X': 19800029656269028920912036386901454132949870580123575760960354354924181501384, 'OTKI.Y': 69895440569003557470617384472167071930464939953285855551313404938026313999153, 'HMACI': 'ec7c7dcbedfced169163e4f6a5465a74e524b9c301d2dfb074b980f4f9a2ffeb'}
OTK with ID number3 is registered successfully
(0x9229efd88f9f397c8018e782c02f39b4da29ed896ab78a20ed2820b500c5d248 , 0x5e18251d3497a442cfe2a0bab3d69ac06e2e8e2fb5829f98ff24aeb868ba480d)
Sending message is:  {'ID': 24906, 'KEYID': 4, 'OTKI.X': 66111771978663328401028904957854040361750408899100546036594349777173923353160, 'OTKI.Y': 42560068248373627250260313442350589188462397670626042811055422482833045342221, 'HMACI': '8a741a29baa0dd2f21f09ba00307098928a855f704a56b51db4972dc707c8f4a'}
OTK with ID number4 is registered successfully
(0x4e140c6e31572109482a3c27ea15421403547a1557a504cc76445d9613ca3d6 , 0xdddcc3b95aec635338c45e014b72c1bdfaf94d55e71f8e1c3672724cd88acfd9)
Sending message is:  {'ID': 24906, 'KEYID': 5, 'OTKI.X': 2207239057658549122259166986933618998763444616417102465136919811196930794454, 'OTKI.Y': 100351196728856224594129724525876362263316833827538275486915680879991421849561, 'HMACI': 'e81abe8305fa7f37db8308c45500587f11f297cd7cd2ec4c861bee4cfb3da589'}
OTK with ID number5 is registered successfully
(0x5f1ba4ffaa64aec8af898269b07945ac0bfe2a661523dbf903b67504918b8a69 , 0x3f7d61cb33bc8ddfe84583163750b2dc3b2469bd80d46a5dc1150c5bbc6663dd)
Sending message is:  {'ID': 24906, 'KEYID': 6, 'OTKI.X': 43018564265291105112770789522714935835454878284524109496979130591988199164521, 'OTKI.Y': 28717240291556386198028315862833026160988266617376337889601119295326778713053, 'HMACI': '98a2b9aa1c8cb0119d0d5a29544fe829f31a68dc98bb36ed47eb162d38611687'}
OTK with ID number6 is registered successfully
(0x5880df7f04daa434b736f4ad00d22544d6874d58da996438ae4ee8dca366f75d , 0x1f28b6430fdc7f37f6657831a3d5c8477305d959b97c916ac8dc300286f5dd18)
Sending message is:  {'ID': 24906, 'KEYID': 7, 'OTKI.X': 40031229613478829428684233900889961106191634823586179065370032246050932586333, 'OTKI.Y': 14093630114494327552553422001831259397247899195288582927122633072019741465880, 'HMACI': '77da7a0826772405d71a4b7d7c7530e0a8710a58d3cce0b87e53db9578740b7b'}
OTK with ID number7 is registered successfully
(0xe3fd969d01a4b816654bd397601abb0c404df3b884c1a88d3e2f1565ca50b61c , 0x34a483e5398f42ca3fd1b0a7fce9c315db21a65bce3c8749328b073ff58b323a)
Sending message is:  {'ID': 24906, 'KEYID': 8, 'OTKI.X': 103123068430627120519046605606700031461441458217173103099733155433773811152412, 'OTKI.Y': 23810941353614458307299488274159851327766083161450002635292397358736988647994, 'HMACI': 'f30d2fd26fb2a1d2df1319036d804dd30d1a925d9c1a82b079fafa4507eb5857'}
OTK with ID number8 is registered successfully
(0x97c4e7ad92528f96bb7cdf1275bcea81cd48d1bc07718718f4f798eab5f94916 , 0x25e774cd253bef4ec7f7569879b49bd2ee1ef82387c66a344210fd81e46b6a56)
Sending message is:  {'ID': 24906, 'KEYID': 9, 'OTKI.X': 68647141143656228175603066690130508620341368797058445658066438241337405425942, 'OTKI.Y': 17144523202831168157894009045200581488226348430998843429757718502865908755030, 'HMACI': 'ba387e1553a53c3744ee459a728eea4688bb20f145bc069aecc0fbee0520d671'}
OTK with ID number9 is registered successfully
Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
Your favourite pseudo-client sent you 5 messages. You can get them from the server
Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'IDB': 18007, 'OTKID': 0, 'MSGID': 1, 'MSG': 67612769709376195479855454213340345580890970265974287169887063067903107302851307739744574133938908650482684470661270971851222766602046689751031192797133469045640694900978427738472035971149647354099648, 'EK.X': 1333154322861904044693705593708683087772711965179226054132448957281465259446, 'EK.Y': 83746079878250496690946644121453460800191679902320794852157235161027026950020}

Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'IDB': 18007, 'OTKID': 0, 'MSGID': 2, 'MSG': 69546088758633927679390088422924948709673638415186843240226992926208756089285799715751327902446728091673582096116726745258951507763354351269662050269111212792325785224004780685113146560404801791948393, 'EK.X': 1333154322861904044693705593708683087772711965179226054132448957281465259446, 'EK.Y': 83746079878250496690946644121453460800191679902320794852157235161027026950020}

Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'IDB': 18007, 'OTKID': 0, 'MSGID': 3, 'MSG': 56642875108455479206559106275898727198675874004165524097135291682183029992089439726390035703520808699600312222965823150654737272824538480279517279442109763855359230448141001932361065076711239775752749, 'EK.X': 1333154322861904044693705593708683087772711965179226054132448957281465259446, 'EK.Y': 83746079878250496690946644121453460800191679902320794852157235161027026950020}

Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'IDB': 18007, 'OTKID': 0, 'MSGID': 4, 'MSG': 31070799908661308076866518325908169312960488024983540734613003856639512112544855012238967504131640988057124626145676518505295347944067276889533729260514151572914362141546532592513361292080537146935721, 'EK.X': 1333154322861904044693705593708683087772711965179226054132448957281465259446, 'EK.Y': 83746079878250496690946644121453460800191679902320794852157235161027026950020}

Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
{'IDB': 18007, 'OTKID': 0, 'MSGID': 5, 'MSG': 23025780686586794623754152288011283633979563641135727575461615076368443200737323513009577433847663299124374186073128776644096867888475618607626395719877767074131559190808532074901860993669989209955035, 'EK.X': 1333154322861904044693705593708683087772711965179226054132448957281465259446, 'EK.Y': 83746079878250496690946644121453460800191679902320794852157235161027026950020}

Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
There is no message in your message box. Pseudo client will send you messages if you call this method: PseudoSendMsg
***************************************************
***************************************************
***************************************************
***************************************************
Sending message is:  {'ID': 24906, 'H': 60544380000576951201106801399621618582580323644753107985569947872488503874552, 'S': 69717220902829183292447818371601392003027527259097856666632383181250481877922}
Your favourite pseudo-client sent you 5 messages. You can get them from the server
Mesage id  1  has valid MAC values
dtext:  https://www.youtube.com/watch?v=KsEjdfXudfM
Mesage id  2  has valid MAC values
dtext:  https://www.youtube.com/watch?v=mJXUNMexT1c
Mesage id  3  has valid MAC values
dtext:  https://www.youtube.com/watch?v=1hLIXrlpRe8
Mesage id  4  has valid MAC values
dtext:  https://www.youtube.com/watch?v=mJXUNMexT1c
Mesage id  5  has valid MAC values
dtext:  https://www.youtube.com/watch?v=CvjoXdC-WkM
************************************************************************************************************************************
************************************************************************************************************************************
************************************************************************************************************************************
************************************************************************************************************************************
************************************************************************************************************************************
Requesting party B's OTK ...
{'KEYID': 999, 'OTK.X': 30568881089037169074576707248814156158979475758222264003724744315000739721181, 'OTK.Y': 85993894123958406896957852312206763898726822265659964875343422367626452147261}
{'KEYID': 999, 'OTK.X': 30568881089037169074576707248814156158979475758222264003724744315000739721181, 'OTK.Y': 85993894123958406896957852312206763898726822265659964875343422367626452147261}
Private key is : 110013247578032698061023901121757702047793874380449191520720356262982376954662
Secret key is : (0x2c7523840c7bd4b8b7e99a038d4f69bd45160b8e7856ec331f58c50ea0934ca5 , 0x6d8cf41864d151a9aaf3946e163caeb45784e91183a1c37a8ba97db26cd12db7)
Sending message is:  {'IDA': 24906, 'IDB': 18007, 'OTKID': 999, 'MSGID': 0, 'MSG': 21083400786934113073577130248762934629438862906358715188523291701101507332618374288211935075801638414987093609652402328420261656773662223791098359485122190733399217789682946394994970975459804062407810, 'EK.X': 20108731565392578384126459045116259685465699064219222877275620983946930769061, 'EK.Y': 49551143768409685054992732388777217177876104231822909771732458423836614929847}
Your message sent succesfully
Sending message is:  {'IDA': 24906, 'IDB': 18007, 'OTKID': 999, 'MSGID': 1, 'MSG': 26878485612019110265589393713610858034571015783663754581517882982245510353870361465534489209556896626114166438901975170574243971132280669376447413026302843528755919264694320775560512262413987284913912, 'EK.X': 20108731565392578384126459045116259685465699064219222877275620983946930769061, 'EK.Y': 49551143768409685054992732388777217177876104231822909771732458423836614929847}
Your message sent succesfully
Sending message is:  {'IDA': 24906, 'IDB': 18007, 'OTKID': 999, 'MSGID': 2, 'MSG': 72984253420341783800689967314832594901627141413114925745453284203071278067881751061199401429948975623937144177972604844440901712892841520969340992112869889752200593837398489532014308240854716236371177, 'EK.X': 20108731565392578384126459045116259685465699064219222877275620983946930769061, 'EK.Y': 49551143768409685054992732388777217177876104231822909771732458423836614929847}
Your message sent succesfully
Sending message is:  {'IDA': 24906, 'IDB': 18007, 'OTKID': 999, 'MSGID': 3, 'MSG': 134788731905689033522420490405354211418162613776938525962761646867296809140299978056002279285874267172948068847709295558362834726878021004011410360500998886339470942042935823575926136457434412486392, 'EK.X': 20108731565392578384126459045116259685465699064219222877275620983946930769061, 'EK.Y': 49551143768409685054992732388777217177876104231822909771732458423836614929847}
Your message sent succesfully
Sending message is:  {'IDA': 24906, 'IDB': 18007, 'OTKID': 999, 'MSGID': 4, 'MSG': 53131105634120999026108140459826848823003704812171273254496060256985299494449733335541105056572661115593417920711858865168207927621598926902820725495287041023830810920530881256399061245376818424802345, 'EK.X': 20108731565392578384126459045116259685465699064219222877275620983946930769061, 'EK.Y': 49551143768409685054992732388777217177876104231822909771732458423836614929847}
Your message sent succesfully


'''
