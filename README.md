# Pythonで実装しながら学ぶソケット通信

最近業務でソケット通信の理解が甘かったことを痛感しました。

こういうのは自分で実装しながら理解を深めるのが一番ということで以下書籍を購入して学習

https://www.amazon.co.jp/Python%E3%81%AB%E3%82%88%E3%82%8BTCP-IP%E3%82%BD%E3%82%B1%E3%83%83%E3%83%88%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-%E5%B0%8F%E9%AB%98-%E7%9F%A5%E5%AE%8F/dp/4274223248

書籍のサンプルコードは mainにコードを書いているが、せっかくなのでクラスで抽象化しながら実装してみる。

## ディレクトリ構成

```
.
├── diagram # draw.ioの図表などを格納
├── input # 基礎知識などのインプット
└── output
    ├── interface # 抽象基底クラスを定義
    └── tcp # tcpの通信用の実装を格納
```

## 基本編の使い方

基本的なソケット通信によるサーバー・クライアントの実装

### TCPによる通信

ipv4での通信

```bash
# サーバー起動
python3 tcp_sever.py ipv4
# クライアントからサーバーにアクセス
python3 tcp_clinet.py ipv4

# サーバー側表示
2022-02-20 11:44:42.796248 接続要求受信
<socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 50000), raddr=('127.0.0.1', 59705)>
('127.0.0.1', 59705)
# クライアント側表示
2022-02-20 11:47:01.218339
```

ipv6での通信

```bash
# サーバー起動
python3 tcp_sever.py ipv6
# クライアントからサーバーにアクセス
puython3 tcp_client.py ipv6
# クライアント側表示
2022-02-20 11:44:42.796248

# サーバー側表示
2022-02-20 11:39:19.132355 接続要求受信
<socket.socket fd=3, family=AddressFamily.AF_INET6, type=SocketKind.SOCK_STREAM, proto=0, laddr=('::1', 50000, 0, 0), raddr=('::1', 59687, 0, 0)>
('::1', 59687, 0, 0)
```
