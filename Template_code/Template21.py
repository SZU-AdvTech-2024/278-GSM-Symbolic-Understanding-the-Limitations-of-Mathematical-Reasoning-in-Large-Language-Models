import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    orange_drink = random.randint(5, 50)  # 橙汁饮料初始体积
    orange_water_ratio = random.choice([1/2,1/4,  3/4, 4/5, 3/5, 2/5, 1/5])  # 橙汁中水的比例
    pineapple_drink = random.randint(5, 50)  # 菠萝饮料体积
    pineapple_water_ratio = random.choice([1/2,1/4,  3/4, 4/5, 3/5, 2/5, 1/5])  # 菠萝饮料中水的比例
    spilled_drink = random.randint(1, orange_drink // 2)  # 泼洒的橙汁体积

    # 计算剩余橙汁和水
    remaining_orange_drink = orange_drink - spilled_drink
    orange_water = int(remaining_orange_drink * orange_water_ratio)
    pineapple_water = int(pineapple_drink * pineapple_water_ratio)
    total_water = orange_water + pineapple_water
    total_drink = remaining_orange_drink + pineapple_drink

    # 确保总饮料体积合理
    if total_drink <= 0 or total_water <= 0:
        return generate_gsm_problem()
    if (remaining_orange_drink*orange_water_ratio)%1!=0 or (pineapple_drink*pineapple_water_ratio)%1!=0:
        return generate_gsm_problem()

    # 问题模板
    question_template = f"""
        I have {orange_drink} liters of orange drink that are {int(orange_water_ratio * 100)}% water and I wish to add it to {pineapple_drink} liters of pineapple drink that is {int(pineapple_water_ratio * 100)}% water.
        But as I pour it, I spill {spilled_drink} liters of the orange drink. How much water is in the remaining {total_drink} liters?
        """

    # 答案模板
    answer_template = f"""
        There are {pineapple_drink} x {pineapple_water_ratio} = <<{pineapple_drink}*{pineapple_water_ratio}={pineapple_water}>>{pineapple_water} liters of water from the {pineapple_drink} liters pineapple drink.
        After {spilled_drink} liters of orange drink were spilled, there were {orange_drink} - {spilled_drink} = <<{orange_drink}-{spilled_drink}={remaining_orange_drink}>>{remaining_orange_drink} liters of orange drink left.
        Out of the {remaining_orange_drink} liters, {remaining_orange_drink} x {orange_water_ratio} = <<{remaining_orange_drink}*{orange_water_ratio}={orange_water}>>{orange_water} liters are water.
        Thus, there are a total of {pineapple_water} + {orange_water} = <<{pineapple_water}+{orange_water}={total_water}>>{total_water} liters of water out of the {total_drink} liters.
        #### {total_water}
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
with open("../Template_data/gsm_problems21.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")