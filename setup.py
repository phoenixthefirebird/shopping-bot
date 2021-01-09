#this sets up the account by saving cookies from the first login to the site 

from selenium import webdriver
from cookies import save_cookie
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(options=options)
driver.get("https://www.walmart.ca/en/ip/t157-tripod/6000200406124") #insert the website you want to track here 

#navigate to sign-in page
elem = driver.find_element_by_class_name("css-1xh2uh0").click()

#fill in the form, fill in your account info here to login
email = driver.find_element_by_id("username")
email.send_keys("<insert your email here>")  
password = driver.find_element_by_id("password")
password.send_keys("<insert your account password here>") 
keep_sign_in = driver.find_element_by_class_name('css-12k6l22').click()  #if exists 
sign_in = driver.find_element_by_css_selector('.css-1i45fk4.edzik9p0').click()

#type some random thing in the terminal and hit enter and enjoyed having your cookies saved for next time!
foo = input()
save_cookie(driver, './tmp/cookie')
