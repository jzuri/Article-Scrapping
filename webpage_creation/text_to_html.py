# Webpage Creation
from xml.etree import ElementTree as ET
def txt_to_html(txt_file, html_file):

  # Read text file content
  with open(txt_file, 'r') as f:
    content = f.readlines()

  # Grab header and paragraph
  header = content[0].strip()
  paragraph = "".join(content[1:]).strip()

  # Create root element for HTML
  root = ET.Element("html")

  # Create head and body elements
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "Aggregation Site"
  body = ET.SubElement(root, "body")

  # Create header and paragraph elements in body
  h1 = ET.SubElement(body, "h1")
  h1.text = header
  p = ET.SubElement(body, "p")
  p.text = paragraph

  # Write HTML tree to file
  with open(html_file, 'wb') as f:
    tree = ET.ElementTree(root)
    tree.write(f, encoding='utf-8')


txt_file = "./webpage_creation/input.txt"
html_file = "./webpage_creation/webpage.html"
txt_to_html(txt_file, html_file)

print(f"Text file: '{txt_file}' to HTML file: '{html_file}'.")
