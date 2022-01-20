#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import matplotlib.pyplot as plt
import pandas as pd
import re


# In[2]:


os.getcwd()
os.chdir('D:\KIM-001\Desktop')


# In[3]:


os.getcwd()


# In[4]:


data = pd.read_csv('lowdata.csv', engine='python',encoding='CP949')


# In[5]:


data.head()


# In[6]:


for i in range(len(data['판매처명'])):
    data['판매처명'][i] = str(data['판매처명'][i])
    if '[' in data['판매처명'][i]:
        region = re.findall(r"\[(.*?)\]", data['판매처명'][i])[0]
        data['판매처명'][i] = region
        
        
    
    else:
        if '#' in data['판매처명'][i]:
            letter = data['판매처명'][i].replace('#', '')[0:2]
            
            data['판매처명'][i] = letter
            
            
    


# In[7]:


for i in range(len(data['수량'])):
    if data['품명 및 규격'][i] == "SAVER P":
        data['수량'][i] = 0
    elif data['품목코드'][i] == '703':
        data['수량'][i] = 0
        
    


# In[180]:


def create_graph(gg, region_year) :
    remove_overlap = list(set(gg))
    dic = {}

    for list_name in remove_overlap:
        dic[list_name] = 0
    for list_count in gg:
        dic[list_count] = dic[list_count] + 1
    dic = {key: value for key, value in dic.items() if key > 0}

    

    d1 = sorted(dic.items())
    dict1 = dict((x, y) for x, y, in d1)


    x = list(dict1.keys())
    y = list(dict1.values())
    values = range(len(x))

    plt.rcParams['font.family'] ='Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] =False
    plt.title(region_year + " 1회 거래량 별 거래 횟수 ")
    plt.plot(values, y, marker='o')
    plt.xticks(values, x)
    plt.savefig('./' + region_year + '.jpg')
    plt.show()


# In[181]:


# 경기도
# 2020+2021 판매 수량
# -값들은 수량이 거의 3미만이라 그냥 제외함

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매처명'][i] == "경기") or (data['판매처명'][i] == "경기총판(스마트정비기기)") or (data['판매처명'][i] == "부천") or (data['판매처명'][i] == "수원") or (data['판매처명'][i] == "안성") or (data['판매처명'][i] == "안산") or (data['판매처명'][i] == "오일플러스(안산카포스)") or (data['판매처명'][i] == "용인") or (data['판매처명'][i] == "화성")):
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "경기도 2020, 2021년")


# In[182]:


# 경기도
# 2020 판매 수량
# -값들은 수량이 거의 3미만이라 그냥 제외함

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2020) and ((data['판매처명'][i] == "경기") or (data['판매처명'][i] == "경기총판(스마트정비기기)") or (data['판매처명'][i] == "부천") or (data['판매처명'][i] == "수원") or (data['판매처명'][i] == "안성") or (data['판매처명'][i] == "안산") or (data['판매처명'][i] == "오일플러스(안산카포스)") or (data['판매처명'][i] == "용인") or (data['판매처명'][i] == "화성"))):
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "경기도 2020년")


# In[183]:


# 경기도
# 2021 판매 수량
# -값들은 수량이 거의 3미만이라 그냥 제외함

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2021) and ((data['판매처명'][i] == "경기") or (data['판매처명'][i] == "경기총판(스마트정비기기)") or (data['판매처명'][i] == "부천") or (data['판매처명'][i] == "수원") or (data['판매처명'][i] == "안성") or (data['판매처명'][i] == "안산") or (data['판매처명'][i] == "오일플러스(안산카포스)") or (data['판매처명'][i] == "용인") or (data['판매처명'][i] == "화성"))):
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "경기도 2021년")


# In[184]:


# data.to_excel('rawdata-1.xlsx')


# In[185]:


# 전라북도
# 2020+2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매처명'][i] == "고창") or (data['판매처명'][i] == "군산") or (data['판매처명'][i] == "김제") or (data['판매처명'][i] == "익산") or (data['판매처명'][i] == "전라북도") or (data['판매처명'][i] == "전북") or (data['판매처명'][i] == "전주") or (data['판매처명'][i] == "전주대리점")):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "전라북도 2020, 2021년")


