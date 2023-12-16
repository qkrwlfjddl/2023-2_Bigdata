'''
# 합칠 CSV 파일들이 있는 디렉토리 경로
directory = 'C:/Users/Jihee/Desktop/오른소리'
output_file = '오른소리.csv'  # 결과를 저장할 파일명
'''


import pandas as pd
import os

# 합칠 CSV 파일들이 있는 디렉토리 경로
directory = 'C:/Users/Jihee/Desktop/오른소리'
output_file = '오른소리.csv'  # 결과를 저장할 파일명

# 디렉토리 내 CSV 파일 목록 가져오기
file_list = [file for file in os.listdir(directory) if file.endswith('.csv')]

# 첫 번째 CSV 파일을 기준으로 데이터를 읽음 (헤더는 제외)
combined_data = pd.read_csv(os.path.join(directory, file_list[0]), header=0)

# 나머지 CSV 파일들을 읽어서 데이터를 추가 (헤더는 제외)
for file in file_list[1:]:
    data = pd.read_csv(os.path.join(directory, file), header=0)
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# 결과를 CSV 파일로 저장
combined_data.to_csv(output_file, index=False)
