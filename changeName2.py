 # -*-coding:utf-8-*-

import os
import xml.etree.ElementTree as ET
import re
import shutil
 
targetDir = r"D:/차량및보행자데이터셋/도로주행영상/압축푼거/labels/test"
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

    ##수정할 부분
    target_tag = root.find("filename") #xml annotation 내의 jpg 파일이름 (target_tag.text)
    modify_filename=target_tag.text.split(".")[0]+'.xml' #변경할 파일이름
    

    if modify_filename == xml_file:
        continue

    ###이부분은 제 데이터 문제로 넣은 부분이므로 사용하실때 바꿔주시거나 없애주시면 되겠습니다.    
    modify_filename2=re.sub("_v001_1","",xml_file)
    if modify_filename != modify_filename2:
        target_tag.text = modify_filename2.split(".")[0] + ".jpg"  #수정
        tree.write(target_path)
        modify=os.path.join(targetDir,modify_filename2) #바꿀 파일경로
        targetXML.close()
        os.rename(target_path,modify)
        print("[" + str(num) + "]" + modify + "[success]")
        num += 1
        continue
    #######################

    modify=os.path.join(targetDir,modify_filename) #바꿀 파일경로
    targetXML.close()
    os.rename(target_path,modify) #변경

    print("[" + str(num) + "]" + modify + "[success]")
    num += 1

print("finished")
