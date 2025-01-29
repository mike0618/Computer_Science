from pythonping import ping
from ipaddress import ip_network


def main():
    # print title
    title = "|      Python Network Ping Scanner      |"
    print(len(title) * "-")
    print(title)
    print(len(title) * "-")
    # get ip addr or hostname
    net_addr = input("Enter single IP address or hostname: ") or "10.0.0.0/24"
    # create a network address object from user input and scan
    scan(ip_network(net_addr))


def scan(hosts):
    """Ping all IP addresses 1-254"""
    for host in hosts:
        host = str(host)
        try:
            res = ping(host, count=1, timeout=2)
            if res.success():
                print(f"{host:14}-> RTT: {res.rtt_avg_ms:>6.2f}ms")
            else:
                print(f"{host:14}inactive")
        except KeyboardInterrupt:
            print("Exit programm")
            return False
        except Exception as e:
            print("Sorry", e)
            return False


if __name__ == "__main__":
    main()
