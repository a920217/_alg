import itertools

# 定義變數數量
n = 3
variables = ['P', 'Q', 'R']

# 使用 product 產生所有 T/F 的組合
# repeat=n 代表將 [True, False] 這個集合重複與自己做乘積 n 次
table_rows = list(itertools.product([True, False], repeat=n))

# 格式化輸出
print(f"{' | '.join(variables)}")
print("-" * (len(variables) * 5))
for row in table_rows:
    # 將布林值轉為 1/0 或 T/F 方便閱讀
    display_row = [("T" if val else "F") for val in row]
    print(f"{' | '.join(display_row)}")
