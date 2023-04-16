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
identifiedLanguage = []
for item in df.URL.values.tolist():
    try:
        url = df.URL.values.tolist()[iterador]
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        if func(soup.get_text()) == "hi":
            identifiedLanguage.append("PASS: " + func(soup.get_text()))
        else:
            identifiedLanguage.append("FAIL: " + func(soup.get_text()))
    except HTTPError:
        # print("HTTPError: Not Found")
        identifiedLanguage.append("FAIL: HTTPError: Not Found")
        continue
    except ValueError:
        # print("Unknown url type: " + item)
        identifiedLanguage.append("FAIL: Unknown url type")
    except SSLError:
        # print("Certificate has expired: " + item)
        identifiedLanguage.append("FAIL: Certificate has expired")
    except URLError:
        # print("Certificate verify failed: certificate has expired: " + item)
        identifiedLanguage.append("FAIL: Certificate verify failed")
    finally:
        iterador += 1

df.insert(loc = 5, column = 'IdentifiedLanguage', value = identifiedLanguage)
print(df) # this is the result in the last column of the dataframe, with PASS or FAIL with the reason of FAILING
imagenes = []
for image in soup.find_all("img"):
    imagenes.append(image)
    



# I read the CSV file with pandas, skipping the bad lines and using the ";" separator
# because of my PC configuration. after that I created a for loop, that looks into each
# of the URLS of the dataframe "df" that contains the CSV read. It uses a try-except-finally
# to control four exception types used from the urllib, urllib3 and ssl modules for those
# pages that could not be opened due to different reasons. For the pages that can be opened I used the urlopen and BeautifulSoup for the webscrapping and then with the soup.get_text() I got the text of the page, which I cleaned with the funcion, making a join with the linejumps and the repeated spaces.
 # In the list "IdentifiedLanguage"
# I saved the result of PASS or FAIL of each page and later in the line 51 I insert the
# column with the result, so the user can export the dataframe "df" with the asked results.
# I configured the Dockerfile with the installation of python, its modules, requirements of the different packages and main files for the deployment in RailWay
# but RailWay for some reason didn't trust in my github repository, so I couldn't build and
# deploy it.
# 
# I created a function that with the langdetect module detects what is the language
# of the visited page.
# 
# I made the commitments to Github to the latest version of this program and I couldn't
# reach the image and bar assesment













