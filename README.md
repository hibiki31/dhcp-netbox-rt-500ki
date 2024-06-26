# DHCP Netbox PR-500KI

ホームゲートウェイ/ひかり電話ルータ (PR-500KI,RS-500KI,RT-500KI)のDHCPリリース情報を取得し、Netboxに書き込みます。

- 新規のリリース情報を追加
- IPに変更があった機器の上書き
- 削除されたリリース情報を削除


![image-20240626233412363](https://private-user-images.githubusercontent.com/35087924/343206069-de0d1a42-aca3-4b9a-b0dc-77d8da5cbc40.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTk0MTI2NjgsIm5iZiI6MTcxOTQxMjM2OCwicGF0aCI6Ii8zNTA4NzkyNC8zNDMyMDYwNjktZGUwZDFhNDItYWNhMy00YjlhLWIwZGMtNzdkOGRhNWNiYzQwLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MjYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjI2VDE0MzI0OFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWU3YzZlZGJhMjAwNjY3MzE5ZDZiNzVmMjQ5YzliM2U4NjIwZjNjNWM3ODgzYWRhODcyN2MzYTU0ZGZiZmNjZjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.uoQYtATpxugK4fhIbxEDrJXcQZUwnImkQ2vtxGuiRdM)
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

