import xml.etree.ElementTree as ET

root = ET.Element("root")
tree = ET.ElementTree(element=root)

employee = ET.SubElement(root, "employee")
employ = ET.SubElement(employee, "employ")

empoly_id = ET.SubElement(employ, id)