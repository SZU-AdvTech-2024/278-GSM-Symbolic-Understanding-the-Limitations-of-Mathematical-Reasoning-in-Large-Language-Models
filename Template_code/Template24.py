import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    melt_rate = 2  # 固定每小时燃烧长度，单位厘米
    start_time = random.randint(1, 6)  # 开始燃烧的小时
    end_time = random.randint(start_time + 1, start_time + 6)  # 结束燃烧的小时
    burn_duration = end_time - start_time  # 燃烧时长
    total_melted = burn_duration * melt_rate  # 总减少长度

    # 随机生成开始时间与结束时间（下午）
    start_hour = f"{start_time}:00 PM"
    end_hour = f"{end_time}:00 PM"

    # GSM 问题模板
    question_template = f"""
        A candle melts by {melt_rate} centimeters every hour that it burns.
        How many centimeters shorter will a candle be after burning from {start_hour} to {end_hour}?
        """

    # GSM 解答模板
    answer_template = f"""
        The candle burns for {end_time} - {start_time} = <<{end_time}-{start_time}={burn_duration}>>{burn_duration} hours.
        Thus, the candle will be {melt_rate} * {burn_duration} = <<{melt_rate}*{burn_duration}={total_melted}>>{total_melted} centimeters shorter.
        #### {total_melted}
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
with open("../Template_data/gsm_problems24.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")