from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

if False:
    #Keep the browser open after we are done.
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://en.wikipedia.org/wiki/Main_Page')
    # TODO:
    #   . get articlecount in english
    article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
    pprint(article_count.text)
    article_count.click()
    #   . print the number.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
fname.send_keys("Curt")
lname.send_keys("Zirzow")
email.send_keys("czirzow@gmail.com", Keys.ENTER)






#driver.quit()
