import outlook
from datetime import datetime


mail = outlook.Outlook()
mail.login('lanelamzc@outlook.com', 'Abcde0415.')
mail.select("HKU 2FA")

# Get Latest email
latest_email = mail.read()

# Parse response
response = dict(latest_email._headers)
_From = response["From"]
_Subject = response["Subject"]
_Date = response["Date"]
# >> datetime
_dt = datetime.strptime(_Date, "%a, %d %b %Y %H:%M:%S %z")
_dtn = datetime.now().replace(tzinfo=_dt.tzinfo)


print("END")
