from xml.etree import ElementTree as et

xml_string=b'<test><name>zhang_san</name><gender>female</gender><phone_number>01234567890</phone_number><note>none</note></test>'

root=et.fromstring(xml_string)

print("*****==================================================*****")
for i in list(root):
    print(i.tag, i.text)
    
print("*****==================================================*****")
test_person=root.getiterator("test")
for i in test_person:
    for j in i:
        print(j.tag, j.text)
    
print("*****==================================================*****")
find_node2=root.findall("name")
print(find_node2[0], find_node2[0].tag, find_node2[0].text)

print("*****==================================================*****")
find_node=root.find("name")
print(find_node, find_node.tag, find_node.text)
