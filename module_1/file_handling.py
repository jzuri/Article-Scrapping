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
import requests 

class FileHandling:
    def __init__(self):
        pass

    def save_file(self, idx, title, body_texts, output_dir):
        filename = f"{output_dir}/article{idx}.txt" 
        with open(filename, "w", encoding="utf-8") as file: 
            file.write(f"Title: {title}\n")  # Writing the title to the file
            file.write(f"Body: {body_texts}\n\n")  # Writing the body text to the file

    def raw_html(self, idx, url, output_dir):
        filename = f"{output_dir}/raw_{idx}.html"  
        response = requests.get(url)  
        raw_html = response.text  # Getting the raw HTML content from the response
        with open(filename, "w", encoding="utf-8") as file:  # Opening the file in write mode
            file.write(raw_html)  # Writing the raw HTML content to the file

    def create_directory(self, directory):
        if not os.path.exists(directory): 
            os.makedirs(directory)  # Creating the directory

    def summary_to_file(self, idx, title, summary, output_dir):
        filename = f"{output_dir}/summary{idx}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Title: {title}\n")  # Writing the title to the file
            file.write(f"Summary: {summary}\n\n")  # Writing the summary to the file
