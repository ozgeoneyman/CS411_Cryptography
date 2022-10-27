import random
import requests
import math
from math import gcd as bltin_gcd
from sympy.ntheory.factor_ import totient


#API_URL = 'http://10.36.52.109:6000'
API_URL = 'http://cryptlygos.pythonanywhere.com'

my_id = 24906   

def getQ1():
  endpoint = '{}/{}/{}'.format(API_URL, "Q1", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    print(res)
    n, t = res['n'], res['t']
    return n,t
  else: print(response.json())

def checkQ1a(order):   #check your answer for Question 1 part a
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1a", my_id, order)
  response = requests.put(endpoint) 	
  print(response.json())

def checkQ1b(g):  #check your answer for Question 1 part b
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1b", my_id, g )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())

def checkQ1c(gH):  #check your answer for Question 1 part c
  endpoint = '{}/{}/{}/{}'.format(API_URL, "checkQ1c", my_id, gH )	#gH is generator of your subgroup
  response = requests.put(endpoint) 	#check result
  print(response.json())


def getQ2():
  endpoint = '{}/{}/{}'.format(API_URL, "Q2", my_id )
  response = requests.get(endpoint) 	
  if response.ok:	
    res = response.json()
    e, cipher = res['e'], res['cipher']
    return e, cipher
  else:  print(response.json())

def checkQ2(ptext):  #check your answer for Question 1 part c
  response = requests.put('{}/{}'.format(API_URL, "checkQ2"), json = {"ID": my_id, "msg":ptext})
  print(response.json())



# Question 1  

print(getQ1()) #n number is 326, t number is 81

checkQ1a(162)  #It prints Congrats! 


def primRoots(modulo):
    required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) == 1 }
    return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

#Above code is taken from https://math.stackexchange.com/questions/4276649/finding-primitive-roots-modulo-n-code

print(primRoots(326)) #which are [3, 7, 11, 19, 29, 45, 63, 67, 73, 75, 79, 89, 101, 103, 107, 109, 117, 129, 137, 139, 147, 149, 153, 159, 165, 175, 181, 183, 195, 205, 207, 213, 215, 229, 231, 233, 235, 239, 243, 245, 255, 257, 269, 271, 275, 277, 279, 283, 285, 287, 291, 293, 311, 317]

checkQ1b(3)   #It prints Congrats! 




# Question 2  

print(getQ2())  
e = 484843768494505746149148347803315248081322820222174761227311295364221165399477321078696608391871793870290246746695975038008033878159214699188832192213297182991030545005799440800688494262195670987091697934758470669146943183215400738236156540102339246394465236595348068151466452234062200481375951686604695358183
c = 1246347887557447092437909386048336660421457690166950791692141874408423891354093802344067456163162644247219799764794347614759256046430230795319296700216551704698632569969309129180524773404650828667556676858520695421158195007001075417668241416296706475104821977439307624996615225938678985865663877667797267181207



def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m 
# above code from stackoverflow 

p = 23736540918088479407817876031701066644301064882958875296167214819014438374011661672830210955539507252066999384067356159056835877781419479023313149139444707
q =62179896404564992443617709894241054520624355558658288422696178839274611833136662241430162694076231401545584449128278988404970580015985140542451087049794069
n = p * q

tot  = totient(p) * totient (q)

d = modinv(e, tot)

m = pow(c, d, n)

m2 = m.to_bytes(len(str(m)), 'big').decode(encoding='utf8')  

print(m2)  

checkQ2("Answer to the ultimate question of life, the universe, and everything is not 42. it is 517")  #It prints Congrats! 






#question 4

#A
n = 100433627766186892221372630785266819260148210527888287465731
a = 336819975970284283819362806770432444188296307667557062083973
b = 25245096981323746816663608120290190011570612722965465081317
print(math.gcd(a,n))
#gcd equal to 1


step1 = pow(a,-1,n)

step2= step1* b

result = step2 %n

print(result) #Result is 56884393062303769019751445983612369117060043083722821988604

#B
n = 301300883298560676664117892355800457780444631583664862397193
a = 1070400563622371146605725585064882995936005838597136294785034
b = 1267565499436628521023818343520287296453722217373643204657115
print(math.gcd(a,n))
#gcd equal to 3

#C
n = 301300883298560676664117892355800457780444631583664862397193
a = 608240182465796871639779713869214713721438443863110678327134
b = 721959177061605729962797351110052890685661147676448969745292
print(math.gcd(a,n))
#gcd equal to 3

