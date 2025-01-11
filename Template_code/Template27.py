import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    num_items = random.randint(2, 5)  # 购买的商品种类数量
    cost_shorts = random.randint(10, 50)  # 每条短裤的价格
    cost_pants = random.randint(20, 60)  # 每条裤子的价格
    cost_shoes = random.randint(30, 70)  # 每双鞋的价格

    # 计算答案并确保符合条件
    total_cost = num_items * (cost_shorts + cost_pants + cost_shoes)
    if total_cost <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)
    family = random.choice(families)

    # GSM 问题模板
    question_template = f"""
        {name} bought {num_items} pairs of shorts, {num_items} pairs of pants, and {num_items} pairs of shoes. 
        One pair of shorts costs ${cost_shorts}. One pair of pants costs ${cost_pants}, and one pair of shoes costs ${cost_shoes}. 
        How many dollars did {name} spend on all the clothing items?
        """

    # GSM 解答模板
    answer_template = f"""
        {name} bought {num_items} * (${cost_shorts} + ${cost_pants} + ${cost_shoes}) = $<<{num_items}*({cost_shorts}+{cost_pants}+{cost_shoes})={total_cost}>>{total_cost}.
        {name} spent ${total_cost} on clothing.
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
with open("../Template_data/gsm_problems27.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")