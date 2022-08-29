import xml.etree.ElementTree as ET

root = ET.Element("root")
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, "employee")
empoly = ET.SubElement(employee, "employ")