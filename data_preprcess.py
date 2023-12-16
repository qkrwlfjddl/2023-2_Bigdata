import pandas as pd
from langdetect import detect, LangDetectException

# csv 불러오기
df = pd.read_csv('/content/gdrive/MyDrive/bigdata/youtube_21_2/combined_data.csv')  

# 중복 댓글 제거
df.drop_duplicates(subset=['댓글 내용'], inplace=True)

def detect_language(text):
    try:
        return detect(text)
    except LangDetectException:
        return 'unknown'  

# 영어 제거
df['language'] = df['댓글 내용'].apply(lambda x: detect_language(x) if pd.notnull(x) else 'unknown')
df = df[df['language'] != 'en']
df = df.drop(columns=['language'])

# csv로 저장
df.to_csv('/content/gdrive/MyDrive/bigdata/youtube_21_2/combined_data2.csv', index=False)

