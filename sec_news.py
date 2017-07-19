import urllib.request
from re import findall
from colorama import Fore, Back, Style
import os


url = "http://sec.jetlib.com/"
response = urllib.request.urlopen(url)
html = response.read()
htmlStr = html.decode()



def getbugs():

    ndata = findall(r'Permalink for(.*?)href=', htmlStr)
    for item in ndata:
        print( Fore.LIGHTGREEN_EX+ Back.BLACK + "--->"+item + Style.RESET_ALL)


os.system('clear')
getbugs()
