import socket

def scan_ports(results, start=1, end=1024):
    target = results["target"]
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Could not resolve {target}")
        return

    print(f"[*] Scanning {ip} ports {start}-{end}...")
    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        if s.connect_ex((ip, port)) == 0:
            results["ports"].append(port)
            print(f"[+] Port {port} open")
        s.close()