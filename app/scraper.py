import httpx
from bs4 import BeautifulSoup
from oui import get_oui_dict
from settings import sts

def scrap_dhcp():
    """
    DHCPサーバーからリース情報をスクレイピングする関数。

    この関数はDHCPサーバーのウェブページからリース情報を取得し、MACアドレス
    のOUIを基にベンダー情報を追加します。リース情報は辞書のリストとして
    返されます。

    戻り値:
    list: リース情報を含む辞書のリスト。各辞書にはIPアドレス、MACアドレス、
          リリース時間、ベンダー情報が含まれます。
    """
    oui_dict = get_oui_dict()

    auth = httpx.BasicAuth(
        username=sts.host_username, 
        password=sts.host_password
    )
    url = f"http://{sts.host_address}/ntt/information/dhcpV4Server"
    res = httpx.get(url=url, auth=auth)

    soup = BeautifulSoup(res.text, 'html.parser')

    data_table = soup.find('table', {'class': 'data'}).find('tbody')
    rows = data_table.find_all('tr')
    lease_info = []
    for row in rows:
        cols = row.find_all('td')
        mac_oui = str(cols[1].text).replace(":","").upper()[0:6]
        
        try:
            mac_vender = oui_dict[mac_oui]
        except:
            mac_vender = None

        lease_info.append({
            'ip': cols[0].text,
            'mac': cols[1].text,
            'release': cols[2].text,
            'vender': mac_vender
        })
    return lease_info