from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

# debug...
from pprint import pprint



class CookieMonster:
    """He does just goble up cookies
    The more cookies you eat the more you make.
    """

    def __init__(self, driver, lang='DE'):
        self.driver = driver
        self.lang = lang
        try:
            language_button = self.driver.find_element(by=By.ID, value=f"langSelect-{self.lang}")
            language_button.click()
        except NoSuchElementException:
            print("Language selection not found")

    def get_cookie(self):
        # I'm not sure if this changes... all other elements do.
        return self.driver.find_element(by=By.ID, value="bigCookie")

    def num_cookies(self):
        cookies = self.driver.find_element(by=By.ID, value="cookies")
        return int(cookies.text.split(' ')[0].replace(',', ''))

    # general names of action here:
    def eat(self, cookie):
        cookie.click()

    def gobble(self, qty:int = 356):
        # I only get this here cause i'm not sure if it changes
        cookie = self.get_cookie()
        i = 0
        while qty > 0:
            self.eat(cookie)
            qty -= 1
            i += 1
            # DEBUG: 
            if i % 100 == 0:
                pprint(self.num_cookies())
            sleep(0.003) # lets breath a moment.



# Main

url = 'https://ozh.github.io/cookieclicker/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# FIXME: I believe we can figure out a state on when to continue instead of sleeping
sleep(3) # wait page load javascript

# Sid: The original name for Cookie Monster by Jim Henson in the late 1960's
Sid = CookieMonster(driver, lang='EN')
# FIXME: We have to wait for javascript to set things up.0
sleep(3) # wait for javascript.

cookies_to_eat = 15
Sid.gobble(cookies_to_eat)
# Now... lets start getting the upgrades to increase per Sec.
# buy a click. at 15.
#    recalculate cookies_to_eat to the next level.
# get what is available and upgrade top down.
# or bottom up? who knows.







