# osint_v3.py - Python 3.11+, Termux
# OSINT Framework V3 (Super Lengkap + Chafa BG Full Width + Tema Biru)
# pip install requests beautifulsoup4 phonenumbers dnspython colorama urllib3
import os, sys, socket, subprocess, requests, urllib3, re
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import phonenumbers
from phonenumbers import carrier, geocoder
import dns.resolver

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36"}

# GAMBAR NO 3
BG_IMAGE = "/storage/emulated/0/avg/4d29cd62eae542edc1ba840085d22d48.jpg"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def print_banner():
    clear()
    if os.path.exists(BG_IMAGE):
        try:
            # Menggunakan ukuran terminal dinamis (100% lebar layar)
            subprocess.run(["chafa", "--size", "100x40", BG_IMAGE], check=True)
        except:
            pass
    print(f"""{Fore.BLUE}
    ╔══════════════════════════════════════════════════════╗
    ║              OSINT FRAMEWORK V3                      ║
    ║                 Author: MR ROBERTO                   ║
    ╚══════════════════════════════════════════════════════╝
    {Style.RESET_ALL}""")

def menu():
    print(f"""{Fore.BLUE}
    ┌──────────────────────────────────────────────────────┐
    │  [1] IP Tracker & Geolocation                        │
    │  [2] Phone Number Info (Operator & Region)           │
    │  [3] DNS & Whois Lookup                              │
    │  [4] Username Checker (Sherlock-like)                │
    │  [5] Email Breach Check (HIBP)                       │
    │  [6] Web Tech & Headers Scan                         │
    │  [7] Subdomain Scanner                               │
    │  [8] Google Dorking Generator                        │
    │  [9] MAC Address Lookup (OUI)                        │
    │  [10] IP Port Scanner (Common Ports)                 │
    │  [11] Pastebin Search (Leak/Paste)                   │
    │  [12] SSL Certificate Info                           │
    │  [13] GitHub User Recon                              │
    │  [0] Exit                                            │
    └──────────────────────────────────────────────────────┘
    {Style.RESET_ALL}""")

def ip_tracker():
    ip = input(f"{Fore.BLUE}Masukkan IP/Domain: {Style.RESET_ALL}")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=10).json()
        print(f"\n{Fore.BLUE}[+] IP: {r.get('query')} | ISP: {r.get('isp')}")
        print(f"[+] Country: {r.get('country')} | City: {r.get('city')}")
        print(f"[+] Coord: {r.get('lat')}, {r.get('lon')}")
        print(f"[+] Map: https://www.google.com/maps?q={r.get('lat')},{r.get('lon')}")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def phone_info():
    nomor = input(f"{Fore.BLUE}Masukkan No HP (0812...): {Style.RESET_ALL}")
    try:
        if nomor.startswith("0"): nomor = "+62" + nomor[1:]
        parsed = phonenumbers.parse(nomor, None)
        print(f"\n{Fore.BLUE}[+] Valid: {phonenumbers.is_valid_number(parsed)}")
        print(f"[+] Operator: {carrier.name_for_number(parsed, 'id')}")
        print(f"[+] Region: {geocoder.description_for_number(parsed, 'id')}")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def dns_whois():
    domain = input(f"{Fore.BLUE}Masukkan Domain: {Style.RESET_ALL}")
    print(f"\n{Fore.BLUE}[+] DNS Records:")
    for rtype in ["A", "MX", "NS", "TXT"]:
        try:
            ans = dns.resolver.resolve(domain, rtype, lifetime=5)
            for r in ans: print(f"    {rtype}: {r.to_text()}")
        except: pass
    print(f"\n{Fore.BLUE}[+] WHOIS Info:")
    try:
        out = subprocess.check_output(["whois", domain], timeout=10, stderr=subprocess.DEVNULL).decode(errors="ignore")
        for line in out.splitlines():
            if re.match(r"(?i)(registrar|creation|expiry|name server)", line):
                print(f"    {line.strip()}")
    except Exception as e: print(f"    {Fore.RED}[-] WHOIS Error: {e}")

def username_checker():
    user = input(f"{Fore.BLUE}Masukkan Username: {Style.RESET_ALL}")
    sites = {
        "GitHub": f"https://github.com/{user}",
        "Instagram": f"https://instagram.com/{user}",
        "Twitter/X": f"https://x.com/{user}",
        "TikTok": f"https://tiktok.com/@{user}",
        "Reddit": f"https://reddit.com/user/{user}",
        "Pinterest": f"https://pinterest.com/{user}",
        "GitLab": f"https://gitlab.com/{user}",
        "Medium": f"https://medium.com/@{user}"
    }
    print(f"\n{Fore.BLUE}[+] Cek Username:")
    for name, url in sites.items():
        try:
            r = requests.get(url, headers=HEADERS, timeout=5)
            status = f"{Fore.BLUE}[FOUND]" if r.status_code == 200 else f"{Fore.RED}[NOT FOUND]"
            print(f"    {status} {name}")
        except: print(f"    {Fore.RED}[ERROR] {name}")

