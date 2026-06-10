import json
import re
# 使用方法

def process_split(input_path, output_path_ner, output_path_re):
    output_ner = []
    output_re = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            if "的" in item["prompt"]:
                output_re.append(line)
            else:
                output_ner.append(line)
    with open(output_path_re, "w", encoding="utf-8") as f:
        for item in output_re:
            f.write(item)

    with open(output_path_ner, "w", encoding="utf-8") as f:
        for item in output_ner:
            f.write(item)



process_split("./data2/dev_split.txt", "./data2/dev_ner.txt", "./data2/dev_re.txt")