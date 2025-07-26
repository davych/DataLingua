# 实操示例：创建待办事项应用

## 🎯 完整流程演示

### 第一步：Web UI规划阶段

#### 1.1 打开Claude (https://claude.ai)

#### 1.2 设置BMad代理
在新对话中输入：

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

#### 1.3 开始项目对话

**你输入**: "我想创建一个简单的待办事项应用"

**Claude回复**: 
```
太好了！让我帮你规划这个项目。我是BMad Orchestrator，可以协调整个开发流程。

首先，让我了解一下你的需求：

1. **目标用户**：这个应用主要给谁使用？
2. **核心功能**：你希望包含哪些基本功能？
3. **技术偏好**：你偏好什么技术栈？

我可以帮你：
- 输入 `*analyst` 进行市场研究和竞品分析
- 输入 `*pm` 直接开始创建PRD
- 输入 `*workflow` 开始完整的工作流程

或者直接告诉我你的想法，我会切换到最合适的角色来帮助你！
```

**你输入**: "*pm"

**Claude回复**:
```
👔 我是BMad项目经理，现在帮你创建PRD（产品需求文档）。

请告诉我以下信息：

1. **用户角色**：
   - 个人用户还是团队协作？
   - 目标用户群体是什么？

2. **核心功能**：
   - 添加、删除、完成、编辑任务？
   - 需要任务分类吗？
   - 需要优先级设置吗？
   - 需要截止日期吗？

3. **技术偏好**：
   - Web应用、移动应用、桌面应用？
   - 偏好什么技术栈？

4. **部署方式**：
   - 本地运行还是云端部署？
   - 需要用户注册登录吗？

请详细描述你的需求，我会据此创建详细的PRD文档。
```

**你输入**: "个人用户，需要添加、删除、完成、编辑任务，Web应用，用React+Node.js，本地运行，不需要登录"

**Claude回复**:
```
完美！现在我来创建PRD文档。

# 产品需求文档 (PRD) - 个人待办事项应用

## 1. 项目概述
- **项目名称**: 个人待办事项应用
- **目标用户**: 个人用户
- **应用类型**: Web应用
- **技术栈**: React + Node.js
- **部署方式**: 本地运行

## 2. 功能需求 (FR)

### 2.1 核心功能
- **添加任务**: 用户可以添加新的待办事项
- **删除任务**: 用户可以删除不需要的任务
- **完成任务**: 用户可以标记任务为已完成
- **编辑任务**: 用户可以修改任务内容

### 2.2 用户界面
- 简洁直观的界面设计
- 任务列表显示
- 添加任务按钮
- 任务操作按钮（编辑、删除、完成）

## 3. 非功能需求 (NFR)
- 响应式设计，支持桌面和移动设备
- 本地数据存储
- 快速加载时间
- 直观的用户体验

## 4. 用户故事
1. 作为用户，我希望能够添加新的待办事项
2. 作为用户，我希望能够查看所有待办事项列表
3. 作为用户，我希望能够标记任务为已完成
4. 作为用户，我希望能够编辑任务内容
5. 作为用户，我希望能够删除不需要的任务

PRD文档创建完成！现在可以输入 `*architect` 开始设计系统架构。
```

**你输入**: "*architect"

**Claude回复**:
```
🏗️ 我是BMad架构师，基于PRD设计系统架构。

# 系统架构设计 - 个人待办事项应用

## 1. 技术栈选择
- **前端**: React 18 + TypeScript
- **后端**: Node.js + Express
- **数据库**: SQLite (本地存储)
- **构建工具**: Vite
- **包管理**: npm

## 2. 系统架构

### 2.1 前端架构
```
src/
├── components/
│   ├── TodoList.tsx      # 任务列表组件
│   ├── TodoItem.tsx      # 单个任务组件
│   ├── AddTodo.tsx       # 添加任务组件
│   └── TodoForm.tsx      # 任务表单组件
├── hooks/
│   └── useTodos.ts       # 任务管理Hook
├── types/
│   └── todo.ts           # 类型定义
└── App.tsx               # 主应用组件
```

### 2.2 后端架构
```
server/
├── routes/
│   └── todos.js          # 任务API路由
├── models/
│   └── Todo.js           # 任务数据模型
├── database/
│   └── db.js             # 数据库连接
└── server.js             # 服务器入口
```

## 3. API设计
- `GET /api/todos` - 获取所有任务
- `POST /api/todos` - 创建新任务
- `PUT /api/todos/:id` - 更新任务
- `DELETE /api/todos/:id` - 删除任务

## 4. 数据库设计
```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 5. 部署配置
- 前端端口: 3000
- 后端端口: 5000
- 数据库: SQLite文件存储

架构设计完成！现在可以开始实现代码了。
```

### 第二步：保存文档到本地

#### 2.1 创建项目文件夹
```bash
mkdir todo-app
cd todo-app
```

#### 2.2 创建文档结构
```bash
mkdir docs
```

#### 2.3 保存Web UI生成的文档
将Claude生成的PRD和架构文档分别保存为：
- `docs/prd.md`
- `docs/architecture.md`

### 第三步：在VSCode中实现

#### 3.1 在VSCode中打开项目
```bash
code .
```

#### 3.2 创建项目结构
```bash
# 创建前端项目
npx create-react-app frontend --template typescript
cd frontend
npm install axios

# 创建后端项目
cd ..
mkdir backend
cd backend
npm init -y
npm install express cors sqlite3
```

#### 3.3 根据架构文档实现代码

**前端实现** (frontend/src/App.tsx):
```typescript
import React, { useState, useEffect } from 'react';
import TodoList from './components/TodoList';
import AddTodo from './components/AddTodo';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetchTodos();
  }, []);

  const fetchTodos = async () => {
    const response = await fetch('http://localhost:5000/api/todos');
    const data = await response.json();
    setTodos(data);
  };

  return (
    <div className="App">
      <h1>待办事项应用</h1>
      <AddTodo onAdd={fetchTodos} />
      <TodoList todos={todos} onUpdate={fetchTodos} />
    </div>
  );
}

export default App;
```

**后端实现** (backend/server.js):
```javascript
const express = require('express');
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();

const app = express();
const port = 5000;

app.use(cors());
app.use(express.json());

// 数据库连接
const db = new sqlite3.Database('./todos.db');

// 创建表
db.run(`CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)`);

// API路由
app.get('/api/todos', (req, res) => {
    db.all('SELECT * FROM todos ORDER BY created_at DESC', (err, rows) => {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json(rows);
    });
});

app.post('/api/todos', (req, res) => {
    const { title } = req.body;
    db.run('INSERT INTO todos (title) VALUES (?)', [title], function(err) {
        if (err) {
            res.status(500).json({ error: err.message });
            return;
        }
        res.json({ id: this.lastID });
    });
});

app.listen(port, () => {
    console.log(`服务器运行在 http://localhost:${port}`);
});
```

## 🎯 关键要点总结

### 文档流转过程：
1. **Web UI生成** → Claude创建PRD和架构文档
2. **保存到本地** → 复制到docs/文件夹
3. **VSCode实现** → 根据文档编写代码

### 角色分工：
- **Web UI (Claude)**: 项目规划、需求分析、文档生成
- **VSCode**: 代码实现、调试、测试
- **GitHub Copilot**: 辅助编码、代码补全

### 工具链：
- **规划工具**: Claude/Gemini/ChatGPT
- **开发工具**: VSCode + GitHub Copilot
- **文档管理**: 本地docs/文件夹
- **版本控制**: Git

这样你就完成了从Web UI规划到VSCode实现的完整流程！ 