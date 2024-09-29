## example.py

def p(str):
    print(str, '\n')

# 라이브러리 임포트
import numpy as np
import pandas as pd


# 전력 데이터 프레임 만들기
df_2019 = pd.read_csv('./assets/한국전력거래소_지역별 시간대별 전력거래량_2019.csv', encoding='cp949')
df_2020 = pd.read_csv('./assets/한국전력거래소_지역별 시간대별 전력거래량_2020.csv', encoding='cp949')
df_2021 = pd.read_csv('./assets/한국전력거래소_지역별 시간대별 전력거래량_2021.csv', encoding='cp949')
df_2022 = pd.read_csv('./assets/한국전력거래소_지역별 시간대별 전력거래량_2022.csv', encoding='cp949')
df_2023 = pd.read_csv('./assets/한국전력거래소_지역별 시간대별 전력거래량_2023.csv', encoding='cp949')

# '서울시'에 해당하는 데이터를 각각 필터링한 후 합침
seoul_df_2019 = df_2019[df_2019['지역'] == '서울시']
seoul_df_2020 = df_2020[df_2020['지역'] == '서울시']
seoul_df_2021 = df_2021[df_2021['지역'] == '서울시']
seoul_df_2022 = df_2022[df_2022['지역'] == '서울시']
seoul_df_2023 = df_2023[df_2023['지역'] == '서울시']

# 두 데이터를 concat으로 이어붙이기
seoul_combined = pd.concat([seoul_df_2019, seoul_df_2020, seoul_df_2021, seoul_df_2022, seoul_df_2023], ignore_index=True)
p(seoul_combined)


# '제주도'에 해당하는 데이터를 각각 필터링한 후 합침
jeju_df_2019 = df_2019[df_2019['지역'] == '제주도']
jeju_df_2020 = df_2020[df_2020['지역'] == '제주도']
jeju_df_2021 = df_2021[df_2021['지역'] == '제주도']
jeju_df_2022 = df_2022[df_2022['지역'] == '제주도']
jeju_df_2023 = df_2023[df_2023['지역'] == '제주도']

# 두 데이터를 concat으로 이어붙이기
jeju_combined = pd.concat([jeju_df_2019, jeju_df_2020, jeju_df_2021, jeju_df_2022, jeju_df_2023], ignore_index=True)
p(jeju_combined)

# '울산시'에 해당하는 데이터를 각각 필터링한 후 합침
ulsan_df_2019 = df_2019[df_2019['지역'] == '울산시']
ulsan_df_2020 = df_2020[df_2020['지역'] == '울산시']
ulsan_df_2021 = df_2021[df_2021['지역'] == '울산시']
ulsan_df_2022 = df_2022[df_2022['지역'] == '울산시']
ulsan_df_2023 = df_2023[df_2023['지역'] == '울산시']

# 두 데이터를 concat으로 이어붙이기
ulsan_combined = pd.concat([ulsan_df_2019, ulsan_df_2020, ulsan_df_2021, ulsan_df_2022, ulsan_df_2023], ignore_index=True)
p(ulsan_combined)

# '전라남도'에 해당하는 데이터를 각각 필터링한 후 합침
jeonnam_df_2019 = df_2019[df_2019['지역'] == '전라남도']
jeonnam_df_2020 = df_2020[df_2020['지역'] == '전라남도']
jeonnam_df_2021 = df_2021[df_2021['지역'] == '전라남도']
jeonnam_df_2022 = df_2022[df_2022['지역'] == '전라남도']
jeonnam_df_2023 = df_2023[df_2023['지역'] == '전라남도']

# 두 데이터를 concat으로 이어붙이기
jeonnam_combined = pd.concat([jeonnam_df_2019, jeonnam_df_2020, jeonnam_df_2021, jeonnam_df_2022, jeonnam_df_2023], ignore_index=True)
p(jeonnam_combined)

# '경기도'에 해당하는 데이터를 각각 필터링한 후 합침
gyeonggi_df_2019 = df_2019[df_2019['지역'] == '경기도']
gyeonggi_df_2020 = df_2020[df_2020['지역'] == '경기도']
gyeonggi_df_2021 = df_2021[df_2021['지역'] == '경기도']
gyeonggi_df_2022 = df_2022[df_2022['지역'] == '경기도']
gyeonggi_df_2023 = df_2023[df_2023['지역'] == '경기도']

# 두 데이터를 concat으로 이어붙이기
gyeonggi_combined = pd.concat([gyeonggi_df_2019, gyeonggi_df_2020, gyeonggi_df_2021, gyeonggi_df_2022, gyeonggi_df_2023], ignore_index=True)
p(gyeonggi_combined)


# -------------------------------------------------------
seoul_combined.to_csv('seoul_power.csv', index=True, encoding='cp949')
gyeonggi_combined.to_csv('gyeonggi_power.csv', index=True, encoding='cp949')
ulsan_combined.to_csv('ulsan_power.csv', index=True, encoding='cp949')
jeju_combined.to_csv('jeju_power.csv', index=True, encoding='cp949')
jeonnam_combined.to_csv('jeonnam_power.csv', index=True, encoding='cp949')



# ----------------------------------------------------------
# 날씨 데이터 불러오기
























































