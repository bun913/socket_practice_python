# -*- coding: utf-8 -*-

"""
サーバー側ソケット通信の実装1
トランスポート層としてはTCPを利用、IPv4の通信を想定
"""

import socket
from datetime import datetime
from interface.server import AbstractServer


class TcpIPv4Server(AbstractServer):
    """TCP/IPV4による通信のサーバー側実装1

    Args:
        AbstractServer (_type_): サーバー側抽象基底クラス
    """

    def __init__(self, port: int = 50000) -> None:
        super().__init__(port=port)

    def _setting(self):
        """TCP/IPV4用の設定
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server

    def do(self) -> str:
        """現在時刻を返却する

        Returns:
            str: 現在時刻
        """
        return str(datetime.now())
