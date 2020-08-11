from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os

def login(drive,username,passwd):
    input = drive.find_element_by_xpath("//input[@name='user']")
    input.send_keys(username)
 
    input = drive.find_element_by_xpath("//input[@name='password']")
    input.send_keys(passwd)
 
    input.send_keys(Keys.ENTER)
    drive.implicitly_wait(300)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1280,1080');
#driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# grafana panel url
url = 'http://你的grafana页面?orgId=1&from=now-1h&to=now'

# create the image path
basedir = "你的截图保存路径/grafana-screenshot/res"
now = datetime.datetime.now()
savedir = basedir + '/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/'
if not os.path.exists(savedir):
    os.makedirs(savedir)

try:
    driver.get(url)
    # 替换成你的 grafana 账号密码 
    login(driver, 'admin', 'admin') 

    # wait the page loading ...
    time.sleep(5)

    # save images
    driver.get_screenshot_as_file(savedir + str(now.hour) + ".png")
finally:
    driver.close()
    driver.quit()
