import os
import shutil
from bs4 import BeautifulSoup
import random



def extract_first_200_words(text):
    # Split the text into words
    words = text.split()

    # Get the first 200 words
    first_200_words = words

    # Join the first 200 words back into a string
    result = ' '.join(first_200_words)

    return result


def short_code_state(state_repl):
    search_categories = open("uscities - Sheet1.csv", "r", encoding="utf-8").readlines()
    for credentials in search_categories:
        credential= credentials.strip().split(',')
        short_code = credential[2].replace('ï»¿', '').upper()
        state_repl1= credential[3].replace('ï»¿', '').title()
        try:
            if state_repl.lower() == state_repl1.lower():
                break
        except:
            break
    return short_code


lot_line= '''



'''


info= '''
<meta property="og:title" content="aloomaidtitle" />
<meta property="og:description" content="aloomaiddescription" />
<meta property="og:type" content="article" />
<meta property="og:site_name" content="Insulation Contractor" />
<meta property="og:image" content="aloomaidimagelink" />
'''
all_image=[]
for sss in os.listdir('insulation-contractor/static/images/og-images'):
    all_image.append(f'../../static/images/og-images/{sss}')
    


for d in os.listdir('insulation-contractor'):
    try:
        for c in os.listdir(f'insulation-contractor/{d}'):
            try:
                for b in os.listdir(f'insulation-contractor/{d}/{c}'):
                    try:
                        search_categories = open(f'insulation-contractor/{d}/{c}/{b}', "r", encoding="utf8").read()
                        
                        op= search_categories.replace("﻿", '').replace(lot_line, '')
                        soup = BeautifulSoup(op, "lxml")
                        state_repl= str(d).replace('ï»¿', '').replace('-', ' ').title()
                        abbr_state= short_code_state(state_repl)
                        city= str(c).replace('ï»¿', '').replace('-', ' ').title()
                        meta_title= f'Insulation Contractor {city} {abbr_state} | Call (206) 804-4514 Insulation Contractor Expert {city} {abbr_state}'

                        over_all=''
                        all_meta_description= soup.find_all('p')
                        for all_meta_descriptio in all_meta_description:
                            over_all+= all_meta_descriptio.text + ' '
                        meta_description= extract_first_200_words(over_all)
                        image_path= random.choice(all_image)
                        all_metatile= info.replace('aloomaiddescription', meta_description).replace('aloomaidtitle', meta_title).replace('aloomaidimagelink', image_path)
                        op= op.replace('</title>', f'</title>{all_metatile}', 1)
                        fp = open(f'insulation-contractor/{d}/{c}/{b}', "w", encoding='utf-8-sig')
                        fp.writelines(op)
                        fp.close()
                    except Exception as oops:
                        print('Error communicating:', oops)
            except:
                pass
    except:
        pass
    

