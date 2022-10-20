import os
import json
from datetime import timezone, datetime, timedelta
import requests
from time import sleep
import threading
def shareao():

    from time import sleep
    import requests,threading,os,sys
    __AUTHOR__ = 'Nguyen Van Nam'
    __USING__= 'Share Free'
    __VERSION__ = 'V1'
    __ZALO__= '0852048795'
    __NOTE__ ='thanks for using'


    def baner():
        print(f'''

            Author: {__AUTHOR__}
            Using: {__USING__}
            Verstion: {__VERSION__}
            Zalo: {__ZALO__}

         ''')
    print('')

os.system('clear')

from time import strftime
ngay=int(strftime('%d'))
key1=str(ngay*1237646546+2318472)
key = 'huy'

url = 'https://namtricker111.000webhostapp.com/web/key.html?key='+key
token_link1s = '8ebe1388d68ad1af7d0b2e154e43a37d41f4b322'
link1s = requests.get(f'https://mneylink.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error":
        print(link1s['message'])
        quit()
else:
        link_key=link1s['shortenedUrl']
keynhap = input('\033[38;5;10mKey:\033[38;5;15m ')
if keynhap == key:
    print('\033[38;5;11mKey Đúng Mời Bạn Dùng Tool')




    uid=input('\033[1m\033[38;5;51mNhập Uid:\033[38;5;15m ')

    # token_fb='EAAGNO4a7r2wBAOJ9BFaxM1mReywdAVQig3PitiHjJetEATWPck4QDfN03vKOBUdLVQ8IMaiLGCw7MF7mNAW6zNEwS7lUBL4OvTOKilVXR3UsDiSTFSJ0DKPubQtnVL5DGBrn37A9oyoYbtjrDx0YfKPR7wvYtkSPMMGTj0oo1dBg858qARTnCGI4Qn8ZD'
    ck_fb=input('\033[1m\033[38;5;51mNhập Cookie Page Business:\033[38;5;15m ')


    print("\033[38;5;11mĐang Get Token..")


    hed_gettoken = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'no-cache',
        'cookie': ck_fb,
        'pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
    }
    try:
        token_fb = requests.get('https://www.facebook.com/dialog/oauth?client_id=124024574287414&redirect_uri=https://www.instagram.com/accounts/signup/&&scope=email&response_type=token', headers=hed_gettoken).url.split('#access_token=')[1].split('&data_access_expiration_time')[0]
        print(f'\033[1m\033[38;5;10mGet Token Thành Công: \033[38;5;15m {token_fb}')
    except:
        print('\033[1,9mGet Token Thất Bại, Vui Lòng Xem Lại Cookie')
        print(token_fb)
        sleep(10)
        quit()

    # token_fb=input('\033[1m\033[38;5;51mEnter token facebook: ')

    header={
        'cookie': ck_fb,
    }
    def Start(l):
        getTokenPage = requests.get(f"https://graph.facebook.com/v12.0/me/accounts?fields=access_token&limit=999999999&access_token={token_fb}",headers=header).json()['data']
        for tach in getTokenPage:
            uid_page=tach['id']
            access_token_page=tach['access_token']
            # print(uid_page)
            # print(access_token_page)
            buff = requests.post(f"https://graph.facebook.com/me/feed?link=https://www.facebook.com/{uid}&published=0&access_token={access_token_page}",headers=header).text
            if "error" in buff:
                print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{uid_page}\033[0m \033[1;31mFaild')
            else:
                print(f'\033[1m\033[38;5;237m[\033[38;5;54m*\033[38;5;237m]\033[0m \033[4m\033[38;5;164m{buff}\033[0m \033[1m\033[38;5;51mSuccess')



    soluong = int(input('\033[1m\033[38;5;51mNhập Số Lượt Share: \033[38;5;15m '))

    threades = []
    for l in range(soluong):
        threades += [threading.Thread(target=Start,args={l},)]
    for t in threades:
        t.start()
    for t in threades:
        t.join()
    print('\033[1;31mĐã Song, Cảm Ơn Bạn Đã Tin Tưởng Dùng Tool')





shareao()