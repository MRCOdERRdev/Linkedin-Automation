import time
from selenium import webdriver
import keyboard         

from selenium.webdriver.common.keys import Keys
names_list=["IIT BOMBAY"]

chrome_driver_path="C:\\Drivers\\Chrome\\chromedriver"
driver=webdriver.Chrome(chrome_driver_path)
for name in names_list:
    driver.get(url="https://www.linkedin.com/mynetwork/")
    try:
        sign_in=driver.find_element_by_link_text("Sign in")
        sign_in.click()



        email_field=driver.find_element_by_id("username")
        email_field.click()
        email_field.send_keys("tech.buis.tanmay@gmail.com")
        password_field=driver.find_element_by_id("password")
        password_field.click()
        password_field.send_keys("-FjLvA!qC92=3y2")
        password_field.send_keys(Keys.ENTER)
        time.sleep(5)
    except:    
    # message_down=driver.find_element_by_class_name("msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view")
    # message_down.click()
        time.sleep(3)
        
    search=driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
    search.click()
    time.sleep(3)
    search.send_keys(name)
    search.send_keys(Keys.ENTER)
    time.sleep(5)

    seeall=driver.find_element_by_link_text("See all people results")
    seeall.click()
    time.sleep(5)
    try:
        ul=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul')
    except:
        ul=driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/ul')    
    list=ul.find_elements_by_tag_name("li")
    count=0
    page_no=0

    for li in list:
        button=li.find_element_by_tag_name("button")
        span=button.find_element_by_tag_name("span")
        text=span.text
        if 'Connect' in text:
            button.click()
            try:
                driver.find_element_by_link_text("Learn why")
                dialog=driver.find_element_by_class_name("artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view")
                dialog.click()
                
            except:
                keyboard.press_and_release("Tab")
                keyboard.press_and_release("Tab")
                keyboard.press_and_release("Tab")
                keyboard.press_and_release("Enter")
                
        else:
            pass
    # search=driver.find_element_by_xpath('//*[@id="global-nav-typeahead"]/input')
    # search.click()
    # time.sleep(3)
    # search.clear()
    # time.sleep(2)
    # search.click()
    # time.sleep(5)
    # search.send_keys["fdkslfj"]
    # search.send_keys[Keys.ENTER]

    # artdeco_card=driver.find_element_by_class_name("artdeco-card pv0 mb6")

    # pagination=artdeco_card.find_element_by_class_name("artdeco-pagination artdeco-pagination--has-controls ember-view pv5 ph2")
    # ul=pagination.find_element_by_tag_name("ul")
    # li=ul.find_elements_by_tag_name("li")
    # for li in list:
    #     button=li.find_element_by_tag_name("button")
    #     button.click()
    