#!/usr/bin/python3

#SITE_TO_POLL = "https://www.cinemacity.bg/films/spider-man-no-way-home/4601s3r"
SITE_TO_POLL = "https://www.cinemacity.bg/films/venom-there-will-be-carnage/4368s3r#/buy-tickets-by-film?for-movie=4368s3r&view-mode=list"
TIME_TO_SLEEP = 60 # in seconds
PATH_TO_DRIVER = "./chromedriver" # get the driver from the net and unzip it in the root folder so not change this
EXEC_CMD = "echo henlo" # add whatever thing you want for a post find hook, shell cmd ofc

# pip install selen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os


chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options,
        executable_path="./chromedriver") # get driver from here https://chromedriver.chromium.org/downloads

while 1:
    driver.get(SITE_TO_POLL)
    driver.implicitly_wait(2)
    try:
        if driver.find_element_by_class_name("quickbook-component"):
            driver.close()
            print('WE WIN THESE')
            os.system(EXEC_CMD)
            exit(0)
    except NoSuchElementException:
        print("ain't it chief")
    time.sleep(TIME_TO_SLEEP)
    driver.refresh()
    print("refreshed page")
