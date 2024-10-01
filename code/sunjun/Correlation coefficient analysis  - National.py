import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 각 지역의 날씨 데이터와 전력 데이터를 읽어온다.
regions = ['gyeonggi', 'jeju', 'jeonnam', 'seoul', 'ulsan']

# 날씨 데이터와 전력 데이터를 담을 빈 리스트
weather_data_list = []
power_data_list = []

# 데이터 경로 설정
base_weather_path = './weather data/'
base_power_path = './power data/'

# 각 지역의 데이터를 읽어오고 리스트에 추가
for region in regions:
    weather_data = pd.read_csv(f'{base_weather_path}{region}_weather.csv', encoding='cp949')
    power_data = pd.read_csv(f'{base_power_path}{region}_power.csv', encoding='cp949')

    # 각 열을 문자열로 변환
    weather_data['지점'] = weather_data['지점'].astype(str)
    power_data['지역'] = power_data['지역'].astype(str)

    # 날짜 데이터 변환
    weather_data['일시'] = pd.to_datetime(weather_data['일시'])
    power_data['거래일자'] = pd.to_datetime(power_data['거래일자'])

    # 병합된 데이터를 리스트에 저장
    merged_data = pd.merge(weather_data, power_data, left_on=['일시', '지점'], right_on=['거래일자', '지역'], how='outer')  # 'outer'로 병합
    weather_data_list.append(merged_data)

# 전국 데이터를 모두 합친다
national_data = pd.concat(weather_data_list, ignore_index=True)

# 병합된 데이터의 상태 확인
print("병합된 데이터 행 개수:", national_data.shape[0])
print(national_data.head())

# 데이터가 비어 있지 않으면 진행
if national_data.shape[0] > 0:
    # 열 이름의 공백 제거
    national_data.columns = national_data.columns.str.strip()

    # 상수 값(모든 값이 동일한 열) 제거
    non_constant_columns = national_data.loc[:, (national_data != national_data.iloc[0]).any()]

    # 분석에 사용할 열 정의
    selected_columns = ['기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)',
                        '일조(hr)', '일사(MJ/m2)', '적설(cm)', '전운량(10분위)', '지면온도(°C)', '전력거래량(MWh)']

    # 숫자형 열만 선택하여 결측값을 평균값으로 채운다
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
    print("상관계수 행렬 (전국 단위 분석):")
    print(correlation_matrix)
else:
    print("병합된 데이터가 비어 있습니다. 병합 조건을 확인하세요.")
