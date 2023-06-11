###############8
import requests
import time
import urllib3
import os
import random 
from datetime import datetime
import socket

def main():
    try:
        os.system('clear')
        r = "\033[1;31m"
        g = "\033[1;32m"
        b2 ="\033[1;33m"
        a = "\033[1;35m"
        f = "\033[1;39m"
        print(f'''\033[1;34m
           ░░╚══╗░╔═╔════╝
           ╚═╦═╗╠═╩═╩╗╔═╦═╗
           ░░║▒╠╣▒▒▒▒╠╣▒║▒
           ╔═╩═╝╠═╦═╦╝╚═╩═╝
           ░░╔══╝░╚═╚════╗''')

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        print(f"{b2}-"*80)
        os.system("figlet DIR-SPIDER|lolcat -a -d 10")

        print(f"{b2}-"*80)
        now = datetime.now()
        print(f"{b2}-"*80)
        date = now.strftime("%m/%d/%Y")
        print(f"data:", date)
        time = now.strftime("%H:%M:%S")
        print(f"horas", time) 
        print(f"criador:default")
        print(f"STATUS-CODE: {f}[200][203] {r}[401][405][403] {a}[301][302][307][308]")
        print(f"{b2}-"*80)

        print(f'\033[1;32mDIGITE UM SITE[+]')
        web = input(f'\033[1;33m>>> ')
        print(f"digite uma wordlist ou default:/pas.txt/")
        ar = input(f"{r}[{g}DIR-SPIDER{r}]{a}•••••{r}>>> ")
        os.system("termux-tts-speak -r 0.8 iniciando dir spider")
        os.system("mpv scifi.mp3")
        arquivo = open(ar,"r")
        for d in arquivo:
            
            requisicao = requests.get(web+"/"+d.replace('\n',''),verify = False)

            if requisicao.status_code == 200:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;39m"+str(requisicao.status_code)+"\033[1;39m")
   
            elif requisicao.status_code == 203:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;39m"+str(requisicao.status_code)+"\033[1;39m")
                os.system("termux-tts-speak -r 0.8 requisição 203")

            elif requisicao.status_code == 401:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;31m"+str(requisicao.status_code)+"\033[1;31m")
                os.system("termux-tts-speak -r 0.8 requisição 401")

            elif requisicao.status_code == 405:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;31m"+str(requisicao.status_code)+"\033[1;31m")
                os.system("termux-tts-speak -r 0.8 requisição 405")
    
            elif requisicao.status_code == 403:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;31m"+str(requisicao.status_code)+"\033[1;31m")
                os.system("termux-tts-speak -r 0.8 requisição 403")

            elif requisicao.status_code == 301:
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;35m"+str(requisicao.status_code)+"\033[1;35m")
                os.system("termux-tts-speak -r 0.8 requisição 301")

            elif requisicao.status_code == 302:
                os.system("termux-tts-speak -r 0.8 requisição 302")
                print(requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;35m"+str(requisicao.status_code)+"\033[1;35m")

            elif requisicao.status_code == 307:
                print(f+requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;35m"+str(requisicao.status_code)+"\033[1;35m")
                os.system("termux-tts-speak -r 0.8 requisição 307")

            elif requisicao.status_code == 308:
                print(f+requisicao.url+"\033[1;31m[=>]\033[1;34m"+"\033[1;35m"+str(requisicao.status_code)+"\033[1;35m")
                os.system("termux-tts-speak -r 0.8 requisição 308")

        print(f"APERTOU: CTRL+C sair")
    except KeyboardInterrupt:
        os.system("clear")
        print("VOCE APERTOU OU CTRL-C-ENTER")
main()
