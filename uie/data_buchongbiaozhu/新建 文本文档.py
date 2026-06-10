import json

file = "train_split.txt"

with open(file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            print(f"第 {i} 行是空行")
            continue
        try:
            json.loads(line)
        except Exception as e:
            print(f"第 {i} 行 JSON 解析失败：{e}")
            print("内容：", line)
            break
