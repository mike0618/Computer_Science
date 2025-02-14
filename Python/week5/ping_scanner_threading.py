import os
from pythonping import ping
from ipaddress import ip_network
from concurrent.futures import ThreadPoolExecutor
from rich import print
from rich.panel import Panel

results = []


def main():
    # print title
    print(Panel.fit("[bold magenta]Python Network Ping Scanner", border_style="cyan"))
    while True:
        # get ip addr or hostname
        print("[green]Enter Network (ex. 192.168.1.0/24):[/green]", end=" ")
        net_addr = input() or "10.0.0.0/24"
        # create a network address object from user input and scan
        hosts = list(ip_network(net_addr))
        L = len(hosts)
        with ThreadPoolExecutor(max_workers=L) as tpe:
            try:
                """Ping all IP addresses 1-254"""
                threads = [tpe.submit(scan, host) for host in hosts]
                [t.result() for t in threads]
            except KeyboardInterrupt:
                print("\nExit programm")
                tpe.shutdown(wait=False)
                os._exit(1)

        for res in sorted(results, key=lambda x: int(x.split()[0].replace(".", ""))):
            print(res)

        results.clear()
        print("Another scan? ([cyan]Y[/cyan]/[bold magenta]N[/bold magenta]):", end=" ")
        if input().strip().lower() != "y":
            break


def scan(host):
    host = str(host)
    try:
        res = ping(host, count=1, timeout=2)
        if res.success():
            results.append(
                f"{host:14}-> RTT: [bold cyan]{res.rtt_avg_ms:>6.2f}[/bold cyan]ms"
            )
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
