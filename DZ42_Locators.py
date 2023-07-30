from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

# XPATH

driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/nav/div[2]/div/div[2]/a')  # 1

driver.find_elements(By.XPATH, '//*[@id="main"]/section/header/div[2]/div/div[1]/h1')  # 2

driver.find_element(By.XPATH, '//input[1]')  # 3

driver.find_elements(By.XPATH, "//div[@class='primary-school-banner single-banner']")  # 4

driver.find_element(By.XPATH, '//li[div/@aria-label="5 клас"]')  # 5

# CSS

driver.find_element(By.CSS_SELECTOR, '.sign-in-btn') #1

driver.find_elements(By.CSS_SELECTOR, '#main > section > header > div.outer-wrapper > div > div.heading-group > h1') # 2

driver.find_elements(By.CSS_SELECTOR, 'input[name='search_query']') # 3

driver.find_elements(By.CSS_SELECTOR, '.index-banners > div') #4

driver.find_elements(By.CSS_SELECTOR, '.is-guideline + .category-listing-item') #5
