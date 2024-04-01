"""
Main Program Functions
Goal: Read urls from a file and scrape data into individual files
Error: From Project 1, all data was in 1 file not seperate
"""


import requests
from bs4 import BeautifulSoup
from module1.file_handler import read_urls_from_file
from module1.file_handler import save_content_to_file
from module_2.data_processing import scrape_article

def scrape_article(url):
    try:
        #Grabbing the webpage data
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        #Extracting content
        #For msnbc body text = showBlogPage, not z-5 relative
        article_content = soup.find('div', class_ ='showBlogPage')
        
        # If article content is found, return the text
        if article_content:
            return article_content.get_text(separator='\n')
        else:
            return "Just go ahead and change your major =P"
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching url, lol")
        return None

def main():
    # Read URLs from the text file
    with open('article_urls.txt', 'r') as file:
        urls = file.readlines()

    # Remove whitespace characters like `\n` at the end of each line
    urls = [url.strip() for url in urls]

    # Scrape content for each URL
    for url in urls:
        article_content = scrape_article(url)
        if article_content:
            # Save the content to a text file
            with open('articles.txt', 'a') as output_file:
                output_file.write(f"URL: {url}\n")
                output_file.write(article_content)
                output_file.write("\n\n")
            print(f"Article scraped")

if __name__ == "__main__":
    main()

