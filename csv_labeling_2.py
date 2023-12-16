import pandas as pd
import re

# CSV 파일 불러오기 (가정: '제목', '아이디', '댓글 내용', '좋아요 수' 컬럼이 있다고 가정)
data = pd.read_csv('오른소리.csv')

# 레이블링 함수
def label_comment(row):
    comment = str(row['댓글 내용'])  # 문자열로 변환
    # 특정 키워드를 통해 정당과 관련된 댓글인지 확인
    if re.search(r'국민의 힘|국힘당|여당|한동훈|이동관|윤정부|원희룡|국힘|굥|윤석열|김기현', comment):
        return 'a'
    elif re.search(r'더불어 민주당|이재명|더민|민주당|야당|홍익표|서은숙|강민정|이해찬|정청래|재명|민정|정현', comment):
        return 'b'
    else:
        return 'a'

# apply 함수를 사용하여 각 행에 레이블링 적용하여 label 열에 값 할당
data['label'] = data.apply(label_comment, axis=1)

# 결과 출력 (label 열이 추가된 데이터프레임 확인)
print(data)

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
data.to_csv('labeled_data.csv', index=False)
