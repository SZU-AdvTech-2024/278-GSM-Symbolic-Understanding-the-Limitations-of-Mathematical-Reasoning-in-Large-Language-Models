import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    discount = random.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])  # 随机选择折扣百分比
    discounted_price = random.randint(2, 50) / 2  # 随机选择折后价格（单位：美元）
    original_price = int(discounted_price / (1 - discount / 100) ) # 原价计算

    if (discounted_price / (1 - discount / 100)) % 1 != 0:
        return generate_gsm_problem()
    # GSM 问题模板
    question_template = f"""
            Kyle bought last year's best-selling book for ${discounted_price}. 
            This is with a {discount}% discount from the original price. 
            What was the original price of the book?
            """

    # GSM 解答模板
    answer_template = f"""
            Let X be the original price of the book. 
            The discounted price is X - X*{discount / 100} = ${discounted_price}.
            Combining like terms, we get {1 - discount / 100}X = ${discounted_price}.
            Dividing both sides by {1 - discount / 100}, we get X = ${original_price}.
            #### {original_price}
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
with open("../Template_data/gsm_problems25.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")