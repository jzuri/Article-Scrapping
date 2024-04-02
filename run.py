"""
Main Program Functions
Goal: Read urls from a file and scrape data into individual files
Error: From Project 1, all data was in 1 file not seperate
"""

import requests
from bs4 import BeautifulSoup
from module_1.file_handling import FileHandling
#from module_1.file_handling import save_content_to_file
from module_2.data_processing import scrape_article
from Adding_API.LLM_API import api_client

"""
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
"""

def main():
    input_file = sys.argv[1]                                          # Getting the path to the input file from command-line arguments
    with open(input_file, "r") as file:
        urls = file.readlines()                                       # Reading URLs from the input file

    data_processing = scrape_article()                                        # Creating an instance of WebScraper class
    file_handling = save_content_to_file()                                      # Creating an instance of FileHandler class
    api_client = api_client(api_key= 'YOUR_API_KEY' )                  # Creating an instance of LLMClient class with API key

    for idx, url in enumerate(urls, start=1):
        url = url.strip()                                              # Removing leading and trailing whitespaces from the URL
        
        # Scrape data from the URL
        headline, body_texts, author, timestamp = data_processing.scrape_article(url)
        
        # Save the processed data to a file in the 'processed' directory
        file_handling.save_file(idx, title=headline, body_texts=body_texts, output_dir="Data/processed")
        
        # Save the raw HTML content to a file in the 'raw' directory
        file_handling.raw_html(idx, url, output_dir="Data/raw")
        
        # Generate summarized version of the article
        result = f"The following article needs to be summarized in 50 words. Article: {body_texts}"
        summarized_article = api_client.summarized_article(result)
        
        # Save the summarized version to a file in the 'summarized' directory
        file_handling.summary_to_file(idx, title=headline, summary=summarized_article, output_dir="Data/summarized")
        
if __name__ == "__main__":
    main()  

