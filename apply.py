import time
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path="C:\\Drivers\\Chrome\\chromedriver"
driver=webdriver.Chrome(chrome_driver_path)

driver.get(url="https://www.linkedin.com/jobs/search/?f_E=1%2C2&keywords=python%20developer")
signin=driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
signin.click()

email_field=driver.find_element_by_id("username")
email_field.click()
email_field.send_keys("YOUR EMAIL")
password_field=driver.find_element_by_id("password")
password_field.click()
password_field.send_keys("YOUR PASSWORD")
password_field.send_keys(Keys.ENTER)
while True:
    easy=driver.find_element_by_class_name("jobs-apply-button--top-card")
    easy_apply=easy.find_element_by_tag_name('button')
    easy_apply.click()
    time.sleep(10)
    keyboard.press_and_release('Tab')
    keyboard.press_and_release('Tab')
    keyboard.press_and_release('Tab')
    keyboard.press_and_release('Tab')
    keyboard.write("7852078342")
    keyboard.press_and_release('Enter')
    time.sleep(10)
