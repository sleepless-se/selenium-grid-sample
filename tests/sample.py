
import time
SELENIUM_HUB = 'http://selenium-hub:4444/wd/hub'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver

try:

    print("starting driver")
    driver = webdriver.Remote(
      command_executor=SELENIUM_HUB,
      desired_capabilities=DesiredCapabilities.CHROME,
    )

    print("opening the page")
    driver.get('https://sleepless-se.net/')

    print("take a screenshot")
    driver.save_screenshot('screenshot.png')

    print("show title")
    print(driver.title)

    time.sleep(2)

except:

    print("error")

finally:

    driver.quit()
    print("finish")