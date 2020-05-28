import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='/home/tanweer/Desktop/github_repo/pycrapper/chromedriver',chrome_options=chrome_options)
driver.get('https://www.thenewbieprojects.com/Login.html')
#print(driver.page_source)
print("Page Title is: %s" %driver.title)
driver.quit()
#time.sleep(10)
#print(driver.execute_script("return document.body.innerHTML")
#print(driver.page_source)
