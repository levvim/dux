import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# setup
options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(sys.argv[0], options=options)

# open site
driver.get('https://docs.python.org/3/');

time.sleep(1)
driver.find_elements_by_xpath('//*[@name="q"]')[0].send_keys("list")
time.sleep(1)
driver.find_elements_by_xpath('//*[@value="Go"]')[0].click()
time.sleep(1)
driver.find_elements_by_xpath("//*[contains(text(),'Data')]")[0].click()
time.sleep(3)
driver.quit()
