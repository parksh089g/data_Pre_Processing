 # -*-coding:utf-8-*-
##targetDir에서 .txt파일 이름들 리스트로 가져오기
import os
import shutil
 
targetDir = r"C:\Users\User\Desktop\road-custom\labels2"
targetDir2 = r"C:\Users\User\Desktop\road-custom\newlabels"
num = 0
file_list = os.listdir(targetDir)

txt_list = []
for file in file_list:
    if '.txt' in file:
        txt_list.append(file)

for txt_file in txt_list:
    target_path = targetDir + "\\" + txt_file
    target_path2 = targetDir2 + "\\" + txt_file
    targetTXT = open(target_path, 'r')
    line= targetTXT.readlines()
    
    for word in line:
        if not word.startswith('None'):
            newfile=open(target_path2,'w')
            newfile.write(word)
        else:
            num+=1
        newfile.close()

print(num)
print("done")