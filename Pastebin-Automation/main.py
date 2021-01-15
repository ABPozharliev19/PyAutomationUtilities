import win32clipboard as clip
from selenium import webdriver
import time

clip.OpenClipboard()
data = clip.GetClipboardData()

PATH = "chromedriver.exe"

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(PATH, options=option)


def openPastebin():
    driver.get("https://pastebin.com/")

    text_area = driver.find_element_by_name("PostForm[text]")
    text_area.send_keys(data)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight - 200);")

    expiration = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[5]/div[1]/div["
                                              "2]/div/span/span[1]/span")
    expiration.click()

    list_item1 = driver.find_element_by_xpath("/html/body/span[2]/span/span[2]/ul/li[5]")
    list_item1.click()

    selector = driver.find_element_by_id("select2-postform-status-container")
    selector.click()

    list_item = driver.find_element_by_xpath("/html/body/span[2]/span/span[2]/ul/li[2]")
    list_item.click()

    button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div/form/div[5]/div[1]/div[8]/button")
    button.click()

    time.sleep(1)

    clip.OpenClipboard()
    clip.EmptyClipboard()
    clip.SetClipboardText(driver.current_url)
    clip.CloseClipboard()

    driver.close()


openPastebin()
