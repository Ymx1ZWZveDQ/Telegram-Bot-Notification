import requests
import base64

def tele_noti_bot(bot_message):
#####
   b64t = "<BASE64_TELEGRAM_API_TOKEN>"
   b64id = "<BASE64_TELEGRAM_USERID>"
   token = base64.b64decode(b64t)
   uID = base64.b64decode(b64id)
   tokenString = str(token, "utf-8")
   uIDString = str(uID, "utf-8")
#####
   send_text = 'https://api.telegram.org/bot' + tokenString + '/sendMessage?chat_id=' + uIDString + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()


test = tele_noti_bot("Test Notification")
print(test)
