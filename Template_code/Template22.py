import random
import json

# 生成 GSM Symbolic Template 问题
def generate_gsm_problem():
    # 定义变量的取值范围
    with open("../Template_data/template_randomlabel.json", encoding="utf-8") as f:
        raw_data = json.load(f)
        names = raw_data["names"]
    samantha_age = random.randint(25, 50)  # 萨曼莎的年龄
    age_gap = random.randint(1, 10)  # 年龄差
    raymond_age_at_son_birth = random.randint(20, 30)  # 雷蒙德有孩子的年龄

    # 计算雷蒙德和萨曼莎的关系
    raymond_age = samantha_age + age_gap  # 雷蒙德当前年龄
    raymond_son_birth_years_ago = raymond_age - raymond_age_at_son_birth  # 雷蒙德儿子出生距今多少年

    # 确保生成的答案为正整数
    if raymond_son_birth_years_ago <= 0:
        return generate_gsm_problem()

    Raymond = random.choice(names)
    Samantha = random.choice(names)
    # 问题模板
    question_template = f"""
        {Raymond} and {Samantha} are cousins. {Raymond} was born {age_gap} years before {Samantha}.
        {Raymond} had a son at the age of {raymond_age_at_son_birth}. If {Samantha} is now {samantha_age}, how many years ago was {Raymond}'s son born?
        """

    # 答案模板
    answer_template = f"""
        When {Raymond}'s son was born, {Samantha} was {raymond_age_at_son_birth} - {age_gap} = <<{raymond_age_at_son_birth}-{age_gap}={raymond_age_at_son_birth - age_gap}>>{raymond_age_at_son_birth - age_gap} years old.
        Thus, it has been {samantha_age} - {raymond_age_at_son_birth - age_gap} = <<{samantha_age}-{raymond_age_at_son_birth - age_gap}={raymond_son_birth_years_ago}>>{raymond_son_birth_years_ago} years since {Raymond}'s son was born.
        #### {raymond_son_birth_years_ago}
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
with open("../Template_data/gsm_problems22.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")