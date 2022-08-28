import xml.etree.ElementTree as ET
while True:
    try:
        file_name = input("filename.xml: ")
        tree = ET.parse(file_name)
        root = tree.getroot()
        xmlstr = ET.tostring(root, encoding='utf-8', method='xml')
        template_name = "1033_xxxx"
        template_name = input("Template_Name: ")
        start1 = f'<?xml version="1.0" encoding="utf-8"?>\n<DocumentData>\n<DocumentProperties>\n<Language>\n<LCID>1033</LCID>\n</Language>\n<Template>\n<Library>Ariel360</Library>\n<Group>OPF</Group>\n<Name>{template_name}</Name>\n<StyleName></StyleName>\n<PortalServiceURI>http://cmtl-dbv1q3xda1.msoext.com/odata4/v15</PortalServiceURI>\n</Template>\n</DocumentProperties>\n<Systems>\n<Ariel360>\n'
        end1 = '\n</Ariel360>\n</Systems>\n</DocumentData>'
        xml_data = start1 + xmlstr.decode() + end1
        res = xml_data.encode('utf-8')
        # tree = ET.XML(xml_data
        with open(file_name, "wb") as f:
            f.write(res)
        f.close()
        print("OPF Ariel360 Envelope Added Successfully")
        break

    except:
        print("Enter valid filename")

input('Press Any Key To Exit')


