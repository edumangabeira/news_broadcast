#-*-coding:utf8-*-

#Eduardo Freire Mangabeira, UFRJ undergraduate student, 2018-06-11
#github:edumangabeira
#Consuming facebook API to acess pages or groups



import requests
#import sys
import time
import json



def read_page(url,page,token):

    link = url%(page,token)
    response = requests.get(link)

    result  = response.json()
    print(result)

    check = response.status_code

        if (check != 200):
            error_log = open('log.txt', 'w')
            error_log.write = 'error'
            time.sleep(10)


    error_log.close()




if __name__ == "__main__":

    url = "https://graph.facebook.com/v3.0/%s?fields=%s?acess_token"
    page = "spottedUFRJresiste"
    api_key =  "EAACEdEose0cBALZCT3DxD7C4c06fSzmMMkGT1w5iR4kLGdqkjeyfhBkTIjTbQ8uAivJJ2x2zC1umikV9C0qTOs1ZC9FtRzIgp0b7f2jQYQPk1Vpegg3B4Vgcxon8wEJcd3Ik6pD8uawJURunrqmfxwN2XKhRQlFOMIhNeiWUGDZAjLZA8Lm0DkgmHeuqFB0ZD"
    result = 0

    read_page(url,page,token,result)

    text = open('json_text.txt', 'w')
    text.write(result['posts']['data'])
    text.close()

    main()
