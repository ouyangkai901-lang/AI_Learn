# AI 应用工程师学习路线（12 个月）

> **适用人群**：有 Java 后端基础，想转型 AI 工程化的工程师
> **学习目标**：成为"既懂业务又懂 AI 工程"的复合型人才
> **学习方式**：工作日每天 1-2 小时，周末 4-6 小时

---

## 📅 第一阶段：基础巩固（第 1-8 周）

### 目标
- [ ] 能用 Python 写简单的 LLM 调用代码
- [ ] 理解 Transformer、Embedding、Prompt 基本原理
- [ ] 搭建一个本地可运行的客服对话 demo

---

### 第 1 周：Python 语法速成

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 1 | Python 环境搭建 | 1. 安装 Python 3.10+<br>2. 安装 PyCharm 或 VSCode<br>3. 配置 pip 镜像源<br>4. 创建第一个 hello.py 运行 | 1h | [✅] |
| Day 2 | 基础语法（上） | 1. 变量与数据类型<br>2. 字符串操作（切片、格式化）<br>3. 列表、元组、字典<br>4. 练习：写一个数据处理小脚本 | 1.5h | [ ] |
| Day 3 | 基础语法（下） | 1. 条件语句（if/elif/else）<br>2. 循环（for/while）<br>3. 练习：实现一个猜数字游戏 | 1.5h | [ ] |
| Day 4 | 函数与模块 | 1. 函数定义与参数<br>2. 返回值与作用域<br>3. import 机制<br>4. 练习：封装昨天的游戏为函数 | 1.5h | [ ] |
| Day 5 | 异常处理 | 1. try/except/finally<br>2. 自定义异常<br>3. 练习：给代码添加完善的异常处理 | 1h | [ ] |
| Day 6 | 文件与 IO | 1. 文件读写操作<br>2. JSON 数据处理<br>3. 练习：实现一个简单的配置文件读取器 | 2h | [ ] |
| Day 7 | 周复习与实战 | 1. 复习本周内容<br>2. 综合练习：写一个带配置的日志记录器<br>3. 整理笔记 | 3h | [ ] |

