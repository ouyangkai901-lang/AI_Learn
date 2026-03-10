"""
Day 6: 文件与 IO
学习内容：文件读写操作、JSON 数据处理、配置文件读取器
"""

import json
import os

# ==================== 基础文件操作 ====================

def demo_basic_file_operations():
    """基础文件读写演示"""
    print("=" * 50)
    print("基础文件操作演示")
    print("=" * 50)

    # 示例文件路径
    demo_file = "demo_test.txt"

    # 1. 写入文件
    print("\n1. 写入文件:")
    with open(demo_file, 'w', encoding='utf-8') as f:
        f.write("你好，Python!\n")
        f.write("这是第二行内容\n")
        f.write("这是第三行内容\n")
    print(f"   ✅ 已写入文件：{demo_file}")

    # 2. 读取整个文件
    print("\n2. 读取整个文件:")
    with open(demo_file, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"   文件内容:\n{content}")

    # 3. 逐行读取
    print("3. 逐行读取:")
    with open(demo_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            print(f"   第{i}行：{line.strip()}")

    # 4. 读取为列表
    print("\n4. 读取为列表:")
    with open(demo_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"   列表内容：{lines}")

    # 清理测试文件
    os.remove(demo_file)
    print(f"\n   ✅ 已清理测试文件：{demo_file}")


def demo_append_file():
    """追加文件内容演示"""
    print("\n" + "=" * 50)
    print("追加文件内容演示")
    print("=" * 50)

    demo_file = "demo_append.txt"

    # 首次写入
    with open(demo_file, 'w', encoding='utf-8') as f:
        f.write("第一行内容\n")
    print("首次写入完成")

    # 追加内容
    with open(demo_file, 'a', encoding='utf-8') as f:
        f.write("追加的第二行\n")
        f.write("追加的第三行\n")
    print("追加内容完成")

    # 读取查看
    with open(demo_file, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"最终内容:\n{content}")

    # 清理
    os.remove(demo_file)
    print("✅ 已清理测试文件")


# ==================== JSON 数据处理 ====================

def demo_json_basics():
    """JSON 基础操作演示"""
    print("\n" + "=" * 50)
    print("JSON 基础操作演示")
    print("=" * 50)

    # Python 数据结构
    data = {
        "name": "张三",
        "age": 25,
        "city": "北京",
        "skills": ["Python", "Java", "Go"],
        "active": True,
        "salary": None
    }

    print("\n1. Python 字典:")
    print(f"   原始数据：{data}")

    # 转换为 JSON 字符串
    print("\n2. 序列化为 JSON 字符串:")
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    print(f"   JSON 格式:\n{json_str}")

    # JSON 字符串转回 Python
    print("\n3. 反序列化为 Python 对象:")
    parsed_data = json.loads(json_str)
    print(f"   解析后：{parsed_data}")
    print(f"   name 字段：{parsed_data['name']}")


def demo_json_file_operations():
    """JSON 文件操作演示"""
    print("\n" + "=" * 50)
    print("JSON 文件操作演示")
    print("=" * 50)

    json_file = "demo_data.json"

    # 要保存的数据
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ]

    config = {
        "app_name": "我的应用",
        "version": "1.0.0",
        "debug": True,
        "users": users,
        "settings": {
            "theme": "dark",
            "language": "zh-CN",
            "timeout": 30
        }
    }

    # 写入 JSON 文件
    print("\n1. 写入 JSON 文件:")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"   ✅ 已写入：{json_file}")

    # 读取 JSON 文件
    print("\n2. 读取 JSON 文件:")
    with open(json_file, 'r', encoding='utf-8') as f:
        loaded_config = json.load(f)
    print(f"   应用名称：{loaded_config['app_name']}")
    print(f"   版本：{loaded_config['version']}")
    print(f"   用户数量：{len(loaded_config['users'])}")

    # 修改并保存
    print("\n3. 修改并保存:")
    loaded_config["version"] = "1.1.0"
    loaded_config["users"].append({"id": 4, "name": "David", "email": "david@example.com"})
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(loaded_config, f, ensure_ascii=False, indent=2)
    print("   ✅ 已更新配置")

    # 清理
    os.remove(json_file)
    print(f"\n   ✅ 已清理测试文件：{json_file}")


# ==================== 配置文件读取器 ====================

