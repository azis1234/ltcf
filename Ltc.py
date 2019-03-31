import requests, os, sys
from bs4 import BeautifulSoup
from time import sleep


url = "http://affi.cryptoplanets.org/ltcfarmer/index.php"
urlclaim = "http://affi.cryptoplanets.org/ltcfarmer/ajax.php"


UA = {
   "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-J610F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.105 Mobile Safari/537.36"
}
data = {
   "PHPSESSID": "37gbi968vsi173v3kc3k7s6nm0"
}
claim1 = {
   "confirm_exploaration_point_claim": "1"
}
claim2 = {
   "confirm_exploaration_point_claim": "2"
}
claim3 = {
   "confirm_exploaration_point_claim": "3"
}
claim4 = {
   "confirm_exploaration_point_claim": "4"
}
claim5 = {
   "confirm_exploaration_point_claim": "5"
}
reset1 = {
   "reset_contest_button": "1"
}
reset2 = {
   "reset_contest_button": "2"
}
reset3 = {
   "reset_contest_button": "3"
}
reset4 = {
   "reset_contest_button": "4"
}
reset5 = {
   "reset_contest_button": "5"
}

c = requests.Session()

def login():
    os.system('clear')
    print ("PHPSESSID/data")
    sleep(1)
    os.system('clear')
    print ("Login ")
    sleep(1)
    os.system('clear')
    print ("Login •")
    sleep(1)
    os.system('clear')
    print ("Login ••")
    sleep(1)
    os.system('clear')
    print ("Login •••")
    sleep(1)
    r = c.post(url, cookies=data, headers=UA)
    soup = BeautifulSoup(r.content, "html.parser")
    for ball in soup.find_all("div", class_="widget-int num-count"):
        print ("Login Success")
        print ("Your Ballance :", ball.text, "Point")


def tmbl1():
   c.post(urlclaim, cookies=data, headers=UA, data=reset1)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim1)
   print ("Succes :",r.text, "Point")
def tmbl2():
   c.post(urlclaim, cookies=data, headers=UA, data=reset2)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim2)
   print ("Succes :",r.text, "Point")
def tmbl3():
   c.post(urlclaim, cookies=data, headers=UA, data=reset3)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim3)
   print ("Succes :",r.text, "Point")
def tmbl4():
   c.post(urlclaim, cookies=data, headers=UA, data=reset4)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim4)
   print ("Succes :",r.text, "Point")
def tmbl5():
   c.post(urlclaim, cookies=data, headers=UA, data=reset5)
   r = c.post(urlclaim, cookies=data, headers=UA, data=claim5)
   print ("Succes :",r.text, "Point")
def tunggu():
    for remaining in range(60, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("{:2d} seconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)

    sys.stdout.write("\rComplete!            \n")

login()
print (" SUBSCRIBE YT AW 2000 ")
print ("\n\n\nStart Claiming......!")
while True:
     tmbl1()
     tunggu()
     tmbl2()
     tunggu()
     tmbl3()
     tunggu()
     tmbl4()
     tunggu()
     tmbl5()
     tunggu()
