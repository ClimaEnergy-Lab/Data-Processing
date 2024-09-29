## making weather data.py

def p(str):
    print(str, '\n')

# 라이브러리 임포트
import numpy as np
import pandas as pd

# 날씨 데이터로 데이터 프레임 만들기
seoul_data2019 = pd.read_csv('./assets2/seoul_2019.csv', encoding='cp949')
seoul_data2020 = pd.read_csv('./assets2/seoul_2020.csv', encoding='cp949')
seoul_data2021 = pd.read_csv('./assets2/seoul_2021.csv', encoding='cp949')
seoul_data2022 = pd.read_csv('./assets2/seoul_2022.csv', encoding='cp949')
seoul_data2023 = pd.read_csv('./assets2/seoul_2023.csv', encoding='cp949')

seoul_combined = pd.concat([seoul_data2019, seoul_data2020, seoul_data2021, seoul_data2022, seoul_data2023], ignore_index=True)

# 날씨 데이터로 데이터 프레임 만들기 (경기도)
gyeonggi_data2019 = pd.read_csv('./assets2/gyeonggi_2019.csv', encoding='cp949')
gyeonggi_data2020 = pd.read_csv('./assets2/gyeonggi_2020.csv', encoding='cp949')
gyeonggi_data2021 = pd.read_csv('./assets2/gyeonggi_2021.csv', encoding='cp949')
gyeonggi_data2022 = pd.read_csv('./assets2/gyeonggi_2022.csv', encoding='cp949')
gyeonggi_data2023 = pd.read_csv('./assets2/gyeonggi_2023.csv', encoding='cp949')

# 경기도 데이터를 하나의 데이터프레임으로 합치기
gyeonggi_combined = pd.concat([gyeonggi_data2019, gyeonggi_data2020, gyeonggi_data2021, gyeonggi_data2022, gyeonggi_data2023], ignore_index=True)

# 날씨 데이터로 데이터 프레임 만들기 (제주도)
jeju_data2019 = pd.read_csv('./assets2/jeju_2019.csv', encoding='cp949')
jeju_data2020 = pd.read_csv('./assets2/jeju_2020.csv', encoding='cp949')
jeju_data2021 = pd.read_csv('./assets2/jeju_2021.csv', encoding='cp949')
jeju_data2022 = pd.read_csv('./assets2/jeju_2022.csv', encoding='cp949')
jeju_data2023 = pd.read_csv('./assets2/jeju_2023.csv', encoding='cp949')

# 제주도 데이터를 하나의 데이터프레임으로 합치기
jeju_combined = pd.concat([jeju_data2019, jeju_data2020, jeju_data2021, jeju_data2022, jeju_data2023], ignore_index=True)

# 날씨 데이터로 데이터 프레임 만들기 (울산시)
ulsan_data2019 = pd.read_csv('./assets2/ulsan_2019.csv', encoding='cp949')
ulsan_data2020 = pd.read_csv('./assets2/ulsan_2020.csv', encoding='cp949')
ulsan_data2021 = pd.read_csv('./assets2/ulsan_2021.csv', encoding='cp949')
ulsan_data2022 = pd.read_csv('./assets2/ulsan_2022.csv', encoding='cp949')
ulsan_data2023 = pd.read_csv('./assets2/ulsan_2023.csv', encoding='cp949')

# 울산시 데이터를 하나의 데이터프레임으로 합치기
ulsan_combined = pd.concat([ulsan_data2019, ulsan_data2020, ulsan_data2021, ulsan_data2022, ulsan_data2023], ignore_index=True)

# 날씨 데이터로 데이터 프레임 만들기 (여수)
yeosu_data2019 = pd.read_csv('./assets2/yeosu_2019.csv', encoding='cp949')
yeosu_data2020 = pd.read_csv('./assets2/yeosu_2020.csv', encoding='cp949')
yeosu_data2021 = pd.read_csv('./assets2/yeosu_2021.csv', encoding='cp949')
yeosu_data2022 = pd.read_csv('./assets2/yeosu_2022.csv', encoding='cp949')
yeosu_data2023 = pd.read_csv('./assets2/yeosu_2023.csv', encoding='cp949')

# 여수 데이터를 하나의 데이터프레임으로 합치기
yeosu_combined = pd.concat([yeosu_data2019, yeosu_data2020, yeosu_data2021, yeosu_data2022, yeosu_data2023], ignore_index=True)

seoul_combined.to_csv('./weather/seoul_weather.csv', index=True, encoding='cp949')
gyeonggi_combined.to_csv('./weather/gyeonggi_weather.csv', index=True, encoding='cp949')
ulsan_combined.to_csv('./weather/ulsan_weather.csv', index=True, encoding='cp949')
jeju_combined.to_csv('./weather/jeju_weather.csv', index=True, encoding='cp949')
yeosu_combined.to_csv('./weather/jeonnam_weather.csv', index=True, encoding='cp949')
