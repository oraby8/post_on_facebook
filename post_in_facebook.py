from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username='Username'
password='Password'
site='https://www.facebook.com'
post="write your post"


def post_post(site,username,password,post):
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
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="loginbutton"]'))).click()


    # Maximizing the browser [optional]
    browser.maximize_window()



    body =browser.find_element_by_tag_name('body')
    for i in range(1):
        body.send_keys(Keys.ESCAPE)




    status= browser.find_element_by_xpath("//textarea[@name='xhpc_message']")
    status.send_keys(post);

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(.,'Share')]"))).click()
    browser.close()
    browser.quit()

post_post(site,username,password,post)
