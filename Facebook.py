#-*-coding:utf8-*-

#Eduardo Freire Mangabeira, UFRJ undergraduate student, 2018-06-11
#github:edumangabeira
#Consuming facebook API to acess pages or groups



import requests
#import sys
import time
import json

def read_article(url):
    response = requests.get(url)
    print (response.json())



def timestamp():



'''if __name__ == "__main__":

    url =
    token =
    page  =


        main()'''
