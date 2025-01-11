import random
import json


# 生成 GSM Symbolic Template 问题
def generate_lemon_tree_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["male_names"]
    tree_cost = random.randint(50, 200)  # 树的种植成本
    yearly_lemon_count = random.randint(5, 15)  # 每年生产的柠檬数量
    lemon_price = random.randint(1, 10)/2  # 每个柠檬的售价
    yearly_cost = random.randint(1, 10)  # 每年的养护成本

    # 计算每年收益和回收年限
    yearly_income = yearly_lemon_count * lemon_price
    yearly_earnings = yearly_income - yearly_cost

    if yearly_earnings <= 0:
        return generate_lemon_tree_problem()  # 确保有正收益

    years_to_break_even = int(tree_cost / yearly_earnings)
    if tree_cost / yearly_earnings % 1 != 0:
        return generate_lemon_tree_problem()

    first_profit_year = years_to_break_even + 1

    # 随机选择名字和家庭关系
    Carlos = random.choice(names)

    # 问题模板
    question_template = f"""
    {Carlos} is planting a lemon tree. The tree will cost ${tree_cost} to plant. 
    Each year it will grow {yearly_lemon_count} lemons, which he can sell for ${lemon_price} each. 
    It costs ${yearly_cost} a year to water and feed the tree. 
    How many years will it take before he starts earning money on the lemon tree?
    """

    # 解答模板
    answer_template = f"""
    He makes ${yearly_income} selling lemons each year because {yearly_lemon_count} x {lemon_price} = <<{yearly_lemon_count}*{lemon_price}={yearly_income}>>{yearly_income}.
    He earns ${yearly_earnings} each year from the lemon tree because {yearly_income} - {yearly_cost} = <<{yearly_income}-{yearly_cost}={yearly_earnings}>>{yearly_earnings}.
    It will take {years_to_break_even} years to earn enough to pay off the tree because {tree_cost} / {yearly_earnings} = <<{tree_cost}/{yearly_earnings}={years_to_break_even}>>{years_to_break_even}.
    He will make money in year {first_profit_year} because {years_to_break_even} + 1 = <<{years_to_break_even}+1={first_profit_year}>>{first_profit_year}.
    #### {first_profit_year}
    """

    return question_template.strip(), answer_template.strip()


# 批量生成问题
def generate_lemon_tree_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_lemon_tree_problem()
        problems.append({"question": question, "answer": answer})
    return problems


# 生成并保存为 JSONL 文件
problems = generate_lemon_tree_problems()
with open("../Template_data/gsm_problems13.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
