# -*- coding: utf-8 -*-

"""
ソケット通信におけるクライアント側の抽象クラスなどを定義
"""

import socket
from abc import ABCMeta, abstractmethod


class AbstractClient(ABCMeta):
    """AbstractClient
    ソケット通信におけるクライアント側の抽象基底クラス

    Args
        ABCMeta (_type_) ABCMeta
    """

    def __init__(self, bufsize: int = 4096, port: int = 50000, host: str = "localhost") -> None:
        self.busize = bufsize
        self.port = port
        self.host = host
        self._setting()

    @abstractmethod
    def _setting(self) -> None:
        client = socket.socket()
        self.client = client

    def connect(self) -> None:
        """create connection

        Args:
            host (str): ホスト名
            port (str): ポート番号
        """
        self.client.connect(self.host, self.port)

    def close(self) -> None:
        """close connection
        """
        self.client.close()

    def receive(self) -> str:
        """receive data fro remote host

        Returns:
            str: UTF8にデコード後の受信データ
        """
        recive_data = self.client.recv(self.busize)
        dec = recive_data.decode("UTF-8")
        return dec
