import matplotlib.pyplot as plt
# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False  


days = ['3/23', '3/24', '3/25', '3/26', '3/27', '3/28', '3/29']
temp_2021 = [25, 24.0, 28, 28, 30, 31,30]
temp_2022 = [25, 25,31, 32, 29, 27, 29]
temp_2023 = [29, 31, 30, 30, 28, 29, 28]
temp_2024 = [30, 31, 31, 31, 30, 30, 29]
temp_2025 = [23, 20, 17, 22, 24,25,25]

# 繪製折線圖
plt.figure(figsize=(10, 6))  # 設定圖表大小
plt.plot(days, temp_2021, marker='o', label='2021')
plt.plot(days, temp_2022, marker='o', label='2022')
plt.plot(days, temp_2023, marker='o', label='2023')
plt.plot(days, temp_2024, marker='o', label='2024')
plt.plot(days, temp_2025, marker='o', label='2025')

# 美化圖表
plt.title('高雄 歷年3/23~3/29每日最高溫 溫度變化', fontsize=14)
plt.xlabel('日期', fontsize=12)
plt.ylabel('平均溫度 (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7) 
plt.legend(title='年份')  # 添加圖例
plt.tight_layout()

# 儲存圖表為圖片（可選）
plt.savefig('kaohsiung_temp_comparison.png', dpi=300)


plt.show()
