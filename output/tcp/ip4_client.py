# -*- coding: utf-8 -*-

"""
クライアント側ソケット通信の実装1
トランスポート層としてはTCPを利用、IPv4の通信を想定

ソケット作成
ソケット設定とサーバーへの接続
データのやり取り
コネクションのクローズ
などクライアント側を想定したアクションを行う
"""

import socket
from interface.client import AbstractClient


class TcpIPv4(AbstractClient):

    def __init__(self, bufsize: int = 4096, port: int = 50000,
                 host: str = "localhost") -> None:
        super().__init__(bufsize, port, host)

    def _setting(self):
        """TCP/IPV4用の設定
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = client
