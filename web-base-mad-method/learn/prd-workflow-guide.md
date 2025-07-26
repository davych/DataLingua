# PRD生成后的完整工作流程指南

## 🎯 PRD生成后你要做什么？

### 第一步：保存PRD文档
```bash
# 在项目根目录创建docs文件夹
mkdir docs
# 将Web UI生成的PRD保存为
docs/prd.md
```

### 第二步：创建架构文档
在Web UI中继续：
1. 输入 `*architect` 切换到架构师模式
2. AI会基于PRD生成架构文档
3. 保存为 `docs/architecture.md`

### 第三步：文档分片 (Document Sharding)
这是BMAD的核心概念！将大文档拆分成小文件，方便AI处理。

## 🔧 如何将BMAD Agents集成到IDE中

### 方法一：使用Cursor (推荐)

Cursor内置了AI功能，可以直接使用BMAD agents：

#### 1. 安装BMAD到项目
```bash
# 在项目根目录执行
npx bmad-method install
```

#### 2. 在Cursor中设置BMAD上下文
创建 `.cursorrules` 文件：
```markdown
# BMad Method Context

你是一个BMad-Method的AI开发助手，可以扮演以下角色：

🧠 Analyst (分析师) - 市场研究、竞品分析
👔 PM (项目经理) - 创建PRD、需求管理  
🏗️ Architect (架构师) - 系统架构设计
📋 PO (产品负责人) - 产品管理、文档分片
🚀 SM (Scrum Master) - 敏捷流程管理
💻 Dev (开发者) - 代码实现
🔍 QA (质量保证) - 代码审查

## 可用命令
@analyst - 切换到分析师模式
@pm - 切换到项目经理模式
@architect - 切换到架构师模式
@po - 切换到产品负责人模式
@sm - 切换到Scrum Master模式
@dev - 切换到开发者模式
@qa - 切换到QA模式

## 项目文档
- PRD: docs/prd.md
- 架构: docs/architecture.md
- 分片文档: docs/prd/ 和 docs/architecture/

## 工作流程
1. 根据PRD和架构文档实现功能
2. 使用@dev进行代码实现
3. 使用@qa进行代码审查
4. 使用@sm管理开发流程
```

#### 3. 使用BMAD Agents
在Cursor中：
```bash
@po 请分片PRD文档
@sm 创建下一个开发故事
@dev 实现用户认证功能
@qa 审查这段代码
```

### 方法二：使用VSCode + GitHub Copilot

#### 1. 安装BMAD
```bash
npx bmad-method install
```

#### 2. 创建VSCode工作区设置
创建 `.vscode/settings.json`：
```json
{
  "bmad.enabled": true,
  "bmad.agents": ["pm", "architect", "po", "sm", "dev", "qa"],
  "bmad.docsPath": "./docs"
}
```

#### 3. 使用GitHub Copilot + BMAD
- Copilot负责代码生成
- BMAD agents负责项目管理和流程控制

### 方法三：使用Claude Desktop

#### 1. 安装Claude Desktop
从 https://claude.ai/download 下载

#### 2. 设置项目上下文
在Claude Desktop中：
1. 打开项目文件夹
2. 上传PRD和架构文档
3. 设置BMAD代理配置

## 📋 详细工作流程

### 阶段1：文档准备

#### 1.1 保存Web UI生成的文档
```bash
# 项目结构
my-project/
├── docs/
│   ├── prd.md              # Web UI生成的PRD
│   ├── architecture.md      # Web UI生成的架构
│   ├── prd/                # 分片后的PRD文档
│   └── architecture/        # 分片后的架构文档
├── src/                    # 源代码
└── README.md
```

#### 1.2 文档分片
```bash
# 使用PO agent分片文档
@po shard-doc docs/prd.md docs/prd
@po shard-doc docs/architecture.md docs/architecture
```

分片后的结构：
```
docs/prd/
├── project-overview.md
├── functional-requirements.md
├── non-functional-requirements.md
├── user-stories.md
└── acceptance-criteria.md

docs/architecture/
├── system-overview.md
├── tech-stack.md
├── database-design.md
├── api-design.md
└── deployment-config.md
```

### 阶段2：开发流程

#### 2.1 创建Epic和Stories
```bash
@sm create-next-story
```

SM会：
1. 读取分片后的PRD
2. 创建用户故事
3. 分配开发任务

#### 2.2 实现功能
```bash
@dev implement-user-authentication
```

Dev会：
1. 读取架构文档
2. 实现具体功能
3. 编写测试代码

#### 2.3 代码审查
```bash
@qa review-code
```

QA会：
1. 审查代码质量
2. 检查测试覆盖
3. 提供改进建议

### 阶段3：持续开发

#### 3.1 故事完成
```bash
@sm mark-story-done
```

#### 3.2 创建下一个故事
```bash
@sm create-next-story
```

## 🎯 实际示例：待办事项应用

### 步骤1：Web UI生成文档
**在Claude中**：
```
你: "我想创建一个待办事项应用"
Claude: [生成PRD]
你: "*architect"
Claude: [生成架构文档]
```

### 步骤2：保存到本地
```bash
mkdir todo-app
cd todo-app
mkdir docs
# 复制PRD和架构文档到docs/
```

### 步骤3：在Cursor中设置
创建 `.cursorrules`：
```markdown
# BMad Method - 待办事项应用

项目文档：
- PRD: docs/prd.md
- 架构: docs/architecture.md

可用命令：
@po - 产品负责人
@sm - Scrum Master  
@dev - 开发者
@qa - 质量保证
```

### 步骤4：开始开发
```bash
# 分片文档
@po shard-doc docs/prd.md docs/prd

# 创建第一个故事
@sm create-next-story

# 实现功能
@dev implement-todo-list

# 代码审查
@qa review-code
```

## 🔄 完整工作流程总结

### 文档流转：
1. **Web UI生成** → PRD + 架构文档
2. **保存到本地** → docs/文件夹
3. **分片文档** → 小文件便于AI处理
4. **IDE集成** → 通过agents使用

### 开发流程：
1. **SM创建故事** → 基于PRD分片
2. **Dev实现功能** → 基于架构文档
3. **QA审查代码** → 质量保证
4. **循环继续** → 下一个故事

### 工具配合：
- **Web UI**: 规划、设计、文档生成
- **IDE + BMAD**: 开发、管理、审查
- **GitHub Copilot**: 代码辅助
- **Git**: 版本控制

## 🚀 立即开始

1. **选择IDE**: Cursor (推荐) 或 VSCode
2. **安装BMAD**: `npx bmad-method install`
3. **设置上下文**: 创建配置文件
4. **开始开发**: 使用@命令调用agents

你想现在就开始设置吗？我可以帮你：
1. 配置具体的IDE环境
2. 设置BMAD agents
3. 演示完整的工作流程 