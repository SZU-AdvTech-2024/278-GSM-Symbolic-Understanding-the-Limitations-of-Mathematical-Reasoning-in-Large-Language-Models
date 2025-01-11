import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["male_names"]
        families = raw_data["families"]
    x = random.randint(5, 100)*10000
    y = random.randint(5, 100)*10000
    z = random.randint(1,20)*10

    # 计算答案并确保符合条件
    xy_sum = x+y
    zz = z/100
    xup = int(x*zz)
    newx = xup+x
    ans = newx + x - xy_sum
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {name} decides to try flipping a house.
    He buys a house for ${x} and then puts in ${y} in repairs.
    This increased the value of the house by {z}%.
    How much profit did he make?
    """

    # GSM 解答模板
    answer_template = f"""
    The cost of the house and repairs came out to {x}+{y}=$<<{x}+{y}={xy_sum}>>{xy_sum}.
    He increased the value of the house by {x}*{zz}=<<{x}*{zz}={xup}>>{xup}.
    So the new value of the house is {xup}+{x}=$<<{xup}+{x}={newx}>>{newx}.
    So he made a profit of {newx}-{xy_sum}=$<<{newx}-{xy_sum}={ans}>>{ans}.
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
with open("../Template_data/gsm_problems3.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")