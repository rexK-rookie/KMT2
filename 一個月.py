import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False 


days = [f'3/{i}' for i in range(1, 32)]  # 3/1 到 3/31
temp_2023 = [20.9, 19.9, 18.9, 19.2, 20.2, 20.5, 20.9, 21.7, 22.3, 22.2, 
             22.4, 22.3, 19.5, 19.7, 21.8, 22.1, 22.4, 22.2, 21.4, 23.1, 
             24.8, 25.7, 25.7, 24.9, 23.2, 21.4, 20.8, 21.0, 21.9, 22.6, 22.2]
temp_2024 = [20.1, 17.9, 19.6, 22.5, 26.0, 25.1, 20.5, 19.1, 18.8, 18.4, 
             20.4, 21.5, 21.3, 21.8, 22.7, 23.7, 24.6, 23.6, 22.2, 21.1, 
             21.1, 23.0, 25.6, 26.4, 26.9, 25.5, 24.1, 25.1, 25.7, 26.2, 27.2]
temp_2025 = [23.8, 24.5, 25.4, 24.4, 22.7, 20.1, 18.8, 20.2, 20.7, 21.8, 
             23.4, 24.4, 24.3, 23.0, 23.2, 19.7, 16.7, 16.5, 15.5, 15.3, 
             17.1, 22.2, 23.0, 24.3, 25.4, 26.8, 27.3, 25.6, 22.3, 20.5, 20.4]

# 繪製折線圖
plt.figure(figsize=(12, 6))  # 圖表寬度適應31天
plt.plot(days, temp_2023, marker='o', label='2023年', color='green', markersize=4)
plt.plot(days, temp_2024, marker='o', label='2024年', color='blue', markersize=4)
plt.plot(days, temp_2025, marker='o', label='2025年', color='red', markersize=4)


plt.title('高雄地區 3/1 至 3/31 平均溫度比較 (2023 vs 2024 vs 2025)', fontsize=14)
plt.xlabel('日期', fontsize=12)
plt.ylabel('平均溫度 (°C)', fontsize=12)
plt.xticks(rotation=45, ha='right')  # 旋轉X軸標籤，避免重疊
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='年份')
plt.tight_layout()  # 調整布局，避免標籤被裁切


plt.savefig('temp_comparison_2023_2024_2025.png', dpi=300)
plt.show()
