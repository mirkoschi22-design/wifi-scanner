# WiFi Scanner - Detector de Intrusos

Mi primer proyecto de ciberseguridad. Un scanner en Python para auditar mi red doméstica y detectar dispositivos conectados.

## 🚀 Qué hace

- **v1 (scanner.py):** Escanea puertos abiertos en un objetivo.
- **v3 (scanner_v3.py):** Escanea toda la red local (192.168.101.x) y detecta todos los dispositivos conectados, con nombre de host.

## 🛠️ Tecnologías

- Python 3.14
- socket, subprocess, threading
- ARP / ICMP (ping)

## 📋 Cómo usarlo

```bash
# Ejecutar como administrador para mejor detección
python scanner_v3.py