from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

#Keep the browser open after we are done.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://python.org/')
# TODO:
#   . get articlecount in english
#   . print the number.



driver.quit()
