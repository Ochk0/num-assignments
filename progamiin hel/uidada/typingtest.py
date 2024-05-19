from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://typingstudy.com/mn-mongolian-3/speedtest")
    i = 1
    while(True):
        text = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", f'//*[@id="text"]/span[{str(i)}]')))
        print(text.text + " asdasd")
        inputArea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("xpath", '//*[@id="type"]')))
        inputArea.send_keys(text.text)
        inputArea.send_keys(" ")
        i+=1
        if( i > 10):
            i = 1

