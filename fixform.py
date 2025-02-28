# import requests
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
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
    
#     hrml_crens_one = open("staticfile/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    
#     for city in hrml_crens_one:
#         split_city= city.replace('\n', '').split(',')
        
#         city_p= split_city[0].replace('ï»¿', '')
#         link_city= city_p.replace(' ', '-').replace(',', '').replace('.', '').lower()
#         link_city= str(link_city.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        
#         state_p= split_city[3].replace('ï»¿', '')
#         link_state= state_p.replace(' ', '-').replace(',', '').replace('.', '').lower()
#         link_state= str(link_state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
#         zip_codes= split_city[15]
#         population= int(credential[8])
#         if population < 1000:
#             continue
#         if state_rep.lower() in state_p.lower() or state_rep[:5].lower() in state_p.lower():
#             html_city= f'<tr><td style="border: none; width:30%;"><a target="_blank" href="/rootasta/{link_state}/{link_city}/">{city_p}</a></td><td style="border: none; width:70%;"><i>{zip_codes}</i></td></tr>'
#             v += html_city
#     return v 
    
# if __name__ == '__main__':
#     Yelpdriver= chrome_driv()
#     c=0

#     search_categories1 = open("staticfile/county.txt", "r", encoding="utf-8").readlines()
#     for credentials1 in search_categories1:
#         c +=1
#         if c<= 1500:
#             continue
#         credential1= credentials1.strip().split('$$')
#         country_repl= credential1[0].title().replace('ï»¿', '')
#         country= credential1[0].replace(' ', '-').replace(',', '').replace('.', '').lower().replace('ï»¿', '')
#         country= str(country.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        
#         state_repl= credential1[1].title().replace('ï»¿', '')
#         state= credential1[1].replace(' ', '-').replace(',', '').replace('.', '').lower().replace('ï»¿', '')
#         state= str(state.encode("ascii", "ignore")).replace("b'", '').replace("'", '').replace('b"', '').replace('"', '')
        
#         search_categories = open("staticfile/uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
#         for credentials in search_categories:
#             credential= credentials.strip().split(',')
#             short_code = credential[2].upper().replace('ï»¿', '')
#             state_repl1= credential[3].title().replace('ï»¿', '')
#             if state_repl1.lower() == state_repl.lower() or state_repl1.lower()[:5] in state_repl.lower():
#                 break
#         country= f'{country}-{short_code.lower()}'
#         print(country)
#         search_contents= f'{country_repl}, {state_repl}'
#         content_web= str(fetch_contents(Yelpdriver, search_contents)).replace('\n', ' ')
#         content_table= str(all_city_url(state_repl)).replace('\n', ' ')
#         rooot= f'pathfirana/rootasta/{country}/'
#         all_data= f'{rooot}$${content_web}$${content_table}\n'
#         f = open("content.csv", "a", encoding='utf-8-sig', errors='replace')
#         f.write(all_data)
#         f.close()
#         print(c)

import os
import shutil
from bs4 import BeautifulSoup


for d in os.listdir('insulation-contractor'):
    try:
        for c in os.listdir(f'insulation-contractor/{d}'):
            try:
                for b in os.listdir(f'insulation-contractor/{d}/{c}'):
                    try:
                        search_categories = open(f'insulation-contractor/{d}/{c}/{b}', "r", encoding="utf8").read()
                        
                        op= search_categories.replace('index.html', '').replace('https://jcinsulation.net.biz/', 'https://s3.amazonaws.com/jcinsulation.net.biz/')

                        soup = BeautifulSoup(op, "html.parser")

                        metas = soup.find_all('a')
                        metas1adnhd = soup.find_all('link')
                        replace_de= [ meta.attrs['href'] for meta in metas ]
                        replace_de = list(dict.fromkeys(replace_de))

                        replace_deajshs= [ metas1adn.attrs['href'] for metas1adn in metas1adnhd ]
                        replace_deajshs = list(dict.fromkeys(replace_deajshs))
                        
                        all_list= replace_deajshs + replace_de
                        all_list = list(dict.fromkeys(all_list))
                        for replace_d in all_list:
                            tobereplaced= replace_d.strip()

                            if 'https://s3.amazonaws.com/jcinsulation.net.biz/' in tobereplaced:
                                op= op.replace(f'"{tobereplaced}"', f'"{tobereplaced}index.html"', 1)
                            
                        
                        
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
        
        op= search_categories.replace('index.html', '').replace('https://jcinsulation.net.biz/', 'https://s3.amazonaws.com/jcinsulation.net.biz/')

        soup = BeautifulSoup(op, "html.parser")

        metas = soup.find_all('a')
        metas1adnhd = soup.find_all('link')
        replace_de= [ meta.attrs['href'] for meta in metas ]
        replace_de = list(dict.fromkeys(replace_de))

        replace_deajshs= [ metas1adn.attrs['href'] for metas1adn in metas1adnhd ]
        replace_deajshs = list(dict.fromkeys(replace_deajshs))
        
        all_list= replace_deajshs + replace_de
        all_list = list(dict.fromkeys(all_list))
        for replace_d in all_list:
            tobereplaced= replace_d.strip()

            if 'https://s3.amazonaws.com/jcinsulation.net.biz/' in tobereplaced:
                op= op.replace(f'"{tobereplaced}"', f'"{tobereplaced}index.html"', 1)
            
        
        
        fp = open(f'insulation-contractor/{d}/index.html', "w", encoding='utf-8-sig')
        fp.writelines(op)
        fp.close()
    except:
        pass

try:
    search_categories = open(f'insulation-contractor/index.html', "r", encoding="utf8").read()

    op= search_categories.replace('index.html', '').replace('https://jcinsulation.net.biz/', 'https://s3.amazonaws.com/jcinsulation.net.biz/')

    soup = BeautifulSoup(op, "html.parser")

    metas = soup.find_all('a')
    metas1adnhd = soup.find_all('link')
    replace_de= [ meta.attrs['href'] for meta in metas ]
    replace_de = list(dict.fromkeys(replace_de))

    replace_deajshs= [ metas1adn.attrs['href'] for metas1adn in metas1adnhd ]
    replace_deajshs = list(dict.fromkeys(replace_deajshs))
    
    all_list= replace_deajshs + replace_de
    all_list = list(dict.fromkeys(all_list))
    for replace_d in all_list:
        tobereplaced= replace_d.strip()

        if 'https://s3.amazonaws.com/jcinsulation.net.biz/' in tobereplaced:
            op= op.replace(f'"{tobereplaced}"', f'"{tobereplaced}index.html"', 1)
        
    
    
    fp = open(f'insulation-contractor/index.html', "w", encoding='utf-8-sig')
    fp.writelines(op)
    fp.close()
except:
    pass




