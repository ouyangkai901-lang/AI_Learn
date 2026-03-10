"""
Day 7: 周复习与实战 - 日志记录器
学习内容：综合本周所学，实现一个带配置的日志记录器
"""

import json
import os
from datetime import datetime

# ==================== 日志级别定义 ====================

class LogLevel:
    """日志级别常量"""
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

    @staticmethod
    def get_level_name(level):
        """获取日志级别名称"""
        names = {
            0: "DEBUG",
            1: "INFO",
            2: "WARNING",
            3: "ERROR",
            4: "CRITICAL"
        }
        return names.get(level, "UNKNOWN")

    @staticmethod
    def get_level_from_name(name):
        """从名称获取日志级别"""
        names = {
            "DEBUG": 0,
            "INFO": 1,
            "WARNING": 2,
            "ERROR": 3,
            "CRITICAL": 4
        }
        return names.get(name.upper(), 1)  # 默认 INFO


# ==================== 日志记录器类 ====================

class Logger:
    """自定义日志记录器"""

    def __init__(self, name="app", log_file=None, level=LogLevel.INFO, config_file=None):
        """
        初始化日志记录器

        Args:
            name: 日志记录器名称
            log_file: 日志文件路径（可选）
            level: 日志级别
            config_file: 配置文件路径（可选）
        """
        self.name = name
        self.level = level
        self.log_file = log_file
        self.logs = []  # 内存中存储日志

        # 如果提供了配置文件，从文件加载配置
        if config_file:
            self.load_config(config_file)

        # 如果指定了日志文件，确保目录存在
        if log_file:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

    def load_config(self, config_file):
        """从配置文件加载设置"""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)

                self.name = config.get('name', self.name)
                self.log_file = config.get('log_file', self.log_file)
                level_name = config.get('level', 'INFO')
                self.level = LogLevel.get_level_from_name(level_name)

                print(f"✅ 已加载配置：{config_file}")
        except Exception as e:
            print(f"⚠️ 加载配置失败：{e}")

    def save_config(self, config_file):
        """保存配置到文件"""
        config = {
            "name": self.name,
            "log_file": self.log_file,
            "level": LogLevel.get_level_name(self.level)
        }

        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            print(f"✅ 配置已保存：{config_file}")
        except Exception as e:
            print(f"❌ 保存配置失败：{e}")

    def _format_message(self, level, message):
        """格式化日志消息"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_name = LogLevel.get_level_name(level)
        return f"[{timestamp}] [{level_name}] [{self.name}] {message}"

    def _log(self, level, message):
        """内部日志方法"""
        # 检查日志级别
        if level < self.level:
            return

        # 格式化消息
        formatted = self._format_message(level, message)

        # 存储到内存
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "level": LogLevel.get_level_name(level),
            "message": message
        })

        # 输出到控制台
        print(formatted)

        # 写入文件
        if self.log_file:
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.write(formatted + "\n")
            except Exception as e:
                print(f"[ERROR] 写入日志文件失败：{e}")

    def debug(self, message):
        """DEBUG 级别日志"""
        self._log(LogLevel.DEBUG, message)

    def info(self, message):
        """INFO 级别日志"""
        self._log(LogLevel.INFO, message)

    def warning(self, message):
        """WARNING 级别日志"""
        self._log(LogLevel.WARNING, message)

    def error(self, message):
        """ERROR 级别日志"""
        self._log(LogLevel.ERROR, message)

    def critical(self, message):
        """CRITICAL 级别日志"""
        self._log(LogLevel.CRITICAL, message)

    def get_logs(self, level=None, limit=None):
        """
        获取日志记录

        Args:
            level: 过滤级别（可选）
            limit: 限制数量（可选）

        Returns:
            日志列表
        """
        logs = self.logs

        if level:
            logs = [log for log in logs if log["level"] == level]

        if limit:
            logs = logs[-limit:]

        return logs

    def clear_logs(self):
        """清空内存中的日志"""
        self.logs = []
        self.info("日志已清空")

    def export_logs(self, output_file):
        """
        导出日志到文件

        Args:
            output_file: 输出文件路径
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(self.logs, f, ensure_ascii=False, indent=2)
            self.info(f"日志已导出：{output_file}")
        except Exception as e:
            self.error(f"导出日志失败：{e}")


# ==================== 日志记录器管理类 ====================

class LoggerManager:
    """日志记录器管理器（单例模式）"""

    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_logger(self, name, **kwargs):
        """获取或创建日志记录器"""
        if name not in self._loggers:
            self._loggers[name] = Logger(name, **kwargs)
        return self._loggers[name]

    def get_all_loggers(self):
        """获取所有日志记录器"""
        return self._loggers

    def set_all_level(self, level):
        """设置所有日志记录器的级别"""
        for logger in self._loggers.values():
            logger.level = level


# ==================== 使用示例 ====================

def demo_basic_logger():
    """基础日志记录器演示"""
    print("=" * 50)
    print("基础日志记录器演示")
    print("=" * 50)

    # 创建日志记录器
    logger = Logger(name="MyApp", level=LogLevel.DEBUG)

    print("\n记录不同级别的日志:")
    logger.debug("这是一条 DEBUG 日志")
    logger.info("这是一条 INFO 日志")
    logger.warning("这是一条 WARNING 日志")
    logger.error("这是一条 ERROR 日志")
    logger.critical("这是一条 CRITICAL 日志")

    print(f"\n内存中的日志数量：{len(logger.get_logs())}")

    # 查看特定级别的日志
    print(f"\nERROR 级别的日志:")
    for log in logger.get_logs(level="ERROR"):
        print(f"  - {log['message']}")