# In[186]:


# 전라북도
# 2020 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2020) and ((data['판매처명'][i] == "고창") or (data['판매처명'][i] == "군산") or (data['판매처명'][i] == "김제") or (data['판매처명'][i] == "익산") or (data['판매처명'][i] == "전라북도") or (data['판매처명'][i] == "전북") or (data['판매처명'][i] == "전주") or (data['판매처명'][i] == "전주대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "전라북도 2020년")


# In[187]:


# 전라북도
# 2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2021) and ((data['판매처명'][i] == "고창") or (data['판매처명'][i] == "군산") or (data['판매처명'][i] == "김제") or (data['판매처명'][i] == "익산") or (data['판매처명'][i] == "전라북도") or (data['판매처명'][i] == "전북") or (data['판매처명'][i] == "전주") or (data['판매처명'][i] == "전주대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "전라북도 2021년")


# In[188]:


# 제주도
# 2020+2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if data['판매처명'][i] == "제주":
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "제주도 2020, 2021년")


# In[189]:


# 제주도
# 2020 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if data['판매년'][i] == 2020 and data['판매처명'][i] == "제주":
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "제주도 2020년")


# In[190]:


# 제주도
# 2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if data['판매년'][i] == 2021 and data['판매처명'][i] == "제주":
        gg.append(int(data['수량'][i]))
        
create_graph(gg, "제주도 2021년")


# In[191]:


# 인천광역시
# 2020+2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매처명'][i] == "인천") or (data['판매처명'][i] == "인천광역시") or (data['판매처명'][i] == "인천대리점")):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "인천광역시 2020, 2021년")


# In[192]:


# 인천광역시
# 2020 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2020) and ((data['판매처명'][i] == "인천") or (data['판매처명'][i] == "인천광역시") or (data['판매처명'][i] == "인천대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "인천광역시 2020년")


# In[193]:


# 인천광역시
# 2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2021) and ((data['판매처명'][i] == "인천") or (data['판매처명'][i] == "인천광역시") or (data['판매처명'][i] == "인천대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "인천광역시 2021년")


# In[194]:


# 경상북도
# 2020+2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매처명'][i] == "경북") or (data['판매처명'][i] == "경상북도") or (data['판매처명'][i] == "구미대리점") or (data['판매처명'][i] == "포항")):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "경상북도 2020, 2021년")


# In[195]:


# 경상북도
# 2020 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2020) and ((data['판매처명'][i] == "경북") or (data['판매처명'][i] == "경상북도") or (data['판매처명'][i] == "구미대리점") or (data['판매처명'][i] == "포항"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "경상북도 2020년")


# In[196]:


# 경상북도
# 2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2021) and ((data['판매처명'][i] == "경북") or (data['판매처명'][i] == "경상북도") or (data['판매처명'][i] == "구미대리점") or (data['판매처명'][i] == "포항"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "경상북도 2021년")


# In[197]:


# 대구광역시
# 2020+2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매처명'][i] == "대구") or (data['판매처명'][i] == "대구광역시") or (data['판매처명'][i] == "대구대리점")):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "대구광역시 2020, 2021년")


# In[198]:


# 대구광역시
# 2020 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2020) and ((data['판매처명'][i] == "대구") or (data['판매처명'][i] == "대구광역시") or (data['판매처명'][i] == "대구대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "대구광역시 2020년")


# In[199]:


# 대구광역시
# 2021 판매 수량

gg = []
for i in range(len(data['판매처명'])):
    if ((data['판매년'][i] == 2021) and ((data['판매처명'][i] == "대구") or (data['판매처명'][i] == "대구광역시") or (data['판매처명'][i] == "대구대리점"))):
        gg.append(int(data['수량'][i]))

        
create_graph(gg, "대구광역시 2021년")


# In[ ]:





# In[ ]:





# In[ ]:




