import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    total_trip_distance = random.randint(50, 200)  # 总旅行距离
    first_stop_distance = random.randint(10, total_trip_distance // 2)  # 第一次停靠距离
    second_stop_distance_before_end = random.randint(1, 20)  # 第二次停靠距离，从终点开始算

    # 计算答案并确保符合条件
    traveled_distance_between_stops = total_trip_distance - (first_stop_distance + second_stop_distance_before_end)
    if traveled_distance_between_stops <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)
    family = random.choice(families)

    # GSM 问题模板
    question_template = f"""
        {name} made two stops during his {total_trip_distance}-mile bike trip. He first stopped after {first_stop_distance} miles. 
        His second stop was {second_stop_distance_before_end} miles before the end of the trip. 
        How many miles did {name} travel between his first and second stops?
        """

    # GSM 解答模板
    answer_template = f"""
        He traveled {first_stop_distance} miles + {second_stop_distance_before_end} miles = <<{first_stop_distance}+{second_stop_distance_before_end}={first_stop_distance + second_stop_distance_before_end}>>{first_stop_distance + second_stop_distance_before_end} miles not counting the distance between stops.
        {name} traveled {total_trip_distance} miles - {first_stop_distance + second_stop_distance_before_end} miles = <<{total_trip_distance}-{first_stop_distance + second_stop_distance_before_end}={traveled_distance_between_stops}>>{traveled_distance_between_stops} miles between his first and second stop.
        #### {traveled_distance_between_stops}
        """

    return question_template.strip(), answer_template.strip()

# 批量生成 GSM 问题
def generate_gsm_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_gsm_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并打印 50 道问题
problems = generate_gsm_problems()
with open("../Template_data/gsm_problems29.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")