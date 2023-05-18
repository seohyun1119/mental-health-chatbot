import os
import pandas as pd

class import_data:
    def __init__(self, path):
        # 읽어올 파일들이 들어있는 폴더 경로
        self.path = "C:/dev/github/mental-health-chatbot/data/Training/data"

    def make_list(self):
        # 폴더 내의 모든 txt 파일 경로 리스트 생성
        file_paths = [os.path.join(self.path, f) for f in os.listdir(self.path) if f.endswith('.txt')]

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
        return df_list

    # 모든 DataFrame 합치기
    result_df = pd.concat(make_list(), ignore_index= False)





###############################################
    # # 읽어올 파일들이 들어있는 폴더 경로
    # folder_path = "C:/dev/github/mental-health-chatbot/data/Training/data_labeling"

    # # 폴더 내의 모든 txt 파일 경로 리스트 생성
    # file_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.json')]

    # # 각 파일을 읽어와서 DataFrame으로 합치기
    # i = 0
    # df_list = []
    # for file_path in file_paths:
    #     with open(file_path, 'r', encoding = "utf-8") as f:
    #         i += 1

    #         # 각 파일의 내용을 DataFrame으로 변환
    #         df = pd.read_csv(f, sep='\t', header=None)
    #         df['구분'] = i 
    #         df_list.append(df)

    # # 모든 DataFrame 합치기
    # result_df_json = pd.concat(df_list, ignore_index= False)


