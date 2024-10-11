# corelationanalysis.py
from ml.clustering_df import correlation


## 상관 분석: 두 변수 간의 관계를 분석 (주로 연속된 값에 대한 관계)

def p(str):
    print(str, '\n')

# economics 데이터 불러오기
import pandas as pd
# pwdata = pd.read_csv('./datapreprocessing_result/경기도_전력사용량_날씨포함_2022.csv')
# 데이터 정규화한 이후 다시 수행
pwdata = pd.read_csv('./datanormalization_result/경기도_전력사용량_날씨포함_2022_nor.csv')
# pwdata.info()
pwdata_df = pd.DataFrame(pwdata)
# 계약종별로 그룹화하여 상관관계 분석
# 기온(°C),풍속(m/s),풍향(16방위),습도(%),현지기압(hPa)
# for type, group in pwdata_df.groupby('계약종별'):
#     p(f'\n[{type}] 상관분석: ')
#     correlation_matrix = group[['전력사용량 평균', '기온(°C)','습도(%)','풍속(m/s)']].corr()
#     p(correlation_matrix)

# Pearson 상관계수 및 p-value 계산
from scipy.stats import pearsonr

# 계약종별로 그룹화하여 Pearson 상관계수 및 p-value 계산
# for type, group in pwdata_df.groupby('계약종별'):
#     print(f"\n[{type}] Pearson 상관분석:")
#     corr, p_value = pearsonr(group['전력사용량 평균'], group['기온(°C)'])
#     print(f"전력사용량-기온 Pearson 상관계수: {corr}, p-value: {p_value}")
#     corr, p_value = pearsonr(group['전력사용량 평균'], group['습도(%)'])
#     print(f"전력사용량-습도 Pearson 상관계수: {corr}, p-value: {p_value}")
#     corr, p_value = pearsonr(group['전력사용량 평균'], group['풍속(m/s)'])
#     print(f"전력사용량-풍속 Pearson 상관계수: {corr}, p-value: {p_value}")

# 계약종별 시각화 상관분석
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams['font.family'] = 'Malgun Gothic'
# 계약종별로 상관계수를 heatmap으로 시각화
# 계약종별로 그룹화하여 heatmap 생성
unique_contracts = pwdata_df['계약종별'].unique()
n_contracts = len(unique_contracts)

# 서브플롯 크기 설정
fig, axes = plt.subplots(1, n_contracts, figsize=(5 * n_contracts, 5), constrained_layout=True)

# 계약종별로 각각 heatmap을 그리기
for i, type in enumerate(unique_contracts):
    group = pwdata_df[pwdata_df['계약종별'] == type]
    correlation_matrix = group[['전력사용량', '전력사용량 평균', '기온(°C)','습도(%)','풍속(m/s)']].corr()

    # subplot 위치에 heatmap 그리기
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=axes[i])
    axes[i].set_title(f'{type} 상관계수 Heatmap')

# 전체 제목 설정
plt.suptitle('계약종별 상관계수 Heatmap', fontsize=16)

import os
# PNG 파일로 저장 (plt.show() 전에 savefig 호출)
output_dir = './corelationanalysis_nor_result/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
plt.savefig(f'{output_dir}/2022경기_계약종별_상관계수_heatmap_nor.png', dpi=300, bbox_inches='tight')

# 그래프 출력
plt.show()
