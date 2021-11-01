import os
import shutil

targetDir=r"C:\Users\User\Desktop\RGB_car dataset\labels\val"
targetDir2=r"C:\Users\User\Desktop\RGB_car dataset\labels\new_val"

file_list=os.listdir(targetDir)
txt_list=[]

fail=0
num=0

for file in file_list:
    if '.txt' in file:
        txt_list.append(file)
print(txt_list)
for txt_file in txt_list:
    target_path = targetDir + "\\" + txt_file
    target_path2 = targetDir2 + "\\" + txt_file
    targetTXT = open(target_path, 'r')
    line=targetTXT.readlines()

    for word in line:
        label_Number=word.split(' ')[0]
        if label_Number == '4' :      #car
            f=word.replace('4 ','1 ')
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '5' :    #car
            f= word.replace('5 ','1 ')
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close() 
        elif label_Number == '8' :    #person
            f= word.replace('8 ','0 ')
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        else :
            fail+=1
    num+=1
    print(num)
print(fail)
