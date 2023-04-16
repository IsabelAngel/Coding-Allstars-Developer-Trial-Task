# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:05:45 2023

@author: ASUS
"""
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
from langdetect import detect, DetectorFactory
from urllib.error import HTTPError, URLError
from urllib3.exceptions import SSLError
import ssl 

def func(string):
    DetectorFactory.seed = 0
    language = detect(" ".join(' '.join(string.splitlines()).split()))  
    return language


df = pd.read_csv('Trial Task Sample URLs.csv', on_bad_lines='skip', sep= ';')

iterador = 0
for item in df.URL.values.tolist():
    try:
        print(item)
        url = df.URL.values.tolist()[iterador]
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        texto = func(soup.get_text())
        print(texto)
    except HTTPError:
        print("Página Inexistente")
        continue
    except ValueError:
        print("Unknown url type: " + item)
    except SSLError:
        print("Certificate has expired: " + item)
    except URLError:
        print("Certificate verify failed: certificate has expired: " + item)
    finally:
        iterador += 1

imagenes = []
for image in soup.find_all("img"):
    imagenes.append(image)
    
# imagenes = soup.find_all("img")

# lista_url = df.URL.values.tolist()