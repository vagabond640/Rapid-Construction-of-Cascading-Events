from sentence_transformers import SentenceTransformer, util
from sklearn.cluster import AgglomerativeClustering
import numpy as np
import os
import pandas as pd

# 1. 加载中文预训练模型 (推荐这个，对短文本语义理解很好)
# 如果本地没有，它会自动从 HuggingFace 下载
model = SentenceTransformer('shibing624/text2vec-base-chinese')
raw_entities = []
data_dir = r"D:\work_project\双击开始工作\灾害链预测\New\返修\数据"
file = "郑州-绘图及中心性计算数据 - 基础设施.xlsx"
file_path = os.path.join(data_dir, file)

df = pd.read_excel(file_path, sheet_name="Sheet3")
entities = df.iloc[:, 1].dropna().astype(str).tolist()
# 2. 模拟你的 UIE 提取数据 (从你的截图中选取的典型短语)
raw_entities.extend(entities)

# 3. 将短语转化为语义向量 (Embedding)
print("正在转换向量...")
embeddings = model.encode(raw_entities)

# 4. 执行层次聚类
# distance_threshold: 距离阈值。越小，分类越细；越大，合并越狠。
# 建议在 0.3 - 0.7 之间尝试。
cluster_model = AgglomerativeClustering(
    n_clusters=None,
    distance_threshold=0.5,
    metric='cosine',
    linkage='average'
)
cluster_model.fit(embeddings)
labels = cluster_model.labels_

# 5. 整理并输出结果
clusters = {}
for idx, label in enumerate(labels):
    if label not in clusters:
        clusters[label] = []
    clusters[label].append(raw_entities[idx])

print("\n--- 聚类对齐结果 ---")
for cluster_id, nodes in clusters.items():
    print(f"【类别 {cluster_id}】包含实体: {nodes}")
    # 这里可以取每组的第一个或最长的一个作为“标准名”
    print(f"建议标准名: {nodes[0]}")
    print("-" * 20)
