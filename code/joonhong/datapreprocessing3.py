# 두 csv 파일에서 일시를 기준으로 엑셀의 vlookup 기능 구현
import pandas as pd

# 전력사용량
power_df = pd.read_csv('./datapreprocessing_result/제주도_전력사용량_2022.csv')
# 날씨
weather_df = pd.read_csv('./datapreprocessing_result/제주도_기온_2022.csv')
# print(weather_df)

merged_df = pd.merge(power_df, weather_df, on='일시', how='inner')
merged_df = merged_df.drop(columns=['강수량(mm)', '일조(hr)', '일사(MJ/m2)', '적설(cm)','전운량(10분위)','지면온도(°C)'])
# merged_df.info()
# print(merged_df)
merged_df.to_csv(f'./datapreprocessing_result/제주도_전력사용량_날씨포함_2022.csv', index=False, encoding='utf-8-sig')