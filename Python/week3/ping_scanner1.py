from pythonping import ping


def main():
    # print title
    title = "|      Python Network Ping      |"
    print(len(title) * "-")
    print(title)
    print(len(title) * "-")
    # get ip addr or hostname
    host_addr = input("Enter single IP address or hostname: ")
    # ping host address
    print(ping(host_addr))


if __name__ == "__main__":
    main()
