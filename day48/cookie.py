from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
#TODO: add the needed type casting abilities

from time import sleep, time

# DEBUG: just in case... it helps.
from pprint import pprint


# Indentation test.
class Asdf():
    def __init__(self):
        pass

class SidsBrain:
    # Sids brain

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
       try:
           cookies = self.driver.find_element(by=By.ID, value="cookies")
           self.cookies = int(cookies.text.split(' ')[0].replace(',', ''))
       except StaleElementReferenceException:
           """Just ignore this.. we will get it at some point."""
           pass
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


class CookieMonster(SidsBrain):
    """He does just gobble up cookies
    The more cookies you eat the more you make.
    """
    def __init__(self, driver, **kwargs):
        """
         driver: a webdriver from selenium.
        """
        # FIXME: not sure if kwargs is done properly. test.
        super().__init__(driver, *kwargs)
        self.cookie = self.get_cookie()

    # general names of action here:
    def _eat_cookie(self):
       """ eat a cookie """
       self.cookie.click()

    def open_cookie_jar(self) -> tuple:
        return(0, 0)

    def want_more_cookies(self):
        pass

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
        start = time()
        while how_many > 0:
            if time() - start >= for_how_long:
                # no need to continue
                return
            self._eat_cookie()
            how_many -= 1

            # DEBUG: 
            #sleep(0.003) # lets breath a moment.


# Main
#----------

url = 'https://ozh.github.io/cookieclicker/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)


Sid = CookieMonster(driver, lang='DE')

# FIXME: I believe we can figure out a state on when to continue instead of sleeping
# FIXME: We have to wait for javascript to set things up.0
sleep(2) # wait for javascript.

RUN_FOR = 600 # seconds
start = time()

# just a caclution I did that we can do with just clicking the cookie.
our_per_second = 24.0

cookies_to_eat = 15
while time() - start <= RUN_FOR:
    _elapsed_time = round(time() - start)
    
    if False:
        (cookies_to_eat, time_to_eat) = Sid.open_cookie_jar()
    else:
        # rethink and move to open_cookie_jar)()
        total_rate = round(our_per_second + Sid.get_per_second(), 2)
        estimated_time = round(cookies_to_eat/total_rate, 2)
        time_to_eat = estimated_time #( Sid.get_per_second()) / cookies_to_eat
        print(_elapsed_time, Sid.num_cookies(), f"eat {cookies_to_eat} for {time_to_eat}")
        print(Sid.get_per_second(), total_rate, estimated_time)

    Sid.gobble(how_many=cookies_to_eat, for_how_long=time_to_eat)

    if False:
        Sid.want_more_cookies()
    else:
        # rethink and move to want_more_cookies()
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
            # TODO: rework the logic on what number to get next.
            #       consider how many cookies that still exist to be eaten.
            cookies_to_eat = int(product.find_element(By.CLASS_NAME, value="price").text.replace(',', ''))
            break
        # in case we have access of cookies
        #cookies_to_eat -= Sid.num_cookies()


print("Cookies per second", Sid.get_per_second())
Sid.get_per_second()








