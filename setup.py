#this sets up the account by saving cookies from the first login to the site 

from selenium import webdriver
from cookies import save_cookie
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://www.walmart.ca/en/ip/t157-tripod/6000200406124")

#navigate to sign-in page
elem = driver.find_element_by_class_name("css-1xh2uh0").click()

#fill in the form, fill in your account info here
email = driver.find_element_by_id("username")
email.send_keys("new2282307660@gmail.com")  
password = driver.find_element_by_id("password")
password.send_keys("@$smolFitness!") 
keep_sign_in = driver.find_element_by_class_name('css-12k6l22').click()  #if exists 
sign_in = driver.find_element_by_css_selector('.css-1i45fk4.edzik9p0').click()

#type some random thing in the terminal and hit enter and enjoyed having your cookies saved for next time!
foo = input()
save_cookie(driver, 'C:/Users/new22/Downloads/selenium/tmp/cookie')
