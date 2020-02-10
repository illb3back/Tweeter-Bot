import telepot
import requests
from bs4 import BeautifulSoup
import time
import oauth2
import json
import pprint
import urllib.parse
Access_token=''
Access_token_secret=''
API_key=''
API_secret_key=''


while True:
    time.sleep(3600)
    rqt=requests.get('http://www.ufrpe.br/br') #Site da ufrpe
    bf=BeautifulSoup(rqt.text,'html.parser')#estrutura
    novo=(bf.find('div','views-row views-row-1 views-row-odd views-row-first').text)#pega informações
    try:
        escre=open('cache.txt','x')#abre o arquivo cache
        escre.write(novo)#caso o arquivo não exista ele e gerado
        escre.close()#fecha o arquivo
    except FileExistsError: #caso o arquivo ja exista
        ler=open('cache.txt','r')
        antigo=ler.read()
        ler.close()
        if antigo == novo:
            print('')
            
            
        else:
            escre2=open('cache.txt','w')
            escre2.write(novo)
            escre2.close()
            ler2=open('cache.txt','r')
            antigo2=ler2.read()
            ler2.close()
            aa=[antigo2]
            vet=(str(aa[0][0:220]))
            vet_mod=urllib.parse.quote('para mais informações acesse:www.ufrpe.br\n\n'+vet,safe='')
            print(vet_mod)
            
            consumer=oauth2.Consumer(API_key,API_secret_key)
            token=oauth2.Token(Access_token,Access_token_secret)
            client=oauth2.Client(consumer,token)
            reque=client.request('https://api.twitter.com/1.1/statuses/update.json?status='+vet_mod,method='POST')
            print('postado')

            









    
