import requests # if this lib isn't installed yet --> pip install requests or pip3 intall requests


### DO NOT CHANGE HERE ######

API_URL = 'http://cryptlygos.pythonanywhere.com' # DO NOT change url 

def getCipher(my_id):
    endpoint = '{}/{}/{}'.format(API_URL, "affine_game", my_id )
    response = requests.get(endpoint) 	#get your ciphertext and most freq. letter
    ctext, letter = "", ""
    if response.ok:	#if you get your ciphertext succesfully
        c = response.json()
        ctext = c[0]    #this is your ciphertext
        letter = c[1] 	#the most frequent letter in your plaintext
    elif(response.status_code == 404):
        print("We dont have a student with this ID. Check your id num")
    else:
        print("It was supposed to work:( Contact your TA")
    
    return ctext, letter
    
    
def sendMessage(my_id, plaintext):    
    endpoint = '{}/{}/{}/{}'.format(API_URL, "affine_game", my_id, plaintext)
    response = requests.put(endpoint)
    if response.ok:
        c = response.json()
        print(c)
    elif(response.status_code == 404):
        print("Nope, Try again")
    elif(response.status_code == 401):
        print("Check your ID number")
    else:
        print("How did you get in here? Contact your TA")
        
###### MOdify below     
    
if __name__ == '__main__':
    my_id = 24906	# change this to your id number. it should be 5 digit number
    
    cipher_text, most_frequent_letter = getCipher(my_id)
    
    print(cipher_text)

    print("**************************************************")

    print("MOST FREQUENT LETTER IN PLAINTEXT=   " + most_frequent_letter)

    print("**************************************************")

    letters = {} 
  
    for i in cipher_text: 

        if i in letters: 

            letters[i] = letters[i] +1
        else: 

            letters[i] = 1
    

    print(str(letters))        

    print("**************************************************")

    
    

    """
    In this question I am finding the plaintext from the helper fucntion which you provided 
    I updated necessary parts and saved as hw1-question3-plaintextcode.py
    You can see how I find from there
    
    """

    
    plainText = "BERGSON BENİ, GENÇLİĞİMDE HERBİRİ BENİM İÇİN BİRER İŞKENCE OLAN, ÇÖZÜLMESİ OLANAKSIZ, FELSEFE SORUNLARINDAN KURTARDI NIETZSCHE İSE, YENI ACILARLA ZENGINLEŞTİRDİ BENİ VE BANA SIKINTIYI, ACIYI VE KARARSIZLIĞI GURURA ÇEVIRMEYİ ÖĞRETTİ ZORBA İSE, HAYATI SEVMEYİ VE ÖLÜMDEN KORKMAMAYI ÖĞRETMİŞTİR BANA.EĞER BUGÜN, DÜNYA'DA BİR RUH KILAVUZU, HİNDLİLERİN DEDİĞİ GİBİ BİR GURU, AYRANOZ PAPAZLARININ DEDİĞİ GİBİ BİR YERONDA SEÇMEM GEREKSEYDİ, KESİNLİKLE ZORBA'YI SEÇERDİM ÇÜNKÜ, MÜREKKEP YALAYAN BİR İNSANIN KENDİNİ KURTARMASI İÇİN NEYE GEREKSİNMESİ VARSA, HEPSİ ONDA VARDI UZAKTAKI BESİNİNİ OK GİBİ YAKALAYAN O İLKEL AVCI GÖRÜŞÜ, RÜZGAR, DENİZ, ATEŞ, KADIN VE EKMEK GİBİ, HER GÜNÜN YÜZYILLIK ÖĞELERİNE BİR BAKİRLIK VERMEK VE ÖLÜMSÜZLÜĞE HER ZAMAN İLK KEZ BAKMAK KONUSUNDA GÖSTERDİĞİ O HER SABAH YENİLENEN YARATICI YALINLIĞI, ELİNİN SAĞLAMLIĞI, YÜREĞİNİN TAZELİĞİ, İÇİNDE RUHTAN DAHA KUVVETLİ BİR GÜÇ VARMIŞ GİBİ, KENDİ RUHU İLE ALAY ETMEK YOLUNDAKİ BABAYİĞİTLİĞİ VE SON OLARAK KRİTİK ANLARDA, ZORBA'NIN İHTİYAR GÖĞSÜNDEN KURTARICI OLARAK FIŞKIRAN, İNSANIN BENLİĞİNDEN DAHA DERİN BİR KAYNAKTAN ÇIKAN, HER ZAMAN YENİ, PÜRÜZSÜZ GÜLÜŞÜ, ZAVALLI VE KORKAK İNSANIN KENDİ HAYATÇIĞINI YARIM YAMALAK GÜVENLİK ALTINA ALMA YOLUNDA ÇEVRESİNE DİKTİĞİ AHLAK, DİN VE VATAN GİBİ ÇİTLERİ YIKMAK İÇİN O SİLKİNİR VE YIKARDI DA BUNCA YILDIR KİTAPLARDA ÖĞRETMENLERİN KUDURMUŞ RUHUMU DOYURMAK İÇİN, BENİ HANGİ BESİNLE BESLEDİKLERİNİ VE ZORBA'NIN BİRKAÇ AYDA, BANA NASIL, ASLANCA BİR BESİNİ VERDİĞİNİ DÜŞÜNDÜĞÜMDE İÇİMDEKİ ACIYI VE KIZGINLIĞI GÜÇLÜKLE ÖNLEYEBİLİYORUM BİR BAKIMA, HAYATIM MAHVOLUP GİTMİŞTİ BU İHTİYARLA ÇOK GEÇ KARŞILAŞMIŞTIM VE HALA İÇİMDE KALAN, KURTULABİLECEK ŞEYLER ÇOK AZDI"
 
    #Check your answer with this function. 
    sendMessage(my_id, plainText)
    
