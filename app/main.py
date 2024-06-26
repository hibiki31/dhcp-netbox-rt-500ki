import httpx
from settings import sts
from netbox import list_ips_in_range
from scraper import scrap_dhcp

def main():
    dhcp_list = scrap_dhcp()
    netbox_address = list_ips_in_range()

    nh = {"Authorization": f"Token {sts.netbox_token}"}

    # DHCPでリースしたIPをPUTすることで、上書きする
    for dhcp_ip in dhcp_list:
        exist_ip = search_dict_in_list(netbox_address["results"], "address", dhcp_ip["ip"])

        post_json = {
            "address": dhcp_ip["ip"],
            "status": "dhcp",
            "vrf": 1,
            "description": f"{dhcp_ip['mac']} ({dhcp_ip['vender'][0]})"
        }

        if exist_ip == []:
            res = httpx.post(url=f"{sts.netbox_url}/api/ipam/ip-addresses/",json=post_json,headers=nh)
        else:
            res = httpx.put(url=f"{sts.netbox_url}/api/ipam/ip-addresses/",json=post_json,headers=nh)

    # レンジ内で、DHCPに登録がないIP（変わったりリリースされたIP）を削除する
    for netbox_ip in netbox_address["results"]:

        serach_ip = search_dict_in_list(dhcp_list, "ip", netbox_ip["address"])
        if serach_ip != []:
            continue

        res = httpx.delete(url=f"{sts.netbox_url}/api/ipam/ip-addresses/{netbox_ip['id']}",headers=nh)

    print(dhcp_list)

def search_dict_in_list(dict_list, key, value):
    """
    辞書のリストから指定されたキーと値に一致する辞書を検索します。

    Args:
    dict_list (list): 辞書が含まれるリスト
    key (str): 検索対象のキー
    value: 検索対象の値

    Returns:
    list: 一致する辞書のリスト
    """
    return [d for d in dict_list if key in d and d[key] == value]

if __name__ == "__main__":
    main()