import pandas as pd

# 데이터 로딩
raw = pd.read_csv('./datapreprocessing_result/경기도_전력사용량_날씨포함_2022.csv',encoding='utf-8-sig')
df = pd.DataFrame(raw)
# df.info()
# 결측치 확인
# ['기온(°C)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)']
# print(df['기온(°C)'].isna().sum()) # 2835
# print(df['풍속(m/s)'].isna().sum()) # 729
# print(df['풍향(16방위)'].isna().sum()) # 972
# print(df['습도(%)'].isna().sum()) # 2673
# print(df['현지기압(hPa)'].isna().sum()) # 648

# '계약종별'과 '일시'를 기준으로 그룹화하여 각 그룹의 평균 계산
# 전력사용량과 기온의 NaN 값을 해당 그룹의 평균으로 대치
df['전력사용량'] = df.groupby(['계약종별', '일시'])['전력사용량'].transform(lambda x: x.fillna(x.mean()))
df['기온(°C)'] = df.groupby(['계약종별', '일시'])['기온(°C)'].transform(lambda x: x.fillna(x.mean()))
df['풍속(m/s)'] = df.groupby(['계약종별', '일시'])['풍속(m/s)'].transform(lambda x: x.fillna(x.mean()))
df['풍향(16방위)'] = df.groupby(['계약종별', '일시'])['풍향(16방위)'].transform(lambda x: x.fillna(x.mean()))
df['습도(%)'] = df.groupby(['계약종별', '일시'])['습도(%)'].transform(lambda x: x.fillna(x.mean()))
df['현지기압(hPa)'] = df.groupby(['계약종별', '일시'])['현지기압(hPa)'].transform(lambda x: x.fillna(x.mean()))

print(df['기온(°C)'].isna().sum()) # 0
print(df['풍속(m/s)'].isna().sum()) # 0
print(df['풍향(16방위)'].isna().sum()) # 0
print(df['습도(%)'].isna().sum()) # 0
print(df['현지기압(hPa)'].isna().sum()) # 0

df.to_csv(f'./datapreprocessing_result/경기_전력사용량_날씨포함_2022_NaN.csv', index=False, encoding='utf-8-sig')