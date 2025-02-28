# import requests
# import random
# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import sys
# from bs4 import BeautifulSoup
# import re 


# def chrome_driv():
#     Yelpdriver = webdriver.Chrome(service=Service(r"chromedriver.exe"))
#     Yelpdriver.get("https://en.wikipedia.org/wiki/Miami")
#     Yelpdriver.maximize_window()
#     return Yelpdriver
    
# def fetch_contents(Yelpdriver, search_contents):
#     while True:
#         try:
#             time.sleep(1)
#             searchfield= Yelpdriver.find_element(By.NAME, "search")
#             searchfield.clear()
#             searchfield.send_keys(search_contents)
#             WebDriverWait(Yelpdriver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchform"]/div/button')))
#             break
#         except:
#             continue
#     try:
#         Yelpdriver.find_element(By.XPATH, '//*[@id="searchform"]/div/button').click()
#     except:
#         searchbotton= Yelpdriver.find_element(By.XPATH, '//*[@id="searchform"]/div/button')
#         Yelpdriver.execute_script("arguments[0].scrollIntoView();", searchbotton)
#         Yelpdriver.execute_script("arguments[0].click();", searchbotton)
#     kpk= 1
        
#     while True:
#         kpk+=1
#         try:
#             WebDriverWait(Yelpdriver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[@id="mw-content-text"]/div[1]/p[{kpk}]')))
#             result= Yelpdriver.find_element(By.XPATH, f'//*[@id="mw-content-text"]/div[1]/p[{kpk}]').text
#             if len(result) < 30:
#                 pass
#             else:
#                 result= re.sub("[\\[].*?[\\]]", "", result)
#                 return result
        
                
            
#         except:
#             if kpk==7:
#                 kpk= 1
#             continue
    
# def all_city_url(state_rep):
#     v= ''
#     v+=''
#     o=0
#     l=0
#     hrml_crens_one = open("staticfile/city.txt", "r", encoding="windows-1254").readlines()
#     pas_sjdjd= len(hrml_crens_one)
#     save_num= []
#     for city in hrml_crens_one:
#         while True:
#             nun= random.randint(0, pas_sjdjd-1)
#             if nun in save_num:
#                 continue
#             else:
#                 break
            
#         save_num.append(nun)
#         split_city= hrml_crens_one[nun].replace('\n', '').split(',')
        
#         city_p= split_city[0].replace('ï»¿', '')
#         state_p= split_city[1].replace('ï»¿', '')
#         link_state= split_city[2].replace('ï»¿', '')
#         link_city= split_city[3].replace('ï»¿', '')
#         if state_rep in state_p or state_rep[:5] in state_p:
#             l +=1
#             o +=1
#             if o==1:
#                 html_city= f'<tr><td><a target="_blank" href="/root/{link_state}/{link_city}/">{city_p}</a></td>'
#             elif o == 5:
#                 html_city= f'<td><a target="_blank" href="/root/{link_state}/{link_city}/">{city_p}</a></td></tr>'
#                 o=0
#             else:
#                 html_city= f'<td><a target="_blank" href="/root/{link_state}/{link_city}/">{city_p}</a></td>'
#             v += html_city
#             if l== 20:
#                 return v  
#     return '' 
# if __name__ == '__main__':
#     Yelpdriver= chrome_driv()
#     c=0
#     search_categories = open("staticfile/uscities - Sheet1.csv", "r", encoding="windows-1254").readlines()
#     for credentials in search_categories:
#         credential= credentials.strip().split(',')
#         sub_ciy_repl= credential[0].title()
#         sub_ciy= credential[0].replace(' ', '-').replace(',', '').replace('.', '').lower()
#         sub_ciy= str(sub_ciy.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
#         short_code = credential[2].upper()
#         state_repl= credential[3].title()
#         state= credential[3].replace(' ', '-').replace(',', '').replace('.', '').lower()
#         state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
#         population= int(credential[8])
#         zip_codes= credential[15]
#         if 'Puerto Rico'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Virgin Islands'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Washington, D.C.'.replace(' ', '-').lower() == state:
#             continue
#         elif 'US Armed Forces Pacific'.replace(' ', '-').lower() == state:
#             continue
#         elif 'American Samoa'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Guam'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Palau'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Federated States of Micronesia'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Northern Mariana Islands'.replace(' ', '-').lower() == state:
#             continue
#         elif 'Marshall Islands'.replace(' ', '-').lower() == state:
#             continue
#         elif 'US Armed Forces Europe'.replace(' ', '-').lower() == state:
#             continue
#         else:
#             pass
        
