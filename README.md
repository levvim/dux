# dux
## Web automation template using python/selenium   

This basic template for a web driver will search the Python documentation.

Set up:

* Download ChromeDriver from `https://chromedriver.chromium.org/downloads` matching your installed version of Chrome
* `pip install selenium`

Run:

* `python dux.py [path to webdriver]`

     
Documentation at `https://selenium-python.readthedocs.io/index.html` for additional options and commands (such as the popular ones below):

```
driver.find_elements_by_xpath("//*[contains(text(), 'search text')]")[0].click()
driver.find_elements_by_xpath('//*[@type="form name"]')[0].send_keys("hello")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("window.scrollTo(0, 0);")
driver.save_screenshot('screenshot.png')
```