def demo_logger_with_file():
    """带文件输出的日志记录器"""
    print("\n" + "=" * 50)
    print("带文件输出的日志记录器")
    print("=" * 50)

    log_file = "logs/app.log"
    config_file = "logs/logger_config.json"

    # 创建带文件输出的日志记录器
    logger = Logger(
        name="FileApp",
        log_file=log_file,
        level=LogLevel.INFO
    )

    print("\n记录日志（同时输出到文件）:")
    logger.info("应用程序启动")
    logger.info("正在初始化模块...")
    logger.warning("检测到配置文件不存在，使用默认配置")
    logger.info("初始化完成")
    logger.error("模拟一个错误")

    # 保存配置
    logger.save_config(config_file)

    # 导出日志
    logger.export_logs("logs/exported_logs.json")

    print(f"\n日志文件：{log_file}")
    print(f"配置文件：{config_file}")
    print(f"导出文件：logs/exported_logs.json")

    # 清理（实际使用时不要删除）
    # os.remove(log_file)
    # os.remove(config_file)


def demo_logger_manager():
    """日志管理器演示"""
    print("\n" + "=" * 50)
    print("日志管理器演示（多日志记录器）")
    print("=" * 50)

    manager = LoggerManager()

    # 获取/创建不同的日志记录器
    db_logger = manager.get_logger("database", level=LogLevel.DEBUG)
    api_logger = manager.get_logger("api", level=LogLevel.INFO)
    user_logger = manager.get_logger("user", level=LogLevel.WARNING)

    print("\n使用不同的日志记录器:")
    db_logger.debug("数据库连接池初始化")
    db_logger.info("执行 SQL: SELECT * FROM users")
    api_logger.info("API 请求：GET /api/users")
    api_logger.warning("API 响应缓慢：2.5s")
    user_logger.warning("用户登录失败：admin")
    user_logger.error("用户数据异常：user_id=123")

    print(f"\n所有日志记录器：{list(manager.get_all_loggers().keys())}")


def demo_business_scenario():
    """业务场景演示"""
    print("\n" + "=" * 50)
    print("业务场景：用户管理系统")
    print("=" * 50)

    # 创建日志记录器
    logger = Logger(
        name="UserSystem",
        log_file="logs/user_system.log",
        level=LogLevel.DEBUG
    )

    # 模拟用户管理操作
    class UserService:
        def __init__(self, logger):
            self.logger = logger
            self.users = {}
            self.logger.info("用户服务初始化完成")

        def register(self, username, email):
            """用户注册"""
            self.logger.debug(f"尝试注册用户：{username}")

            if not username or len(username) < 3:
                self.logger.warning(f"用户名太短：{username}")
                return False, "用户名至少 3 个字符"

            if '@' not in email:
                self.logger.error(f"邮箱格式错误：{email}")
                return False, "邮箱格式不正确"

            if username in self.users:
                self.logger.warning(f"用户已存在：{username}")
                return False, "用户已存在"

            self.users[username] = {"email": email, "status": "active"}
            self.logger.info(f"用户注册成功：{username}")
            return True, "注册成功"

        def login(self, username, password):
            """用户登录"""
            self.logger.debug(f"尝试登录：{username}")

            if username not in self.users:
                self.logger.warning(f"登录失败 - 用户不存在：{username}")
                return False, "用户不存在"

            # 模拟密码验证
            if len(password) < 6:
                self.logger.error(f"登录失败 - 密码太短：{username}")
                return False, "密码错误"

            self.logger.info(f"用户登录成功：{username}")
            return True, "登录成功"

        def delete_user(self, username):
            """删除用户"""
            self.logger.info(f"尝试删除用户：{username}")

            if username not in self.users:
                self.logger.warning(f"删除失败 - 用户不存在：{username}")
                return False

            del self.users[username]
            self.logger.info(f"用户已删除：{username}")
            return True

    # 运行业务场景
    service = UserService(logger)

    print("\n1. 用户注册测试:")
    service.register("ab", "test@example.com")  # 用户名太短
    service.register("alice", "invalid-email")   # 邮箱格式错误
    service.register("alice", "alice@example.com")  # 成功
    service.register("alice", "alice2@example.com")  # 重复注册
    service.register("bob", "bob@example.com")  # 成功

    print("\n2. 用户登录测试:")
    service.login("alice", "123")    # 密码太短
    service.login("unknown", "123456")  # 用户不存在
    service.login("bob", "password123")  # 成功

    print("\n3. 用户删除测试:")
    service.delete_user("nonexistent")
    service.delete_user("alice")

    print(f"\n当前用户列表：{list(service.users.keys())}")
    print(f"总日志数：{len(logger.get_logs())}")


# ==================== 主程序 ====================

def run_all_demos():
    """运行所有演示"""
    print("\n" + "=" * 60)
    print("Day 7: 周复习与实战 - 日志记录器")
    print("=" * 60)

    # 基础演示
    demo_basic_logger()

    # 文件输出演示
    demo_logger_with_file()

    # 管理器演示
    demo_logger_manager()

    # 业务场景
    demo_business_scenario()

    print("\n" + "=" * 60)
    print("第一周学习完成！🎉")
    print("=" * 60)
    print("""
本周学习内容回顾:
- Day 1: Python 环境搭建
- Day 2: 基础语法（变量、字符串、列表、字典）
- Day 3: 条件语句与循环（猜数字游戏）
- Day 4: 函数与模块
- Day 5: 异常处理
- Day 6: 文件与 IO
- Day 7: 综合实战（日志记录器）
""")


if __name__ == "__main__":
    run_all_demos()
