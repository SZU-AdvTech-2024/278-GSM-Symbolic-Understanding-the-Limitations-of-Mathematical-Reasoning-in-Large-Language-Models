import random
import json

# 生成 GSM Symbolic Template 问题
def generate_merchant_profit_problem():
    # 随机生成数据
    jewelry_cost = random.randint(3, 15) *1000 # 首饰价格
    gadget_cost = random.randint(3, 15) *1000  # 电子产品价格
    jewelry_rate = random.randint(10, 100)/10  # 首饰增长百分比
    gadget_rate = random.randint(10, 100)/10 # 电子产品增长百分比

    # 计算答案
    jewelry_profit = int(jewelry_cost * jewelry_rate/100)
    gadget_profit = int(gadget_cost * gadget_rate/100)

    if jewelry_cost * jewelry_rate / 100 %1 != 0:
        return generate_merchant_profit_problem()
    if gadget_cost * gadget_rate / 100 %1 != 0:
        return generate_merchant_profit_problem()
    if jewelry_profit > gadget_profit:
        max_profit = jewelry_profit
        choice = "jewelry"
    else:
        max_profit = gadget_profit
        choice = "electronic gadgets"

    # GSM 问题模板
    question_template = f"""
    A merchant wants to make a choice of purchase between 2 purchase plans: 
    jewelry worth ${jewelry_cost} or electronic gadgets worth ${gadget_cost}. 
    His financial advisor speculates that the jewelry market will go up {jewelry_rate}% 
    while the electronic gadgets market will rise {gadget_rate}% within the same month. 
    If the merchant is looking to maximize profit at the end of this month by making a choice, how much profit would this be?
    """

    # GSM 解答模板
    answer_template = f"""
    If he purchases jewelry, he will make a profit of {jewelry_rate}% which is ${jewelry_cost}*({jewelry_rate}/100) = $<<{jewelry_cost}*({jewelry_rate}/100)={jewelry_profit}>>{jewelry_profit}.
    If he purchases electronic gadgets, he will make a profit of {gadget_rate}% which is ${gadget_cost}*({gadget_rate}/100) = $<<{gadget_cost}*({gadget_rate}/100)={gadget_profit}>>{gadget_profit}.
    If he wants to maximize profit, since ${max(jewelry_profit, gadget_profit)} > ${min(jewelry_profit, gadget_profit)}, 
    he will choose to purchase {choice}, thereby making a profit of $<<{max_profit}={max_profit}>>{max_profit}.
    #### {max_profit}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_merchant_profit_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_merchant_profit_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_merchant_profit_problems()
with open("../Template_data/gsm_problems16.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
