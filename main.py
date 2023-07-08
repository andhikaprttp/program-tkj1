import subprocess
from colorama import Fore, Style

def konversi_bilangan():
    while True:
        try:
            desimal = int(input("Masukkan bilangan desimal: "))
            print("Bilangan biner:", Fore.GREEN, bin(desimal), Style.RESET_ALL)
            print("Bilangan oktal:", Fore.GREEN, oct(decimal), Style.RESET_ALL)
            print("Bilangan heksadesimal:", Fore.GREEN, hex(decimal), Style.RESET_ALL)
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan bilangan desimal.")

def ipcalc():
    ip_address = input("Masukkan alamat IP: ")
    subnet_mask = input("Masukkan subnet mask: ")
    result = subprocess.run(['ipcalc', '-n', '-b', ip_address, subnet_mask], capture_output=True, text=True)
    print(result.stdout)

def cek_port_terbuka():
    remote_host = input("Masukkan alamat host: ")
    port = input("Masukkan nomor port: ")
    result = subprocess.run(['nc', '-z', '-v', remote_host, port], capture_output=True, text=True)
    if 'succeeded!' in result.stdout:
        print(Fore.GREEN + "Port terbuka" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Port tertutup" + Style.RESET_ALL)

def whois():
    domain = input("Masukkan nama domain: ")
    result = subprocess.run(['whois', domain], capture_output=True, text=True)
    print(result.stdout)

def konfigurasi_mikrotik():
    print("Berikut adalah langkah-langkah konfigurasi MikroTik:")
    print("1. Masuk ke router MikroTik menggunakan SSH atau Winbox.")
    print("2. Konfigurasi jaringan dengan menentukan alamat IP dan subnet mask.")
    print("3. Mengaktifkan layanan yang diinginkan seperti DHCP, firewall, atau VPN.")
    print("4. Mengatur kebijakan akses jaringan dan pengaturan keamanan.")
    print("5. Simpan konfigurasi dan reboot router jika diperlukan.")

def netstat():
    result = subprocess.run(['netstat', '-tuln'], capture_output=True, text=True)
    print(result.stdout)

def dig():
    domain = input("Masukkan nama domain: ")
    result = subprocess.run(['dig', domain], capture_output=True, text=True)
    print(result.stdout)

def traceroute():
    host = input("Masukkan alamat host: ")
    result = subprocess.run(['traceroute', host], capture_output=True, text=True)
    print(result.stdout)

def ifconfig():
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    print(result.stdout)

def print_banner():
    banner = r"""

█████████████████████████
█─▄─▄─█▄─█─▄███▄─▄███▀░██
███─████─▄▀██─▄█─█████░██
▀▀▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▀▀▀▀▄▄▄▀                                        
    """
    print(Fore.YELLOW + banner + Style.RESET_ALL)

while True:
    print_banner()
    print("Selamat datang di Program TKJ 1")
    print("SMK RADEN PAKU")
    print("1. Konversi Sistem Bilangan")
    print("2. IPCALC")
    print("3. Cek Port Terbuka")
    print("4. Whois")
    print("5. Konfigurasi MikroTik")
    print("6. Netstat")
    print("7. Dig")
    print("8. Traceroute")
    print("9. Ifconfig")
    print("0. Keluar")

    pilihan = input("Silakan pilih fitur yang ingin Anda gunakan (0-9): ")

    if pilihan == "1":
        konversi_bilangan()
    elif pilihan == "2":
        ipcalc()
    elif pilihan == "3":
        cek_port_terbuka()
    elif pilihan == "4":
        whois()
    elif pilihan == "5":
        konfigurasi_mikrotik()
    elif pilihan == "6":
        netstat()
    elif pilihan == "7":
        dig()
    elif pilihan == "8":
        traceroute()
    elif pilihan == "9":
        ifconfig()
    elif pilihan == "0":
        print("Terima kasih telah menggunakan Program TKJ 1!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih nomor fitur yang tersedia.")
      
# XI TKJ 1 | SMK RADEN PAKU 