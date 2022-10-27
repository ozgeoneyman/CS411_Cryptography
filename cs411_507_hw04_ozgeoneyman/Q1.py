import random
import requests
from random import randint
import math
import warnings
import sympy

API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 24906  

def RSA_Oracle_Get():
  response = requests.get('{}/{}/{}'.format(API_URL, "RSA_Oracle", my_id)) 	
  c, N, e = 0,0,0 
  if response.ok:	
    res = response.json()
    print(res)
    return res['c'], res['N'], res['e']
  else:
    print(response.json())

def RSA_Oracle_Query(c_):
  response = requests.get('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Query", my_id, c_)) 
  print(response.json())
  m_= ""
  if response.ok:	m_ = (response.json()['m_'])
  else: print(response)
  return m_

def RSA_Oracle_Checker(m):
  response = requests.put('{}/{}/{}/{}'.format(API_URL, "RSA_Oracle_Checker", my_id, m))
  print(response.json())


c, N, e = RSA_Oracle_Get()

c_ = ((pow(2, e, N) * c) % N)

m_ = RSA_Oracle_Query(c_)   

m = (m_ //2).to_bytes(( m_.bit_length() +7 ) // 8, byteorder='big')

print(m)   #The output is: Bravo! You find it. Your secret code is 3777

RSA_Oracle_Checker(m) 

