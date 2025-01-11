import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    x = random.randint(5, 100)
    y = random.randint(5, 100)
    z = random.randint(5, 100)
    p = random.randint(5, 100)

    # 计算答案并确保符合条件
    x_y_z = x - y - z
    ans = (x-y-z)*p
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)
    family = random.choice(families)

    # GSM 问题模板
    question_template = f"""
    {name}'s ducks lay {x} eggs per day.
    She eats {y} for breakfast every morning and bakes muffins for her {family} every day with {z}. 
    She sells the remainder at the farmers' market daily for ${p} per fresh duck egg.
    How much in dollars does she make every day at the farmers' market?
    """

    # GSM 解答模板
    answer_template = f"""
    {name} sells {x} - {y} - {z} = <<{x}-{y}-{z}={x_y_z}>>{x_y_z} duck eggs a day.
    She makes {x_y_z} * {p} = $<<{x_y_z}*{p}={ans}>>{ans} every day at the farmer's market.
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
with open("../Template_data/gsm_problems1.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")