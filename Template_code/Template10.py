import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
    worktime = random.randint(1, 50)
    price = random.randint(1, 10)*10
    jiabantimes = random.randint(11, 50)/10
    alltime = random.randint(worktime+1, worktime+10)

    # 计算答案并确保符合条件
    leaftime = alltime - worktime
    jiabanprice = int(jiabantimes * price)
    jiabanmoney = jiabanprice * leaftime
    workmoney = worktime * price
    ans = workmoney + jiabanmoney
    if jiabanprice%1 != 0:
        return generate_gsm_problem()
    if ans < 0:
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    Eliza = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {Eliza}'s rate per hour for the first {worktime} hours she works each week is ${price}.
    She also receives an overtime pay of {jiabantimes} times her regular hourly rate.
    If {Eliza} worked for {alltime} hours this week, how much are her earnings for this week?
    """

    # GSM 解答模板
    answer_template = f"""
    {Eliza} is entitled to {alltime} -{worktime} = <<{alltime}-{worktime}={leaftime}>>{leaftime} hours overtime pay.
    Her hourly rate for the overtime pay is ${price} x {jiabantimes} = $<<{price}*{jiabantimes}={jiabanprice}>>{jiabanprice}.
    So, {Eliza} will receive ${jiabanprice} x {leaftime} =$<<{jiabanprice}*{leaftime}={jiabanmoney}>>{jiabanmoney} for overtime pay.
    Her regular weekly earning is ${price} x {worktime} = $<<{price}*{worktime}={workmoney}>>{workmoney}.
    Thus, {Eliza} will receive a total of ${workmoney} + ${jiabanmoney} = $<<{workmoney}+{jiabanmoney}={ans}>>{ans} for this week's work.
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
with open("../Template_data/gsm_problems10.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")