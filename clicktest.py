import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dir_path = os.path.dirname(os.path.realpath(__file__))
path_index = os.path.join(dir_path, 'index.html')

#driver = webdriver.Firefox()
caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = False
driver=webdriver.Firefox(capabilities=caps)
driver.get("file:///" + path_index)
driver.execute_script("document.getElementById('clickety').click()")

assert "Happy New Year :-)" in driver.page_source

driver.close()
