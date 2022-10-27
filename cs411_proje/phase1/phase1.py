#CS 411 PROJECT PHASE 1
#Ozge Oneyman 24906
#Nafiye Melda Topaloglu 25326

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

curve = E
#*****************************************************************Identity Key 2.1***********************************************************************************
secret_key = random.randint(0, E.order-2)
print(secret_key)
secret_key=26976342948598823328591013699338247285993361436327857303375628528398446733146
public_key = secret_key*P 
public_key=Point(35567389869680402551795541665043160581833719528695756461010094243531766778575,15918718625843594182129387409997771297560797564613038181669402622292924010412,E)
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
print(r + m)
print(m)
print(hash)

h_obj = SHA3_256.new(hash).digest()


h = (int.from_bytes(h_obj, byteorder='big'))% n

print("H:", h)

s = ( k - ( secret_key*int.from_bytes(h_obj, byteorder='big') ) ) % n

print("S:" , s)

#server's Identitiy public key
IKey_Ser = Point(93223115898197558905062012489877327981787036929201444813217704012422483432813 , 8985629203225767185464920094198364255740987346743912071843303975587695337619, curve)

#Send Public Identitiy Key Coordinates and corresponding signature
def IKRegReq(h,s,x,y):
    mes = {'ID':stuID, 'H': h, 'S': s, 'IKPUB.X': x, 'IKPUB.Y': y}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "IKRegReq"), json = mes)		
    if((response.ok) == False): print(response.json())


#IKRegReq(h,s,x,y)  
code = 598493
#Send the verification code
def IKRegVerify(code):
    mes = {'ID':stuID, 'CODE': code}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "IKRegVerif"), json = mes)
    if((response.ok) == False): raise Exception(response.json())
    print(response.json())


#IKRegVerify(code)

#rcode = 975275 (resetcode)
print("----------------------------------------------------------------------------------------------")
print("**************************************2.2***************************************************")
print("----------------------------------------------------------------------------------------------")

#**********************************************************************2.2 Signed Pre-key (SPK)*********************************************************************
spk_secret = random.randint(0, E.order-2)

print("SPK secret",spk_secret)
spk_secret=31197233491753819378282140643114429723792587762581761883646613118095765438895
spk_public = spk_secret*P 
spk_public=Point(58065729385292233341296079103806449203969554007689575337009902027314338949931,38157503582775474656044444912093398009301179390302637676687391352619237622326, E)
print("SPK public on curve?", E.is_on_curve(spk_public))

print("public", spk_public)



x = spk_public.x
y = spk_public.y

x2 = x.to_bytes(( x.bit_length() +7 ) // 8, byteorder='big')
y2 = y.to_bytes(( y.bit_length() +7 ) // 8, byteorder='big')

concay_key = x2 + y2
print("X is :", x)
print("Y is :", y)
print("X+Y is:", concay_key)



k = random.randint(0, E.order-3)
R = k*P

r = (R.x) % n

r = r.to_bytes((r.bit_length()+7)//8, byteorder='big')
m = concay_key


hash = r+ m
print(hash)

h_obj = SHA3_256.new(hash).digest()


h = (int.from_bytes(h_obj, byteorder='big'))% n

print("H:", h)

s = ( k - ( secret_key*int.from_bytes(h_obj, byteorder='big') ) ) % n

print("S:" , s)



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

message2=SPKReg(h,s,x,y)
print(message2)
server_spk_public= Point(85040781858568445399879179922879835942032506645887434621361669108644661638219,46354559534391251764410704735456214670494836161052287022185178295305851364841, curve)
h_s = message2[2]
s_s = message2[3]
server_spk_public_x = server_spk_public.x.to_bytes((server_spk_public.x.bit_length() + 7) // 8, byteorder='big')
server_spk_public_y = server_spk_public.y.to_bytes((server_spk_public.y.bit_length() + 7) // 8, byteorder='big')
m= server_spk_public_x + server_spk_public_y 
V = (s_s * P) + (h_s * IKey_Ser)
v = V.x % n
byte_v = v.to_bytes((v.bit_length() + 7) // 8, byteorder='big')
hash2 = SHA3_256.new(byte_v + m).digest()
h_int = int.from_bytes(hash2, byteorder='big') % n

print(h_s)
print(h_int)

def verification(): #Verification of SPK
   if h_s == h_int:
     print("Accept the signature")
     return True
   else:
     print("Reject the signature")
     return False

is_verified=verification()
#***********************************************************************2.3 One Time Pre-Key(OTK)*************************************************************************
#Generating HMAC key
T = spk_secret * server_spk_public
T_x = T.x
T_y = T.y
T_x = T.x.to_bytes((T.x.bit_length() + 7) // 8, byteorder='big')
T_y = T.y.to_bytes((T.y.bit_length() + 7) // 8, byteorder='big')
U = T_x + T_y + b'NoNeedToRideAndHide'
Khmac = SHA3_256.new(U).digest()

#Send OTK Coordinates and corresponding hmac
def OTKReg(keyID,x,y,hmac):
    mes = {'ID':stuID, 'KEYID': keyID, 'OTKI.X': x, 'OTKI.Y': y, 'HMACI': hmac}
    print("Sending message is: ", mes)
    response = requests.put('{}/{}'.format(API_URL, "OTKReg"), json = mes)		
    print(response.json())
    if((response.ok) == False): return False
    else: return True

def OTKS(i): 
    otk_secret = random.randint(0, E.order-2)
    otk_public = otk_secret*P 
    print(otk_public)
    x = otk_public.x
    y = otk_public.y
    x_b = x.to_bytes(( x.bit_length() +7 ) // 8, byteorder='big')
    y_b = y.to_bytes(( y.bit_length() +7 ) // 8, byteorder='big')
    concay_key = x_b + y_b
    hmac = HMAC.new(key = Khmac, msg = concay_key, digestmod = SHA256).hexdigest()
    OTKReg(i, otk_public.x, otk_public.y, hmac)
  


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




#Send the reset code to delete your Identitiy Key
#Reset Code is sent when you first registered
def ResetIK(rcode):
    mes = {'ID':stuID, 'RCODE': rcode}
    print("Sending message is: ", mes)
    response = requests.delete('{}/{}'.format(API_URL, "ResetIK"), json = mes)		
    print(response.json())
    if((response.ok) == False): return False
    else: return True

#If we neet to reset private identity key / pair
# We can use the above function:
# ResetIK(rcode)

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

