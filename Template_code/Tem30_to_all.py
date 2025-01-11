import os
import json

# 定义文件路径
input_folder = "../Template_data"  # 存放 30 个 JSONL 文件的文件夹
output_file = "../Template_data/gsm_problems_both.jsonl"  # 最终输出的文件

# 构建文件名列表（确保按顺序读取）
input_files = [os.path.join(input_folder, f"gsm_problems{i}.jsonl") for i in range(1, 31)]
print(input_files)

# 确保所有文件存在
for file_path in input_files:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件 {file_path} 不存在，请检查路径和命名。")

# 读取所有文件数据
all_data = []
for file_path in input_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [json.loads(line.strip()) for line in f]
        assert len(lines) == 50, f"文件 {file_path} 的行数错误：{len(lines)}，应为 50"
        all_data.append(lines)

# 确保每个文件包含 50 行数据
assert len(all_data) == 30, "数据文件数不足 30，请检查输入文件夹中的文件数量。"

# 重新组织数据为 50 组，每组包含 30 个数据
reshaped_data = []
for i in range(50):  # 遍历每一行
    group = [all_data[file_idx][i] for file_idx in range(30)]  # 从每个文件中取第 i 行
    reshaped_data.append(group)

# 保存结果到输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    for group in reshaped_data:
        f.write(json.dumps(group, ensure_ascii=False) + "\n")

print(f"数据已重组并保存到文件：{output_file}")
