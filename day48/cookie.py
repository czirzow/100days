from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep, time

# debug...
from pprint import pprint


class CookieMonster:
    """He does just gobble up cookies
    The more cookies you eat the more you make.
    """

    def __init__(self, driver, lang='DE'):
        self.driver = driver
        self.lang = lang
        self.cookies = 0
        self.cookies_per_sec = 0.0
        try:
            # I cheated on this, that damn langSlect-EN would never work.
            # it was all about the sleeping
            sleep(3)
            language_button = self.driver.find_element(by=By.ID, value=f"langSelect-{self.lang}")
            language_button.click()
        except NoSuchElementException:
            print("Language selection not found")

    def get_cookie(self):
        # I'm not sure if this changes... all other elements do.
        return self.driver.find_element(by=By.ID, value="bigCookie")

    def num_cookies(self):
        cookies = self.driver.find_element(by=By.ID, value="cookies")
        self.cookies = int(cookies.text.split(' ')[0].replace(',', ''))
        return self.cookies

    def get_per_second(self):
        # this item isn't always ready and can be missing.
        per_sec = self.driver.find_element(by=By.ID, value="cookiesPerSecond")
        try:
            self.cookies_per_sec = float(per_sec.text.replace('per second: ', '').replace(',',''))
        except StaleElementReferenceException:
            """Just ignore this.. we will get it at some point."""
            pass
        return self.cookies_per_sec

    def get_products(self):
        return self.driver.find_elements(by=By.CSS_SELECTOR, value=".product.unlocked.enabled")

    def get_upgrades(self):
        return self.driver.find_elements(by=By.CSS_SELECTOR, value=".crate.upgrade.enabled")
        

    # general names of action here:
    def eat(self, cookie):
        cookie.click()

    def gobble(self, how_many: int = 100, for_how_long: float = 5.0):
        """
        Eat cookies until a limit is reached.

        Args:
            how_many (int): Number of cookies to eat.
            for_how_long (float): Number of seconds to run.

        Returns:
            None
        """

        # I only get this here cause i'm not sure if it changes
        cookie = self.get_cookie()
        start = time()
        while how_many > 0:
            if time() - start >= for_how_long:
                # no need to continue
                break
            how_many -= 1
            self.eat(cookie)

            # DEBUG: 
            #sleep(0.003) # lets breath a moment.



# Main
#----------

url = 'https://ozh.github.io/cookieclicker/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


# Sid: The original name for Cookie Monster by Jim Henson in the late 1960's
Sid = CookieMonster(driver, lang='EN')

# FIXME: I believe we can figure out a state on when to continue instead of sleeping
# FIXME: We have to wait for javascript to set things up.0
sleep(2) # wait for javascript.

run_for = 300
start = time()

our_per_second = 24.0
cookies_to_eat = 15
while time() - start <= run_for:
    time_to_eat = (our_per_second + Sid.get_per_second()) / cookies_to_eat
    Sid.gobble(how_many=cookies_to_eat, for_how_long=time_to_eat)

    upgrades = Sid.get_upgrades()
    for upgrade in upgrades[::-1]:
        try:
            upgrade.click()
            print('upgrade')
            break
        except StaleElementReferenceException:
            """Just ignore this.. we will get it at some point."""
            print('missed upgrade')
            pass

    products = Sid.get_products()
    for product in products[::-1]:
        product.click()
        cookies_to_eat = int(product.find_element(By.CLASS_NAME, value="price").text.replace(',', ''))
        print(cookies_to_eat, Sid.get_per_second())
        break


    #sleep(0.5)
    #product.click()


# Now... lets start getting the upgrades to increase per Sec.
# buy a click. at 15.
#    recalculate cookies_to_eat to the next level.
# get what is available and upgrade top down.
# or bottom up? who knows.







