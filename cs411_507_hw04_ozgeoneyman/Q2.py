import math
import timeit
import random
import sympy
import warnings
import requests
from Crypto.Hash import SHA3_256
from Crypto.Hash import SHA3_384
from Crypto.Hash import SHA3_512
from Crypto.Hash import SHAKE128, SHAKE256

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 24906  

k0 = 8
k1 = 128

def RSA_OAEP_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id )) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())
    return c, N, e

def RSA_OAEP_Checker(PIN_):
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_OAEP", my_id, PIN_))
  print(response.json())

def RSA_OAEP_Enc(m, e, N, R):
    k = N.bit_length()-2
    m0k1 = m << k1
    shake = SHAKE128.new(R.to_bytes(k0//8, byteorder='big'))
    GR =  shake.read((k-k0)//8)
    m0k1GR = m0k1 ^ int.from_bytes(GR, byteorder='big')
    shake = SHAKE128.new(m0k1GR.to_bytes((m0k1GR.bit_length()+7)//8, byteorder='big'))
    Hm0k1GR =  shake.read(k0//8)
    RHm0k1GR = R ^ int.from_bytes(Hm0k1GR, byteorder='big')
    m_ = (m0k1GR << k0) + RHm0k1GR
    c = pow(m_, e, N)
    return c

c, N, e = RSA_OAEP_Get()
PIN_ = 0

a = 128
b = 255

for m in range(10000):
  for R in range(a, b):
    c2 = RSA_OAEP_Enc(m, e, N, R)
    if(c2 == c):
      PIN_ = m
      break

print(PIN_)  ## The randomly choosen PIN is 1832.
print(R)     ## R is equal to 254.
RSA_OAEP_Checker(PIN_)
    
