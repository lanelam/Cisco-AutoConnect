__author__ = 'lane_lam'


from EmailManager import EmailManager

import win32com.client

import time
import configparser
import subprocess


if __name__ == "__main__":

    # Load configs from local config.ini
    print("[AutoConnect] Load configs.")
    config = configparser.ConfigParser()
    config.read('config.ini')
    # -- cisco
    dirt = config.get('cisco', 'dirt').strip()  # absolute App directory
    PASSWORD = config.get('cisco', 'pwd').strip()    # App password
    # -- outlook
    EmailAccount = config.get(
        'outlook', 'EmailAccount').strip()     # your email account
    EmailPassword = config.get(
        'outlook', 'EmailPassword').strip()     # your email password
    # your folder to receive Token emails
    FolderName = config.get('outlook', 'FolderName').strip()
    SenderEmailAccount = config.get(
        'outlook', 'SenderEmailAccount').strip()     # sender email address

    # Call App
    print("[AutoConnect] Calling Cisco app ...")
    process = subprocess.Popen(dirt)
    time.sleep(2)   # wait process initializing
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.AppActivate("Cisco AnyConnect Secure Mobility Client")
    print("[AutoConnect] Initializing service ...")
    time.sleep(5)   # wait service initializing
    shell.SendKeys("{TAB}")
    shell.SendKeys("{TAB}")
    shell.SendKeys("{TAB}")
    shell.SendKeys("{TAB}")
    shell.SendKeys("{TAB}")
    shell.SendKeys("{TAB}")
    shell.SendKeys("{ENTER}")
    time.sleep(5)   # wait Log in
    print("[AutoConnect] Enter Password.")
    shell.SendKeys(PASSWORD)
    shell.SendKeys("{ENTER}")

    # Get Token from Outlook
    print("[AutoConnect] Waiting for Token ...")
    em = EmailManager()
    em(EmailAccount, EmailPassword, FolderName, SenderEmailAccount)
    TOKEN = em.getToken()
    shell.SendKeys(TOKEN)
    shell.SendKeys("{ENTER}")
    print("[AutoConnect] Launching service ...")
    time.sleep(10)  # wait service launching

    # Terminate
    process.terminate()
    process.wait()
    print("[AutoConnect] Complete connection. Enjoy!")
