import numpy as np
import matplotlib.pyplot as plt

# 設定中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
plt.rcParams['axes.unicode_minus'] = False

S0 = 1361  
sigma = 5.67e-8 
alpha = 0.3
epsilon = 0.8

S = S0 / 4 * (1 - alpha) 


def solve_two_layer_model():
    #猜測初始溫度
    Ts = 288  
    T1 = 250  
    T2 = 200  
    
    
    tolerance = 1e-3 
    max_iter = 1000
    for _ in range(max_iter):
        # 計算各層輻射通量
        Fs = sigma * Ts**4  # 地表向上發射的熱輻射
        F1_up = epsilon * sigma * T1**4  # 第一層向上發射
        F1_down = epsilon * sigma * T1**4  # 第一層向下發射
        F2_up = epsilon * sigma * T2**4  # 第二層向上發射
        F2_down = epsilon * sigma * T2**4  # 第二層向下發射
        
        # 地表：太陽輻射 + 第一層向下輻射 = 地表向上輻射
        Ts_new = ((S + F1_down) / sigma)**0.25
        # 第一層：吸收地表輻射 + 第二層向下輻射 = 第一層向上 + 向下輻射
        T1_new = ((epsilon * Fs + F2_down) / (2 * epsilon * sigma))**0.25
        # 第二層：吸收第一層輻射 = 第二層向上 + 向下輻射
        T2_new = ((epsilon * F1_up) / (2 * epsilon * sigma))**0.25
        
        if (abs(Ts_new - Ts) < tolerance and 
            abs(T1_new - T1) < tolerance and 
            abs(T2_new - T2) < tolerance):
            break
        
        Ts = Ts_new
        T1 = T1_new
        T2 = T2_new
    
    return Ts, T1, T2

# 執行模型
Ts, T1, T2 = solve_two_layer_model()

# 轉換為攝氏度
Ts_C = Ts - 273.15
T1_C = T1 - 273.15
T2_C = T2 - 273.15

# 輸出結果
print(f"地表溫度 (Ts): {Ts_C:.2f} °C")
print(f"第一層大氣溫度 (T1): {T1_C:.2f} °C")
print(f"第二層大氣溫度 (T2): {T2_C:.2f} °C")

# 繪製溫度分佈
layers = ['地表', '第一層大氣', '第二層大氣']
temps = [Ts_C, T1_C, T2_C]

plt.figure(figsize=(8, 5))
plt.bar(layers, temps, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('大氣雙層模型溫度分佈', fontsize=14)
plt.ylabel('溫度 (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 保存並顯示
plt.savefig('two_layer_atmosphere.png', dpi=300)
plt.show()
