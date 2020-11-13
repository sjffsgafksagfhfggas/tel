import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(executable_path=r'chrome.exe')
driver.get("https://persian-follower.000webhostapp.com/tel/online.php")
time.sleep(5) # Let the user actually see something!
driver.close()