from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')

driver.get("https://www.youtube.com/")
searchbar = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchbar.send_keys('Beyonce Halo')

searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
searchbutton.click()

WebDriverWait(xpath-or-some-other-type)

#Function for clicking video is not working
video = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-radio-renderer')
video.click()