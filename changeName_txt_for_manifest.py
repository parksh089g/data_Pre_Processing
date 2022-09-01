from tqdm import tqdm
import os

targetDir=r'D:\LLVIP\infrared\train'

file_list = os.listdir(targetDir)
jpg_list = []
for file in file_list:
    if '.jpg' in file:
        jpg_list.append(file)

f2=open('train_ir.txt','a')

for line in tqdm(jpg_list):
    a= targetDir + '\\' + line +'\n'
    f2.write(a)

f2.close()