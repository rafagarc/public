#import libraries
import requests
from bs4 import BeautifulSoup

# Specify the path to your text file
file_path = input('Which file contains the URLs list? > ')

# Read the file and create a list of URLs
with open(file_path, 'r') as file:
    url_list = [line.strip() for line in file]

# choose word to search for
my_word = input('Which substring you want to search for? > ')

# Function to check if the chose word is present in the HTML content of a webpage
def has_word(url):
    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP request

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the word "banana" is present in the HTML content
        return my_word in soup.get_text().lower()

    except Exception as e:
        print(f"Error processing {url}: {e}")
        return False

# Filter URLs that contain the chosen word
matching_urls = [url for url in url_list if has_word(url)]

def generate_html_with_links(urls):
    # Create the HTML document with a list of links
    html_document = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Crawling results</title>
    </head>
    <body>
        <h1>Crawling results</h1>
        <ul>
    """

    # Add each link to the HTML document
    for url in urls:
        html_document += f"            <li><a href=\"{url}\">{url}</a></li>\n"

    # Close the HTML document
    html_document += """
        </ul>
    </body>
    </html>
    """

    return html_document

html_content = generate_html_with_links(matching_urls)

# my_file_name = input('Please name the html file that will hold the links. > ')
my_file_name = 'crawling_results'

with open(f"{my_file_name}.html", "w") as file:
    file.write(html_content)