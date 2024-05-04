# Webpage Design Project
from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
  # Clear variables
  read_file = ''
  content = ''
  # Open file
  with open(txt_file, 'r') as f:
    # Create root element
    root = ET.Element("html")
    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "Aggregation Site"
    body = ET.SubElement(root, "body")

    with open(txt_file, 'r') as f:
        # Set range to number of articles
        for i in range(10):
            # Collect title and content of article
            header = f.readline()
            read_file = f.readline()
            content = read_file
            while read_file != '\n':
                content += read_file
                read_file = f.readline()
            
            # set paragraph to content
            paragraph = content
            # Create header and paragraph elements in body
            h1 = ET.SubElement(body, "h1")
            h1.text = header if header else ''
            p = ET.SubElement(body, "p")
            p.text = paragraph if paragraph else ''


    # Write HTML tree to file
    with open(html_file, 'wb') as file:
        tree = ET.ElementTree(root)
        tree.write(file, encoding='utf-8')


txt_file = "./webpage_creation/input.txt"
html_file = "./webpage_creation/webpage.html"

txt_to_html(txt_file, html_file)
