import sys

from tcp.ip4_sever import TcpIPv4Server
from tcp.ip6_server import TcpIPv6Server

if __name__ == "__main__":
    #　第１引数に ipv4 または ipv6を指定
    args = sys.argv
    ip_family = args[1]

    if ip_family not in set(["ipv4", "ipv6"]):
        print("ipv4あたはipv4を指定してください")
        sys.exit(1)

    server = TcpIPv4Server()
    if ip_family == "ipv6":
        server = TcpIPv6Server()
    server.listen()
