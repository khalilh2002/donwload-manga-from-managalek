import os
import time

from bs4 import BeautifulSoup
import requests
from tkinter import filedialog


url = 'https://manga-like.net/manga/' #change url cause the website is banned
count = 1
count_ch = 1

#new
download_path="C:/Users/Khalil El Houssine/Downloads/web_manga"  #use this for donwload path using tkinter or somthing else 
download_path= filedialog.askdirectory()


def get_request(link):
    r = requests.get(link)
    if r.status_code in range(200, 301):
        return r.text
    else:
        print(f'error code : {r.status_code}')


def operation(n):
    global path_ch, path_manga, count, new_url
    path_ch = path_manga + n
    try:
        os.mkdir(path_ch)
    except Exception:
        pass

    new_url = new_url + n
    html_data = get_request(new_url)
    soup = BeautifulSoup(html_data, 'lxml')
    all_images = soup.findAll("img")
    for img in all_images:
        try:
            save_image(img["src"])
        except Exception:
            break
        count += 1
    count = 1
    

def save_image(src):
    global count, path_ch
    os.chdir(path_ch)
    data = requests.get(src)
    data = data.content
    open(f"img_{count}.jpg", "wb").write(data) #create and write data in the image
    print(f'Download {count}')


manga_name = input('the name of manga :  ')
name = manga_name.replace(" ", "-")
new_url = url+name+"/"

try:
    os.mkdir(f'{download_path}/{manga_name}/')
except Exception:
    pass

path_manga = f'{download_path}/{manga_name}/' 
ch = input("chapter number : ")
path_ch = path_manga + ch
total = 10
if ch == 'all':
    for i in range(1, total):
        operation(str(i))
        print(f"folder {i} end")
        time.sleep(5)
    count_ch += 1
else:
    operation(ch)
