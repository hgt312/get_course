import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# login CAS
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://cas.sustc.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.sustc.edu.cn%2Fjsxsd%2F')

username = browser.find_element_by_name("username")
username.send_keys("")  # your sid
password = browser.find_element_by_name("password")
password.send_keys("")  # your password
password.send_keys(Keys.RETURN)

# enter true page
browser.get("http://jwxt.sustc.edu.cn/jsxsd/xsxk/xklc_list?Ves632DSdyV=NEW_XSD_PYGL")
for i in browser.find_elements_by_tag_name("a"):
    if "进入选课" == i.get_attribute("text"):
        i.click()

button = browser.find_element_by_class_name("button")
button.click()

time.sleep(0.2)
browser.get('http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/comeInBxqjhxk')
time.sleep(0.2)
browser.get('http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/bxqjhxkOper?jx0404id=%s&xkzy=&trjf=' % '')  # your course id
print('', browser.current_url[-27: -12], BeautifulSoup(browser.page_source, 'lxml').body.string[:-1])

time.sleep(0.2)
browser.get('http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/comeInFawxk')
time.sleep(0.2)
browser.get('http://jwxt.sustc.edu.cn/jsxsd/xsxkkc/fawxkOper?jx0404id=%s&xkzy=&trjf=' % '')
print('', browser.current_url[-27: -12], BeautifulSoup(browser.page_source, 'lxml').body.string[:-1])
