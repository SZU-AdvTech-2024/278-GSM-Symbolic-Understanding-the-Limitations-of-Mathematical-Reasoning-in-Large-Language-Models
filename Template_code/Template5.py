import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
        families = raw_data["families"]
    onechicken_cups = random.randint(1, 10)
    chickens = random.randint(10, 50)
    all_cups = onechicken_cups * chickens
    morning_cups = random.randint(0, all_cups)
    afternoon_cups = random.randint(0, all_cups-morning_cups)

    # 计算答案并确保符合条件
    ans = all_cups - morning_cups - afternoon_cups
    if ans <= 0:  # 确保答案有效
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    name = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    Every day, {name} feeds each of her chickens {onechicken_cups} cups of mixed chicken feed, containing seeds, mealworms and vegetables to help keep them healthy.
    She gives the chickens their feed in three separate meals.
    In the morning, she gives her flock of chickens {morning_cups} cups of feed.
    In the afternoon, she gives her chickens another {afternoon_cups} cups of feed.
    How many cups of feed does she need to give her chickens in the final meal of the day if the size of Wendi's flock is {chickens} chickens?
    """

    # GSM 解答模板
    answer_template = f"""
    If each chicken eats {onechicken_cups} cups of feed per day, then for {chickens} chickens they would need {onechicken_cups}*{chickens}=<<{onechicken_cups}*{chickens}={all_cups}>>{all_cups} cups of feed per day.
    If she feeds the flock {morning_cups} cups of feed in the morning, and {afternoon_cups} cups in the afternoon, then the final meal would require {all_cups}-{morning_cups}-{afternoon_cups}=<<{all_cups}-{morning_cups}-{afternoon_cups}={ans}>>{ans} cups of chicken feed.
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
with open("../Template_data/gsm_problems5.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")