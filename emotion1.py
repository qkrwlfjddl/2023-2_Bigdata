'''
import requests

# 네이버 감성 분석 API 엔드포인트
url = 'https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze'

# 네이버 개발자 센터에서 받은 클라이언트 ID와 시크릿을 사용하여 헤더 설정
headers = {
    'X-NCP-APIGW-API-KEY-ID': 'YOUR_CLIENT_ID',
    'X-NCP-APIGW-API-KEY': 'YOUR_CLIENT_SECRET'
}

# 감정 분석할 텍스트 데이터
comment = "여기에 댓글 내용을 넣어주세요."

# API 요청 데이터 형식에 맞게 파라미터 설정
data = {
    'content': comment,
    'lang': 'ko'
}

# API 호출
response = requests.post(url, headers=headers, data=data)

# 결과 확인
if response.status_code == 200:
    result = response.json()
    # 여기서 result를 활용하여 감성 분석 결과를 처리합니다.
    print(result)
else:
    print("API 요청 실패:", response.status_code)
'''
import requests
import pandas as pd
p=0
# 네이버 감성 분석 API 엔드포인트
url = 'https://naveropenapi.apigw.ntruss.com/sentiment-analysis/v1/analyze'

# 네이버 개발자 센터에서 받은 클라이언트 ID와 시크릿을 사용하여 헤더 설정
headers = {
    'X-NCP-APIGW-API-KEY-ID': 'minofcpf4w',
    'X-NCP-APIGW-API-KEY': 'SPBfwHMBuW6Wnzk3McRaWPMfUJfjnugTOtSSBmTG'
}

# 감정 분석 함수 정의
def analyze_comment(url, headers, comment):
    data = {
        'content': comment
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        # 여기서 결과를 처리하고 반환합니다.
        # 예시로 결과를 반환하도록 설정
        sentiment = result['document']['sentiment']
        if sentiment == 'positive':
            return int(1)
        elif sentiment == 'negative':
            return int(-1)
        else:
            return int(0)
    else:
        print("API 요청 실패:", response.status_code)
        print("에러 메시지:", response.text)
        return None

# CSV 파일 불러오기
data = pd.read_csv('labeled_data.csv')

# '댓글 내용'에 대해 감성 분석 API 호출하여 '감정' 열에 결과 추가
for index, row in data.iterrows():
    comment = row['댓글 내용']
    print(p)
    p+=1
    if pd.notnull(comment):  # NaN이 아닌 경우에만 API 요청
        data.loc[index, '감정'] = analyze_comment(url, headers, comment)
        
# 결과 출력
print(data)

# 수정된 데이터프레임을 새로운 CSV 파일로 저장
data.to_csv('감정분석_결과.csv', index=False)
