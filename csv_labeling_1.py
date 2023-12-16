import pandas as pd

# CSV 파일 로드
df = pd.read_csv('./filtered_comments.csv' , encoding='cp949', lineterminator='\n')

def label_comment(row):
    content = row['댓글 내용']
    title = row['제목']
    
    if '국민의 힘' in content or '국힘' in content or '한동훈' in content or '장관' in content or '동훈' in content or '굥' in content or '여당' in content:
        return 'a'
    elif '더불어 민주당' in content or '민주당' in content or '재명' in content or '제명' in content or '민정' in content or '정현' in content or '민주' in content or '야당' in content:
        return 'b'
    else:
        # 여기서 유튜브 제목을 확인하여 라벨을 다시 결정
        if '국민의 힘' in title or '국힘' in title or '한동훈' in title or '장관' in title or '동훈' in title or '굥' in title or '여당' in title:
            return 'a'
        elif '더불어 민주당' in title or '민주당' in title or '재명' in title or '제명' in title or '민정' in title or '정현' in title or '민주' in title or '야당' in title:
            return 'b'
        else:
            return '0'

# 라벨 열 추가
df['label'] = df.apply(label_comment, axis=1)

# CSV 파일로 저장
df.to_csv('label_csv.csv', encoding='cp949', index=False)