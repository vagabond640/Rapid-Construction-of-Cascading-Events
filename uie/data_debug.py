import json

input_file = "./data_buchongbiaozhu/dev_split.txt"
output_file = "./data_buchongbiaozhu/dev_split_cleaned.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    removed = 0
    kept = 0

    for line in fin:
        line = line.strip()
        if not line:
            continue

        try:
            data = json.loads(line)
        except:
            # 如果某行不是合法 JSON，跳过
            continue

        prompt = data.get("prompt", "")

        # 如果 prompt 中包含“台风”，跳过该样本
        if "台风" in prompt:
            removed += 1
            continue

        # 否则写入新文件
        fout.write(json.dumps(data, ensure_ascii=False) + "\n")
        kept += 1

print(f"处理完成：保留 {kept} 条，删除 {removed} 条（包含 '台风' 的样本）")
