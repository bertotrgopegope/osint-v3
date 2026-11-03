
<div align="center">
  <img src="https://raw.githubusercontent.com/bertotrgopegope/osint-v3/main/4d29cd62eae542edc1ba840085d22d48.jpg" alt="OSINT V3 Banner" width="100%">
  
  <br>

  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=30&pause=1000&color=0088FF&center=true&vCenter=true&width=600&lines=OSINT+FRAMEWORK+V3;Author:+MR+ROBERTO;Super+Lengkap+%26+Powerful" alt="Typing SVG" />
  </a>

  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Termux-Supported-black?style=for-the-badge&logo=android&logoColor=white" alt="Termux">
    <img src="https://img.shields.io/badge/Version-3.0-blue?style=for-the-badge" alt="Version">
  </p>

  <p><i>An advanced Command-Line OSINT (Open Source Intelligence) tool designed for Termux and Linux.</i></p>
</div>

---

## 🚀 Features
- **[1] IP Tracker & Geolocation** - Lacak lokasi, ISP, dan koordinat Maps.
- **[2] Phone Number Info** - Cek operator dan region nomor HP.
- **[3] DNS & Whois Lookup** - Tarik record DNS dan info pendaftar domain.
- **[4] Username Checker** - Cek eksistensi username di berbagai platform.
- **[5] Email Breach Check** - Cek kebocoran email via HIBP.
- **[6] Web Tech & Headers Scan** - Analisa server, header, dan judul web.
- **[7] Subdomain Scanner** - Cari subdomain aktif.
- **[8] Google Dorking Generator** - Bikin query pencarian celah.
- **[9] MAC Address Lookup** - Cek vendor dari MAC Address.
- **[10] IP Port Scanner** - Scan port umum yang terbuka.
- **[11] Pastebin Search** - Cari data bocor di Pastebin.
- **[12] SSL Certificate Info** - Cek masa berlaku dan penerbit SSL.
- **[13] GitHub User Recon** - Tarik info profil GitHub target.

## 🛠️ Installation

1. Update Termux packages and install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python chafa -y
```

2. Install required Python libraries:
   ```bash
   pip install requests beautifulsoup4 phonenumbers dnspython colorama urllib3
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/bertotrgopegope/osint-v3.git
   cd osint-v3
   ```

💻 Usage

Run the script:

```bash
python osint_v3.py
```

⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only. Do not use it on targets without written permission. The author is not responsible for any misuse.
