from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    アプリケーション設定を管理するクラス。

    このクラスはホストのアドレス、認証情報、NetBoxのURLとトークン、
    DHCPプレフィックス、待機時間などの設定を環境変数から読み込みます。

    属性:
    host_address (str): ホストのアドレス。
    host_username (str): ホストのユーザー名。
    host_password (str): ホストのパスワード。
    netbox_url (str): NetBoxのURL。
    netbox_token (str): NetBoxのトークン。
    netbox_dhcpprefix (str): DHCPプレフィックス。
    wait_seconds (int): 待機時間（秒）。

    クラス属性:
    Config: 設定クラス。
        env_file (str): 環境変数ファイルのパス。
        case_sensitive (bool): 大文字小文字の区別を行うかどうか。
    """
    host_address: str
    host_username: str
    host_password: str
    netbox_url: str
    netbox_token: str
    netbox_dhcpprefix: str
    wait_seconds:int

    class Config:
        env_file = ".env"
        case_sensitive = False

sts = Settings()