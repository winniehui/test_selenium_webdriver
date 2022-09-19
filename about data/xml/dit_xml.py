from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import Element

dict = {"name":"zhang_san","gender":"female","phone_number":"01234567890","note":"none"}

def convert(tag_name,dict):
    elem= Element(tag_name)
    for key,value in dict.items():
        print(key,":",value)

        xml_elem=Element(key)
        xml_elem.text=str(value)

        elem.append(xml_elem)
    return elem

print("#字典转换")
dict_convert=convert("test",dict)
print("-----------------------------------------")
print(dict_convert,'\n')

print("# 转化为刻度的标准xml")
print(tostring(dict_convert),'\n')

print("# 设置最外层标签的属性")
dict_convert.set('id_number','0123456789')
print(tostring(dict_convert))
