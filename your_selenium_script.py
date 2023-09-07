from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
options.add_argument('--log-level=DEBUG')  # Add this line to enable WebDriver logging
options.add_argument('--headless')

# Adjust the URL to the onion site you want to visit
onion_url = 'http://omegalock5zxwbhswbisc42o2q2i54vdulyvtqqbudqousisjgc7j7yd.onion/'

driver = webdriver.Firefox(options=options)

# Visit the onion site
driver.get(onion_url)

# Get and print the title of the site
site_title = driver.title
print(f'Title of the site: {site_title}')

# Close the browser when done
driver.quit()
