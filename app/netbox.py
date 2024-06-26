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
    url = f"{sts.netbox_url}/api/ipam/ip-addresses/?parent={sts.netbox_dhcpprefix}"
    res = httpx.get(url=url, headers=HEADERS)
    return res.json()