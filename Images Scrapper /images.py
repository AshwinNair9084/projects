from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://images.google.com/')

search_Element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_Element.send_keys("giraffe")
search_Element.send_keys(Keys.ENTER)

# Will keep scrolling down the webpage until it cannot scroll no more

last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,
                            "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
    except:
        pass
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

for i in range(2):
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[' + str(
                                i + 1) + ']/a[1]/div[1]/img').screenshot('giraffe (' + str(i + 1) + ').png')
    except:
        pass

driver.close()