class ConfigReader:
    """配置文件读取器类"""

    def __init__(self, config_file="config.json"):
        """初始化配置读取器"""
        self.config_file = config_file
        self.config = {}
        self.load()

    def load(self):
        """
        加载配置文件

        Returns:
            bool: 是否加载成功
        """
        try:
            if not os.path.exists(self.config_file):
                print(f"⚠️  配置文件不存在：{self.config_file}")
                self.config = {}
                return False

            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
            print(f"✅ 成功加载配置文件：{self.config_file}")
            return True

        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析错误：{e}")
            self.config = {}
            return False
        except Exception as e:
            print(f"❌ 加载失败：{e}")
            self.config = {}
            return False

    def get(self, key, default=None):
        """
        获取配置值

        Args:
            key: 配置键（支持点号分隔，如 'database.host'）
            default: 默认值

        Returns:
            配置值或默认值
        """
        keys = key.split('.')
        value = self.config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def set(self, key, value):
        """
        设置配置值

        Args:
            key: 配置键
            value: 配置值
        """
        keys = key.split('.')
        config = self.config

        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]

        config[keys[-1]] = value

    def save(self):
        """
        保存配置到文件

        Returns:
            bool: 是否保存成功
        """
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            print(f"✅ 配置已保存：{self.config_file}")
            return True
        except Exception as e:
            print(f"❌ 保存失败：{e}")
            return False

    def show(self):
        """显示所有配置"""
        print("\n当前配置:")
        print(json.dumps(self.config, ensure_ascii=False, indent=2))


def demo_config_reader():
    """配置读取器演示"""
    print("\n" + "=" * 50)
    print("配置文件读取器演示")
    print("=" * 50)

    config_file = "demo_config.json"

    # 创建示例配置文件
    sample_config = {
        "app": {
            "name": "我的应用",
            "version": "1.0.0",
            "debug": True
        },
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb",
            "user": "admin"
        },
        "server": {
            "host": "0.0.0.0",
            "port": 8080,
            "workers": 4
        },
        "features": {
            "enable_cache": True,
            "enable_logging": True,
            "max_connections": 100
        }
    }

    # 写入示例配置
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(sample_config, f, ensure_ascii=False, indent=2)
    print(f"✅ 创建示例配置文件：{config_file}")

    # 创建配置读取器
    config = ConfigReader(config_file)

    # 获取配置
    print("\n获取配置值:")
    print(f"   app.name = {config.get('app.name', '未知')}")
    print(f"   app.version = {config.get('app.version', '未知')}")
    print(f"   database.host = {config.get('database.host', 'localhost')}")
    print(f"   database.port = {config.get('database.port', 3306)}")
    print(f"   server.port = {config.get('server.port', 80)}")
    print(f"   features.enable_cache = {config.get('features.enable_cache', False)}")

    # 获取不存在的配置（使用默认值）
    print(f"\n不存在的配置（使用默认值）:")
    print(f"   app.secret = {config.get('app.secret', 'default_secret')}")
    print(f"   timeout = {config.get('timeout', 30)}")

    # 修改配置
    print("\n修改配置:")
    config.set('app.version', '2.0.0')
    config.set('database.password', 'secret123')
    config.set('new_feature.enabled', True)
    config.show()

    # 保存配置
    config.save()

    # 清理
    os.remove(config_file)
    print(f"\n✅ 已清理测试文件：{config_file}")


# ==================== 实用工具函数 ====================

def read_text_file(filename):
    """
    读取文本文件

    Args:
        filename: 文件路径

    Returns:
        文件内容字符串，失败返回 None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"读取文件失败：{e}")
        return None


def write_text_file(filename, content):
    """
    写入文本文件

    Args:
        filename: 文件路径
        content: 文件内容

    Returns:
        bool: 是否成功
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"写入文件失败：{e}")
        return False


def read_json_file(filename):
    """
    读取 JSON 文件

    Args:
        filename: 文件路径

    Returns:
        解析后的数据，失败返回 None
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"读取 JSON 失败：{e}")
        return None


def write_json_file(filename, data):
    """
    写入 JSON 文件

    Args:
        filename: 文件路径
        data: 要保存的数据

    Returns:
        bool: 是否成功
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"写入 JSON 失败：{e}")
        return False


# ==================== 主程序 ====================

def run_all_demos():
    """运行所有演示"""
    print("\n" + "=" * 60)
    print("Day 6: 文件与 IO 完整演示")
    print("=" * 60)

    # 基础文件操作
    demo_basic_file_operations()

    # 追加文件演示
    demo_append_file()

    # JSON 基础
    demo_json_basics()

    # JSON 文件操作
    demo_json_file_operations()

    # 配置读取器
    demo_config_reader()

    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    run_all_demos()
