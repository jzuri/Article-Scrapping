#SOLID Principle - Single Responsibility Principle
#In this case, the data_processing file follows this principle by only handling one responsibility.
#The file is only responsible for hanlding data processing of the information and that is it.
#Splitting up the responsibilities makes sure that the data_processing file handles scraping the data, while the file_handling file reads the data and saves it to the proper file.

#Input
#file_path - The path to the text file containing URLs

#Output
#A list of URLs read from the file.

#Working
#This module contains functions for reading URLs from a text file and saving content to a text file
#read_urls_from_file(file_path) function reads URLs from a text file specified by file_path
#save_content_to_file(file_path, url, content) function saves content to a text file specified by file_path


import os

def read_urls_from_file(file_path):
    """Read URLs from a text file and return a list."""
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()
        return [url.strip() for url in urls]
    except FileNotFoundError:
        print("File not found.")
        return []

def save_content_to_file(file_path, url, content):
    """Save the content to a text file."""
    try:
        with open(file_path, 'a') as output_file:
            output_file.write(f"URL: {url}\n")
            output_file.write(content)
            output_file.write("\n\n")
        print("Content saved to file.")
    except IOError:
        print("Error writing to file.")
