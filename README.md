# data_Pre_Processing

## 인공지능 학습에 필요한 데이터들을 전처리하기 위한 코드들 모음

>### 1. 여러개의 파일 트리가 있을 때, 하위 데이터(ex. jpg,xml) 등 특정 파일들 한 곳에 모으는 코드
>### moveFile.py
>58번째 줄에 ```f.find_file_path(type='xml')``` 에서 원하는 'jpg','txt' 등의 형식을 줄 수 있음. 

>### 2. xml 파일들에 대한 이름을 수정하는 코드(라벨과 이미지 이름을 맞추기 위해)
>### changeName.py(annotation의 file명을 xml file명과 일치하도록 변경하는 코드)
>### changeName2.py(xml file명을 annotation의 file명과 일치하도록 변경하는 코드)

>### 3. txt 라벨 파일들 중에 데이터 클래스가 None인 라벨을 지우고, 지운 라벨 데이터를 새로운 폴더에 모으는 코드
>### LabelParsing.py

>### 4. bounding box 정보가 주어지면 yolo txt형식의 라벨로 변환해 주는 코드
>### https://velog.io/@parksh089g/yolov5-custom-train-2
>### https://velog.io/@parksh089g/yolov5-custom-train-3

>### 5. yolo형식으로 바꿔주는 코드
>### https://deepbaksuvision.github.io/Modu_ObjectDetection/posts/02_02_Convert2Yolo.html

>### 6. json형식을 yolo형식으로 바꿔주는 코드
>### json2yolo.py

>### 7. 기존의 라벨링된 데이터를 특정 라벨만 쓰기 위해 전처리 해주는 코드
>### change_labelnum.py

추후 계속 업데이트 할 예정
