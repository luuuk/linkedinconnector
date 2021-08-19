import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui as pag
import csv

def login_to_linkedin(driver):
  username = driver.find_element_by_id("session_key")
  username.send_keys("YOUR LI USERNAME")
  password = driver.find_element_by_id("session_password")
  password.send_keys("YOUR LI PW!")
  driver.find_element_by_class_name("sign-in-form__submit-button").click()

def  goto_network_page(driver,network_url):
  driver.get(network_url)

def send_requests_to_users(driver):
  with open('LinkedIn - Amazon Interns.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i, row in enumerate(csv_reader):
            if i != 0:
              url = list(row)[1]
              try:
                time.sleep(5)
                driver.get(url)
                connectButton = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[3]/div/div/div/div/div[3]/div/div/main/div/section/div[2]/div[3]/div/button/span')))
                connectButton.click()
                sendButton = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]/span')))
                sendButton.click()
              except:
                print("Already connected with " + row[0])

def start_bot(driver,url,network_url):
  driver.get(url)
  login_to_linkedin(driver)
  goto_network_page(driver,network_url)
  send_requests_to_users(driver)

def main():
  try: 
    url =  "http://linkedin.com/"
    network_url =  "http://linkedin.com/mynetwork/"
    path = '/Usr/local/bin/chromedriver'
    driver = webdriver.Chrome(path)
    start_bot(driver,url,network_url)
  finally:
    driver.quit()

if __name__ == "__main__":
  main()