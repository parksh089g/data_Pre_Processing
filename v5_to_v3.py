import os
from PIL import Image
from sympy import false
from tqdm import tqdm

def convert(size, box):
    dw = size[0]
    dh = size[1]
    x_center=box[0]*dw
    y_center=box[1]*dh
    w = box[2]*dw
    h = box[3]*dh
    xmin = x_center - w/2
    xmax = x_center + w/2
    ymin = y_center - h/2
    ymax = y_center + h/2

    return (int(xmin), int(ymin), int(xmax), int(ymax))

def collect_label_list(image_path, targetDir, targetDir2, flag):
    file_list = os.listdir(targetDir)
    txt_list = []

    print(f"Collecting Label List about {targetDir}")
    for file in tqdm(file_list):
        if '.txt' in file:
            txt_list.append(file)

    print("Converting...")
    for txt_file in tqdm(txt_list):
        target_path = targetDir + "/" + txt_file
        target_path2 = targetDir2 + "/" + txt_file
        img_path= image_path + "/" + txt_file.split('.')[0] + ".jpg" ##이미지 파일 형식에 맞게 수정
        image = Image.open(img_path)
        targetTXT = open(target_path, 'r')
        
        width = int(image.size[0])
        height = int(image.size[1])

        items = targetTXT.readlines()

        for item in items: 
            #바운딩박스 위치 가져오기
            data=item.split()
            x = data[1]
            y = data[2]
            w = data[3]
            h = data[4]
            
            #바운딩박스  변환하기
            b = (float(x), float(y), float(w), float(h))
            bb = convert((width, height), b)
            
            #변환한거 저장하기
            if flag:
                f = open(target_path2, 'a')
                f.write('crack' + " " + " ".join([str(a) for a in bb]) + '\n')
                f.close()
            else:
                f = open(target_path2, 'a')
                f.write('crack' + " " +"0.5"+ " " +" ".join([str(a) for a in bb]) + '\n') #confident default=0.5 필요에 맞게 수정
                f.close()
        

# if __name__ == '__main__':
def converting():
    output_detection_results = './input/detection-results'
    output_ground_truth = './input/ground-truth'
    # output_images = './input/images-optional/'

    detection_results = './input_img/detection-results'
    ground_truth = './input_img/ground-truth'
    images = './input_img/images'

    print("검출 라벨 변환 시작...")
    collect_label_list(images, detection_results, output_detection_results, False)
    print("정답 라벨 변환 시작...")
    collect_label_list(images, ground_truth, output_ground_truth, True)
    print("변환 완료")