#         if population < 1000:
#             continue
        
#         c +=1
#         if c <= 7845:
#             continue
        
#         search_contents= f'{sub_ciy_repl}, {state_repl}'.title()
#         content_web= str(fetch_contents(Yelpdriver, search_contents)).replace('\n', ' ')
#         content_table= str(all_city_url(state_repl)).replace('\n', ' ')
#         rooot= f'path/root/{state}/{sub_ciy}'
#         all_data= f'{rooot}$${content_web}$${content_table}\n'
#         f = open("content.csv", "a", encoding='utf-8-sig', errors='replace')
#         f.write(all_data)
#         f.close()
#         print(c)


import os
import shutil


preloader='''<div class="slider-item" style="background-image: url('static/images/bg_2.jpg');">
        <div class="overlay"></div>
        <div class="container">
          <div class="row slider-text align-items-center" data-scrollax-parent="true">
            <div class="col-m-6 col-s-12 ftco-animate" data-scrollax=" properties: { translateY: '70%' }">
              <h1 class="mb-4" data-scrollax="properties: { translateY: '30%', opacity: 1.6 }">Niobrara Dental Service USA</h1>
              <p class="mb-4" style="font-family:calibri;">we are dedicated to providing comprehensive oral care to our patients. We offer a wide range of services to ensure your dental health is in excellent condition.</p>
              <p><a href="tel:8312595557" class="btn btn-primary px-4 py-3" style="background-color:red;">Click Here To Call Us  (831) 259-5557</a></p>
            </div>
          </div>
        </div>
      </div>
'''

for d in os.listdir('insulation-contractor'):
    try:
        for c in os.listdir(f'insulation-contractor/{d}'):
            try:
                for b in os.listdir(f'insulation-contractor/{d}/{c}'):
                    try:
                        search_categories = open(f'insulation-contractor/{d}/{c}/{b}', "r", encoding="utf8").read()
                        
                        op= search_categories.replace("﻿", '').replace('https://jcinsulation.net/', 'https://jcinsulation.netlify.app/').replace('(206) 804-4514', '(888) 498-9391').replace('tel:2068044514', 'tel:8884989391')
         
                        
                        fp = open(f'insulation-contractor/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except:
                        pass
            except:
                pass
    except:
        pass
    
for d in os.listdir('insulation-contractor'):
    try:
        search_categories = open(f'insulation-contractor/{d}/index.html', "r", encoding="utf8").read()
        op= search_categories.replace("﻿", '').replace('https://jcinsulation.net/', 'https://jcinsulation.netlify.app/').replace('(206) 804-4514', '(888) 498-9391').replace('tel:2068044514', 'tel:8884989391')
        # if 'insulation-contractor' in str(d):
        #     shutil.rmtree(f'insulation-contractor/{d}')
            
        #     parent_dir= r'C:\Users\Administrator\Downloads\duplicate script\insulation-contractor'
        #     state= str(d).replace('insulation-contractor', 'home-inspection')
        #     path = os.path.join(parent_dir, state)
        #     os.makedirs(path) 
        #     fp = open(f'insulation-contractor/{state}/index.html', "w", encoding='utf-8-sig')
        #     fp.writelines(op)
        #     fp.close()
        # else:
            
        fp = open(f'insulation-contractor/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass


try:
    search_categories = open(f'insulation-contractor/index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("﻿", '').replace('https://jcinsulation.net/', 'https://jcinsulation.netlify.app/').replace('(206) 804-4514', '(888) 498-9391').replace('tel:2068044514', 'tel:8884989391')
    
    fp = open(f'insulation-contractor/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass

try:
    search_categories = open(f'index.html', "r", encoding="utf8").read()
    
    op= search_categories.replace("﻿", '').replace('https://jcinsulation.net/', 'https://jcinsulation.netlify.app/').replace('(206) 804-4514', '(888) 498-9391').replace('tel:2068044514', 'tel:8884989391')
    
    fp = open(f'index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass
