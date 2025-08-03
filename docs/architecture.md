# DataLingua MVP 架构文档

> 本节聚焦 MVP 范围，后续为历史/扩展内容，仅供参考。

## 1. 架构总览（MVP 范围）

DataLingua MVP 实现自然语言到结构化数据查询的最小可用产品。核心架构包括：

- NLU 语义解析节点
- SQLCoder 查询 Agent
- Workflow 流程编排（LangGraph）
- API 层（对外接口）
- 数据存储（仅限 MVP 所需）

## 2. 技术选型与理由

- **LangGraph**：用于编排 NLU 及 SQLCoder 节点，实现多 Agent 协作。
- **SQLCoder**：开源大模型，负责自然语言到 SQL 的转换。
- **FastAPI**：对外 API 服务。
- **SQLite**：轻量级数据库，满足 MVP 阶段需求。

## 3. LangGraph NLU 节点设计

### 3.1 节点功能
负责将用户自然语言输入解析为结构化语义对象，作为 SQLCoder agent 的输入。

### 3.2 输入输出
- 输入：用户自然语言问题
- 输出：结构化语义对象（如意图、实体、表字段等）-参考 [docs/nlu.md](docs/nlu.md)

### 3.3 关键实现要点
- 基于 LangGraph 定义 NLU 节点，支持上下文传递
- MVP 阶段仅需单轮解析，输出需与 SQLCoder agent 输入兼容

## 4. SQLCoder Agent 节点设计

### 4.1 节点功能
将结构化语义对象转换为 SQL 查询，并执行数据库检索。

### 4.2 输入输出
- 输入：结构化语义对象（来自 NLU 节点）
- 输出：SQL 语句

### 4.3 关键实现要点
- 在 LangGraph 中定义 2 个 agent 节点 分别为 NLU 和 SQLCoder
- NLU 节点输出直接作为 SQLCoder 节点输入
- 支持基础 SQL 生成与执行，MVP 阶段不考虑复杂优化

## 5. Workflow 运行机制

### 5.1 节点协作流程（LangGraph）
1. 用户输入自然语言问题
2. NLU 节点解析语义，输出结构化对象
3. SQLCoder agent根据输入生成 SQL
4. db服务拿到sql之后，去查询数据库
5. 汇总并返回查询结果

### 5.2 典型调用链路
- LangGraph workflow 串联 NLU → SQLCoder → 数据返回
- 支持节点间数据传递与状态跟踪

### 5.3 错误处理与扩展性
- MVP 阶段仅做基础异常捕获与提示
- 节点可扩展为更多 agent 或支持更复杂的分支

## 6. MVP 范围说明与后续展望

本架构仅覆盖 MVP 必需功能，未包含企业级优化、权限管理、分布式扩展等内容。后续可基于 LangGraph 节点体系，逐步引入更复杂的 agent、数据源和安全机制。
