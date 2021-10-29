import json

def convert(size, box): #box: coco형식 xmin , ymin , w , h
    dw = 1/size[0]
    dh = 1/size[1]
    w = box[2]
    h = box[3]
    x = box[0]+ w/2
    y = box[1]+ h/2
    x = round(x*dw,6)
    w = round(w*dw,6)
    y = round(y*dh,6)
    h = round(h*dh,6)
    if w <0 or h < 0:
        return False
    return (x,y,w,h)

with open('./train_annotation.json') as f:
    data=json.load(f)

## 라벨 추출
# label_list=open('label_list.txt','w')

# for i in data['categories']:
#     label_name=i['name']
#     label_id=i['id']
#     line=f'{label_name}\n'
#     label_list.write(line)

# label_list.close()

size=[640,512]
#annotation 분리
for i in data['annotations']:
    file_number=i['image_id']+1
    file_number=f'label_train/FLIR_{file_number:0>5}.txt'
    b=i['bbox']

    bb=convert(size, b)

    if bb==False:
        continue

    label_file=open(file_number,'a')
    
    label_number=i['category_id']
    
    line=f'{label_number} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n'

    label_file.write(line)
    label_file.close()

    progress=i['id']
    print(f'{progress}/67844')

print('finish')