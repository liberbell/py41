from encodings import utf_8
import xml.etree.ElementTree as ET

root = ET.Element("root")
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, "employee")
employ = ET.SubElement(employee, "employ")

empoly_id = ET.SubElement(employ, "id")
empoly_id.text = "111"
empoly_id = ET.SubElement(employ, "name")
empoly_id.text = "Eric"

empoly_id = ET.SubElement(employ, "id")
empoly_id.text = "222"
empoly_id = ET.SubElement(employ, "name")
empoly_id.text = "Alex"

tree.write("test.xml", encoding=utf_8, xml_declaration=True) 