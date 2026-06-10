# 拆分实体识别与关系抽取
import json

input_file = "dev.json"
output_with_de = "dev_with_de.json"
output_without_de = "dev_without_de.json"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with_de = []
without_de = []

for line in lines:
    line = line.strip()
    if not line:
        continue
    data = json.loads(line)

    prompt = data.get("prompt", "")

    if "的" in prompt:
        with_de.append(line)
    else:
        without_de.append(line)

# 写入两个文件
with open(output_with_de, "w", encoding="utf-8") as f:
    for l in with_de:
        f.write(l + "\n")

with open(output_without_de, "w", encoding="utf-8") as f:
    for l in without_de:
        f.write(l + "\n")

print("包含 '的' 的样本数量：", len(with_de))
print("不包含 '的' 的样本数量：", len(without_de))
print("已生成：", output_with_de, "和", output_without_de)
