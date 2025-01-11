import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["male_names"]
    beforetime = random.randint(1, 50)
    beforespeed = random.randint(10, 120)
    wanttime = random.randint(3, 50)
    duchetime = random.randint(1, wanttime-2)
    firsttime = random.randint(1, wanttime-duchetime)
    firstspeed = random.randint(10, 120)
    secondspeed = random.randint(10, 120)

    # 计算答案并确保符合条件
    beforemiles = beforetime * beforespeed
    firstmiles = firsttime * firstspeed
    leaftime = wanttime - duchetime
    secondtime = leaftime - firsttime
    secondmiles = secondtime * secondspeed
    backmiles = firstmiles + secondmiles
    ans = beforemiles - backmiles
    if secondtime <= 0:
        return generate_gsm_problem()
    if ans < 0:
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    John = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {John} drives for {beforetime} hours at a speed of {beforespeed} mph and then turns around because he realizes he forgot something very important at home.
    He tries to get home in {wanttime} hours but spends the first {duchetime} hours in standstill traffic.
    He spends the next {firsttime} driving at a speed of {firstspeed}mph, before being able to drive the remaining time of the {wanttime} hours going at {secondspeed} mph.
    How far is he from home at the end of those {wanttime} hours?
    """

    # GSM 解答模板
    answer_template = f"""
    When he turned around he was {beforetime}*{beforespeed}=<<{beforetime}*{beforespeed}={beforemiles}>>{beforemiles} miles from home.
    He was only able to drive {wanttime}-{duchetime}=<<{wanttime}-{duchetime}={leaftime}>>{leaftime} hours in the first {wanttime} hours.
    In {firsttime} hour he goes {firstspeed}*{firsttime}=<<{firstspeed}*{firsttime}={firstmiles}>>{firstmiles} miles.
    He then drives another {leaftime}-{firsttime}=<<{leaftime}-{firsttime}={secondtime}>>{secondtime} hours.
    In that time he goes {secondspeed}*{secondtime}=<<{secondspeed}*{secondtime}={secondmiles}>>{secondmiles} miles.
    So he drove {secondmiles}+{firstmiles}=<<{secondmiles}+{firstmiles}={backmiles}>>{backmiles} miles.
    So he is {beforemiles}-{backmiles}=<<{beforemiles}-{backmiles}={ans}>>{ans} miles away from home.
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
with open("../Template_data/gsm_problems9.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")