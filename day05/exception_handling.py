"""
Day 5: 异常处理
学习内容：try/except/finally、自定义异常、完善异常处理
"""

# ==================== 基础异常处理 ====================

def demo_basic_try_except():
    """基础 try/except 演示"""
    print("=" * 50)
    print("基础异常处理演示")
    print("=" * 50)

    # 示例 1: 除零异常
    print("\n1. 除零异常处理:")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("   ❌ 错误：除数不能为零！")
        result = None
    print(f"   结果：{result}")

    # 示例 2: 值错误异常
    print("\n2. 值错误异常处理:")
    try:
        age = int("不是数字")
    except ValueError:
        print("   ❌ 错误：无法转换为整数！")
        age = 0
    print(f"   年龄：{age}")

    # 示例 3: 索引错误异常
    print("\n3. 索引错误异常处理:")
    try:
        items = [1, 2, 3]
        value = items[10]
    except IndexError:
        print("   ❌ 错误：索引超出范围！")
        value = None
    print(f"   值：{value}")


def demo_multiple_exceptions():
    """多个异常处理演示"""
    print("\n" + "=" * 50)
    print("多个异常处理演示")
    print("=" * 50)

    test_cases = [
        ("10", 2),      # 正常
        ("abc", 2),     # ValueError
        ("10", 0),      # ZeroDivisionError
        (None, 2),      # TypeError
    ]

    for i, (num_str, divisor) in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}: input='{num_str}', divisor={divisor}")
        try:
            num = int(num_str)
            result = num / divisor
            print(f"   ✅ 结果：{result}")
        except ValueError:
            print("   ❌ ValueError: 无法转换为整数")
        except ZeroDivisionError:
            print("   ❌ ZeroDivisionError: 除数不能为零")
        except TypeError as e:
            print(f"   ❌ TypeError: {e}")


def demo_finally():
    """finally 子句演示"""
    print("\n" + "=" * 50)
    print("finally 子句演示")
    print("=" * 50)

    def open_file(filename):
        """模拟文件操作"""
        file = None
        try:
            print(f"\n尝试打开文件：{filename}")
            # 模拟打开文件
            file = f"FileHandle({filename})"
            print(f"   文件已打开：{file}")

            # 模拟读取操作（可能出错）
            if "error" in filename:
                raise FileNotFoundError(f"文件 {filename} 不存在")

            content = "文件内容预览..."
            print(f"   读取内容：{content}")
            return content

        except FileNotFoundError as e:
            print(f"   ❌ 错误：{e}")
            return None
        except Exception as e:
            print(f"   ❌ 未知错误：{e}")
            return None
        finally:
            # 无论是否出错，都会执行
            if file:
                print(f"   关闭文件：{file}")
            print("   finally: 清理资源完成")

    open_file("data.txt")
    open_file("error_file.txt")


# ==================== 自定义异常 ====================

class InsufficientFundsError(Exception):
    """余额不足异常"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"余额不足：当前余额{balance}，需要{amount}")


class InvalidAgeError(Exception):
    """无效年龄异常"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"无效年龄：{age}，必须在 0-150 之间")


class ValidationError(Exception):
    """通用验证异常"""
    def __init__(self, field, message):
        self.field = field
        self.message = message
        super().__init__(f"{field}: {message}")


# ==================== 自定义异常使用示例 ====================

class BankAccount:
    """银行账户类（用于演示自定义异常）"""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """存款"""
        if amount <= 0:
            raise ValidationError("存款金额", "必须大于 0")
        self.balance += amount
        print(f"✅ 存入 {amount}，当前余额：{self.balance}")
        return self.balance

    def withdraw(self, amount):
        """取款"""
        if amount <= 0:
            raise ValidationError("取款金额", "必须大于 0")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"✅ 取出 {amount}，当前余额：{self.balance}")
        return self.balance


