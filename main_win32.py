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
    AppDirt = config.get('cisco', 'AppDirt').strip()  # App absolute directory
    AppUsername = config.get('cisco', 'AppUsername').strip()    # App username
    AppPassword = config.get('cisco', 'AppPassword').strip()    # App password
    # -- outlook
    EmailAccount = config.get('outlook', 'EmailAccount').strip()     # your email account
    EmailPassword = config.get('outlook', 'EmailPassword').strip()     # your email password
    FolderName = config.get('outlook', 'FolderName').strip()    # your folder to receive Token emails
    SenderEmailAccount = config.get('outlook', 'SenderEmailAccount').strip()    # sender email address
    
    # Call App
    appHandler = AppHandler_win32(AppDirt)
    appHandler.open_app()
    status = appHandler.check_status()
    # >> Homepage: Connected
    if status=="homepage_connected":
        pass
    # >> Homepage: Disconnected
    elif status=="homepage_disconnected":
        appHandler.wait_status("homepage_disconnected")
        print("[AppHandler] >> Home")
        appHandler.click_buttom("Connect")
        print("[AppHandler] >> Home >> Click <Connect>")
        # >> Login
        appHandler.wait_status("login")
        print("[AppHandler] >> Login")
        appHandler.enter_text(AppUsername,"Username")
        print("[AppHandler] >> Login >> Enter <Username>")
        appHandler.enter_text(AppPassword,"Password")
        print("[AppHandler] >> Login >> Enter <Password>")
        appHandler.click_buttom("OK")
        # >> Auth
        appHandler.wait_status("auth")
        # Get Token
        print("[AppHandler] >> Auth >> Waiting for Token ...")
        em = EmailManager()
        em(EmailAccount, EmailPassword, FolderName, SenderEmailAccount)
        TOKEN = em.getToken()
        appHandler.back_to_app(appHandler.hwnd_auth)
        appHandler.enter_text(TOKEN,"Token")
        print("[AppHandler] >> Auth >> Enter <Token>")
        appHandler.click_buttom("Continue")
        print("[AppHandler] >> Auth >> Click <Continue>")
        # Wait service launching
        print("[AppHandler] Service Launching...")
        time.sleep(5)
    # END
    print("[AppHandler] You are connected. Enjoy!")
    time.sleep(2)