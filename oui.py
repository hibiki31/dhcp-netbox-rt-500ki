import httpx
from datetime import datetime
import os

def get_oui_dict():
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