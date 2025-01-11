import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["male_names"]
        families = raw_data["families"]
    oneglassprice = random.randint(1, 20)
    buyglasses = random.randint(2, 100)
    zhekou = random.randint(1, 9)*10

    # 计算答案并确保符合条件
    price2 = int(oneglassprice * zhekou / 100)
    halfbuyglasses = int(buyglasses/2)
    zhekouglassesprice = price2*halfbuyglasses
    glassesprice = oneglassprice*halfbuyglasses
    ans = zhekouglassesprice+glassesprice
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()
    if buyglasses%2 != 0:
        return generate_gsm_problem()
    if (oneglassprice * zhekou / 100)%1 !=0:
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {name} went to the store to buy glasses for his new apartment.
    One glass costs ${oneglassprice}, but every second glass costs only {zhekou}% of the price.
    {name} wants to buy {buyglasses} glasses.
    How much does he need to pay for them?
    """

    # GSM 解答模板
    answer_template = f"""
    The discount price of one glass is {zhekou}/100 * {oneglassprice} = $<<{zhekou}/100*{oneglassprice}={price2}>>{price2}.
    If every second glass is cheaper, that means {name} is going to buy {buyglasses} / 2 = <<{buyglasses}/2={halfbuyglasses}>>{halfbuyglasses} cheaper glasses.
    So for the cheaper glasses, {name} is going to pay {halfbuyglasses} * {price2} = $<<{halfbuyglasses}*{price2}={zhekouglassesprice}>>{zhekouglassesprice}.
    And for the regular-priced glasses, {name} will pay {halfbuyglasses} * {oneglassprice} = $<<{halfbuyglasses}*{oneglassprice}={glassesprice}>>{glassesprice}.
    So in total {name} needs to pay {zhekouglassesprice} + {glassesprice} = $<<{zhekouglassesprice}+{glassesprice}={ans}>>{ans} for the glasses he wants to buy.
    #### {ans}
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
with open("../Template_data/gsm_problems6.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")