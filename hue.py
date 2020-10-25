# -*- coding: utf-8 -*-
import requests
import time
import settings

HUE_API_PATH = settings.HUE_API_PATH

requests.put(HUE_API_PATH + '/lights/4/state',
             json={"on": True, "bri": 128, "xy": [0.48, 0.41]})

time.sleep(5)

requests.put(HUE_API_PATH + '/lights/4/state', json={"on": False})
