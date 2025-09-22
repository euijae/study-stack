import xml.etree.ElementTree as ET

tree = ET.parse("../file/example.xml")
root = tree.getroot()

for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    print(f"{title} by {author}")