import random
import json

# 生成 GSM Symbolic Template 问题
def generate_dance_class_problem():
    # 定义变量
    total_students = random.randint(20, 100)  # 总学生数
    contemporary_percentage = random.randint(1, 8) * 10 # 报名现代舞的百分比
    jazz_percentage = random.randint(1, 8) * 10  # 剩余学生中报名爵士舞的百分比

    # 计算答案
    contemporary_students = int(total_students * contemporary_percentage / 100)
    remaining_students = total_students - contemporary_students
    jazz_students = int(remaining_students * jazz_percentage / 100)
    hip_hop_students = remaining_students - jazz_students
    hip_hop_percentage = round((hip_hop_students / total_students) * 100)

    if total_students * contemporary_percentage / 100 % 1 != 0:
        return generate_dance_class_problem()
    if remaining_students * jazz_percentage / 100 % 1 != 0:
        return generate_dance_class_problem()
    if hip_hop_percentage < 0 or hip_hop_percentage > 100:
        return generate_dance_class_problem()  # 确保百分比有效

    # GSM 问题模板
    question_template = f"""
    In a dance class of {total_students} students, {contemporary_percentage}% enrolled in contemporary dance, 
    {jazz_percentage}% of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop dance. 
    What percentage of the entire students enrolled in hip-hop dance?
    """

    # GSM 解答模板
    answer_template = f"""
    There are {total_students} x {contemporary_percentage}/100 = <<{total_students}*{contemporary_percentage}/100={contemporary_students}>>{contemporary_students} students who enrolled in contemporary dance.
    So, {total_students} - {contemporary_students} = <<{total_students}-{contemporary_students}={remaining_students}>>{remaining_students} students are enrolled in either jazz or hip-hop dance.
    There are {remaining_students} x {jazz_percentage}/100 = <<{remaining_students}*{jazz_percentage}/100={jazz_students}>>{jazz_students} students who enrolled in jazz dance.
    Hence, {remaining_students} - {jazz_students} = <<{remaining_students}-{jazz_students}={hip_hop_students}>>{hip_hop_students} students enrolled in hip-hop dance.
    This is {hip_hop_students}/{total_students} x 100% = {hip_hop_percentage}% of the entire students.
    #### {hip_hop_percentage}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_dance_class_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_dance_class_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_dance_class_problems()
with open("../Template_data/gsm_problems15.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
