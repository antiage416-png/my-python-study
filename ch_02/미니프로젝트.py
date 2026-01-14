import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from step_3_2 import OUT_3_2

df_raw = pd.read_excel(OUT_3_2)

sns.set_theme(context='poster', style='whitegrid', font='Malgun Gothic')
sns.set_style({'gird.linestyle': '--', 'grid.color': '#EEEEEE'}) # 그리드설정

fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
fig.suptitle('분류별 누적 사용금액')
sns.barplot(data=df_raw, x='분류', y='누적금액', hue='분류', ax=ax)
sns.despine(top=True, right=True, bottom=True, left=True)
plt.show()