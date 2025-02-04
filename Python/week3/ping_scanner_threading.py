from pythonping import ping
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor

results = []


def main():
    # print title
    title = "|      Python Network Ping Scanner      |"
    print(len(title) * "-")
    print(title)
    print(len(title) * "-")
    # get ip addr or hostname
    net_addr = input("Enter single IP address or hostname: ") or "10.0.0.0/24"
    # create a network address object from user input and scan
    hosts = list(ip_network(net_addr))
    L = len(hosts)
    with ThreadPoolExecutor(max_workers=L) as tpe:
        """Ping all IP addresses 1-254"""
        threads = [tpe.submit(scan, host) for host in hosts]
        [t.result() for t in threads]
    for res in sorted(results, key=lambda x: int(x.split()[0].split(".")[3])):
        print(res)


def scan(host):
    host = str(host)
    try:
        res = ping(host, count=1, timeout=2)
        if res.success():
            results.append(f"{host:14}-> RTT: {res.rtt_avg_ms:>6.2f}ms")
            # print(f"{host:14}-> RTT: {res.rtt_avg_ms:>6.2f}ms")
        # else:
        #     print(f"{host:14}inactive")
    except KeyboardInterrupt:
        print("Exit programm")
        return False
    except Exception as e:
        print("Sorry", e)
        return False


if __name__ == "__main__":
    main()
