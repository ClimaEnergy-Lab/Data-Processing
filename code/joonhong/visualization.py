import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 데이터 로드
raw = pd.read_csv('./datapreprocessing_result/경기도_전력사용량_날씨포함_2022.csv',encoding='utf-8-sig')
df = pd.DataFrame(raw)
# df.info()
plt.rcParams['font.family'] = 'Malgun Gothic'

# 원하는 계약종별 데이터 필터링 (예: '산업용' 계약종별로 필터링)
selected_contract = '주택용'
filtered_df = df[df['계약종별'] == selected_contract]

# 산점도를 사용하여 필터링된 데이터에 대해 온도와 전력사용량 간의 관계 시각화
sns.scatterplot(x='현지기압(hPa)', y='전력사용량', data=filtered_df)
plt.title(f'{selected_contract} - 기압과 전력사용량 간의 산점도')
plt.show()

# # 시각화할 변수 목록 (x축 변수들)
# x_vars = ['기온(°C)', '풍속(m/s)', '풍향(16방위)', '습도(%)', '현지기압(hPa)']
# y_var = '전력사용량'

#
# # 계약종별로 데이터를 그룹화
# grouped = df.groupby('계약종별')
#
# # 계약종별 데이터 수
# n_contracts = len(grouped)
#
# # 서브플롯 크기 설정 (계약종별 행, 변수별 열로 구성)
# fig, axes = plt.subplots(n_contracts, len(x_vars), figsize=(20, 5 * n_contracts), sharey=True)
#
# # 계약종별로 산점도 그리기
# for row_idx, (type, group) in enumerate(grouped):
#     for col_idx, x_var in enumerate(x_vars):
#         sns.scatterplot(x=x_var, y=y_var, data=group, ax=axes[row_idx, col_idx])
#         axes[row_idx, col_idx].set_title(f'{x_var} vs {y_var} ({type})')
#         axes[row_idx, col_idx].set_xlabel(x_var)
#         axes[row_idx, col_idx].set_ylabel(y_var)
#
# # 전체 제목 설정
# plt.suptitle('계약종별 전력사용량과 변수 간의 산점도', fontsize=16)
#
# # 그래프 간 간격 조정
# plt.tight_layout(rect=[0, 0.03, 1, 0.95])
#
# # 그래프 출력
# plt.show()