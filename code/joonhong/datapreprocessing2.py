import os.path
import pandas as pd

# 데이터 로딩: 2023년의 기후와 전력 사용량
rawdata_2022_weather=pd.read_csv('./rawdataclimate/jeju_2022.csv', encoding='cp949')

# 기존 데이터프레임 생성 (기온 데이터를 기반으로)
weather_df = pd.DataFrame(rawdata_2022_weather)

# 변경한 날짜와 시간 칼럼을 합쳐서 '날짜' 칼럼 생성 (YYYY-MM-DD HH:MM 형식)
weather_df['일시'] = pd.to_datetime(weather_df['일시'], format='%Y-%m-%d %H:%M', errors='coerce')

# 0:00을 24:00으로 변환하고 날짜를 하루 전으로 변경하는 함수
def convert_midnight_to_24(row):
    if row.hour == 0 and row.minute == 0:
        return (row - pd.Timedelta(days=1)).strftime('%Y-%m-%d 24:00')
    return row.strftime('%Y-%m-%d %H:%M')

# 적용하여 '0:00'을 '24:00'으로 변환
weather_df['일시'] = weather_df['일시'].apply(convert_midnight_to_24)
# print(weather_df)

# to_csv
output_dir = './datapreprocessing_result/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# csv 파일로 저장
weather_df.to_csv(f'{output_dir}제주도_기온_2022.csv', index=False, encoding='utf-8-sig')