import feedparser
import schedule
import json
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from io import BytesIO
import win32clipboard
from PIL import Image

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


def screenshot(URL,Type):
    options = Options()
    options.add_argument("lang=ko_KR")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--window-size=1280,720')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36')
    
    driver = webdriver.Chrome(options=options)

    driver.set_page_load_timeout(10) # timeout 10 sec

    crawling_success = False
    for i in range(5):
        print(f'==try count:[{i+1}]')
        try:
            driver.get(url=URL)
            crawling_success = True
        except Exception as ex:
            print(f'==try count:[{i+1}] => exception:\n{ex}')
        if crawling_success == True:
            break
        time.sleep(5)
    if crawling_success == False:
        raise AirflowException('retry gogo!') # Airflow Exception
    screenshot = driver.save_screenshot(f'{Type}.png')
    
if __name__ == "__main__":
    with open("./Notice_recent.json", 'r') as file:
        data = json.load(file)
        try:
            screenshot(data['entries'][0]['link'], 'Notice')
            filepath = 'C:/Users/nuc/project/CSE_Chat_Project/Notice.png'
            image = Image.open(filepath)

            output = BytesIO()
            image.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()

            send_to_clipboard(win32clipboard.CF_DIB, data)
        except:
            print("오류")
    