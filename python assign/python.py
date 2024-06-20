import xml.etree.ElementTree as ET
import scribus

def import_xml_to_scribus(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        if root.tag != 'articles':
            raise ValueError('Invalid XML format: Root tag is not <articles>')

        y_offset = 20  # Initial offset for placing text frames

        for article in root.findall('article'):
            title = article.find('title').text
            description = article.find('description').text

            # Create title text frame
            title_frame = scribus.createText(20, y_offset, 400, 50)
            scribus.setText(title, title_frame)
            scribus.setFont('Arial Bold', title_frame)
            scribus.setFontSize(18, title_frame)
            y_offset += 60  # Update y_offset for the next frame

            # Create description text frame
            desc_frame = scribus.createText(20, y_offset, 400, 50)
            scribus.setText(description, desc_frame)
            scribus.setFont('Arial', desc_frame)
            scribus.setFontSize(12, desc_frame)
            y_offset += 60  # Update y_offset for the next frame

    except FileNotFoundError:
        print(f"Error: The file {xml_file} was not found.")
    except ET.ParseError:
        print(f"Error: The file {xml_file} is not a valid XML.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
import_xml_to_scribus('example.xml')
