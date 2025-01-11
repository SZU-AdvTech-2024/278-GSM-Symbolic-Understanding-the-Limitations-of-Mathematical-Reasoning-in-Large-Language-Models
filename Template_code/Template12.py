import random
import json

# 生成 GSM Symbolic Template 问题
def generate_bakery_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
    item1_count = random.randint(1, 5)  # 第一个商品的数量（以打为单位）
    item2_count = random.randint(1, 5)  # 第二个商品的数量
    item3_count = random.randint(1, 5)  # 第三个商品的数量

    item1_price = random.randint(50, 100)  # 第一个商品每打的价格
    item2_price = random.randint(50, 100)  # 第二个商品每打的价格
    item3_price = random.randint(50, 100)  # 第三个商品每打的价格

    # 计算单项和总金额
    cost1 = item1_count * item1_price
    cost2 = item2_count * item2_price
    cost3 = item3_count * item3_price
    total_cost = cost1 + cost2 + cost3

    # 商品名称随机选择
    items = ["donuts", "mini cupcakes", "mini cheesecakes", "croissants", "bagels", "eclairs"]
    random.shuffle(items)
    item1, item2, item3 = items[:3]

    # 随机选择名字和家庭关系
    Toula = random.choice(names)

    # 问题模板
    question_template = f"""
    {Toula} went to the bakery and bought various types of pastries. 
    She bought {item1_count} dozen {item1} which cost ${item1_price} per dozen, 
    {item2_count} dozen {item2} which cost ${item2_price} per dozen, 
    and {item3_count} dozen {item3} which cost ${item3_price} per dozen. 
    How much was the total cost?
    """

    # 解答模板
    answer_template = f"""
    The total charge for the {item1} was {item1_count} x ${item1_price} = $<<{item1_count}*{item1_price}={cost1}>>{cost1}.
    The total charge for the {item2} was {item2_count} x ${item2_price} = $<<{item2_count}*{item2_price}={cost2}>>{cost2}.
    The total charge for the {item3} was {item3_count} x ${item3_price} = $<<{item3_count}*{item3_price}={cost3}>>{cost3}.
    Therefore the total amount {Toula} paid for the pastries was ${cost1} + ${cost2} + ${cost3} = $<<{cost1}+{cost2}+{cost3}={total_cost}>>{total_cost}.
    #### {total_cost}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_bakery_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_bakery_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_bakery_problems()
with open("../Template_data/gsm_problems12.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
