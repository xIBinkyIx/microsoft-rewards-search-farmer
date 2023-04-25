from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import time

options = webdriver.EdgeOptions()
options.set_capability("unhandledPromptBehavior", "ignore")
driver = webdriver.Edge(options=options)

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.bing.com/")

search_box: WebElement = driver.find_element(By.NAME, "q")
search_box.send_keys("alphabet")
search_box.send_keys(Keys.RETURN)

alphabet = list("abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789")

for letter in alphabet:
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[-1])

    search_box: WebElement = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(letter)
    search_box.send_keys(Keys.RETURN)
    time.sleep(0.2)

driver.switch_to.window(driver.window_handles[0])

driver.quit()
