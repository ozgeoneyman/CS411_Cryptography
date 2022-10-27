#OZGE ONEYMAN 24906
#NAFIYE MELDA TOPALOGLU 25326

#PHASE 2



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

stuID =  25326  ## Change this to your ID number

E = Curve.get_curve('secp256k1')
n = E.order
P = E.generator

#server's Identitiy public key
IKey_Ser = Point(93223115898197558905062012489877327981787036929201444813217704012422483432813 , 8985629203225767185464920094198364255740987346743912071843303975587695337619, E)
secret_key=4041932665413802062402047183420134136173319527554937338484617913195876001949
public_key=Point(75746073423283178053213843073264790490783040943182323972802513593726551668549,16532552681082346629362061922838076487181662827517293421201539768254727589613,E)
OTK0_secret=21700456348422869021557260253991863847343754934196646713206152298822217731574
OTK0={'ID': 25326, 'KEYID': 0, 'OTKI.X': 21226054786462071292368899721842385554168497098536087869724309023882655209214, 'OTKI.Y': 39800202799940087235378724058843820486913472922832637393759196985087290525958, 'HMACI': '52673a9f249b7244a2c356b0f029a5ae30621ab12e1587392065ee61b7298e4d'}
OTK1_secret=74280941608170582286279902407276481280603930881521594296615074018990357883768
OTK1={'ID': 25326, 'KEYID': 1, 'OTKI.X': 25807938685898806371968276602939787934583297430773158269725079116064342365967, 'OTKI.Y': 77587582592356044457426710051988345921893507635501171249285325798727060836213, 'HMACI': '0efe1be99d8d87997296e0b215902c51f3ef53aa871a531cb663a256fed47301'}
OTK2_secret=82723063985980724904986341598127137504293740456629899880916043081991371638783
OTK2={'ID': 25326, 'KEYID': 2, 'OTKI.X': 76634866717860072803061759292266913345819474353456010787776658039641573605375, 'OTKI.Y': 60235969095565046057691176593539273403001378639467722031963597234893683871532, 'HMACI': 'cb7b1cb0e81f7e8552aeaa326d636a3f87969470c734252429b7f0b567da4c93'}
OTK3_secret =46806028129489886661726426982858229522420097359532622035988690861309766912505
OTK3={'ID': 25326, 'KEYID': 3, 'OTKI.X': 11717953431503521051342080642774407893627809858930777314966843844258639581771, 'OTKI.Y': 59423474558139778862149846842558075351473261435067742465928333753195343739504, 'HMACI': 'a3fa1e52c3945d07fc42df4d3295b99ea65912cd5d9feab5e7e2058eafba2488'}
OTK4_secret=88493315325371394041667843726071483261549110295922590902683989563314355407876
OTK4={'ID': 25326, 'KEYID': 4, 'OTKI.X': 58191397061058971225769191685360669664605540383981017563319286023379835763380, 'OTKI.Y': 102582279692875395584473110633175565965372894607996806566257970162124547187700, 'HMACI': '4ef8586227aceb91c1ad92844c78af8bff577f2ebac7d1ea90566e6492ee23e7'}
OTK5_secret=51806995054881847584645113131437952989078603907386534310917943201022281202209
OTK5={'ID': 25326, 'KEYID': 5, 'OTKI.X': 13796485109516207099037848897194992150573054071941381281199533175818358057101, 'OTKI.Y': 44334804387346481776809158764376369689607775707134786372393497826588698114095, 'HMACI': '7573222a963138ef3af86c1245d2c6abccd6dedf1b8d8625944d7562a41f6c86'}
OTK6_secret=56018815435900294016628125368396870048999290192435898392354091698352057440285
OTK6={'ID': 25326, 'KEYID': 6, 'OTKI.X': 22814852735601733832730588705954398308581993104976922306461862819424342890525, 'OTKI.Y': 75441792863853227222828278689886996051434528449288303547822870418070881218237, 'HMACI': '160e31965fa32163bda11dbd47654c41619e0a151347517c9d1243f80d9236f7'}
OTK7_secret=74832513564357126090061996224736391621686012917458298793951445511967308995707
OTK7={'ID': 25326, 'KEYID': 7, 'OTKI.X': 47795942045601932888906668764491819097927424544754425382566618674382662270732, 'OTKI.Y': 34467282403340983755022281171396362828500529894279977673532624511842664052991, 'HMACI': '0f87f7dc860652b9c5e33c122ff7cda0a9eeb633e9a57e8f01d03761093af78e'}
OTK8_secret=65219042917690236949080395998067071222205272840457049855946595079968078963444
OTK8={'ID': 25326, 'KEYID': 8, 'OTKI.X': 107761381049227624889443737580148628835698377352269477771351352973085072636250, 'OTKI.Y': 113175378980961196072855850947646656071720465216676587244078299055099363505878, 'HMACI': 'b59ac4cd7837e667f41ae83070c80d578b621b6fe0bc7fcacac8312e26a2afde'}
OTK9_secret=107912191168760313712165630922636744732292264213796384399406927305132207670501
OTK9={'ID': 25326, 'KEYID': 9, 'OTKI.X': 22327967552573596773246116391749827601180476636079711452091582381209209918360, 'OTKI.Y': 7381018668732137170727782790318153841760557036990048504184216404849374337616, 'HMACI': '7a39f7eebfeace129dcfdeb876e0bac59a0cb4766e4f05d11e9ee2c31a9778f0'}


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
def ResetOTK(h,s):
    mes = {'ID':stuID, 'H': h, 'S': s}
    print("Sending message is: ", mes)
    response = requests.delete('{}/{}'.format(API_URL, "ResetOTK"), json = mes)		
    if((response.ok) == False): print(response.json())

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
m= 25326
r = r.to_bytes((r.bit_length()+7)//8, byteorder='big')
m = m.to_bytes((m.bit_length()+7)//8, byteorder='big')
hash = r+ m
h_obj = SHA3_256.new(hash).digest()
h = (int.from_bytes(h_obj, byteorder='big'))% n
s = ( k - ( secret_key*int.from_bytes(h_obj, byteorder='big') ) ) % n
print("H:", h)
print("S:" , s)

PseudoSendMsg(h, s)
#message = ReqMsg(h,s)

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

def keyderivation_function(kdf):
    U = kdf + b'LeaveMeAlone'
    KENC = SHA3_256.new(U).digest() 
    U2 = KENC + b'GlovesAndSteeringWheel'
    KHMAC = SHA3_256.new(U2).digest() 
    U3 = KHMAC + b'YouWillNotHaveTheDrink'
    KKDF_next = SHA3_256.new(U3).digest() 
    return KENC, KHMAC, KKDF_next
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
  



def Checker(stuID, stuIDB, msgID, decmsg):
    mes = {'IDA':stuID, 'IDB':stuIDB, 'MSGID': msgID, 'DECMSG': decmsg}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "Checker"), json = mes)		
    print(response.json())

