import sys

from tcp.ip4_client import TcpIPv4
from tcp.ip6_client import TcpIPv6

if __name__ == "__main__":
    #　第１引数に ipv4 または ipv6を指定
    args = sys.argv
    ip_family = args[1]

    if ip_family not in set(["ipv4", "ipv6"]):
        print("ipv4あたはipv4を指定してください")
        sys.exit(1)

    client = TcpIPv4()
    if ip_family == "ipv6":
        client = TcpIPv6()
    # 接続と情報の受信
    client.connect()
    data = client.receive()
    print(data)
