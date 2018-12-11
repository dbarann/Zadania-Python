import xml.dom.minidom
example = xml.dom.minidom.parse(open("example.xml"))
temp = example.getElementsByTagName("movie")[0]
temp.tagName = "nomovie"
result = example.toxml("utf-8")
print(result)