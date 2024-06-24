from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

web = 'https://www.thesun.co.uk/sport/football/'
path = r'C:\Users\hrith\OneDrive\Desktop\chromedriver-win64\chromedriver.exe' # introduce path here

# Creating the driver
driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service)
driver.get(web)

# Finding Elements
containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a/span').text
    subtitle = container.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a/h3').text
    link = container.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting data to a CSV file
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv('headline.csv')

driver.quit()