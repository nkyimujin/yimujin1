from selenium import webdriver
import time


def openurl(url):
    browser = webdriver.Chrome()
    shenxinfu_url = "https://192.168.0.254"
    browser.get(shenxinfu_url)
    username = 'admin'
    password = '1qaz@wsx'
    browser.find_element_by_name('user').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)
    time.sleep(3)
    browser.find_element_by_class_name('button').click()
    print('登陆成功')
    time.sleep(10)
    browser.find_element_by_id('ext-comp-1040').click()
    time.sleep(3)
    browser.find_element_by_id('ext-gen92').click()
    time.sleep(10)
    print(browser.find_element_by_link_text('系统诊断').text)
    browser.find_element_by_link_text('系统诊断').click()
    time.sleep(5)
    browser.find_element_by_link_text('重启操作').click()
    print('重启操作')
    time.sleep(5)
    browser.find_element_by_class_name('sysreboot-link').click()
    time.sleep(3)
    browser.find_element_by_id('ext-comp-1042').click()
    time.sleep(3)
    print('重启成功')
    browser.close()
    return openurl(url)
print(openurl(str))