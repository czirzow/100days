from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

#Keep the browser open after we are done.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

if False:
    driver.get("https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CYMYK6?th=1")
    a_price_whole = driver.find_element(By.CLASS_NAME, value='a-price-whole')
    a_price_fraction = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
    price = float(f"{a_price_whole.text}.{a_price_fraction.text}")
    print(price)
    #XPath
    #/html/body/div
    element = driver.find_element(By.XPATH, value='/html/body/div')

# quiz 
driver.get('https://python.org/')

latest_news = driver.find_element(By.CLASS_NAME, value="shrubbery")
news_items = latest_news.find_elements(By.TAG_NAME, 'li')
#pprint(news_items)
for item in news_items:
    time_tag = item.find_element(By.TAG_NAME, value='time')
    a_tag = item.find_element(By.TAG_NAME, value='a')
    print(time_tag.get_attribute('datetime'), a_tag.text)
    # TODO: make the dict converting the datetime value as well.



# driver.close()
driver.quit()
