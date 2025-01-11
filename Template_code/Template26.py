import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["names"]
        families = raw_data["families"]
    chicken_meal_cost = random.randint(10, 50)  # 鸡肉餐的价格
    milk_pack_price = random.randint(1, 10)  # 每包牛奶的价格
    milk_pack_quantity = random.randint(5, 20)  # 牛奶包的数量
    apple_price = random.randint(1, 5)  # 每个苹果的价格
    apple_quantity = random.randint(5, 20)  # 苹果的数量
    pizza_box_price = random.randint(5, 20)  # 每盒比萨的价格
    total_payment = random.randint(50, 300)  # Marie支付的总费用

    # 计算答案并确保符合条件
    milk_total_cost = milk_pack_price * milk_pack_quantity  # 牛奶总费用
    apple_total_cost = apple_price * apple_quantity  # 苹果总费用
    total_expenses = chicken_meal_cost + milk_total_cost + apple_total_cost  # 鸡肉餐、牛奶和苹果的总费用
    pizza_total_cost = total_payment - total_expenses  # 比萨费用
    pizza_boxes = int(pizza_total_cost / pizza_box_price)  # 比萨的盒数

    if pizza_boxes <= 0:  # 确保答案有效
        return generate_gsm_problem()
    if (pizza_total_cost / pizza_box_price)%1!=0:
        return generate_gsm_problem()

    Marie = random.choice(names)

    # 问题模板
    question_template = f"""
        {Marie} ordered one chicken meal that costs ${chicken_meal_cost}, {milk_pack_quantity} packs of milk that cost ${milk_pack_price} each, {apple_quantity} apples that cost ${apple_price} each, and some boxes of pizza. {Marie} paid a total of ${total_payment}. How many boxes of pizza did {Marie} order if each box costs ${pizza_box_price}?
        """

    # 解答模板
    answer_template = f"""
        {milk_pack_quantity} packs of milk cost ${milk_pack_price} x {milk_pack_quantity} = ${milk_total_cost}.
        {apple_quantity} apples cost ${apple_price} x {apple_quantity} = ${apple_total_cost}.
        The total cost of the chicken meal, milk, and apples is ${chicken_meal_cost} + ${milk_total_cost} + ${apple_total_cost} = ${total_expenses}.
        Thus, the boxes of pizza cost ${total_payment} - ${total_expenses} = ${pizza_total_cost}.
        Therefore, {Marie} ordered ${pizza_total_cost} / ${pizza_box_price} = {pizza_boxes} boxes of pizza.
        #### {pizza_boxes}
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
with open("../Template_data/gsm_problems26.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")