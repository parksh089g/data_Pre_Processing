 # -*-coding:utf-8-*-

import os
import xml.etree.ElementTree as ET
	
import shutil
 
targetDir = r"C:\Users\User\Desktop\road(custom)"
num = 1

##targetDir에서 .xml파일 이름들 리스트로 가져오기
file_list = os.listdir(targetDir)
xml_list = []
for file in file_list:
    if '.xml' in file:
        xml_list.append(file)

##모든 .xml파일에 대해 수정
for xml_file in xml_list:
    target_path = targetDir + "\\" + xml_file
    targetXML = open(target_path, 'rt', encoding='UTF8')

    tree = ET.parse(targetXML)

    root = tree.getroot()
    filename=xml_file.split(".")[0]

    ##수정할 부분
    target_tag = root.find("filename")
    target_tag.text = filename + ".jpg"  #수정
    print("[" + str(num) + "]" + xml_file + "[success]")
    
    tree.write(target_path)
    num += 1

print("finished")