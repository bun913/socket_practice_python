# -*- coding: utf-8 -*-

"""
クライアント側ソケット通信の実装2
トランスポート層としてはTCPを利用、IPv6の通信を想定

ソケット作成
ソケット設定とサーバーへの接続
データのやり取り
コネクションのクローズ
などクライアント側を想定したアクションを行う
"""

import socket
from interface.client import AbstractClient


class TcpIPv6(AbstractClient):

    def __init__(self, bufsize: int = 4096, port: int = 50000,
                 host: str = "localhost") -> None:
        super().__init__(bufsize, port, host)

    def _setting(self):
        """TCP/IPV6用の設定
        """
        client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        self.client = client
