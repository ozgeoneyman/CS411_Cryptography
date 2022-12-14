import math
import random
import fractions

# This is method to compute Euler's function
# The method here is based on "counting", which is not good for large numbers in cryptography
def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

# The extended Euclidean algorithm (EEA)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Modular inverse algorithm that uses EEA
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

# You can use the the following variables for encoding an decoding of English letters
lowercase = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
         'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
         'r':17, 's':18,  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
         'z':25}

uppercase ={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
         'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
         'R':17, 'S':18,  'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}

inv_lowercase = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
         25:'z'}

inv_uppercase = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H',
                 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P',
                 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
                 24:'Y', 25:'Z'}

letter_count = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
         'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
         'R':0, 'S':0,  'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}

# You can use the Turkish alphabet for Question 3
# Note that encyrption and decryption algorithms are slightly different for
# Turkish texts
turkish_alphabet ={'A':0, 'B':1, 'C':2, '??':3, 'D':4, 'E':5, 'F':6, 'G':7, '??':8, 'H':9, 'I':10,
         '??': 11, 'J':12, 'K':13, 'L':14, 'M':15, 'N':16, 'O':17, '??':18, 'P':19,
         'R':20, 'S':21,  '??':22, 'T':23, 'U':24, '??':25, 'V':26, 'Y':27,
         'Z':28, '.' : 29, ',': 30}

inv_turkish_alphabet = {0:'A', 1:'B', 2:'C', 3:'??', 4:'D', 5:'E', 6:'F', 7:'G', 8:'??', 9:'H',
              10:'I', 11:'??', 12:'J', 13:'K', 14:'L', 15:'M', 16:'N', 17:'O', 18:'??',
              19:'P', 20:'R', 21:'S',  22:'??', 23:'T', 24:'U', 25:'??', 26:'V',
              27:'Y', 28:'Z' , 29: '.', 30: ','}

# Affine cipher encryption and decryption routines only for English texts
def Affine_Enc(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range (0,plen):
        letter = ptext[i]
        if letter in turkish_alphabet:
            poz = turkish_alphabet[letter]
            poz = (key.alpha*poz+key.beta)%31
            ctext += inv_turkish_alphabet[poz]
        else:
            ctext += ptext[i]
    return ctext

def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range (0,plen):
        letter = ptext[i]
        if letter in turkish_alphabet:
            poz = turkish_alphabet[letter]
            poz = (key.gamma*poz+key.theta)%31
            ctext += inv_turkish_alphabet[poz]
        else:
            ctext += ptext[i]
    return ctext

# key object for Affine cipher
# (alpha, beta) is the encryption key
# (gamma, theta) is the decryption key
class key(object):
    alpha=0
    beta=0
    gamma=0
    theta=0

# I tried all possible alpha values for finding plain text

key.alpha = 27
key.beta = 2
key.gamma = modinv(key.alpha, 31)# you can compute decryption key from encryption key
key.theta = 31-(key.gamma*key.beta)%31

print(key.gamma)  #23
print(key.theta)    #16

ctext = ".KME??YA .KARF EKAS??RBRDOK ZKM.RMR .KARD RSRA .RMKM RGJKA??K Y??CAF STLV??DK??R Y??CACJ??ULF HK????KHK ??YM,A??CMUAOCA J,M??CMOU AUK??L????ZK R??KF ??KAU C??U??CM??C LKAEUA??KG??RMOR .KAR ??K .CAC ??UJUA??U??UF C??U??U ??K JCMCM??UL??UBU E,M,MC SK??UMDK??R TBMK????R LYM.C R??KF ZC??C??U ??K??DK??R ??K T??VDOKA JYMJDCDC??U TBMK??DRG??RM .CACIKBKM .,EVAF OVA??C'OC .RM M,Z JU??C??,L,F ZRAO??R??KMRA OKORBR ER.R .RM E,M,F C??MCAYL PCPCL??CMUAUA OKORBR ER.R .RM ??KMYAOC ??KSDKD EKMKJ??K??ORF JK??RA??RJ??K LYM.C'??U ??KSKMORD SVAJVF DVMKJJKP ??C??C??CA .RM RA??CAUA JKAORAR J,M??CMDC??U RSRA AK??K EKMKJ??RADK??R ??CM??CF ZKP??R YAOC ??CMOU ,LCJ??CJU .K??RARAR YJ ER.R ??CJC??C??CA Y R??JK?? C????U ETMVGVF MVLECMF OKARLF C??KGF JCOUA ??K KJDKJ ER.RF ZKM EVAVA ??VL??U????UJ TBK??KMRAK .RM .CJRM??UJ ??KMDKJ ??K T??VD??VL??VBK ZKM LCDCA R??J JKL .CJDCJ JYA,??,AOC ET????KMORBR Y ZKM ??C.CZ ??KAR??KAKA ??CMC??U??U ??C??UA??UBUF K??RARA ??CB??CD??UBUF ??VMKBRARA ??CLK??RBRF RSRAOK M,Z??CA OCZC J,????K????R .RM EVS ??CMDUG ER.RF JKAOR M,Z, R??K C??C?? K??DKJ ??Y??,AOCJR .C.C??RBR????RBR ??K ??YA Y??CMCJ JMR??RJ CA??CMOCF LYM.C'AUA RZ??R??CM ETB??VAOKA J,M??CMU??U Y??CMCJ HUGJUMCAF RA??CAUA .KA??RBRAOKA OCZC OKMRA .RM JC??ACJ??CA SUJCAF ZKM LCDCA ??KARF PVMVL??VL EV??VGVF LC??C????U ??K JYMJCJ RA??CAUA JKAOR ZC??C??SUBUAU ??CMUD ??CDC??CJ EV??KA??RJ C????UAC C??DC ??Y??,AOC SK??MK??RAK ORJ??RBR CZ??CJF ORA ??K ??C??CA ER.R SR????KMR ??UJDCJ RSRA Y ??R??JRARM ??K ??UJCMOU OC .,A??C ??U??OUM JR??CP??CMOC TBMK??DKA??KMRA J,O,MD,G M,Z,D, OY??,MDCJ RSRAF .KAR ZCAER .K??RA??K .K????KORJ??KMRAR ??K LYM.C'AUA .RMJCS C??OCF .CAC AC??U??F C????CA??C .RM .K??RAR ??KMORBRAR OVGVAOVBVDOK RSRDOKJR C??U??U ??K JULEUA??UBU EVS??VJ??K TA??K??K.R??R??YM,D .RM .CJUDCF ZC??C??UD DCZ??Y??,P ER??DRG??R ., RZ??R??CM??C SYJ EKS JCMGU??CGDUG??UD ??K ZC??C RSRDOK JC??CAF J,M??,??C.R??K??KJ GK????KM SYJ CLOU"
dtext = Affine_Dec(ctext, key)

print("ciphertext: ", ctext)
print("**************************************************")
print("plaintext: ", dtext)