def demo_custom_exceptions():
    """自定义异常演示"""
    print("\n" + "=" * 50)
    print("自定义异常演示")
    print("=" * 50)

    # 银行账户示例
    print("\n1. 银行账户操作:")
    account = BankAccount("张三", 1000)

    operations = [
        ("deposit", 500),    # 成功
        ("withdraw", 300),   # 成功
        ("withdraw", 2000),  # 余额不足
        ("deposit", -100),   # 验证错误
    ]

    for op, amount in operations:
        print(f"\n执行操作：{op}({amount})")
        try:
            if op == "deposit":
                account.deposit(amount)
            else:
                account.withdraw(amount)
        except InsufficientFundsError as e:
            print(f"   ❌ {e}")
        except ValidationError as e:
            print(f"   ❌ {e.field} - {e.message}")

    # 年龄验证示例
    print("\n2. 年龄验证:")
    ages = [25, -5, 200, "abc"]

    for age in ages:
        print(f"\n验证年龄：{age}")
        try:
            if not isinstance(age, int):
                raise TypeError("年龄必须是整数")
            if age < 0 or age > 150:
                raise InvalidAgeError(age)
            print(f"   ✅ 有效的年龄：{age}")
        except (InvalidAgeError, TypeError) as e:
            print(f"   ❌ {e}")


# ==================== 完整的异常处理示例 ====================

def safe_divide(a, b):
    """
    安全的除法运算

    Args:
        a: 被除数
        b: 除数

    Returns:
        除法结果，如果出错则返回 None 和错误信息
    """
    try:
        result = a / b
        return {"success": True, "result": result, "error": None}
    except ZeroDivisionError:
        return {"success": False, "result": None, "error": "除数不能为零"}
    except TypeError:
        return {"success": False, "result": None, "error": "输入必须是数字"}
    except Exception as e:
        return {"success": False, "result": None, "error": str(e)}


def get_user_age():
    """
    获取用户年龄（带完整异常处理）

    Returns:
        有效的年龄整数，或 None
    """
    max_attempts = 3

    for attempt in range(1, max_attempts + 1):
        try:
            user_input = input(f"请输入年龄 (第{attempt}次尝试): ")

            if user_input.lower() == 'q':
                print("用户取消输入")
                return None

            age = int(user_input)

            if age < 0 or age > 150:
                raise ValueError(f"年龄必须在 0-150 之间，当前输入：{age}")

            print(f"✅ 有效年龄：{age}")
            return age

        except ValueError as e:
            print(f"❌ 输入无效：{e}")
            if attempt == max_attempts:
                print("已达到最大尝试次数")
                return None

    return None


def read_config_file(filename):
    """
    读取配置文件（带完整异常处理）

    Args:
        filename: 配置文件路径

    Returns:
        文件内容字典，或空字典
    """
    import json

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            config = json.loads(content)
            print(f"✅ 成功读取配置文件：{filename}")
            return config

    except FileNotFoundError:
        print(f"❌ 文件不存在：{filename}")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析错误：{e}")
        return {}
    except PermissionError:
        print(f"❌ 权限错误：无法读取 {filename}")
        return {}
    except Exception as e:
        print(f"❌ 未知错误：{e}")
        return {}


# ==================== 主程序 ====================

def run_all_demos():
    """运行所有演示"""
    print("\n" + "=" * 60)
    print("Day 5: 异常处理 完整演示")
    print("=" * 60)

    # 基础异常处理
    demo_basic_try_except()

    # 多个异常处理
    demo_multiple_exceptions()

    # finally 子句
    demo_finally()

    # 自定义异常
    demo_custom_exceptions()

    # 安全除法演示
    print("\n" + "=" * 50)
    print("安全除法演示")
    print("=" * 50)

    test_cases = [(10, 2), (10, 0), ("10", 2), (10, "2")]
    for a, b in test_cases:
        print(f"\n计算 {a} / {b}:")
        result = safe_divide(a, b)
        if result["success"]:
            print(f"   ✅ 结果：{result['result']}")
        else:
            print(f"   ❌ 错误：{result['error']}")

    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    run_all_demos()

    # 测试用户输入（取消注释）
    # get_user_age()
