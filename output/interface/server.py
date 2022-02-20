# -*- coding: utf-8 -*-

"""
ソケット通信におけるサーバー側の抽象クラスなどを定義
"""

import socket
from abc import ABCMeta, abstractmethod


class AbstractServer(metaclass=ABCMeta):
    """AbstractServer
    ソケット通信におけるサーバー側の抽象基底クラス

    Args
        ABCMeta (_type_) ABCMeta
    """

    def __init__(self, port: int = 50000) -> None:
        self.port = port
        self._setting()
        self._bind()

    @abstractmethod
    def _setting(self) -> None:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server

    def _bind(self) -> None:
        """bind処理
        """
        self.server.bind(("", self.port))

    def listen(self) -> None:
        """応答を待ち受け続ける
        """
        self.server.listen()
        while True:
            client, addr = self.server.accept()
            msg = self.do()
            client.sendall(msg.encode("UTF-8"))
            print(msg, "接続要求受信")
            print(client)
            print(addr)
            client.close()

    @abstractmethod
    def do(self):
        """サーバー側処理
        サーバー側で必要な処理を記載する
        何がしかの情報を返却
        """
        return "Do Something"

    def close(self) -> None:
        """close connection
        """
        self.client.close()
