import random
import json

# 生成 GSM Symbolic Template 问题
def generate_saleswoman_problem():
    # 定义变量
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
    remaining = random.randint(3, 10)  # 剩余数量
    red_house_sales = random.randint(1, 5)  # 在红房子售出的数量

    # 确保初始总数为整数
    pre_orange = remaining * 2  # 橙房子之前的数量
    pre_red = pre_orange + red_house_sales  # 红房子之前的数量
    total_cleaners = int(pre_red * 3 / 2)  # 初始总数量

    if total_cleaners % 1 != 0:
        return generate_saleswoman_problem()  # 确保答案为整数

    # 随机选择名字
    name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {name} is a door-to-door saleswoman. She sold a third of her vacuum cleaners at the green house, 
    {red_house_sales} more to the red house, and half of what was left at the orange house. 
    If {name} has {remaining} vacuum cleaners left, how many did she start with?
    """

    # GSM 解答模板
    answer_template = f"""
    First multiply the {remaining} remaining vacuum cleaners by two to find out how many {name} had before she visited the orange house: 
    {remaining} * 2 = <<{remaining}*2={pre_orange}>>{pre_orange}.
    Then add {red_house_sales} to figure out how many vacuum cleaners {name} had before visiting the red house: 
    {pre_orange} + {red_house_sales} = <<{pre_orange}+{red_house_sales}={pre_red}>>{pre_red}.
    Now we know that 2/3 * x = {pre_red}, where x is the number of vacuum cleaners {name} started with. 
    We can find x by dividing each side of the equation by 2/3, which produces: 
    x = {total_cleaners}.
    #### {total_cleaners}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_saleswoman_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_saleswoman_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_saleswoman_problems()
with open("../Template_data/gsm_problems14.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
