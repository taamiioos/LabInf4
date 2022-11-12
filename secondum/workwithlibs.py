import yaml, xmlplain, xml
from time import time
sec = time()
with open("ye.yaml", encoding="utf8") as inf:  root = xmlplain.obj_from_yaml(inf)
with open("total.xml", "w") as outf:  xmlplain.xml_from_obj(root, outf=None, pretty=True)
print(f'Time:{time() - sec}')
#https://guillon.github.io/xmlplain/(читала тут)