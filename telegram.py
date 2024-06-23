import requests

token = "7417294360:AAGL0XSFFIbinSG7O6qyshVoGIKvAZSb8Tc"
channel_id = "-1002211298841"
url = f'https://api.telegram.org/bot{token}/sendMessage'
params={
    "chat_id":channel_id,
    "text":"hey shristi"
}
r = requests.post(url,params=params)
print(r.json())

# r.josn show what message is send on terminal but only print r dont show it shows directly on telegram only

# import requests

# token = "7417294360:AAGL0XSFFIbinSG7O6qyshVoGIKvAZSb8Tc"
# channel_id = "-1002211298841"
# url = f'https://api.telegram.org/bot{token}/sendMessage'
# params={
#     "chat_id":channel_id,
#     "text":"<b>Hey shristi</b>",
#     "parse_mode":"HTML",
    
# }
# r = requests.post(url,params=params)
# print(r.json())

# 

import requests
token = "7417294360:AAGL0XSFFIbinSG7O6qyshVoGIKvAZSb8Tc"
url = "https://countriesnow.space/api/v0.1/cpuntries/captial"
tele_url = f'https://api.telegram.org/bot{token}/sendMessage'
channel_id = "-1002211298841"
country = requests.get(url=url)


for i in country.json(['data'][:10]):
    params ={
         "chat_id":channel_id,
        "text":f'country:{i["iso3"]}',
        "capital":{i["capital"]},
        "parse_mode":"HTML",
    }
r = requests.post(url=tele_url,params=params)
print(r.json())