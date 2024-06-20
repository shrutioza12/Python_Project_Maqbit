# Python_Project_Maqbit


## Description
This project contains a Python script for Scribus that imports news article titles and descriptions from an XML file and creates text frames in a Scribus document.

## Requirements
- Scribus
- Python 3.x
- xml.etree.ElementTree

## Setup
1. Install Scribus.
2. Clone the repository.
3. Place the `example.xml` file in the project directory.

## Running the Script
1. Open Scribus.
2. Run the script from the Scribus Scripter console:
   ```python
   import import_xml_to_scribus
   import_xml_to_scribus('example.xml')

