from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username='USERNAME'
password='PASSWORD"
site='https://www.facebook.com'
page_url="write your page URL"
post="POST"

def post_post(site,username,password,post,page_url):
    browser = webdriver.Chrome("chromedriver.exe")

    # Email and password elements
    username_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='pass']"
    login_button_xpath = '//*[@id="loginbutton"]'

    browser.get(site)

    username_element = browser.find_element_by_xpath(username_xpath)
    password_element = browser.find_element_by_xpath(password_xpath)

    # Writing the username and password
    username_element.send_keys(username)
    password_element.send_keys(password)


    # Logging in
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginbutton"]'))).click()


    body =browser.find_element_by_tag_name('body')
    for i in range(1):
        body.send_keys(Keys.ESCAPE)


    #browsing the page
    browser.get(page_url)
    body = browser.find_element_by_tag_name('body')
    for i in range(10):
        body.send_keys(Keys.ESCAPE)


    
    #//*[@id="js_r"]

    status=browser.find_element_by_class_name("_5yk2")
    

##    status= browser.find_element_by_xpath('//*[@id="placeholder-c90ip"]')
    status.send_keys(post)
    
    sleep(2)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Publish')]"))).click()
    sleep(20)
    browser.close()
    sleep(1)
    browser.quit()


post_post(site,username,password,post,page_url)