**本周资源**：
- [廖雪峰 Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [Python 官方教程](https://docs.python.org/3/tutorial/)

---

### 第 2 周：Python 进阶与异步编程

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 8 | 装饰器 | 1. 理解装饰器原理<br>2. 写一个简单的计时装饰器<br>3. 练习：实现重试装饰器 | 1.5h | [ ] |
| Day 9 | 类型注解 | 1. 基础类型注解<br>2. 泛型与 Optional<br>3. 练习：给已有代码添加类型注解 | 1h | [ ] |
| Day 10 | 异步编程基础 | 1. async/await 概念<br>2. asyncio 基础<br>3. 练习：写一个异步 hello world | 1.5h | [ ] |
| Day 11 | aiohttp 库 | 1. 安装 aiohttp<br>2. 异步 GET/POST 请求<br>3. 练习：异步爬取多个网页 | 1.5h | [ ] |
| Day 12 | HTTP 请求封装 | 1. 封装带重试的 HTTP 客户端<br>2. 添加超时控制<br>3. 添加请求日志 | 2h | [ ] |
| Day 13 | 实战练习 | 1. 完善 HTTP 客户端<br>2. 添加连接池概念<br>3. 写单元测试 | 3h | [ ] |
| Day 14 | 周复习与整理 | 1. 复习异步编程概念<br>2. 整理代码到 GitHub<br>3. 写学习心得 | 2h | [ ] |

**本周产出**：一个带重试、超时、日志的异步 HTTP 客户端

---

### 第 3 周：LLM 基础与 Prompt Engineering

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 15 | LLM 基础概念 | 1. 什么是 LLM<br>2. Token 概念与计算<br>3. 主流模型对比（GPT/Claude/文心/通义）<br>4. 注册一个模型 API（推荐硅基流动/DeepSeek） | 1.5h | [ ] |
| Day 16 | API 调用实战 | 1. 阅读 API 文档<br>2. 用 curl 测试接口<br>3. 用 Python 调用并打印响应<br>4. 理解响应结构 | 2h | [ ] |
| Day 17 | 生成参数详解 | 1. Temperature 参数实验<br>2. Top-P、Max Tokens<br>3. 练习：同一 prompt 不同参数对比输出 | 1.5h | [ ] |
| Day 18 | Prompt 基础 | 1. Zero-shot Prompting<br>2. Few-shot Prompting<br>3. 练习：设计客服场景的 few-shot 示例 | 1.5h | [ ] |
| Day 19 | 高级 Prompt 技巧 | 1. Chain of Thought（CoT）<br>2. Role Prompting<br>3. 练习：用 CoT 解决数学问题 | 2h | [ ] |
| Day 20 | Prompt 模板化 | 1. 用 Jinja2 或 f-string 做模板<br>2. 设计 5 个客服场景模板<br>3. 测试模板效果 | 2h | [ ] |
| Day 21 | 周实战 | 1. 整合本周内容<br>2. 写一个 Prompt 测试工具<br>3. 对比不同 prompt 的效果 | 3h | [ ] |

**本周产出**：
- 10 个客服场景 prompt 模板
- 一个 prompt 测试小工具

**资源**：
- [Learn Prompting](https://learnprompting.org/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

---

### 第 4 周：Transformer 原理与模型调用框架

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 22 | Transformer 架构 | 1. 观看 3Blue1Brown 或李宏毅讲解视频<br>2. 理解 Encoder-Decoder 结构<br>3. 画出架构图 | 2h | [ ] |
| Day 23 | Attention 机制 | 1. 理解 Self-Attention 概念<br>2. 不用推导公式，理解"注意力"思想<br>3. 看一篇科普文章 | 1.5h | [ ] |
| Day 24 | Embedding 详解 | 1. 什么是词向量<br>2. 调用 Embedding API<br>3. 练习：计算词语相似度 | 2h | [ ] |
| Day 25 | 封装模型调用 | 1. 设计统一的 LLM 调用类<br>2. 支持多个模型切换<br>3. 添加错误处理和重试 | 2h | [ ] |
| Day 26 | 配置管理 | 1. 用 YAML 管理配置<br>2. 支持环境变量<br>3. 密钥安全管理 | 1.5h | [ ] |
| Day 27 | 日志系统 | 1. Python logging 模块<br>2. 结构化日志<br>3. 集成到调用框架 | 1.5h | [ ] |
| Day 28 | 阶段项目启动 | 1. 设计"客服对话模拟器"架构<br>2. 创建项目结构<br>3. 完成基础框架代码 | 4h | [ ] |

**本周产出**：一个可配置的 LLM 调用框架

**资源**：
- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
- 李宏毅 Transformer 讲解视频

---

### 第 5 周：阶段项目 - 客服对话模拟器（上）

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 29 | 项目架构设计 | 1. 画系统架构图<br>2. 定义模块接口<br>3. 创建 Git 仓库 | 2h | [ ] |
| Day 30 | 意图识别模块 | 1. 设计意图分类 prompt<br>2. 实现意图识别函数<br>3. 定义 5-10 个客服意图 | 2h | [ ] |
| Day 31 | 关键词抽取模块 | 1. 设计抽取 prompt<br>2. 实现关键词提取<br>3. 定义行业关键词表 | 2h | [ ] |
| Day 32 | 回复生成模块 | 1. 设计生成 prompt<br>2. 整合意图和关键词<br>3. 实现回复生成 | 2h | [ ] |
| Day 33 | 对话管理模块 | 1. 设计对话历史结构<br>2. 实现多轮对话支持<br>3. 添加上下文长度控制 | 2h | [ ] |
| Day 34 | 接口层 | 1. 用 FastAPI 写 HTTP 接口<br>2. 定义请求/响应结构<br>3. 添加 API 文档 | 3h | [ ] |
| Day 35 | 周测试与优化 | 1. 手动测试各模块<br>2. 修复 bug<br>3. 优化 prompt | 4h | [ ] |

---

### 第 6 周：阶段项目 - 客服对话模拟器（下）

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 36 | 数据持久化 | 1. SQLite 基础<br>2. 设计对话存储表<br>3. 实现 CRUD 操作 | 2h | [ ] |
| Day 37 | 管理后台（上） | 1. 设计后台页面结构<br>2. 实现对话列表页<br>3. 实现详情页 | 3h | [ ] |
| Day 38 | 管理后台（下） | 1. 实现数据统计<br>2. 实现意图分布图表<br>3. 添加导出功能 | 3h | [ ] |
| Day 39 | 测试与调试 | 1. 编写单元测试<br>2. 集成测试<br>3. 修复问题 | 3h | [ ] |
| Day 40 | 性能优化 | 1. 分析瓶颈<br>2. 添加缓存<br>3. 优化响应速度 | 2h | [ ] |
| Day 41 | 文档编写 | 1. 写 README<br>2. 画部署架构图<br>3. 写使用说明 | 3h | [ ] |
| Day 42 | 项目总结 | 1. 整理代码到 GitHub<br>2. 写项目总结文章<br>3. 复盘学习收获 | 4h | [ ] |

**第一阶段完结！** 🎉

**产出物**：
- [ ] 客服对话模拟器（完整代码 + 文档）
- [ ] GitHub 仓库
- [ ] 学习总结文章

---

## 📅 第二阶段：RAG 与 Agent 实战（第 7-14 周）

### 目标
- [ ] 掌握 LangChain 核心概念
- [ ] 能独立搭建 RAG 系统
- [ ] 理解 Agent 设计模式

---

### 第 7 周：LangChain 基础

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 43 | LangChain 入门 | 1. 安装 langchain<br>2. 理解 LLM、ChatModel 区别<br>3. 跑通官方 quickstart | 2h | [ ] |
| Day 44 | Prompt Templates | 1. ChatPromptTemplate<br>2. SystemMessage/UserMessage<br>3. 练习：改造之前的 prompt | 2h | [ ] |
| Day 45 | Chains 基础 | 1. LCEL 语法<br>2. 串联多个组件<br>3. 练习：写一个翻译 chain | 2h | [ ] |
| Day 46 | Output Parsers | 1. PydanticOutputParser<br>2. StructuredOutputParser<br>3. 练习：解析结构化输出 | 2h | [ ] |
| Day 47 | Memory 模块 | 1. ConversationBufferMemory<br>2. ConversationSummaryMemory<br>3. 练习：实现对话记忆 | 2h | [ ] |
| Day 48 | 综合练习 | 1. 整合 Prompt+Chain+Memory<br>2. 写一个完整的对话机器人<br>3. 添加历史记录 | 3h | [ ] |
| Day 49 | 周复习 | 1. 复习 LCEL 语法<br>2. 整理笔记<br>3. 看 LangChain 博客文章 | 2h | [ ] |

**资源**：
- [LangChain 官方文档](https://python.langchain.com/docs/get_started/introduction)
- [LangChain 中文教程](https://liaokong.gitbook.io/llm-kai-fa-jiao-cheng)

---

### 第 8 周：LangChain Tools 与 Chains

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 50 | Tool 基础 | 1. 理解 Tool 概念<br>2. 使用内置 Tools<br>3. 练习：调用搜索工具 | 2h | [ ] |
| Day 51 | 自定义 Tool | 1. 用 @tool 装饰器<br>2. 用 Tool 类<br>3. 练习：封装一个业务 API 为 Tool | 2h | [ ] |
| Day 52 | 常用 Chains | 1. RetrievalQA<br>2. ConversationalRetrievalChain<br>3. 练习：跑通示例 | 2h | [ ] |
| Day 53 | Router Chain | 1. 理解路由概念<br>2. MultiPromptChain<br>3. 练习：多意图路由 | 2h | [ ] |
| Day 54 | Transform Chain | 1. MapReduce<br>2. Refine<br>3. 练习：长文档处理 | 2h | [ ] |
| Day 55 | 综合练习 | 1. 设计多工具协作场景<br>2. 实现工具选择逻辑<br>3. 测试效果 | 3h | [ ] |
| Day 56 | 周复习 | 1. 整理 Tool 清单<br>2. 写使用心得<br>3. 预览下周内容 | 2h | [ ] |

---

### 第 9 周：RAG 基础 - Embedding 与向量存储

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 57 | Embedding 深入 | 1. 常见 Embedding 模型<br>2. 调用 Embedding API<br>3. 练习：语义相似度计算 | 2h | [ ] |
| Day 58 | 向量数据库概念 | 1. 理解向量检索<br>2. 对比常见向量库<br>3. 选择要学习的向量库 | 1.5h | [ ] |
| Day 59 | Chroma 入门 | 1. 安装 Chroma<br>2. 创建 Collection<br>3. 添加和查询文档 | 2h | [ ] |
| Day 60 | 文档加载 | 1. Document Loaders<br>2. 加载 PDF/TXT/MD<br>3. 练习：加载客服知识库 | 2h | [ ] |
| Day 61 | 文本切片 | 1. RecursiveCharacterTextSplitter<br>2. 实验不同 chunk 大小<br>3. 找到适合客服场景的配置 | 2h | [ ] |
| Day 62 | 完整流程 | 1. 文档→切片→向量化→存储<br>2. 封装为函数<br>3. 测试检索效果 | 3h | [ ] |
| Day 63 | 周实战 | 1. 搭建一个简单的文档问答<br>2. 测试不同问题的回答效果<br>3. 记录问题 | 4h | [ ] |

**资源**：
- [Chroma 官方文档](https://docs.trychroma.com/)
- 可选：FAISS、Milvus、Weaviate

---

### 第 10 周：RAG 检索优化

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 64 | 检索策略 | 1. Similarity Search<br>2. MMR（最大边际相关）<br>3. 练习：对比两种策略 | 2h | [ ] |
| Day 65 | 多路召回 | 1. 关键词检索 + 向量检索<br>2. 结果融合<br>3. 练习：实现双路召回 | 2.5h | [ ] |
| Day 66 | 重排序（Rerank） | 1. 理解 Rerank 概念<br>2. 使用 Cohere Rerank 或 BGE<br>3. 练习：对比 rerank 前后效果 | 2.5h | [ ] |
| Day 67 | Query 改写 | 1. 多版本查询生成<br>2. HyDE（假设性文档嵌入）<br>3. 练习：实现 query 改写 | 2h | [ ] |
| Day 68 | 上下文压缩 | 1. Contextual Compression<br>2. 过滤无关内容<br>3. 练习：集成到 RAG 流程 | 2h | [ ] |
| Day 69 | 综合优化 | 1. 整合多路召回 +Rerank<br>2. 设计评估指标<br>3. 测试优化效果 | 3h | [ ] |
| Day 70 | 周总结 | 1. 整理检索优化技巧<br>2. 写对比测试报告<br>3. 规划下周 | 2h | [ ] |

---

### 第 11 周：RAG 生成优化

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 71 | Prompt 优化 | 1. 设计更好的 RAG prompt<br>2. 添加引用标注<br>3. 练习：减少幻觉 | 2h | [ ] |
| Day 72 | 上下文管理 | 1. 上下文窗口限制<br>2. 智能选择相关片段<br>3. 练习：实现选择策略 | 2h | [ ] |
| Day 73 | 元数据过滤 | 1. 给文档添加元数据<br>2. 基于元数据过滤<br>3. 练习：按类别/时间过滤 | 2h | [ ] |
| Day 74 | 父子文档检索 | 1. Parent Document Retriever<br>2. 小切片检索 + 大片段生成<br>3. 练习：实现父子检索 | 2.5h | [ ] |
| Day 75 | 自助 RAG | 1. Self-RAG 概念<br>2. 模型自我评估<br>3. 阅读论文或文章 | 2h | [ ] |
| Day 76 | 综合实战 | 1. 整合本周优化<br>2. 对比优化前后效果<br>3. 写测试报告 | 3h | [ ] |
| Day 77 | 周总结 | 1. 整理 RAG 优化清单<br>2. 更新笔记<br>3. 准备 Agent 学习 | 2h | [ ] |

---

### 第 12 周：Agent 基础

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 78 | Agent 概念 | 1. 什么是 Agent<br>2. Agent 适用场景<br>3. 观看 Demo 视频 | 1.5h | [ ] |
| Day 79 | ReAct 模式 | 1. 理解 ReAct 论文思想<br>2. Reason + Action<br>3. 练习：手动模拟 ReAct 流程 | 2h | [ ] |
| Day 80 | LangChain Agent | 1. AgentExecutor<br>2. 内置 Agent 类型<br>3. 跑通官方示例 | 2h | [ ] |
| Day 81 | 工具集成 | 1. 集成 3-5 个工具<br>2. 设计工具描述<br>3. 测试 Agent 调用 | 2.5h | [ ] |
| Day 82 | 自定义 Agent | 1. 自定义 prompt<br>2. 调整停止条件<br>3. 练习：定制客服 Agent | 2h | [ ] |
| Day 83 | 调试与优化 | 1. 分析 Agent 决策过程<br>2. 优化工具描述<br>3. 修复常见问题 | 2.5h | [ ] |
| Day 84 | 周实战 | 1. 设计一个完整的 Agent 场景<br>2. 实现并测试<br>3. 录制演示视频 | 4h | [ ] |

**资源**：
- [ReAct 论文解读](https://react-lm.github.io/)
- LangChain Agent 文档

---

### 第 13 周：高级 Agent 模式

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 85 | Plan-and-Solve | 1. 理解 PSA 模式<br>2. 与 ReAct 对比<br>3. 练习：实现 PSA | 2h | [ ] |
| Day 86 | 多 Agent 协作 | 1. 理解多 Agent 概念<br>2. Supervisor 模式<br>3. 看 LangGraph 示例 | 2h | [ ] |
| Day 87 | LangGraph 入门 | 1. 安装 LangGraph<br>2. 理解 State Graph<br>3. 跑通 hello world | 2.5h | [ ] |
| Day 88 | 状态管理 | 1. 定义 State<br>2. 定义 Node<br>3. 定义 Edge | 2h | [ ] |
| Day 89 | 条件分支 | 1. Conditional Edge<br>2. 实现决策逻辑<br>3. 练习：客服路由 | 2.5h | [ ] |
| Day 90 | 综合练习 | 1. 设计多 Agent 协作流程<br>2. 实现并测试<br>3. 调试问题 | 3h | [ ] |
| Day 91 | 周总结 | 1. 整理 Agent 模式<br>2. 对比各模式优劣<br>3. 写总结文章 | 2h | [ ] |

---

### 第 14 周：阶段项目 - RAG 客服系统

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 92 | 项目规划 | 1. 需求分析<br>2. 技术选型<br>3. 架构设计 | 2h | [ ] |
| Day 93 | 知识库模块 | 1. 文档上传接口<br>2. 自动切片和向量化<br>3. 知识库管理 | 3h | [ ] |
| Day 94 | 检索模块 | 1. 多路召回实现<br>2. Rerank 集成<br>3. 检索 API | 3h | [ ] |
| Day 95 | 生成模块 | 1. RAG Prompt 设计<br>2. 上下文组装<br>3. 生成 API | 2.5h | [ ] |
| Day 96 | 对话模块 | 1. 多轮对话支持<br>2. 历史记录管理<br>3. 会话状态 | 2.5h | [ ] |
| Day 97 | 管理后台 | 1. 知识库管理页面<br>2. 对话历史页面<br>3. 数据统计页面 | 4h | [ ] |
| Day 98 | 测试与文档 | 1. 完整测试<br>2. 写 README<br>3. 部署说明 | 4h | [ ] |

**第二阶段完结！** 🎉

**产出物**：
- [ ] RAG 客服系统（完整代码）
- [ ] GitHub 仓库（带文档）
- [ ] 技术总结文章（RAG 实战）

---

## 📅 第三阶段：系统进阶（第 15-30 周）

### 目标
- [ ] 掌握生产级系统设计能力
- [ ] 能优化性能和成本
- [ ] 建立可观测性体系

---

### 第 15-16 周：LLM 网关设计

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W15 | 网关架构 | 1. 理解 API 网关概念<br>2. 设计 LLM 网关架构<br>3. 实现路由模块<br>4. 实现限流模块 | 网关原型 |
| W16 | 高级功能 | 1. 实现熔断降级<br>2. 添加请求队列<br>3. 实现计费统计<br>4. 集成监控 | 完整网关 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 99-105 | LLM 网关核心 | 实现模型路由、限流（令牌桶）、请求队列、超时控制、重试策略 | 每天 2h | [ ] |
| Day 106-112 | 网关完善 | 添加熔断器、降级策略、多模型负载均衡、计费统计、监控面板 | 每天 2h | [ ] |

---

### 第 17-18 周：缓存策略

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W17 | 缓存基础 | 1. Semantic Cache 原理<br>2. Redis 集成<br>3. 实现语义缓存<br>4. 缓存失效策略 | 语义缓存模块 |
| W18 | 高级缓存 | 1. Prompt Cache<br>2. 响应缓存<br>3. 分层缓存策略<br>4. 缓存监控 | 完整缓存方案 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 113-119 | 缓存实现 | Redis 基础、语义相似度缓存、精确匹配缓存、TTL 管理、缓存预热、缓存穿透处理 | 每天 2h | [ ] |
| Day 120-126 | 缓存优化 | 实现分层缓存（本地+Redis）、Prompt 模板缓存、流式响应缓存、命中率分析 | 每天 2h | [ ] |

---

### 第 19-20 周：异步任务队列

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W19 | Celery 基础 | 1. Celery 架构<br>2. Redis Broker<br>3. 实现异步任务<br>4. 任务状态追踪 | Celery 示例 |
| W20 | 生产实践 | 1. 任务重试机制<br>2. 定时任务<br>3. 任务监控<br>4. 错误处理 | 完整任务队列 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 127-133 | Celery 实战 | 安装配置、定义 Task、异步执行、进度追踪、重试机制、结果存储、定时任务 | 每天 2h | [ ] |
| Day 134-140 | 任务系统完善 | 任务优先级、任务取消、错误告警、任务看板、性能优化 | 每天 2h | [ ] |

---

### 第 21-22 周：流式响应与实时通信

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W21 | SSE 基础 | 1. Server-Sent Events<br>2. 实现流式接口<br>3. 前端对接 | 流式 Demo |
| W22 | WebSocket | 1. WebSocket 基础<br>2. 实现对话接口<br>3. 连接管理 | WebSocket 服务 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 141-147 | SSE 实现 | 理解 SSE 协议、FastAPI StreamingResponse、对接模型流式输出、前端 EventSource、断线重连 | 每天 2h | [ ] |
| Day 148-154 | WebSocket 实现 | WebSocket 协议、FastAPI WebSocket、连接管理、心跳机制、广播消息 | 每天 2h | [ ] |

---

### 第 23-24 周：性能优化实战

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W23 | 性能分析 | 1. 性能测试工具<br>2. 瓶颈分析<br>3.  profiling | 性能报告 |
| W24 | 优化实践 | 1. Token 优化<br>2. 批处理<br>3. 并发优化 | 优化方案 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 155-161 | 性能分析 | Locust 压测、瓶颈定位、Token 优化、请求批处理、并发控制 | 每天 2h | [ ] |
| Day 162-168 | 深度优化 | 向量检索优化、响应压缩、连接池优化、资源限制、成本分析 | 每天 2h | [ ] |

---

### 第 25-28 周：可观测性体系

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W25 | 日志系统 | 结构化日志、ELK/Loki、日志聚合、日志分析 | 日志平台 |
| W26 | 指标监控 | Prometheus、Grafana、自定义指标、告警规则 | 监控面板 |
| W27 | 链路追踪 | OpenTelemetry、Jaeger、全链路追踪、性能分析 | 追踪系统 |
| W28 | LLM 专项监控 | Token 监控、延迟分析、错误分析、质量评估 | 完整可观测性 |

**详细任务分解**：

| 日期范围 | 主题 | 具体任务 | 产出 |
|----------|------|----------|------|
| Day 169-175 | 日志系统 | Python 结构化日志、搭建 Loki+Grafana、日志收集、日志查询与分析 | 日志平台 |
| Day 176-182 | 指标监控 | Prometheus 基础、自定义指标、Grafana 面板、告警规则配置 | 监控面板 |
| Day 183-189 | 链路追踪 | OpenTelemetry 接入、Jaeger 部署、跨服务追踪、性能瓶颈分析 | 追踪系统 |
| Day 190-196 | LLM 专项 | Token 消耗统计、延迟分布、错误类型分析、用户行为分析 | 专项监控 |

---

### 第 29-30 周：生产级项目实战

| 周次 | 学习内容 | 具体任务 | 产出 |
|------|----------|----------|------|
| W29 | 系统集成 | 整合之前所有模块、完善异常处理、添加配置管理、编写文档 | 完整系统 |
| W30 | 压测与部署 | 全链路压测、性能调优、Docker 部署、CI/CD配置 | 可部署系统 |

**详细任务分解**：

| 日期 | 学习内容 | 具体任务 | 耗时 | 完成打卡 |
|------|----------|----------|------|----------|
| Day 197-203 | 系统集成 | 架构整合、异常处理完善、配置中心、文档编写、代码审查 | 每天 2-3h | [ ] |
| Day 204-210 | 部署实战 | Docker 容器化、K8s 基础、CI/CD 配置、压测报告、部署文档 | 每天 2-3h | [ ] |

**第三阶段完结！** 🎉

**产出物**：
- [ ] 生产级 LLM 网关
- [ ] 完整的监控体系
- [ ] 压测报告和优化文档
- [ ] 可部署的 Docker 镜像

---

## 📅 第四阶段：专项突破（第 31-52 周）

### 选择一个方向深耕

---

### 方向 A：RAG 专家路线

| 周次 | 学习主题 | 具体任务 | 产出 |
|------|----------|----------|------|
| W31-32 | 高级检索 | 混合检索、多向量检索、Graph RAG | 检索优化方案 |
| W33-34 | 文档处理 | 复杂文档解析、表格处理、多模态 | 文档处理 pipeline |
| W35-36 | 评估体系 | RAGAS、TruLens、人工评估流程 | 评估工具 |
| W37-38 | 专项优化 | 针对业务场景优化、AB 测试 | 优化报告 |
| W39-42 | 大型项目 | 企业级 RAG 系统、技术文章 | 完整项目 + 文章 |

---

### 方向 B：Agent 专家路线

| 周次 | 学习主题 | 具体任务 | 产出 |
|------|----------|----------|------|
| W31-32 | 高级 Agent | Tool Learning、Self-Reflection | 高级 Agent Demo |
| W33-34 | 多 Agent 系统 | Agent 协作、角色设计、通信机制 | 多 Agent 系统 |
| W35-36 | 任务规划 | 分解、排序、并行执行 | 规划系统 |
| W37-38 | 工具生态 | 丰富工具库、工具发现、自动注册 | 工具平台 |
| W39-42 | 大型项目 | 复杂 Agent 应用、技术文章 | 完整项目 + 文章 |

---

### 方向 C：平台架构路线

| 周次 | 学习主题 | 具体任务 | 产出 |
|------|----------|----------|------|
| W31-32 | 多租户架构 | 租户隔离、资源配额、权限管理 | 多租户方案 |
| W33-34 | 成本优化 | 用量统计、成本分摊、优化建议 | 成本系统 |
| W35-36 | 安全合规 | 数据加密、审计日志、合规检查 | 安全方案 |
| W37-38 | 高可用 | 容灾、备份、故障恢复 | HA 方案 |
| W39-42 | 大型项目 | 企业级平台、架构文档 | 完整平台 + 文档 |

---

### 方向 D：评估与质量路线

| 周次 | 学习主题 | 具体任务 | 产出 |
|------|----------|----------|------|
| W31-32 | 评估方法 | 自动化评估、人工评估、混合评估 | 评估框架 |
| W33-34 | 质量监控 | 实时监控、异常检测、质量告警 | 监控系统 |
| W35-36 | Badcase 分析 | 自动化归因、问题聚类、改进建议 | 分析工具 |
| W37-38 | 持续优化 | 数据闭环、迭代流程、效果对比 | 优化流程 |
| W39-42 | 大型项目 | 评估平台、技术文章 | 完整平台 + 文章 |

---

### 第 43-52 周：影响力建设

| 周次 | 任务 | 产出 |
|------|------|------|
| W43-44 | 技术博客 1 | RAG 实战总结 |
| W45-46 | 技术博客 2 | Agent 实战总结 |
| W47-48 | 开源贡献 | 给 LangChain 等项目提 PR |
| W49-50 | 技术分享 | 团队内部分享或线上分享 |
| W51-52 | 年度总结 | 学习历程回顾、明年规划 |

---

## 📊 学习检查清单

### 月度检查

每个月末回答以下问题：

- [ ] 这个月完成了哪些天的任务？
- [ ] 产出了哪些代码/文档/文章？
- [ ] 遇到了什么困难？如何解决的？
- [ ] 下个月的学习计划需要调整吗？
- [ ] 有什么想深入或 skipped 的内容？

### 季度检查

每季度末进行一次全面复盘：

- [ ] 季度目标是否达成？
- [ ] 最大的收获是什么？
- [ ] 哪些地方可以做得更好？
- [ ] 是否需要调整后续学习方向？
- [ ] 是否有余力提前进入下一阶段？

---

## 🛠️ 学习资源汇总

### 在线课程

| 课程 | 平台 | 链接 | 推荐度 |
|------|------|------|--------|
| LLM University | DeepLearning.AI | https://www.deeplearning.ai/courses/ | ⭐⭐⭐⭐⭐ |
| 李宏毅 LLM 课程 | YouTube | 搜索"李宏毅 LLM" | ⭐⭐⭐⭐⭐ |
| Full Stack LLM Bootcamp | UC Berkeley | https://fullstackdeeplearning.com/llm-bootcamp | ⭐⭐⭐⭐ |
| LangChain 官方教程 | LangChain | https://python.langchain.com/ | ⭐⭐⭐⭐⭐ |

### 书籍

- 《LLM 应用开发指南》
- 《Building Agentic RAG with LangGraph》
- 《Designing Machine Learning Systems》- Chip Huyen
- 《Hands-On LLMs》

### 博客/资讯

- [Sebastian Raschka 博客](https://magazine.sebastianraschka.com/)
- [Hugging Face Blog](https://huggingface.co/blog)
- [LangChain Blog](https://blog.langchain.dev/)
- [Jay Alammar 博客](https://jalammar.github.io/)
- 国内：李rumor、知乎"AI 工程化"话题

### 代码参考

- [LangChain Examples](https://github.com/langchain-ai/langchain)
- [LlamaIndex Examples](https://github.com/run-llama/llama_index)
- [Awesome LLM](https://github.com/Hannibal046/Awesome-LLM)
- [Dify](https://github.com/langgenius/dify)
- [FastGPT](https://github.com/labring/FastGPT)

### 社区

- LangChain Discord
- Hugging Face Forums
- Reddit r/LocalLLaMA
- 知乎 AI 工程化话题
- 微信 AI 技术社群

---

## 💡 学习建议

### 1. 保持节奏
- 不要追求完美，完成比完美重要
- 某天没学没关系，第二天继续
- 周末可以补进度，但也要休息

### 2. 动手优先
- 看懂≠会做，一定要动手写代码
- 每个知识点都要有代码产出
- 遇到问题先自己尝试解决

### 3. 记录成长
- 每天在打卡表打勾
- 每周写学习总结
- 每月整理 GitHub 仓库

### 4. 学以致用
- 学到的东西尽快用到工作中
- 哪怕是小优化也是有价值
- 工作中的问题是最好的学习素材

### 5. 找人交流
- 加入学习社群
- 关注行业大牛
- 有机会做技术分享

### 6. 接受变化
- AI 领域变化快，不要追求"学完"
- 掌握学习方法比掌握知识重要
- 保持好奇心和持续学习

---

## 📝 附录：环境准备清单

### 软件安装

- [ ] Python 3.10+
- [ ] PyCharm / VSCode
- [ ] Git
- [ ] Docker Desktop
- [ ] Postman / Insomnia

### 账号注册

- [ ] GitHub
- [ ] Hugging Face
- [ ] 硅基流动/DeepSeek（模型 API）
- [ ] 阿里云/腾讯云（可选，部署用）

### Python 库

```bash
# 基础库
pip install requests aiohttp httpx
pip install pydantic pyyaml python-dotenv

# LLM 相关
pip install langchain langchain-community langchain-core
pip install llama-index

# 向量数据库
pip install chromadb faiss-cpu

# Web 框架
pip install fastapi uvicorn websockets

# 任务队列
pip install celery redis

# 监控
pip install prometheus-client opentelemetry-api

# 工具库
pip install jinja2 python-jose passlib
```

---

**祝你学习顺利！有任何问题随时可以回顾这个文档或寻求帮助。** 🚀

---

*最后更新：2026-03-09*
