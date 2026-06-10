import json
import re

def split_paragraphs(text):
    """
    按段落拆分，保留换行符位置
    """
    paragraphs = re.split(r'\n+', text.strip())
    return [p for p in paragraphs if p.strip()]

def adjust_entities_for_paragraph(paragraph, paragraph_start, entities):
    """
    重新定位实体到当前段落
    """
    new_entities = []
    for ent in entities:
        if ent["start"] >= paragraph_start and ent["end"] <= paragraph_start + len(paragraph):
            new_entities.append({
                "text": ent["text"],
                "start": ent["start"] - paragraph_start,
                "end": ent["end"] - paragraph_start
            })
    return new_entities

def process_uie_file(input_path, output_path):
    new_data = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)
            content = item["content"]
            entities = item.get("result_list", [])
            prompt = item["prompt"]

            # 按段落拆分
            paragraphs = split_paragraphs(content)

            # 计算每个段落在原文中的起始位置
            offset = 0
            for para in paragraphs:
                para_start = content.find(para, offset)
                offset = para_start + len(para)

                # 重新定位实体
                new_entities = adjust_entities_for_paragraph(para, para_start, entities)

                # 只保留有实体的段落（如果你想保留所有段落，可以去掉这个判断）
                # if not new_entities:
                #     continue

                new_data.append({
                    "content": para,
                    "result_list": new_entities,
                    "prompt": prompt
                })

    # 写入新文件
    with open(output_path, "w", encoding="utf-8") as f:
        for item in new_data:
            if item["result_list"] != []:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"处理完成，共生成 {len(new_data)} 条样本。")


# 使用方法
process_uie_file("./data_buchongbiaozhu/train.txt", "./data_buchongbiaozhu/train_split.txt")
