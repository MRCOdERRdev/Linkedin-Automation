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
email_field.send_keys("tech.buis.tanmay@gmail.com")
password_field=driver.find_element_by_id("password")
password_field.click()
password_field.send_keys("-FjLvA!qC92=3y2")
password_field.send_keys(Keys.ENTER)
while True:
    # easy=driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/div')
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

    # phone=driver.find_element_by_class_name("ember-text-field ember-view fb-single-line-text__input")
    # phone.click()
    # phone.send_keys("7852078342")
    # phone.send_keys(Keys.ENTER)
    # time.sleep(10)
# driver.set_page_load_timeout(40)

# jobs=driver.find_element_by_id("ember20")
# jobs.click()
# driver.set_page_load_timeout(40)
# search=driver.find_element_by_class_name("jobs-home-soho-search-card__truncated-text t-14 t-black t-bold")
# print(search.text)
# search.send_keys("python developer")
# search.send_keys(Keys.ENTER)
# while True:
#     cookie.click()
#     cookie_number=driver.find_element_by_xpath('//*[@id="cookies"]')
#     product3_click=driver.find_element_by_id("product3")

#     cookie_number=cookie_number.text
#     cookie_number=cookie_number.split(" ")
#     cookie_nu=cookie_number[0]
#     cookie_num=int(cookie_nu)
#     cursor=driver.find_element_by_id("product0")
#     cursor_price=driver.find_element_by_id("productPrice0")
#     cursor_pric=int(cursor_price.text)
#     product3=int(driver.find_element_by_id("productPrice3").text)
#     grandma=driver.find_element_by_id("product1")
#     price_grandma=driver.find_element_by_id("productPrice1")
#     price=int(price_grandma.text)
#     if cookie_num>product3:
#         product3_click.click()
#     elif cookie_num>    