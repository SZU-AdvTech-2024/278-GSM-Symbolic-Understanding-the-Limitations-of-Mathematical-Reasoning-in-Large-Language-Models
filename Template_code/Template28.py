import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    servings_per_carton = random.randint(10, 20)  # 每个冰淇淋盒子的份量
    cost_per_carton = random.randint(1, 10)  # 每个冰淇淋盒子的价格，避免多位小数
    total_days = random.randint(20, 60)  # 总共的天数，避免过大
    servings_per_day = 1  # 每天吃1份冰淇淋

    # 计算答案并确保符合条件
    num_cartons_needed = int(total_days / servings_per_carton)  # 用整除，确保结果为整数
    total_cost = num_cartons_needed * cost_per_carton
    if total_cost <= 0:  # 确保答案有效
        return generate_gsm_problem()
    if (total_days / servings_per_carton)%1!=0:
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)
    family = random.choice(families)

    # GSM 问题模板
    question_template = f"""
        {name} eats one serving of ice cream every night. 
        She buys cartons of ice cream with {servings_per_carton} servings of ice cream per carton at a cost of ${cost_per_carton}. 
        After {total_days} days, how much will {name} spend on ice cream?
        """

    # GSM 解答模板
    answer_template = f"""
        Each container of ice cream has {servings_per_carton} servings and {name} eats {servings_per_day} serving a night, so after {total_days} days she will need {total_days} // {servings_per_carton} = {num_cartons_needed} containers of ice cream.
        If each carton costs ${cost_per_carton} and she needs {num_cartons_needed} containers, then it will cost her {num_cartons_needed} * ${cost_per_carton} = $<<{num_cartons_needed}*{cost_per_carton}={total_cost}>>{total_cost}.
        #### {total_cost}
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
with open("../Template_data/gsm_problems28.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")