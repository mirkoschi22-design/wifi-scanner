import socket
from datetime import datetime

servicios = {21:"FTP", 22:"SSH", 23:"Telnet (INSEGURO)", 80:"HTTP Web", 443:"HTTPS Web", 3306:"MySQL", 8080:"Proxy Web"}

objetivo = input("IP a escanear: ")
print(f"\n--- Escaneando {objetivo} {datetime.now()} ---\n")

abiertos = []
for puerto, nombre in servicios.items():
    s = socket.socket()
    s.settimeout(1)
    if s.connect_ex((objetivo, puerto)) == 0:
        print(f"[ABIERTO] {puerto} -> {nombre}")
        abiertos.append(f"{puerto} - {nombre}")
    s.close()

# Guarda reporte
with open("reporte_escaneo.txt", "w") as f:
    f.write(f"Reporte para {objetivo} - {datetime.now()}\n")
    if abiertos:
        f.write("\n".join(abiertos))
    else:
        f.write("Todo cerrado - seguro\n")

print("\nReporte guardado en reporte_escaneo.txt")