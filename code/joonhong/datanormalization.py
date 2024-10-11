import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

raw = pd.read_csv('./datapreprocessing_result/경기도_전력사용량_날씨포함_2022.csv')
df = pd.DataFrame(raw)
# 정규화를 위한 MinMaxScaler 사용
scaler = MinMaxScaler()

# 온도와 전력사용량에 대해 정규화 적용
df[['전력사용량', '전력사용량 평균', '기온(°C)','풍속(m/s)','풍향(16방위)','습도(%)','현지기압(hPa)']] = scaler.fit_transform(df[['전력사용량', '전력사용량 평균', '기온(°C)','풍속(m/s)','풍향(16방위)','습도(%)','현지기압(hPa)']])

output_dir = './datanormalization_result/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

df.to_csv(f'{output_dir}/경기도_전력사용량_날씨포함_2022_nor.csv', index=False, encoding='utf-8-sig')
