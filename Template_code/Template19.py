import random
import json

# 生成 GSM Symbolic Template 问题
def generate_omelet_problem():
    # 随机生成数据
    eggs_per_day = random.randint(1, 6)  # 每天吃的鸡蛋数量
    weeks = random.randint(3, 50)  # 持续的周数

    # 计算答案
    eggs_per_week = eggs_per_day * 7
    total_eggs = eggs_per_week * weeks
    dozens = total_eggs // 12
    if  total_eggs / 12 % 1 != 0:
        return generate_omelet_problem()

    # GSM 问题模板
    question_template = f"""
    Alex makes a {eggs_per_day} egg omelet every morning for breakfast.
    How many dozens of eggs will Alex eat in {weeks} weeks?
    """

    # GSM 解答模板
    answer_template = f"""
    Alex eats {eggs_per_day} eggs every day, and there are 7 days in a week, so Alex eats {eggs_per_day}*7 = <<{eggs_per_day}*7={eggs_per_week}>>{eggs_per_week} eggs a week.
    After {weeks} weeks, Alex will have eaten {weeks}*{eggs_per_week} = <<{weeks}*{eggs_per_week}={total_eggs}>>{total_eggs} eggs.
    There are 12 eggs in 1 dozen, and Alex will eat {total_eggs} eggs, so that's {total_eggs}/12 = <<{total_eggs}/12={dozens}>>{dozens} dozen eggs.
    #### {dozens}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_omelet_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_omelet_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_omelet_problems()
with open("../Template_data/gsm_problems19.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
