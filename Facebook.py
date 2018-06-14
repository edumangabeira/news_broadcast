#-*-coding:utf8-*-

#Eduardo Freire Mangabeira, UFRJ undergraduate student, 2018-06-11
#github:edumangabeira
#Consuming facebook API to acess a page and gather its data.

import requests
#import sys
import time
import json
import csv

'''
reads the facebook page content and gains access to its posts texts
'''
def read_page(page,fields,token,posts):

    url = 'https://graph.facebook.com/v3.0/%s?fields=%s?access_token=%s' % (page,fields,token)

    #link = url%(page,token)
    response = requests.get(url)

    posts = ['posts']

    for post in posts:
        post  = response.json()
        print(post)

    check = response.status_code

    if (check != 200):
            error_log = open('log.txt', 'w')
            error_log.write = 'error'
            time.sleep(10)

    error_log.close()
'''
converts the gathered data to a .csv file
'''
def convert_to_csv():

    with open('night_posts.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['post','shares','comments','likes'])

        for linha in lista_final:
            writer.writerow(linha)

if __name__ == "__main__":

    #url = 'https://graph.facebook.com/v3.0/%s?fields=%s?access_token=%s' % ['pages']['data']
    page = ""
    token  =  ""
    field = 0
    post = 0

    fields = 'posts,page,id'
    field_posts = ['posts']

    for field in field_posts:
        read_page(page,token,post)
        text = open('json_text.txt', 'w')
        text.write(post['posts']['data'][field]['id'])
        text.close()

    main()
