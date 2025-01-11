import random
import json


# 生成 GSM Symbolic Template 问题
def generate_hiking_problem():
    total_distance = random.randint(10, 40)  # 总距离，10-20英里
    first_distance = random.randint(2, total_distance // 2)  # 第一段行走的距离
    second_distance = random.randint(1, (total_distance - first_distance) // 2)  # 第二段行走的距离
    average_speed = random.randint(3, 6)  # 平均速度3-6英里每小时

    # 计算答案
    total_time = total_distance / average_speed  # 总所需时间
    remaining_time = total_time - 2  # 剩余时间
    if total_time % 1 != 0:
        return generate_hiking_problem()
    if remaining_time <= 0:
        return generate_hiking_problem()
    remaining_distance = total_distance - first_distance - second_distance  # 剩余距离
    required_speed = int(remaining_distance / remaining_time)  # 剩余距离的速度

    # 确保剩余的速度是整数
    if remaining_distance / remaining_time % 1 != 0:
        return generate_hiking_problem()

    # GSM 问题模板
    question_template = f"""
    Marissa is hiking a {total_distance}-mile trail. She took 1 hour to walk the first {first_distance} miles, then another hour to walk the next {second_distance} miles. 
    If she wants her average speed to be {average_speed} miles per hour, what speed (in miles per hour) does she need to walk the remaining distance?
    """

    # GSM 解答模板
    answer_template = f"""
    First, figure out how many hours it takes to hike a {total_distance}-mile trail at {average_speed} mph by dividing the distance by the speed: 
    {total_distance} miles / {average_speed} mph = <<{total_distance}/{average_speed}={total_time}>>{total_time} hours.
    Next, subtract the time Marissa already spent walking to find out how much time she has left: 
    {total_time} hours - 1 hours - 1 hours = <<{total_time}-2={remaining_time}>>{remaining_time} hours.
    Now figure out how much distance she has left by subtracting the distance she already traveled from the total distance: 
    {total_distance} miles - {first_distance} miles - {second_distance} miles = <<{total_distance}-{first_distance}-{second_distance}={remaining_distance}>>{remaining_distance} miles.
    Now divide the remaining distance by the remaining time to find out how fast in miles per hour Marissa has to travel: 
    {remaining_distance} miles / {remaining_time} hours = <<{remaining_distance}/{remaining_time}={required_speed}>>{required_speed} mph.
    #### {required_speed}
    """

    return question_template.strip(), answer_template.strip()


# 批量生成问题
def generate_hiking_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_hiking_problem()
        problems.append({"question": question, "answer": answer})
    return problems


# 生成并保存为 JSONL 文件
problems = generate_hiking_problems()
with open("../Template_data/gsm_problems20.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
