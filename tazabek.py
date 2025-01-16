from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
main_url = "https://www.tazabek.kg/lenta/page:1"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(main_url)
elements = driver.find_elements(By.XPATH, "//div[@class='lenta-row-title']")

urls = []
for element in elements:
    title = element.find_element(By.XPATH, ".//a").get_attribute("href")
    urls.append(title)

for url in urls:
    driver.get(url)
    title = driver.find_element(By.XPATH, "//h2[@class='title']").text
    article =driver.find_element(By.XPATH, "//div[@class='text']").text
    time = driver.find_element(By.XPATH, "//span[@class='date']").text
    img = driver.find_element(By.XPATH, "//div[@class='cg_content_type_1']")
    img_2 = img.find_element(By.XPATH, ".//img").get_attribute('src')
    print(img_2)
    # with open("tazabek.txt", "a") as f:
    #     f.write(f'url: {url}\n')
    #     f.write(f'Time: {time}\n')
    #     f.write(f'Title: {title}\n')
    #     f.write(f'Article: {article}\n')
    #     f.write(("-"*40 + "\n"))