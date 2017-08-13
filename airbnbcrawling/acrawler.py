
# coding: utf-8

# # used packages

import requests
from bs4 import BeautifulSoup
import numpy as np
#import time


# Define search url and dictionary to save


base_url = 'http://airbnb.com/rooms/'
test_room = ''
test_dic = {}
test_dic[test_room] = {}


# main function


def crawler(room, dic=test_dic):
    if room not in dic.keys():
        dic[room] = {}
    cont = requests.get(base_url + room)
    soup = BeautifulSoup(cont.text, 'lxml')
    super_host = soup.find_all(attrs={'class': 'superhost-photo-badge superhost-photo-badge'})
    try:
        total = soup.find_all('div', attrs={'class':'star-rating-wrapper'})[0]['aria-label']
        dic[room]['Average stars'] = float(total.split()[1])
        dic[room]['Total reviews'] = int(total.split()[7])
        i = 0
        for item in soup.find_all('div', attrs={'class':'star-rating-wrapper'})[3:]:
            i += 1
            dic[room]['review %d'%i] = float(item['aria-label'].split()[1])
    except:
        pass
    if super_host:
        dic[room]['superhost'] = 1
        #if prt: print('superhost')
    else:
        dic[room]['superhost'] = 0
        
    # Other information
    tlist = []
    for item in soup.find_all('div', attrs={'class':'col-md-6', 'class':'bottom-spacing-2'}):
        x = item.text
        if ':' in x:
            dic[room][x.split(':')[0]] = x.split(':')[1]
        else:
            tlist.append(x)
    dic[room]['others'] = tlist
    return dic
