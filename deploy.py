# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 18:01:40 2024

@author: aritr
"""

text_1 = ("Hago contenido con mucho esfuerzo, "
          "sería muy motivador si pudieras"
          "suscribirte a mi canal")
text_2 = "मेरा नाम अरित्र है। मई एक लड़का हूँ। "
text_3 = "Mera naam Aritra hai. Mai ek ladka huun"
text_4 = "আমার নাম অরিত্র। আমি একটা ছেলে।"
text_5 = "Amar naam Aritra. Ami ekta chele"

import requests


url = "http://127.0.0.1:8000/detection"


data = {"lang": text_5}


response = requests.post(url, json=data)


if response.status_code == 200:
    result = response.json()
    print("Detected language:", result["detected_language"])
else:
    print("Error:", response.status_code)
    print("Detail:", response.text)
