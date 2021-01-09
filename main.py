from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("user-data-dir=C:/Users/your user name/AppData/Local/Google/Chrome/User Data") #change user name here 
driver = webdriver.Chrome(options=options)
driver.get("https://www.walmart.ca/en/ip/t157-tripod/6000200406124")


while(driver.find_elements_by_xpath("//*[text() = 'Add to Cart']").size() == 0 ):
    driver.refresh()
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'css-1i45fk4')))
add = driver.find_element_by_class_name('css-1i45fk4')
add.click()
