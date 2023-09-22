from AppHandler import AppHandler_win32
from EmailManager import EmailManager

import time
import configparser


if __name__ == "__main__":
    # Load configs from local config.ini
    print("[AutoConnect] Load configs.")
    config = configparser.ConfigParser()
    config.read('config.ini')
    # -- cisco
    AppDirt = config.get('cisco', 'AppAppDirt').strip()  # App absolute directory
    AppPassword = config.get('cisco', 'AppPassword').strip()    # App password
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
    appHandler = AppHandler_win32(AppDirt)
    appHandler.open_app()
    appHandler.back_to_app(appHandler.app_hwnd)
    status = appHandler.check_status()
    
    # >> Homepage: Connected
    if status=="homepage_connected":
        print("[AppHandler] You are connected. Enjoy!")
    # >> Homepage: Disconnected
    elif status=="homepage_disconnected":
        appHandler.wait_status("homepage_disconnected")
        print("[AppHandler] >> Home")
        appHandler.click_buttom("Connect")
        print("[AppHandler] >> Home >> Click <Connect>")
        # >> Login
        appHandler.wait_status("login")
        print("[AppHandler] >> Login")
        appHandler.back_to_app(appHandler.hwnd_login)
        appHandler.shell.SendKeys(AppPassword)
        print("[AppHandler] >> Login >> Enter Password")
        time.sleep(1)
        appHandler.click_buttom("OK")
        # >> Auth
        appHandler.wait_status("auth")
        # Get Token
        print("[AppHandler] >> Auth >> Waiting for Token ...")
        em = EmailManager()
        em(EmailAccount, EmailPassword, FolderName, SenderEmailAccount)
        TOKEN = em.getToken()
        appHandler.back_to_app(appHandler.hwnd_auth)
        appHandler.shell.SendKeys(TOKEN)
        time.sleep(1)
        appHandler.click_buttom("Continue")
        print("[AppHandler] >> Auth >> Click <Continue>")
        # END
        print("[AppHandler] Service Launching. Enjoy!")
        time.sleep(2)