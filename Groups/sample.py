from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

# Set up Firefox options for headless mode
options = Options()
options.headless = True

# Set up the Tor SOCKS proxy
tor_proxy_port = 9150  # Replace with the actual SOCKS proxy port if it's different
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = f"socks5://127.0.0.1:{tor_proxy_port}"
proxy.socks_proxy = f"socks5://127.0.0.1:{tor_proxy_port}"
proxy.ssl_proxy = f"socks5://127.0.0.1:{tor_proxy_port}"

# Create a DesiredCapabilities object and set the proxy
capabilities = DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(capabilities)

# Initialize the Firefox WebDriver with the specified options and capabilities
driver = webdriver.Firefox(options=options, desired_capabilities=capabilities)

# Replace 'https://example.com' with the URL of the website you want to visit
url = 'https://example.com'
driver.get(url)

# Extract and print the title of the webpage
title = driver.title
print(f'Title of the webpage: {title}')

# Close the browser
driver.quit()
