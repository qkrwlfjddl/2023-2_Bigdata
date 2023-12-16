import os
import pandas as pd

#csv 합치기

def concatenate_csv_files(input_folder, output_file):
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    # 폴더 내부 csv 파일 존재 확인
    if not csv_files:
        print("No CSV files found in the folder.")
        return

    combined_data = pd.DataFrame()

    # csv 파일 확인
    for file in csv_files:
        file_path = os.path.join(input_folder, file)
        data = pd.read_csv(file_path, encoding='utf-8-sig')
        combined_data = pd.concat([combined_data, data], ignore_index=True)

    combined_data.to_csv(output_file, index=False)
    print(f"Concatenation completed. Data saved to {output_file}")

# 합칠 파일이 있는 폴더
input_folder = '/content/gdrive/MyDrive/bigdata/youtube_21_2/'
# 합친 결과
output_file = '/content/gdrive/MyDrive/bigdata/youtube_21_2/combined_data.csv'

concatenate_csv_files(input_folder, output_file)




