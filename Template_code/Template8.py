import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["female_names"]
    alltime = random.randint(10, 500)
    speed = random.randint(1, 50)
    baifenbi = random.randint(1, 9)*10
    windowtime = random.randint(1, 500)

    # 计算答案并确保符合条件
    alldata = alltime * speed
    beforedata = alldata * baifenbi *0.01
    beforetime = int(beforedata/speed)
    ans = windowtime+alltime+beforetime
    if beforetime % 1 != 0:
        return generate_gsm_problem()

    # 随机选择名字和家庭关系
    Carla = random.choice(names)

    # GSM 问题模板
    question_template = f"""
    {Carla} is downloading a {alldata} GB file.
    Normally she can download {speed} GB/minute, but {baifenbi}% of the way through the download, Windows forces a restart to install updates, which takes {windowtime} minutes.
    Then {Carla} has to restart the download from the beginning.
    How load does it take to download the file?
    """

    # GSM 解答模板
    answer_template = f"""
    First find how many gigabytes are in {baifenbi}% of the file: {alldata} GB * {baifenbi}% = <<{alldata}*{baifenbi}*0.01={beforedata}>>{beforedata} GB.
    Then divide that number by the download rate to find the time until Windows restarts: {beforedata} GB / {speed} GB/minute = <<{beforedata}/{speed}={beforetime}>>{beforetime} minutes.
    Then find the time to download the whole file after the restart: {alldata} GB / {speed} GB/minute = <<{alldata}/{speed}={alltime}>>{alltime} minutes.
    Then add the time to download {baifenbi}% of the file, to download the whole file, and to wait for Windows to update: {beforetime} minutes + {alltime} minutes + {windowtime} minutes = <<{beforetime}+{alltime}+{windowtime}={ans}>>{ans} minutes.
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
with open("../Template_data/gsm_problems8.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")