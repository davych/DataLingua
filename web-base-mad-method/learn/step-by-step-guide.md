# BMad完整操作指南：从Web UI到VSCode

## 🎯 第一步：Web UI规划阶段

### 1.1 选择AI平台
打开以下任一平台：
- **Claude**: https://claude.ai
- **Gemini**: https://gemini.google.com  
- **ChatGPT**: https://chat.openai.com

### 1.2 设置BMad代理
在新对话中，复制粘贴以下内容：

```
你是一个BMad-Method的AI代理系统，专门进行AI驱动的敏捷开发。

你的角色是BMad Orchestrator，可以协调不同的专业角色：

🧠 Analyst (分析师) - 市场研究、竞品分析
👔 PM (项目经理) - 创建PRD、需求管理  
🏗️ Architect (架构师) - 系统架构设计
📋 PO (产品负责人) - 产品管理、文档分片

所有命令以*开头：
*help - 显示帮助
*analyst - 切换到分析师
*pm - 切换到项目经理
*architect - 切换到架构师
*create-prd - 创建PRD文档
*create-architecture - 创建架构文档

现在请扮演BMad Orchestrator，帮助用户进行项目规划。
```

### 1.3 开始项目规划
输入你的项目想法，例如：
```
"我想创建一个简单的待办事项应用"
```

AI会引导你完成规划过程。

## 🎯 第二步：生成PRD和架构文档

### 2.1 创建PRD (产品需求文档)
在Web UI中：
1. 输入 `*pm` 切换到项目经理模式
2. 回答AI的问题（用户需求、功能特性等）
3. AI会生成完整的PRD文档

### 2.2 创建架构文档
在Web UI中：
1. 输入 `*architect` 切换到架构师模式
2. AI会基于PRD设计系统架构
3. 生成技术栈、数据库设计、API设计等

### 2.3 保存文档
AI会生成两个主要文档：
- **PRD文档**：产品需求、功能列表、用户故事
- **架构文档**：技术栈、系统设计、API规范

## 🎯 第三步：在VSCode中实现

### 3.1 创建项目文件夹
```bash
mkdir my-todo-app
cd my-todo-app
```

### 3.2 在VSCode中打开项目
```bash
code .
```

### 3.3 创建文档文件夹
```bash
mkdir docs
```

### 3.4 保存Web UI生成的文档
将Web UI中生成的PRD和架构文档保存到：
- `docs/prd.md`
- `docs/architecture.md`

### 3.5 开始编码
根据架构文档中的技术栈开始实现：
- 前端：React/Vue/Angular
- 后端：Node.js/Python/Java
- 数据库：MySQL/PostgreSQL/MongoDB

## 🎯 具体示例：待办事项应用

### Web UI对话示例：

**你**: "我想创建一个简单的待办事项应用"

**AI (BMad Orchestrator)**: "太好了！让我帮你规划这个项目。

首先了解一下需求：
1. 目标用户是谁？
2. 需要哪些核心功能？
3. 偏好什么技术栈？

输入 `*pm` 开始创建PRD，或直接告诉我你的想法。"

**你**: "*pm"

**AI (PM模式)**: "👔 我是BMad项目经理，现在帮你创建PRD。

请告诉我：
1. 用户角色：个人用户还是团队协作？
2. 核心功能：添加、删除、完成、编辑任务？
3. 额外功能：分类、优先级、截止日期？
4. 技术偏好：Web应用、移动应用、桌面应用？"

**你**: "个人用户，需要添加、删除、完成、编辑任务，Web应用，用React+Node.js"

**AI**: "完美！现在创建PRD文档..."

[AI会生成详细的PRD文档]

**你**: "*architect"

**AI (架构师模式)**: "🏗️ 我是BMad架构师，基于PRD设计系统架构..."

[AI会生成详细的架构文档]

### 保存到VSCode：

1. **创建项目结构**：
```
my-todo-app/
├── docs/
│   ├── prd.md          # Web UI生成的PRD
│   └── architecture.md  # Web UI生成的架构
├── frontend/            # React前端
├── backend/             # Node.js后端
└── README.md
```

2. **根据架构文档开始编码**：
- 前端：React组件、状态管理
- 后端：Express API、数据库连接
- 数据库：MongoDB/PostgreSQL

## 🎯 关键要点

### 文档流转：
1. **Web UI生成** → PRD + 架构文档
2. **保存到本地** → docs/文件夹
3. **VSCode实现** → 根据文档编码

### 角色分工：
- **Web UI**: 规划、设计、文档生成
- **VSCode**: 代码实现、调试、测试

### 工具配合：
- **GitHub Copilot**: 辅助编码
- **Cursor**: AI辅助开发
- **BMad**: 项目规划和文档管理

## 🎯 下一步行动

1. **现在就开始**：选择一个AI平台，复制上面的代理配置
2. **选择简单项目**：待办事项、个人博客、计算器
3. **完整体验**：从规划到实现的完整流程
4. **逐步深入**：熟悉后再尝试复杂项目

你想现在就开始体验吗？我可以帮你设置具体的AI平台和项目！ 