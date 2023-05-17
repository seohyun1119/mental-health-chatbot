import os
import pandas as pd
import zipfile


# 추출할 zip 파일 경로
for i in range(1,5):
    zip_file_path = f"C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/TS_01. KAKAO({i}).zip"
    # 추출할 위치
    extract_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/data"
    # zipfile 객체 생성
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 추출
        zip_ref.extractall(extract_path)



# 읽어올 파일들이 들어있는 폴더 경로
folder_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/data"

# 폴더 내의 모든 txt 파일 경로 리스트 생성
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]

# 각 파일을 읽어와서 DataFrame으로 합치기
i = 0
df_list = []
for file_path in file_paths:
    with open(file_path, 'r', encoding = "utf-8") as f:
        i += 1

        # 각 파일의 내용을 DataFrame으로 변환
        df = pd.read_csv(f, sep='\t', header=None)
        df['구분'] = i 
        df_list.append(df)

# 모든 DataFrame 합치기
result_df = pd.concat(df_list, ignore_index= False)


# 추출할 zip 파일 경로
for i in range(1,5):
    zip_file_path = f"C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/TL_01. KAKAO({i}).zip"

    # 추출할 위치
    extract_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/data_labeling"

    # zipfile 객체 생성
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 추출
        zip_ref.extractall(extract_path)

# 추출할 zip 파일 경로
zip_file_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Validation/VL_01. KAKAO.zip"

# 추출할 위치
extract_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Validation/VL_01. KAKAO"

# zipfile 객체 생성
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:

    # 추출
    zip_ref.extractall(extract_path)


# 읽어올 파일들이 들어있는 폴더 경로
folder_path = "C:/dev/github/pythonbasic/mental-health-chatbot/data/Training/data_labeling"

# 폴더 내의 모든 txt 파일 경로 리스트 생성
file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

# 각 파일을 읽어와서 DataFrame으로 합치기
i = 0
df_list = []
for file_path in file_paths:
    with open(file_path, 'r', encoding = "utf-8") as f:
        i += 1

        # 각 파일의 내용을 DataFrame으로 변환
        df = pd.read_csv(f, sep='\t', header=None)
        df['구분'] = i 
        df_list.append(df)

# 모든 DataFrame 합치기
result_df_json = pd.concat(df_list, ignore_index= False)


