import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("C:\Windows\chromedriver.exe")
    driver=webdriver.Chrome(service=ser_obj)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("C:\Windows\msedgedriver.exe")
    driver=webdriver.Edge(service=ser_obj)
    return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("C:\Windows\geckodriver.exe")
    driver=webdriver.Firefox(service=ser_obj)
    return driver

driver=chrome_setup()
driver.maximize_window()
driver.get("https://awesomeqa.com/ui/")
driver.implicitly_wait(10)

# search item
driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("iphone")
driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//img[@title='iPhone']").click()

# clear the quantity and enter 2 ,click add to cart button
driver.find_element(By.XPATH,"//input[@id='input-quantity']").clear()
driver.find_element(By.XPATH,"//input[@id='input-quantity']").send_keys("2")
driver.find_element(By.XPATH,"//button[@id='button-cart']").click()
driver.implicitly_wait(10)

# click on Cart items
driver.find_element(By.XPATH,"//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']").click()

# click on View cart
driver.find_element(By.XPATH,"//strong[normalize-space()='View Cart']").click()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# click on checkout
driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
driver.implicitly_wait(10)

# click on Guest Checkout
driver.find_element(By.XPATH,"//label[normalize-space()='Guest Checkout']").click()
driver.implicitly_wait(10)

# click on continue
driver.find_element(By.XPATH,"//input[@id='button-account']").click()
driver.implicitly_wait(10)

# enter the details
driver.find_element(By.XPATH,"//input[@id='input-payment-firstname']").send_keys("jabez")
driver.find_element(By.XPATH,"//input[@id='input-payment-lastname']").send_keys("NR")
driver.find_element(By.XPATH,"//input[@id='input-payment-email']").send_keys("jabez@gmail.com")
driver.find_element(By.XPATH,"//input[@id='input-payment-telephone']").send_keys("9972976889")
driver.find_element(By.CSS_SELECTOR,"#input-payment-address-1").send_keys("# 3 coromandel")
driver.find_element(By.XPATH,"//input[@id='input-payment-city']").send_keys("Robertsonpet")
driver.find_element(By.XPATH,"//input[@id='input-payment-postcode']").send_keys("563118")

# select country from dropdown
country=Select(driver.find_element(By.XPATH,"//select[@id='input-payment-country']"))
country.select_by_visible_text("India")
driver.implicitly_wait(10)
state=Select(driver.find_element(By.XPATH,"//select[@id='input-payment-zone']"))
state.select_by_visible_text("Karnataka")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='button-guest']").click()
time.sleep(2)

#add comments
textbox=driver.find_element(By.XPATH,"//div[@id='collapse-shipping-method']//textarea[@name='comment']")
textbox.click()
textbox.send_keys("i am happy to place this order")
driver.find_element(By.XPATH,"//input[@id='button-shipping-method']").click()
time.sleep(2)

# click on checkbox in Payment method page and click on continue
driver.find_element(By.XPATH,"//input[@name='agree']").click()
driver.find_element(By.XPATH,"//input[@id='button-payment-method']").click()

driver.find_element(By.XPATH,"//input[@id='button-confirm']").click()
driver.implicitly_wait(10)
driver.save_screenshot(os.getcwd()+"\\orderplaced1.jpg")
time.sleep(5)

driver.quit()