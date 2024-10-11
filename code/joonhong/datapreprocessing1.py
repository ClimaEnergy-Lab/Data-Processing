import os.path

import pandas as pd



# 데이터 로딩: 2023년의 기후와 전력 사용량
rawdata_2022_power=pd.read_excel('./rawdatapowerconsumption/rawdata2022poconsumptbyhour.xlsx')
# rawdata_2022_seoulclimate=pd.read_csv('./rawdataclimate/seoul_2023.csv',encoding='cp949')
# print(rawdata_2023_power)
# print(rawdata_2023_seoulclimate)

# 데이터 추출: 서울 전력 사용량 중, 주거용과 산업용 추출
'''
컬럼 필터링:
계약종별: '산업용', '주택용' 으로 필터링
본부: '서울'이 포함된 데이터만 필터링
시계열 데이터 처리: 년월일 시간으로 형식 통일
데이터 전처리: 본부 별, 계약종 별, 시간 별 데이터로 변환
'''
# 기존 데이터프레임 생성 (전력 사용량 데이터를 기반으로)
power_df = pd.DataFrame(rawdata_2022_power)
#print(power_df)
# '본부'에 '원하는 지역'이 포함된 데이터만 필터링
power_df = power_df[power_df['본부'].str.contains('제주')]
#print(power_df)
# '계약종별'이 '산업용' 또는 '주택용'인 데이터만 필터링
power_df = power_df[power_df['계약종별'].isin(['산업용', '주택용', '일반용'])]
#print(power_df)
# '년도', '월', '일'을 합쳐서 '날짜' 칼럼 생성
power_df['날짜'] = power_df[['년도', '월', '일']].astype(str).agg(lambda x: f"{x['년도']}-{x['월'].zfill(2)}-{x['일'].zfill(2)}", axis=1)
#print(power_df)
# 시간대별 칼럼(0100 ~ 2400)의 범위 파악
time_columns = [col for col in power_df.columns if col.isdigit()]
#print(time_columns)
# 가로 시간대 데이터들을 세로로 변환
power_df = pd.melt(power_df,
                    id_vars=['본부', '지사', '계약종별', '계기호수', '날짜'],  # 고정할 칼럼들
                    value_vars=time_columns,  # 시간대별 칼럼들 (0100, 0200, ... 2400)
                    var_name='시간',  # 시간대가 들어갈 칼럼명
                    value_name='전력사용량')  # 각 시간대의 전력사용량이 들어갈 칼럼명
#print(power_df)
# 변경한 날짜와 시간 칼럼을 합쳐서 '날짜' 칼럼 생성 (YYYY-MM-DD HH:MM 형식)
power_df['일시'] = power_df.apply(lambda row: f"{row['날짜']} {row['시간'][:2]}:{row['시간'][2:]}", axis=1)
#print(power_df)
# '시간', '본부', '지사' 칼럼 제거
power_df = power_df.drop(columns=['날짜', '시간', '본부'])
#print(power_df)
# '계약종별'과 '날짜' 기준으로 '계기호수'와 '전력사용량'을 그룹화하여 합산
power_df = power_df.groupby(['지사', '계약종별', '일시'], as_index=False).agg({
    '계기호수': 'sum',
    '전력사용량': 'sum'
})
# '지사' = '서울' 칼럼 생성
power_df['지사'] = '제주'
power_df['전력사용량 평균'] = power_df['전력사용량'] / power_df['계기호수']
# print(power_df)
# 전처리된 데이터 저장 위치 설정
output_dir = './datapreprocessing_result/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# csv 파일로 저장
power_df.to_csv(f'{output_dir}제주도_전력사용량_2022.csv', index=False, encoding='utf-8-sig')