
# coding: utf-8

# # 크롤링에 필요한 패키지

# In[19]:

import requests
from bs4 import BeautifulSoup
import numpy as np
import time


# ## 검색 url과 저장할 dictionary 정의

# In[20]:

base_url = 'http://airbnb.com/rooms/'
test_room = '8769074'
test_dic = {}
test_dic[test_room] = {}


# ## 크롤링 함수

# In[21]:

def other_info(soup, dic=test_dic[test_room]):
    tlist = []
    for item in soup.find_all('div', attrs={'class':'col-md-6', 'class':'bottom-spacing-2'}):
        x = item.text
        if ':' in x:
            dic[x.split(':')[0]] = x.split(':')[1]
        else:
            tlist.append(x)
    dic['others'] = tlist


# In[22]:

def crawler(room, dic=test_dic, prt=True):
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
            if prt: print((i),item['aria-label'])
        if prt: print(total)
    except:
        pass
    if super_host:
        dic[room]['superhost'] = 1
        if prt: print('superhost')
    else:
        dic[room]['superhost'] = 0
        if prt: print('ordinary')
    #print(total)
    
    # 기타 정보 
    other_info(soup, dic[room])
    return dic


# ### 테스트용 roomid로 시범

# In[23]:

dic = crawler(test_room, prt=False)


# In[24]:

dic


# In[25]:

test_dic


# ### Superhost 아닌 호스트 방 test

# In[26]:

crawler('3853024', dic=test_dic)


# ## 리뷰 평점이 없는 유저

# In[27]:

crawler('11213409', dic=dic)


# ## delay 추가 명령어

# In[12]:

time.sleep(1) # 1초 딜레이


# In[ ]:



