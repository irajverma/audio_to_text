from selenium import webdriver
from selenium.webdriver.chrome.service import Service

Service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=Service)


driver.get("https://google.com")

driver.quit()