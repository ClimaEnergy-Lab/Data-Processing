import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 스크립트의 경로를 가져옵니다.
script_dir = os.path.dirname(os.path.abspath(__file__))

# 날씨 데이터와 전력 데이터 파일을 읽어온다.
gyeongggi_weather_data = pd.read_csv('./weather data/gyeonggi_weather.csv', encoding='cp949')
gyeongggi_power_data = pd.read_csv('./power data/gyeonggi_power.csv', encoding='cp949')

# '지점'과 '지역'을 문자열로 변환
gyeongggi_weather_data['지점'] = gyeongggi_weather_data['지점'].astype(str)
gyeongggi_power_data['지역'] = gyeongggi_power_data['지역'].astype(str)

# '일시'와 '거래일자'를 datetime 형식으로 변환
gyeongggi_weather_data['일시'] = pd.to_datetime(gyeongggi_weather_data['일시'])
gyeongggi_power_data['거래일자'] = pd.to_datetime(gyeongggi_power_data['거래일자'])

# 날씨 데이터와 전력 데이터를 시간과 지역 기준으로 병합
merge_data = pd.merge(
    gyeongggi_weather_data,
    gyeongggi_power_data,
    left_on=['일시', '지점'],
    right_on=['거래일자', '지역'],
    how='outer'  # outer로 병합하여 모든 데이터를 확인
)

# 병합된 데이터의 상태 확인
print("병합된 데이터 행 개수:", merge_data.shape[0])
print(merge_data.head())

if merge_data.shape[0] > 0:
    # 열 이름의 공백 제거
    merge_data.columns = merge_data.columns.str.strip()

    # 상수 값(모든 값이 동일한 열) 제거
    non_constant_columns = merge_data.loc[:, (merge_data != merge_data.iloc[0]).any()]

    # 선택된 열 정의 (상관계수를 구할 열들만 선택)
    selected_columns = ['기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)',
                        '일조(hr)', '일사(MJ/m2)', '적설(cm)', '전운량(10분위)', '지면온도(°C)', '전력거래량(MWh)']

    # 숫자형 열만 선택하여 결측값을 평균값으로 채움
    numeric_columns = non_constant_columns[selected_columns].select_dtypes(include=['float64', 'int64'])
    merge_data_clean = numeric_columns.fillna(numeric_columns.mean())

    # 데이터 표준화
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(merge_data_clean)

    # 표준화된 데이터프레임으로 변환
    scaled_df = pd.DataFrame(scaled_data, columns=merge_data_clean.columns)

    # 상관계수 계산
    correlation_matrix = scaled_df.corr()

    # 상관계수 출력
    print("상관계수 행렬 (표준화 후):")
    print(correlation_matrix)
else:
    print("병합된 데이터가 비어 있습니다. 병합 조건을 확인하세요.")
