# Import libraries
import requests
from bs4 import BeautifulSoup

# Define the target URL
url = "https://www.example.com"  # Replace with the target website

# Send an HTTP request and get the HTML content
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
  # Parse the HTML content
  soup = BeautifulSoup(response.content, "html.parser")

  # Extract text
  text_data = soup.get_text(separator='\n')  # Combine text with newlines

  # Extract links
  links = []
  for a_tag in soup.find_all('a'):
    link = a_tag.get('href')
    if link and link.startswith('http'):  # Check for valid links
      links.append(link)

  # Extract images (source attribute)
  images = []
  for img_tag in soup.find_all('img'):
    image = img_tag.get('src')
    if image and image.startswith('http'):  # Check for valid image URLs
      images.append(image)

  # Print the extracted data
  print("Extracted Text:\n", text_data)
  print("Extracted Links:")
  for link in links:
    print(link)
  print("Extracted Images:")
  for image in images:
    print(image)
else:
  print("Error:", response.status_code)