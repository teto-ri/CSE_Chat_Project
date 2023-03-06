import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("lang=ko_KR")
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--window-size=1920,1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')

driver = webdriver.Chrome(options=options)

URL = 'http://his.pusan.ac.kr/bbs/cse/2605/1134410/artclView.do'

driver.get(url=URL)
screenshot = driver.save_screenshot('my_screenshot.png')