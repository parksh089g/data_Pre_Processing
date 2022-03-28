from ntpath import join
import os
import shutil
from tqdm import tqdm

targetDir=r"D:\FLIR_ADAS_v2\images_rgb_val\label_val"
targetDir2=r"D:\FLIR_ADAS_v2\images_rgb_val\rgb_val_label"

file_list=os.listdir(targetDir)
txt_list=[]

fail=0
num=0

for file in file_list:
    if '.txt' in file:
        txt_list.append(file)

for txt_file in tqdm(txt_list):
    target_path = targetDir + "\\" + txt_file
    target_path2 = targetDir2 + "\\" + txt_file
    targetTXT = open(target_path, 'r')
    line=targetTXT.readlines()

    for word in line:
        label_Number=word.split(' ')[0]
        words=word.split(' ')[1:]
        if label_Number == '3' :      #car  1
            f='1 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '1' :    #person  0
            f='0 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '6':       #vehicle  2
            f='2 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '8':
            f='2 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '79':
            f='2 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '2':       #bicycle   3
            f='3 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '4':       #bicycle   3
            f='3 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '10':       #traffic light   5
            # f= word.replace('10 ','5 ')
            f='5 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        elif label_Number == '12':       #traffic sign   6
            f='6 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
        else :
            f='7 '+' '.join(words)
            newfile=open(target_path2,'a')
            newfile.write(f)
            newfile.close()
            
print(fail)
