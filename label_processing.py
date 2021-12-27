from tqdm import tqdm
import os

def slicing(word):
    word=word.split(": ")[1]
    word=list(map(int,word.split()))
    return word

def label_class(word):
    word=word.replace("-","")
    index_number=[]
    index=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for j in word:
        for i,name in enumerate(index):
            if j==name:
                index_number.append(i)

    return index_number

def label_position(word,position):
    word=slicing(word)
    char_position=[word[0]-position[0],word[1]-position[1],word[2],word[3]]
    return char_position

def convert(box,size):
    dw = 1./size[2]
    dh = 1./size[3]
    x = box[0] + box[2]/2.0
    y = box[1] + box[3]/2.0
    w = box[2]
    h = box[3]
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)    
    return (x,y,w,h)

targetDir = r"C:\Users\User\Desktop\processing\UFPR-ALPR dataset\validation_label"
targetDir2 = r"C:\Users\User\Desktop\processing\UFPR-ALPR dataset\validation_label_output"

file_list = os.listdir(targetDir)
if not os.path.exists(targetDir2):
    os.mkdir(targetDir2)

txt_list = []

print("Collecting Label List...")
for file in tqdm(file_list):
    if '.txt' in file:
        txt_list.append(file)

print("Converting...")
for txt_file in tqdm(txt_list):
    target_path = targetDir + "\\" + txt_file
    target_path2 = targetDir2 + "\\" + txt_file
    targetTXT = open(target_path, 'r')
    line= targetTXT.readlines()

    class_number=None
    position=None
    char_position=[]

    for word in line:
        if word.startswith('plate:'):
            class_number=label_class(word.split(": ")[1])
        elif word.startswith("position_plate:"):
            position=slicing(word)
        elif word.startswith("\tchar"):
            char_position.append(label_position(word,position))
        else:
            continue
    
    newfile=open(target_path2,'a')

    for num,pos in enumerate(char_position):
        x=convert(pos,position)
        newfile.write(f'{class_number[num]} {x[0]} {x[1]} {x[2]} {x[3]}\n')

    newfile.close()
