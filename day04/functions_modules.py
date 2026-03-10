"""
Day 4: 函数与模块
学习内容：函数定义与参数、返回值与作用域、import 机制
"""

# ==================== 基础函数定义 ====================

def greet(name):
    """简单的问候函数"""
    print(f"你好，{name}！欢迎来到 Python 世界！")


def greet_with_return(name, time_of_day="今天"):
    """带返回值的问候函数"""
    return f"{time_of_day}好，{name}！祝你学习愉快！"


# ==================== 函数参数类型 ====================

def positional_args(a, b, c):
    """位置参数示例"""
    print(f"位置参数：a={a}, b={b}, c={c}")
    return a + b + c


def keyword_args(a, b=10, c=20):
    """默认参数示例"""
    print(f"默认参数：a={a}, b={b}, c={c}")
    return a + b + c


def flexible_args(*args, **kwargs):
    """可变参数示例"""
    print(f"位置可变参数：{args}")
    print(f"关键字可变参数：{kwargs}")
    return sum(args)


# ==================== 返回值与作用域 ====================

global_counter = 0  # 全局变量


def demonstrate_scope():
    """演示作用域"""
    local_var = "我是局部变量"
    global global_counter
    global_counter += 1
    print(f"  {local_var}")
    print(f"  全局计数器：{global_counter}")
    return local_var


def multiple_returns(x, y):
    """多返回值示例"""
    sum_val = x + y
    diff_val = x - y
    product_val = x * y
    quotient_val = x / y if y != 0 else "除数不能为 0"
    return sum_val, diff_val, product_val, quotient_val


# ==================== 高阶函数 ====================

def apply_operation(numbers, operation):
    """
    高阶函数：对列表应用操作

    Args:
        numbers: 数字列表
        operation: 操作函数

    Returns:
        操作后的结果列表
    """
    result = []
    for num in numbers:
        result.append(operation(num))
    return result


def square(x):
    """平方函数"""
    return x * x


def cube(x):
    """立方函数"""
    return x * x * x


# ==================== Lambda 表达式 ====================

def demo_lambda():
    """Lambda 表达式演示"""
    # 简单的 lambda
    add = lambda x, y: x + y
    print(f"lambda 加法：5 + 3 = {add(5, 3)}")

    # 与 sorted 一起使用
    students = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
    ]
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
    print(f"按成绩排序：{sorted_students}")


# ==================== 装饰器基础 ====================

def timer_decorator(func):
    """简单的计时装饰器（概念演示）"""
    def wrapper(*args, **kwargs):
        print(f"开始执行：{func.__name__}")
        result = func(*args, **kwargs)
        print(f"执行完成：{func.__name__}")
        return result
    return wrapper


@timer_decorator
def say_hello(name):
    """被装饰的函数"""
    print(f"你好，{name}！")


# ==================== 模块导入演示 ====================

def demo_imports():
    """演示 import 机制"""
    import math
    import random

    print(f"π = {math.pi}")
    print(f"√16 = {math.sqrt(16)}")
    print(f"随机数 (1-100): {random.randint(1, 100)}")


# ==================== 猜数字游戏（封装版） ====================

def guess_number_game_v2():
    """
    封装后的猜数字游戏
    包含完整的异常处理和游戏逻辑
    """
    import random

    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("=" * 50)
    print("猜数字游戏（封装版）")
    print(f"我已想好一个 1-100 的数字，你有{max_attempts}次机会")
    print("=" * 50)

    while attempts < max_attempts:
        try:
            user_input = input(f"\n第 {attempts + 1} 次猜测：")

            if user_input.lower() == 'q':
                print(f"游戏结束！答案是 {secret_number}")
                return False

            guess = int(user_input)
            attempts += 1

            if guess == secret_number:
                print(f"\n🎉 恭喜！你用了{attempts}次猜对了！")
                return True
            elif guess < secret_number:
                print("📈 太小了")
            else:
                print("📉 太大了")

        except ValueError:
            print("❌ 请输入有效的数字！")
            attempts -= 1  # 无效输入不消耗机会

    print(f"\n游戏结束！答案是 {secret_number}")
    return False


# ==================== 主程序 ====================

def run_all_demos():
    """运行所有演示"""
    print("=" * 50)
    print("Day 4: 函数与模块 演示")
    print("=" * 50)

    # 基础函数
    print("\n1. 基础函数:")
    greet("张三")
    print(greet_with_return("李四", "下午"))

    # 参数类型
    print("\n2. 参数类型:")
    positional_args(1, 2, 3)
    keyword_args(5)
    keyword_args(5, 15)
    keyword_args(5, c=25, b=20)

    print("\n3. 可变参数:")
    flexible_args(1, 2, 3, 4, 5)
    flexible_args(name="Alice", age=25)
    flexible_args(1, 2, 3, name="Bob", age=30)

    # 作用域
    print("\n4. 作用域演示:")
    demonstrate_scope()
    demonstrate_scope()
    print(f"最终全局计数器：{global_counter}")

    # 多返回值
    print("\n5. 多返回值:")
    s, d, p, q = multiple_returns(20, 4)
    print(f"20 和 4 的：和={s}, 差={d}, 积={p}, 商={q}")

    # 高阶函数
    print("\n6. 高阶函数:")
    numbers = [1, 2, 3, 4, 5]
    print(f"原列表：{numbers}")
    print(f"平方：{apply_operation(numbers, square)}")
    print(f"立方：{apply_operation(numbers, cube)}")

    # Lambda
    print("\n7. Lambda 表达式:")
    demo_lambda()

    # 装饰器
    print("\n8. 装饰器:")
    say_hello("王五")

    # import 演示
    print("\n9. Import 机制:")
    demo_imports()


if __name__ == "__main__":
    run_all_demos()

    # 玩游戏（取消注释）
    # guess_number_game_v2()
