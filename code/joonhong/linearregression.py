import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# 데이터 불러오기
raw = pd.read_csv('./datapreprocessing_result/경기_전력사용량_날씨포함_2022_NaN.csv', encoding='utf-8-sig')
df = pd.DataFrame(raw)

# 원하는 계약종별로 필터링 (주택용, 일반용, 산업용)
selected_contract = '일반용'
filtered_df = df[df['계약종별'] == selected_contract]

# 독립 변수(X)와 종속 변수(y) 설정
# ['기온(°C)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)']
X = filtered_df['현지기압(hPa)'].values.reshape(-1, 1)
y = filtered_df['전력사용량'].values

# 선형 회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, y)

# 회귀선을 그리기 위해 예측값 계산
y_pred = model.predict(X)

# 시각화
plt.rcParams['font.family'] = 'Malgun Gothic'  # 한글 폰트 설정
plt.scatter(X, y, color='blue', label='실제 데이터')  # 실제 데이터
plt.plot(X, y_pred, color='red', label='회귀선')  # 예측된 회귀선
plt.title(f'{selected_contract} - 선형회귀분석: 현지기압(hPa) vs 전력사용량 (kWh)')
plt.xlabel('현지기압(hPa)')
plt.ylabel('전력사용량 (kWh)')
plt.legend()

# 회귀 계수와 절편을 플롯에 추가
coef_text = f"회귀 계수 (기울기): {model.coef_[0]:.2f}"
intercept_text = f"절편: {model.intercept_:.2f}"

# 텍스트를 플롯 위에 추가 (x=최소 기온 값, y=최대 전력사용량에 위치)
plt.text(X.min(), y.max(), coef_text, fontsize=12, color='green')
plt.text(X.min(), y.max() * 0.95, intercept_text, fontsize=12, color='green')

plt.show()
