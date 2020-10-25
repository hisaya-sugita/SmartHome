# -*- coding: utf-8 -*-
import requests
import time
import settings

HUE_API_PATH = settings.HUE_API_PATH

for i in range(10):
    requests.put(HUE_API_PATH + "/groups/" + str(i) + "/action",
                json={"on": False})

time.sleep(5)

for i in range(10):
    requests.put(HUE_API_PATH + "/groups/" + str(i) + "/action",
                json={"on": True, "bri": 255, "ct": 255})
