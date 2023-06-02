import json
import http.server
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Update the path to the Chrome WebDriver executable
webdriver_path = 'C:\WebDriver\chromedriver.exe'  # Replace with the actual path to chromedriver

# Create a web server to serve the HTML file
server_address = ('', 8000)  # Use a specific port number if needed
httpd = http.server.ThreadingHTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
httpd_thread = threading.Thread(target=httpd.serve_forever)
httpd_thread.start()

# Launch a headless Chrome browser
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the HTML file using the local web server
driver.get('file:///C:/MyProject/form.html')

# Execute JavaScript code to retrieve the stored data
stored_data = driver.execute_script('return localStorage.getItem("formData");')

# Check if stored_data is not None before parsing it as JSON
if stored_data is not None:
    # Parse the retrieved JSON data
    data = json.loads(stored_data)

    # Access the stored values
    name = data['name']
    password = data['password']

    # Print the retrieved values
    print('Name:', name)
    print('Password:', password)
else:
    print('No data found in localStorage')

# Quit the browser
driver.quit()

# Stop the web server
httpd.shutdown()
httpd_thread.join()
