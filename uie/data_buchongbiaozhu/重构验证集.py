import json
from collections import Counter

file_path = "dev_split.txt"   # 你的文件路径

prompt_counter = Counter()

with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
            prompt = data.get("prompt", None)
            if prompt:
                prompt_counter[prompt] += 1
        except Exception as e:
            print(f"第 {i} 行 JSON 解析失败，已跳过：{e}")
            continue

# 按出现次数排序
sorted_prompts = prompt_counter.most_common()

print("=== 按出现次数排序的 prompt 类型 ===")
for prompt, count in sorted_prompts:
    print(f"{prompt}: {count}")

print("\n总类型数量：", len(sorted_prompts))
