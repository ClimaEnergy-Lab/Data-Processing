import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 각 지역의 날씨 데이터와 전력 데이터를 읽어올다.
regions = ['gyeonggi', 'jeju', 'jeonnam', 'seoul', 'ulsan']

# 지점 코드와 지역명 매핑 테이블
station_to_region = {
    'gyeonggi': ['98', '99', '119', '202', '203'],
    'jeju': ['184', '185', '188', '189'],
    'jeonnam': ['168'],
    'seoul': ['108'],
    'ulsan': ['152']
}

# 데이터 경로 설정
base_weather_path = './weather data/'
base_power_path = './power data/'

# 각 지역의 데이터를 분석하고 상관계수를 출력하는 함수
def analyze_region(region):
    print(f"\n==== {region.upper()} 지역 분석 ====")

    # 날씨 데이터와 전력 데이터를 읽어옴
    weather_data = pd.read_csv(f'{base_weather_path}{region}_weather.csv', encoding='cp949')
    power_data = pd.read_csv(f'{base_power_path}{region}_power.csv', encoding='cp949')

    # 각 열을 문자열로 변환 및 공백 제거
    weather_data['지점'] = weather_data['지점'].astype(str).str.strip()
    power_data['지역'] = power_data['지역'].astype(str).str.strip()

    # 지점 코드와 지역명 매핑 (전력 데이터의 지역명을 지점 코드로 변환)
    weather_data = weather_data[weather_data['지점'].isin(station_to_region[region])]
    power_data['지점'] = station_to_region[region][0]

    # 날짜에서 시간 단위를 제외하고 일 단위로 통일 (날짜 형식 통일)
    weather_data['일시'] = pd.to_datetime(weather_data['일시']).dt.date
    power_data['거래일자'] = pd.to_datetime(power_data['거래일자']).dt.date

    # 두 데이터를 병합
    merged_data = pd.merge(weather_data, power_data, left_on=['일시', '지점'], right_on=['거래일자', '지점'], how='inner')

    # 병합된 데이터 상태 확인
    print(f"병합된 데이터 행 개수: {merged_data.shape[0]}")

    if merged_data.shape[0] > 0:
        # 열 이름의 공백 제거
        merged_data.columns = merged_data.columns.str.strip()

        # 상수 값(모든 값이 동일한 열) 제거
        non_constant_columns = merged_data.loc[:, (merged_data != merged_data.iloc[0]).any()]

        # 분석에 사용할 열 정의
        selected_columns = ['기온(°C)', '강수량(mm)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)',
                            '일조(hr)', '일사(MJ/m2)', '적설(cm)', '전운량(10분위)', '지면온도(°C)', '전력거래량(MWh)']

        # 숫자형 열만 선택하여 결측값을 평균값으로 채움
        numeric_columns = non_constant_columns[selected_columns].select_dtypes(include=['float64', 'int64'])
        merge_data_clean = numeric_columns.fillna(numeric_columns.mean())

        # 결측값 처리 후 표준화 수행
        if merge_data_clean.isnull().values.any():
            print("결측값을 0으로 대체합니다.")
            merge_data_clean = merge_data_clean.fillna(0)  # 남은 NaN 값 0으로 대체

        # 데이터 표준화
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(merge_data_clean)

        # 표준화된 데이터프레임으로 변환
        scaled_df = pd.DataFrame(scaled_data, columns=merge_data_clean.columns)

        # 상관계수 계산
        correlation_matrix = scaled_df.corr()

        # 상관계수 출력
        print("상관계수 행렬:")
        print(correlation_matrix)
    else:
        print("병합된 데이터가 없습니다.")

# 각 지역에 대해 분석을 실행
for region in regions:
    analyze_region(region)
