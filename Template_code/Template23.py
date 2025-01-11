import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    customers = random.randint(6, 50)  # 顾客总数
    first_group = random.randint(2, 40)  # 第一组顾客人数
    second_group = random.randint(1, 40)  # 第二组顾客人数
    no_purchase_group = customers - first_group - second_group  # 没有购买的顾客人数
    first_group_purchases = random.randint(1, 20)  # 第一组顾客每人购买的数量
    second_group_purchases = random.randint(2, 20)  # 第二组顾客每人购买的数量

    # 计算总销售数量
    first_group_total = first_group * first_group_purchases
    second_group_total = second_group * second_group_purchases
    total_sales = first_group_total + second_group_total

    if no_purchase_group<=0:
        return generate_gsm_problem()

    # 随机生成名字
    seller_name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
        {seller_name} sells DVDs. He has {customers} customers on Tuesday.
        His first {first_group} customers buy {first_group_purchases} DVD{'s' if first_group_purchases > 1 else ''} each.
        His next {second_group} customers buy {second_group_purchases} DVD{'s' if second_group_purchases > 1 else ''} each.
        His last {no_purchase_group} customers don't buy any DVDs.
        How many DVDs did {seller_name} sell on Tuesday?
        """

    # GSM 解答模板
    answer_template = f"""
        {seller_name}'s first {first_group} customers buy {first_group} * {first_group_purchases} = <<{first_group}*{first_group_purchases}={first_group_total}>>{first_group_total} DVDs.
        His next {second_group} customers buy {second_group} * {second_group_purchases} = <<{second_group}*{second_group_purchases}={second_group_total}>>{second_group_total} DVDs.
        He sells a total of {first_group_total} + {second_group_total} + 0 = <<{first_group_total}+{second_group_total}+0={total_sales}>>{total_sales} DVDs.
        #### {total_sales}
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
with open("../Template_data/gsm_problems23.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")