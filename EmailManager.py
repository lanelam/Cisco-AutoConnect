__author__ = 'lanelam'

import outlook

import time
import re
from datetime import datetime, timedelta
from typing import Any


class EmailManager:
    def __init__(self) -> None:
        pass

    def __call__(self, EmailAccount, EmailPassword, FolderName,
                 SenderEmailAccount="hku2fa@hku.hk") -> Any:
        self.EmailAccount = EmailAccount
        self.EmailPassword = EmailPassword
        self.FolderName = FolderName
        self.SenderEmailAccount = SenderEmailAccount
        print(f">>[EmailManager] My Email: <{self.EmailAccount}>")
        print(f">>[EmailManager] My Folder: <{self.FolderName}>")
        print(f">>[EmailManager] Sender Email: <{self.SenderEmailAccount}>")

    def getToken(self) -> str:
        """ Get Token from latest 2FA Email. """
        requestTime = getTime()
        self.client = outlook.Outlook()
        self.client.login(self.EmailAccount, self.EmailPassword)
        self.client.select(self.FolderName)
        while True:
            print(
                ">>[EmailManager] Listening Auth Email ...")
            time.sleep(5)
            # Read Latest Token Email
            mail = self.readNewEmail()
            if mail is not None:
                # Get received time and token
                receivedTime, token = parseEmail(mail)
                # >> Token?
                if token is None:
                    continue
                # >> New receive?
                isNew = isNewReceive(requestTime, receivedTime)
                if isNew:
                    print(f">>[EmailManager] Token Retreival: <{token}>")
                    break
        self.client.logout()
        return token

    def readNewEmail(self):
        """ Get latest Auth Email. """
        # Get latest 5 email
        latest_emails = self.client.readMulti(k=5)
        latest_emails.reverse()  # desc by receivedTime

        # Get latest email from Sender
        for latest_email in latest_emails:
            # Parse response
            response = dict(latest_email._headers)
            _From = response["From"]
            if _From == self.SenderEmailAccount:
                return latest_email
        return None


def getTime():
    """ Get current time in format: 'yyyy-mm-dd HH:MM:SS'. """
    return str(datetime.now())[:-7]


def parseEmail(mail):
    """ Parse email to retreive ReceivedTime and Token. """
    # Parse response
    response = dict(mail._headers)
    _Subject = response["Subject"]
    # >> Date: formatted str
    _Date = response["Date"]
    _dt = datetime.strptime(_Date, "%a, %d %b %Y %H:%M:%S %z")
    _dt += timedelta(seconds=15)   # simulate a latency
    receivedTime = _dt.strftime("%Y-%m-%d %H:%M:%S")
    # >> Subject: find longest digit from subject
    subject = _Subject.strip()
    tokens = re.findall(r"\d+", subject)
    token = max(tokens, key=len) if tokens else None
    return receivedTime, token


def isNewReceive(requestTime: str, receivedTime: str):
    """ Check timeliness. Basically comparing 'requestTime' and 'receivedTime' by str method. """
    return True if receivedTime >= requestTime else False
