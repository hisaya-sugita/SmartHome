# -*- coding: utf-8 -*-
import requests
import time

HUE_API = 'http://192.168.1.2/api/bCQvM-LF70eAr6TDQtKCE3qxiu5x7BCSWEDgfbDH/lights'

requests.put(HUE_API + '/4/state',
             json={"on": True, "bri": 128, "xy": [0.48, 0.41]})

time.sleep(5)

requests.put(HUE_API + '/4/state', json={"on": False})
