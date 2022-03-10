
import nmap
import ipaddress

# port_min = 0
# port_max = 65535

while True:
    ip= input("Entre o ip que voce quer scanear ")
    print()
    print("Entre as portas que deseja scanear, se desejar scanear tudo coloque 0")
    print()
    port_min = int(input("Enter port min: "))
    port_max = int(input("Enter port max: "))
    print()
    break
    

nm = nmap.PortScanner()

if port_min == 0 and port_max == 0:
    port_max = 65535

for porta in range(port_min, port_max + 1):
    try:
        
        resultado = nm.scan(ip, str(porta))
        # print(resultado)
        print()
        port_status = (resultado['scan'][ip]['tcp'][porta]['state'])
        port_service = (resultado['scan'][ip]['tcp'][porta]['name'])
        port_name = (resultado['scan'][ip]['hostnames'][0]['name'])
        port_state = (resultado['scan'][ip]['status']['state'])
        print(f"PORTA {porta} | STATUS {port_status} | SERVICO {port_service} | NAME {port_name} | STATE {port_state}")
    except:
        print(f"Nao pode abrir a porta {porta}.")
