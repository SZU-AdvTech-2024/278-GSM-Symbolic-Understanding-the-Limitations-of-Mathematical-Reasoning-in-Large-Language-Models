import random
import json

# 生成 GSM Symbolic Template 问题
def generate_train_distance_problem():
    # 随机生成数据
    first_day_distance = random.randint(50, 150)  # 每列火车第一天行驶的距离
    second_day_distance = random.randint(100, 200)  # 每列火车第二天行驶的距离

    # 计算答案
    total_distance = first_day_distance + second_day_distance
    total_combined_distance = total_distance * 2

    # GSM 问题模板
    question_template = f"""
    Two trains leave the same station at the same time. They begin traveling westward, both traveling for {first_day_distance} miles on the first day. 
    The next day, they travel northward, covering {second_day_distance} miles each. 
    What's the distance covered by each train in the two days?
    """

    # GSM 解答模板
    answer_template = f"""
    On the first day, the trains covered 2 trains * {first_day_distance} miles/train = <<2*{first_day_distance}={2 * first_day_distance}>>{2 * first_day_distance} miles together.
    They also covered {second_day_distance} miles/train * 2 trains = <<{second_day_distance}*2={2 * second_day_distance}>>{2 * second_day_distance} miles together on the second day.
    The combined distance the two trains covered in the two days is {2 * first_day_distance} miles + {2 * second_day_distance} miles = <<{2 * first_day_distance}+{2 * second_day_distance}={total_combined_distance}>>{total_combined_distance} miles.
    The average distance for the two days is {total_combined_distance} miles / 2 trains = <<{total_combined_distance}/2={total_distance}>>{total_distance} miles/train.
    #### {total_distance}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_train_distance_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_train_distance_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_train_distance_problems()
with open("../Template_data/gsm_problems17.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
