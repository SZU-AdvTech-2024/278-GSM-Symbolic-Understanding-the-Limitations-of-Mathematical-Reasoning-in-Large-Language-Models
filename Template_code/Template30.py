import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    price_of_first_pair_of_heels = random.randint(10, 40)  # 第一双高跟鞋的价格
    price_of_second_pair_of_heels = price_of_first_pair_of_heels * random.randint(2, 5)  # 第二双高跟鞋的价格是第一双的2到3倍

    # 计算答案并确保符合条件
    total_heels_cost = price_of_first_pair_of_heels + price_of_second_pair_of_heels
    boots_price = total_heels_cost + 5  # 靴子的价格比两双高跟鞋贵5美元
    if boots_price <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)
    family = random.choice(families)

    # GSM 问题模板
    question_template = f"""
        {name} is shoe shopping when she comes across a pair of boots that fit her shoe budget. 
        However, she has to choose between the boots and two pairs of high heels that together cost five dollars less than the boots. 
        If one pair of heels costs ${price_of_first_pair_of_heels} and the other costs twice as much, how many dollars are the boots?
        """

    # GSM 解答模板
    answer_template = f"""
        The second pair of heels costs {price_of_first_pair_of_heels} * 2 = $<<{price_of_first_pair_of_heels}*2={price_of_second_pair_of_heels}>>{price_of_second_pair_of_heels}.
        The heels together cost {price_of_second_pair_of_heels} + {price_of_first_pair_of_heels} = $<<{price_of_second_pair_of_heels}+{price_of_first_pair_of_heels}={total_heels_cost}>>{total_heels_cost}.
        The boots cost $5 more than both pairs of heels together, so the boots cost {total_heels_cost} + 5 = $<<{total_heels_cost}+5={boots_price}>>{boots_price}.
        #### {boots_price}
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
with open("../Template_data/gsm_problems30.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")