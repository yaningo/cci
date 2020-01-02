from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///C:/temp/personal/GitHub/index.html")
driver.execute_script("document.getElementById('clickety').click()")

assert "Happy New Year :-)" in driver.page_source

driver.close()
