import random
import json

# 生成 GSM Symbolic Template 问题
def generate_download_problem():
    # 定义变量的取值范围
    first_month_downloads = random.randint(10, 100)
    multiplier = random.randint(2, 5)
    reduction_percentage = random.randint(10, 50)

    # 计算数据
    second_month_downloads = first_month_downloads * multiplier
    total_first_two_months = first_month_downloads + second_month_downloads
    reduction = int((reduction_percentage / 100) * second_month_downloads)
    third_month_downloads = second_month_downloads - reduction
    total_downloads = total_first_two_months + third_month_downloads

    # 问题模板
    question_template = f"""
    A new program had {first_month_downloads} downloads in the first month.
    The number of downloads in the second month was {multiplier} times as many as the downloads in the first month,
    but then reduced by {reduction_percentage}% in the third month.
    How many downloads did the program have total over the three months?
    """

    # 解答模板
    answer_template = f"""
    The number of downloads of the program in the second month increased to {multiplier}*{first_month_downloads} = <<{multiplier}*{first_month_downloads}={second_month_downloads}>>{second_month_downloads}.
    In the first two months, the total number of downloads of the program was {second_month_downloads}+{first_month_downloads} = <<{second_month_downloads}+{first_month_downloads}={total_first_two_months}>>{total_first_two_months}.
    In the third month, the number of downloads of the program reduced by {reduction_percentage}/100*{second_month_downloads} = <<{reduction_percentage}/100*{second_month_downloads}={reduction}>>{reduction}.
    There were {second_month_downloads}-{reduction} = <<{second_month_downloads}-{reduction}={third_month_downloads}>>{third_month_downloads} downloads in the third month.
    In the three months, the total number of downloads of the program was {third_month_downloads}+{total_first_two_months} = <<{third_month_downloads}+{total_first_two_months}={total_downloads}>>{total_downloads}.
    #### {total_downloads}
    """

    return question_template.strip(), answer_template.strip()

# 批量生成问题
def generate_download_problems(n=50):
    problems = []
    for _ in range(n):
        question, answer = generate_download_problem()
        problems.append({"question": question, "answer": answer})
    return problems

# 生成并保存为 JSONL 文件
problems = generate_download_problems()
with open("../Template_data/gsm_problems11.jsonl", "w", encoding="utf-8") as f:
    for i, item in enumerate(problems, start=1):
        message = {
            "question": item["question"],
            "answer": item["answer"],
        }
        f.write(json.dumps(message) + "\n")
        print(f"question {i}:\n{item['question']}\n")
        print(f"answer {i}:\n{item['answer']}\n")