def breach_check():
    email = input(f"{Fore.BLUE}Masukkan Email: {Style.RESET_ALL}")
    print(f"\n{Fore.BLUE}[+] Cek HIBP untuk {email}...")
    try:
        r = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}", headers=HEADERS, timeout=10)
        if r.status_code == 200:
            breaches = [b['Name'] for b in r.json()]
            print(f"    [!] BOCOR di: {', '.join(breaches[:5])}")
        elif r.status_code == 404: print("    [-] Aman (Tidak ditemukan).")
        elif r.status_code == 401: print("    [-] HIBP butuh API Key berbayar.")
    except Exception as e: print(f"    {Fore.RED}[-] Error: {e}")

def web_scan():
    domain = input(f"{Fore.BLUE}Masukkan URL: {Style.RESET_ALL}")
    if not domain.startswith("http"): domain = "https://" + domain
    try:
        r = requests.get(domain, headers=HEADERS, timeout=10, verify=False, allow_redirects=True)
        print(f"\n{Fore.BLUE}[+] Status: {r.status_code} ({len(r.content)} bytes)")
        for h in ["Server", "X-Powered-By", "X-Frame-Options", "Content-Security-Policy"]:
            if h in r.headers: print(f"    {h}: {r.headers[h]}")
        title = BeautifulSoup(r.text, "html.parser").title
        if title and title.string: print(f"    Title: {title.string[:80]}")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def subdomain_scan():
    domain = input(f"{Fore.BLUE}Masukkan Domain: {Style.RESET_ALL}")
    subs = ["www", "api", "dev", "admin", "mail", "blog", "cpanel", "webmail", "ftp"]
    print(f"\n{Fore.BLUE}[+] Scanning {len(subs)} subdomains...")
    for s in subs:
        host = f"{s}.{domain}"
        try:
            ip = socket.gethostbyname(host)
            print(f"    {Fore.BLUE}[FOUND] {host} -> {ip}")
        except: pass

def google_dork():
    domain = input(f"{Fore.BLUE}Masukkan Domain: {Style.RESET_ALL}")
    print(f"\n{Fore.BLUE}[+] Dorking untuk {domain}:")
    dorks = [
        f"site:{domain} ext:env OR ext:log OR ext:sql",
        f"site:{domain} intitle:index.of",
        f"site:{domain} inurl:admin OR inurl:login",
        f"site:{domain} ext:pdf OR ext:docx"
    ]
    for d in dorks: print(f"    {d}")

def mac_lookup():
    mac = input(f"{Fore.BLUE}Masukkan MAC Address (00:11:22...): {Style.RESET_ALL}")
    try:
        r = requests.get(f"https://api.macvendors.com/{mac}", timeout=10)
        if r.status_code == 200: print(f"{Fore.BLUE}[+] Vendor: {r.text}")
        else: print(f"{Fore.RED}[-] Vendor tidak ditemukan.")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def port_scan():
    domain = input(f"{Fore.BLUE}Masukkan IP/Domain: {Style.RESET_ALL}")
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389]
    print(f"\n{Fore.BLUE}[+] Scanning common ports...")
    try:
        ip = socket.gethostbyname(domain)
        for p in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            if s.connect_ex((ip, p)) == 0:
                print(f"    {Fore.BLUE}[OPEN] {p}/tcp")
            s.close()
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def pastebin_search():
    query = input(f"{Fore.BLUE}Masukkan kata kunci (email/nama): {Style.RESET_ALL}")
    print(f"\n{Fore.BLUE}[+] Cek Pastebin via Google Dork...")
    print(f"    https://www.google.com/search?q=site:pastebin.com+{query}")

def ssl_info():
    domain = input(f"{Fore.BLUE}Masukkan Domain: {Style.RESET_ALL}")
    try:
        cmd = f"echo | openssl s_client -connect {domain}:443 -servername {domain} 2>/dev/null | openssl x509 -noout -subject -issuer -dates"
        out = subprocess.check_output(cmd, shell=True).decode()
        print(f"\n{Fore.BLUE}[+] SSL Info:\n{out}")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def github_recon():
    user = input(f"{Fore.BLUE}Masukkan Username GitHub: {Style.RESET_ALL}")
    try:
        r = requests.get(f"https://api.github.com/users/{user}", timeout=10).json()
        print(f"\n{Fore.BLUE}[+] Nama: {r.get('name')}")
        print(f"[+] Bio: {r.get('bio')}")
        print(f"[+] Repos: {r.get('public_repos')}")
        print(f"[+] Lokasi: {r.get('location')}")
    except Exception as e: print(f"{Fore.RED}[-] Error: {e}")

def main():
    while True:
        print_banner()
        menu()
        choice = input(f"{Fore.BLUE}OSINT > {Style.RESET_ALL}").strip()
        
        if choice == "1": ip_tracker()
        elif choice == "2": phone_info()
        elif choice == "3": dns_whois()
        elif choice == "4": username_checker()
        elif choice == "5": breach_check()
        elif choice == "6": web_scan()
        elif choice == "7": subdomain_scan()
        elif choice == "8": google_dork()
        elif choice == "9": mac_lookup()
        elif choice == "10": port_scan()
        elif choice == "11": pastebin_search()
        elif choice == "12": ssl_info()
        elif choice == "13": github_recon()
        elif choice == "0": 
            print(f"{Fore.RED}Exiting...")
            break
        else: print(f"{Fore.RED}[!] Pilihan tidak valid.")
            
        input(f"\n{Fore.BLUE}Tekan Enter untuk kembali...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