for i in range(5):
    if message9 is not None:
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
                     
        else:
            print("Mesage id ", message9[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message9[i][0], message9[i][2], dtext) 
    elif message8 is not None:
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
                     
        else:
            print("Mesage id ", message8[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message8[i][0], message8[i][2], dtext) 

    elif message7 is not None:
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
                     
        else:
            print("Mesage id ", message7[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message7[i][0], message7[i][2], dtext) 

    elif message6 is not None:
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
                     
        else:
            print("Mesage id ", message6[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message6[i][0], message6[i][2], dtext) 
    elif message5 is not None:
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
                     
        else:
            print("Mesage id ", message5[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message5[i][0], message5[i][2], dtext) 
    elif message4 is not None:
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
                     
        else:
            print("Mesage id ", message4[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message4[i][0], message4[i][2], dtext) 
    elif message3 is not None:
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
                     
        else:
            print("Mesage id ", message3[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message3[i][0], message3[i][2], dtext)     
    elif message2 is not None:
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
                     
        else:
            print("Mesage id ", message2[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message2[i][0], message2[i][2], dtext)  

    elif message1 is not None:
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
                     
        else:
            print("Mesage id ", message1[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message1[i][0], message1[i][2], dtext)  

    elif message0 is not None:
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
                     
        else:
            print("Mesage id ", message0[i][2], " has invalid MAC values")
            dtext = "invalid MAC VALUES"
        Checker(stuID, message0[i][0], message0[i][2], dtext)                           





'''
THE RESULT IS LIKE BELOW FOR OTK9:


Mesage id  1  has valid MAC values
dtext:  https://www.youtube.com/watch?v=s3Nr-FoA9Ps
Sending message is:  {'IDA': 25326, 'IDB': 18007, 'MSGID': 1, 'DECMSG': 'https://www.youtube.com/watch?v=s3Nr-FoA9Ps'}
You decrypted it correctly, wow!
Mesage id  2  has valid MAC values
dtext:  https://www.youtube.com/watch?v=mJXUNMexT1c
Sending message is:  {'IDA': 25326, 'IDB': 18007, 'MSGID': 2, 'DECMSG': 'https://www.youtube.com/watch?v=mJXUNMexT1c'}
You decrypted it correctly, wow!
Mesage id  3  has valid MAC values
dtext:  https://www.youtube.com/watch?v=KsEjdfXudfM
Sending message is:  {'IDA': 25326, 'IDB': 18007, 'MSGID': 3, 'DECMSG': 'https://www.youtube.com/watch?v=KsEjdfXudfM'}
You decrypted it correctly, wow!
Mesage id  4  has valid MAC values
dtext:  https://www.youtube.com/watch?v=CvjoXdC-WkM
Sending message is:  {'IDA': 25326, 'IDB': 18007, 'MSGID': 4, 'DECMSG': 'https://www.youtube.com/watch?v=CvjoXdC-WkM'}
You decrypted it correctly, wow!
Mesage id  5  has invalid MAC values
Sending message is:  {'IDA': 25326, 'IDB': 18007, 'MSGID': 5, 'DECMSG': 'invalid MAC VALUES'}
Pseudo-client says she didn't send you that message. Who are you talking to behind her back!!1!
'''




