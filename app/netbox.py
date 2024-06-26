from pydantic_settings import BaseSettings
from pydantic import Field
import httpx
from bs4 import BeautifulSoup
from oui import get_oui_dict
from settings import sts
import ipaddress

HEADERS = {"Authorization": f"Token {sts.netbox_token}"}

# IPレンジ内のIPアドレスをリストアップする関数
def list_ips_in_range():
    """
    IPレンジ内のIPアドレスをリストアップする関数。

    この関数はNetBoxのAPIを呼び出し、指定されたDHCPプレフィックスに含まれる
    IPアドレスのリストを取得します。APIリクエストには事前に定義されたURLと
    ヘッダーを使用します。

    戻り値:
    dict: レスポンスのJSONデータを含む辞書。
    """
    url = f"{sts.netbox_url}/api/ipam/ip-addresses/?parent={sts.netbox_dhcpprefix}"
    res = httpx.get(url=url, headers=HEADERS)
    return res.json()