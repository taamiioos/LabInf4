import yaml, xmlplain, xml

#доп.задание №3
from time import time
sec = time()
#доп.задание №3

with open("ye.yaml", encoding="utf8") as inf:  root = xmlplain.obj_from_yaml(inf)
with open("total.xml", "w") as outf:  xmlplain.xml_from_obj(root, outf=None, pretty=True)

#доп.задание №3
print(f'Time:{time() - sec}')

