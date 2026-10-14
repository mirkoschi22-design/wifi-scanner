"""
SCANNER WiFi v3 - Detector de Intrusos
Copyright (c) 2026 Mirko David Schiavi
Licensed under MIT License
https://github.com/mirkoschi22-design/scanner
"""
import socket
import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

print("=== SCANNER WiFi v3 - Detector de Intrusos ===\n")

# Detecta tu IP automaticamente
hostname = socket.gethostname()
mi_ip = socket.gethostbyname(hostname)
print(f"Tu IP es: {mi_ip}")

# Asume que tu red es /24 (ej: 192.168.0.xxx)
red = str(ipaddress.IPv4Network(mi_ip + '/24', strict=False))
print(f"Escaneando red: {red}\n")

vivos = []

def pingear(ip):
    try:
        # Hace ping a cada IP
        resultado = subprocess.call(f"ping -n 1 -w 1000 {ip}",
                                    stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL, shell=True)
        if resultado == 0:
            try:
                nombre = socket.gethostbyaddr(str(ip))[0]
            except:
                nombre = "Desconocido"
            vivos.append((str(ip), nombre))
            print(f"[CONECTADO] {ip} - {nombre}")
    except:
        pass

ips = list(ipaddress.IPv4Network(red).hosts())

print("Buscando dispositivos... (tarda 20 seg)\n")
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(pingear, ips)

print("\n" + "="*40)
print(f"Se encontraron {len(vivos)} dispositivos:")
for ip, nombre in vivos:
    print(f" - {ip} | {nombre}")

# Guarda reporte
with open("reporte_wifi.txt", "w") as f:
    f.write(f"Dispositivos en red {red}\n")
    for ip, nombre in vivos:
        f.write(f"{ip} - {nombre}\n")

print("\nReporte guardado en reporte_wifi.txt")
print("Revisa si conoces todos los dispositivos. Si hay uno raro, cambia la clave del WiFi.")