from selenium import webdriver
from selenium.webdriver import firefox
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()

driver.get('https://na.chargepoint.com/charge_point')
driver.find_element_by_xpath('//*[@id = "search_field"]').send_keys('Geneva, Switzerland')

time.sleep(4)


driver.find_elements_by_xpath('//*[@id = "i_chargespots_sort"]//..//..//div[@class="slimScrollDiv"]//div[@class="slimScrollBar"]')

    
for i in range(5):
    # Scroll page down
    driver.fin('//*[@id = "i_chargespots_sort"]//..//..//div[@class="slimScrollDiv"]').send_keys(Keys.END)
    time.sleep(2)

