import random
import json

# 生成 GSM Symbolic Template 问题
def generate_annual_salary_problem():
    # 随机生成数据
    teaching_rate = random.randint(15, 30)  # 每小时教学工资
    coaching_rate = random.randint(25, 40)  # 每小时教练工资
    teaching_hours = random.randint(30, 40)  # 每周教学小时数
    coaching_hours = random.randint(10, 20)  # 每周教练小时数
    weeks_per_year = random.randint(48, 52)  # 每年工作周数

    # 计算答案
    weekly_teaching_income = teaching_rate * teaching_hours
    weekly_coaching_income = coaching_rate * coaching_hours
    total_weekly_income = weekly_teaching_income + weekly_coaching_income
    annual_salary = total_weekly_income * weeks_per_year

    # GSM 问题模板
    question_template = f"""
    Alex gets paid ${teaching_rate} per hour to teach and ${coaching_rate} to be a sports coach.
    If Alex works {weeks_per_year} weeks a year, {teaching_hours} hours a week as a teacher and {coaching_hours} hours a week as a coach, what's their annual salary?
    """

    # GSM 解答模板
    answer_template = f"""
    First, find the total amount Alex makes per week teaching: ${teaching_rate}/hour * {teaching_hours} hours/week = $<<{teaching_rate}*{teaching_hours}={weekly_teaching_income}>>{weekly_teaching_income}/week.
    Then, find the total amount Alex makes per week coaching: ${coaching_rate}/hour * {coaching_hours} hours/week = $<<{coaching_rate}*{coaching_hours}={weekly_coaching_income}>>{weekly_coaching_income}/week.
    Add those two amounts to find the total amount Alex makes per week: ${weekly_teaching_income}/week + ${weekly_coaching_income}/week = $<<{weekly_teaching_income}+{weekly_coaching_income}={total_weekly_income}>>{total_weekly_income}/week.
    Finally, multiply that number by the number of weeks Alex works in a year to find their annual salary: ${total_weekly_income}/week * {weeks_per_year} weeks/year = $<<{total_weekly_income}*{weeks_per_year}={annual_salary}>>{annual_salary}.
    #### {annual_salary}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_annual_salary_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_annual_salary_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_annual_salary_problems()
with open("../Template_data/gsm_problems18.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
