"""
Day 3: 猜数字游戏
学习内容：条件语句（if/elif/else）、循环（for/while）
"""

import random


def guess_number_game():
    """猜数字游戏主函数"""
    # 生成 1-100 之间的随机数
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("=" * 50)
    print("欢迎来到猜数字游戏！")
    print(f"我已经想好了一个 1 到 100 之间的数字。")
    print(f"你有 {max_attempts} 次机会来猜出它。")
    print("=" * 50)

    while attempts < max_attempts:
        # 获取用户输入
        user_input = input(f"\n第 {attempts + 1} 次猜测，请输入你的猜测：")

        # 检查是否想退出游戏
        if user_input.lower() in ['q', 'quit', 'exit']:
            print(f"\n游戏结束！正确答案是 {secret_number}")
            return

        # 验证输入是否为数字
        if not user_input.isdigit():
            print("❌ 请输入一个有效的数字！")
            continue

        guess = int(user_input)
        attempts += 1

        # 检查猜测结果
        if guess < secret_number:
            print("📈 太小了！再试一次。")
        elif guess > secret_number:
            print("📉 太大了！再试一次。")
        else:
            print(f"\n🎉 恭喜你！你猜对了！")
            print(f"   答案就是 {secret_number}，你用了 {attempts} 次机会。")

            # 根据尝试次数给出评价
            if attempts <= 3:
                print("   🌟 太厉害了！你真是猜数字高手！")
            elif attempts <= 5:
                print("   👍 不错哦！表现很好！")
            else:
                print("   💪 再接再厉！下次会更好！")
            return

    # 机会用完
    print(f"\n😢 很遗憾，机会用完了！")
    print(f"   正确答案是 {secret_number}")
    print(f"   继续加油，下次一定能猜对！")


def guess_number_with_hint():
    """带提示的猜数字游戏（进阶版）"""
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n" + "=" * 50)
    print("高级猜数字游戏（带提示）")
    print("=" * 50)

    while True:
        user_input = input(f"\n第 {attempts + 1} 次猜测（输入 q 退出）：")

        if user_input.lower() == 'q':
            print(f"游戏结束！正确答案是 {secret_number}")
            return

        if not user_input.isdigit():
            print("请输入一个有效的数字！")
            continue

        guess = int(user_input)
        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 恭喜你！猜对了！答案是 {secret_number}")
            print(f"   总共用了 {attempts} 次尝试。")
            return
        else:
            # 给出更详细的提示
            diff = abs(guess - secret_number)
            if diff <= 5:
                print("🔥 非常接近了！")
            elif diff <= 10:
                print("👍 比较接近！")

            if guess < secret_number:
                print("📈 太小了！")
            else:
                print("📉 太大了！")


def demo_if_elif_else():
    """if/elif/else 条件语句演示"""
    print("\n" + "=" * 50)
    print("条件语句演示")
    print("=" * 50)

    # 示例 1：成绩评级
    score = 85
    if score >= 90:
        grade = 'A'
        comment = '优秀'
    elif score >= 80:
        grade = 'B'
        comment = '良好'
    elif score >= 70:
        grade = 'C'
        comment = '中等'
    elif score >= 60:
        grade = 'D'
        comment = '及格'
    else:
        grade = 'F'
        comment = '不及格'

    print(f"成绩 {score} 分，等级：{grade}，评价：{comment}")

    # 示例 2：判断闰年
    year = 2024
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} 年是闰年")
    else:
        print(f"{year} 年是平年")


def demo_for_loop():
    """for 循环演示"""
    print("\n" + "=" * 50)
    print("for 循环演示")
    print("=" * 50)

    # 遍历列表
    fruits = ['苹果', '香蕉', '橙子', '葡萄']
    print("水果列表：")
    for i, fruit in enumerate(fruits, 1):
        print(f"  {i}. {fruit}")

    # 范围循环
    print("\n计算 1-10 的和：")
    total = 0
    for i in range(1, 11):
        total += i
    print(f"  总和 = {total}")

    # 九九乘法表
    print("\n九九乘法表（部分）：")
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j}", end="\t")
        print()


def demo_while_loop():
    """while 循环演示"""
    print("\n" + "=" * 50)
    print("while 循环演示")
    print("=" * 50)

    # 倒计时
    print("倒计时：")
    count = 5
    while count > 0:
        print(f"  {count}...", end=" ")
        count -= 1
    print("🚀 发射！")

    # 累加直到满足条件
    print("\n累加 1+2+3+... 直到和超过 50：")
    total = 0
    num = 1
    while total <= 50:
        total += num
        num += 1
    print(f"  加到 {num - 1} 时，总和为 {total}")


if __name__ == "__main__":
    # 运行演示
    demo_if_elif_else()
    demo_for_loop()
    demo_while_loop()

    # 运行游戏（取消注释来玩游戏）
    # guess_number_game()
    # guess_number_with_hint()
