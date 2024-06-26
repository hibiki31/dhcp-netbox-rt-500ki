# DHCP Netbox PR-500KI

ホームゲートウェイ/ひかり電話ルータ (PR-500KI,RS-500KI,RT-500KI)のDHCPリリース情報を取得し、Netboxに書き込みます。

- 新規のリリース情報を追加
- IPに変更があった機器の上書き
- 削除されたリリース情報を削除

## Quick Start

> Docker composeを利用します。事前にインストールしてください。

.envを作成します

```
HOST_ADDRESS="192.168.X.X"
HOST_USERNAME="user"
HOST_PASSWORD="pass"
NETBOX_URL="http://example.com:8000"
NETBOX_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
NETBOX_DHCPPREFIX="192.168.X.X/26"
WAIT_SECONDS=600
```

| 環境変数名        | 内容                                                         |
| ----------------- | ------------------------------------------------------------ |
| HOST_ADDRESS      | 192.168.0.1 ルータのアドレス                                 |
| HOST_USERNAME     | ルータのBasic認証 ユーザ名                                   |
| HOST_PASSWORD     | ルータのBasic認証 ユーザ名                                   |
| NETBOX_URL        | http://example.com:8000などエンドポイントを指定します。      |
| NETBOX_TOKEN      | Netboxのトークンを取得して利用してください。                 |
| NETBOX_DHCPPREFIX | DHCP Range/Prefix。DHCPで取得したIPに含まれてないIPは削除されます。DHCPアドレスが返却されたときの処理のためです。 |
| WAIT_SECONDS      | 実行間隔を秒で指定します。実際には実行時間が加算されるため厳密にこの指定時間おきに実行されるわけではありません。 |

ビルドを行います。

```
docker compose build
```

起動します。

```
docker compose up -d
```

