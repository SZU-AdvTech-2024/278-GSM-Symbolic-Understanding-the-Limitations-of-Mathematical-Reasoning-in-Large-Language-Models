import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["male_names"]
        families = raw_data["families"]
    x = random.randint(1, 7)
    y = random.randint(1, 10)
    z = random.randint(1,40)*10

    # 计算答案并确保符合条件
    xy = x*y
    ans = xy*z
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {name} decides to run {y} sprints {x} times a week.
    He runs {z} meters each sprint.
    How many total meters does he run a week?
    """

    # GSM 解答模板
    answer_template = f"""
    He sprints {y}*{x}=<<{y}*{x}={xy}>>{xy} times.
    So he runs {xy}*{z}=<<{xy}*{z}={ans}>>{ans} meters.
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
with open("../Template_data/gsm_problems4.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")