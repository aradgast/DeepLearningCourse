from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://us02web.zoom.us/j/83486128071?pwd=eW1GMm9hemsrVzBRU2k5Q01vclY0QT09"
# url = "https://www.youtube.com/"
page = urlopen(url)
html = page.read().decode("utf-8")
# print(html)
title_index = html.find("<title>")
# print(title_index)
start_index = title_index + len("<title>")
# print(start_index)
end_index = html.find("</title>")
# print(end_index)
title = html[start_index:end_index]
# print(title)
driver = webdriver.Chrome()
# driver.get('https://www.google.com/')
driver.get('https://us02web.zoom.us/j/83486128071?pwd=eW1GMm9hemsrVzBRU2k5Q01vclY0QT09')

# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys(Keys.ENTER)
# webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
# action = webdriver.ActionChains(driver)
# dennis = action.move_to_element_with_offset(to_element='<span dir="ltr">Dennis Lloyd</span>')
# driver.quit()
# search_botton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
# search_botton.click()
