import httpx
from datetime import datetime
import os

def get_oui_dict():
    """
    OUI（Organizationally Unique Identifier）の辞書を取得する関数。

    この関数はIEEEのOUI標準データをダウンロードし、ローカルファイルに保存します。
    ローカルファイルが既に存在する場合は再ダウンロードを行わず、既存のファイルを使用します。
    ファイルからデータを読み取り、MACアドレスをキーとして関連情報を含む辞書を作成します。

    戻り値:
    dict: OUIデータを含む辞書。キーはMACアドレスで、値は関連企業情報のリスト。
    """
    date_flag = datetime.now().strftime("%Y%m%d")
    dui_file = f"./oui.{date_flag}.txt"

    if not os.path.exists(dui_file):
        res = httpx.get(url="https://standards-oui.ieee.org/")
        with open(dui_file, "w") as f:
            f.write(res.text)

    data = {}
    with open(dui_file) as f:
        i = 0
        for s_line in f:
            i = i + 1
            if i < 5:
                continue
            p = i % 6
            if p == 0:
                mac = s_line.split("     (base 16)\t\t")[0].strip("\n")
                inc = s_line.split("     (base 16)\t\t")[1].strip("\n")
                data[mac] = [inc]

            if p == 1:
                if s_line == "\n":
                    i = i + 3

            if p == 3:
                ccltd = s_line.strip()
                data[mac].append(ccltd)


    return data