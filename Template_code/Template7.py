import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["names"]
    times = random.randint(3, 100)
    Seattlesheep = random.randint(1, 500)


    # 计算答案并确保符合条件
    Charlestonsheep = times * Seattlesheep
    Toulousesheep = Charlestonsheep*Seattlesheep
    ans = Seattlesheep+Toulousesheep+Charlestonsheep
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    Toulouse = random.choice(names)
    Charleston = random.choice(names)
    Seattle = random.choice(names)
    if Toulouse==Charleston or Toulouse==Seattle or Charleston==Seattle:
        return generate_gsm_problem()

    # GSM 问题模板
    question_template = f"""
    {Toulouse} has twice as many sheep as {Charleston}.
    {Charleston} has {times} times as many sheep as {Seattle}.
    How many sheep do {Toulouse}, {Charleston}, and {Seattle} have together if {Seattle} has {Seattlesheep} sheep?
    """

    # GSM 解答模板
    answer_template = f"""
    If {Seattle} has {Seattlesheep} sheep, {Charleston} has {times} * {Seattlesheep} sheep = <<{Seattlesheep}*{times}={Charlestonsheep}>>{Charlestonsheep} sheep.
    {Toulouse} has twice as many sheep as Charleston, which is 2 * {Charlestonsheep} sheep = <<2*{Charlestonsheep}={Toulousesheep}>>{Toulousesheep} sheep.
    Together, the three has {Seattlesheep} sheep + {Toulousesheep} sheep + {Charlestonsheep} sheep = <<{Seattlesheep}+{Toulousesheep}+{Charlestonsheep}={ans}>>{ans} sheep.
    #### {ans}
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
with open("../Template_data/gsm_problems7.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")