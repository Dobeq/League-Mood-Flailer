# -*- coding: utf-8 -*-1:50 2018

import requests, time, passgetter
message = input("enter your largest mood: ")
creds = passgetter.getCreds()
while True:
    mood = message
    for i in range(2):
        for i in range(len(mood)):
            mood = mood[:i] + mood[i].swapcase() + mood[i + 1:]
            headerjson={"Accept": "application/json"}
            req = requests.put(
                    "https://127.0.0.1:" + creds[0] + "/lol-chat/v1/me",
                    json={"statusMessage":mood},
                    verify=False,
                    headers=headerjson,
                    auth=('riot', creds[1]))
            print(req.status_code)
            time.sleep(.2)