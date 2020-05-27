import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(executable_path='/home/tanweer/Desktop/github_repo/pycrapper/chromedriver',chrome_options=chrome_options)
url = r'https://twitter.com/explore/tabs/trending'
driver.get(url)
time.sleep(3)
print(driver.page_source)
