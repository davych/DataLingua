# BMAD Agent文件映射配置

## 🎯 BMAD Agent文件对应关系

### 实际Agent文件列表
```
bmad-core/agents/
├── analyst.md          # 分析师 - 市场研究、竞品分析
├── architect.md        # 架构师 - 系统架构设计
├── bmad-master.md     # 万能执行器 - 可执行任何任务
├── bmad-orchestrator.md # 协调器 - 协调所有agents
├── dev.md             # 开发者 - 代码实现
├── pm.md              # 项目经理 - PRD创建、需求管理
├── po.md              # 产品负责人 - 产品管理、文档分片
├── qa.md              # 质量保证 - 代码审查
├── sm.md              # Scrum Master - 故事创建、流程管理
└── ux-expert.md       # UX专家 - 用户体验设计
```

## 🔧 VSCode + GitHub Copilot 配置

### 第一步：创建Agent映射配置

#### 1. 创建 `.vscode/bmad-agents.json`
```json
{
  "agents": {
    "analyst": {
      "file": "bmad-core/agents/analyst.md",
      "name": "Analyst",
      "role": "市场研究和竞品分析专家",
      "commands": ["*help", "*create-doc", "*facilitate-brainstorming"],
      "description": "专门进行市场研究、竞品分析、需求调研"
    },
    "architect": {
      "file": "bmad-core/agents/architect.md", 
      "name": "Architect",
      "role": "系统架构设计专家",
      "commands": ["*help", "*create-doc", "*create-architecture"],
      "description": "专门设计系统架构、技术栈选择、API设计"
    },
    "bmad-master": {
      "file": "bmad-core/agents/bmad-master.md",
      "name": "BMad Master", 
      "role": "万能任务执行器",
      "commands": ["*help", "*task", "*create-doc", "*execute-checklist"],
      "description": "可以执行任何BMAD任务，无需角色切换"
    },
    "bmad-orchestrator": {
      "file": "bmad-core/agents/bmad-orchestrator.md",
      "name": "BMad Orchestrator",
      "role": "协调器",
      "commands": ["*help", "*agent", "*workflow", "*plan"],
      "description": "协调所有agents，推荐合适的角色"
    },
    "dev": {
      "file": "bmad-core/agents/dev.md",
      "name": "James",
      "role": "全栈开发专家", 
      "commands": ["*help", "*develop-story", "*run-tests", "*explain"],
      "description": "专门负责代码实现、测试、优化"
    },
    "pm": {
      "file": "bmad-core/agents/pm.md",
      "name": "John",
      "role": "产品经理",
      "commands": ["*help", "*create-prd", "*create-epic", "*shard-prd"],
      "description": "专门负责PRD创建、需求管理、产品规划"
    },
    "po": {
      "file": "bmad-core/agents/po.md",
      "name": "Sarah", 
      "role": "产品负责人",
      "commands": ["*help", "*execute-checklist-po", "*shard-doc", "*validate-story-draft"],
      "description": "专门负责产品管理、文档分片、故事验证"
    },
    "qa": {
      "file": "bmad-core/agents/qa.md",
      "name": "Quinn",
      "role": "高级开发者和QA架构师",
      "commands": ["*help", "*review"],
      "description": "专门负责代码审查、重构、质量保证"
    },
    "sm": {
      "file": "bmad-core/agents/sm.md",
      "name": "Bob",
      "role": "Scrum Master",
      "commands": ["*help", "*draft", "*story-checklist"],
      "description": "专门负责故事创建、流程管理、敏捷指导"
    },
    "ux-expert": {
      "file": "bmad-core/agents/ux-expert.md",
      "name": "UX Expert",
      "role": "用户体验专家",
      "commands": ["*help", "*create-doc", "*generate-ai-frontend-prompt"],
      "description": "专门负责用户界面设计、用户体验优化"
    }
  },
  "workflows": {
    "planning": ["analyst", "pm", "architect"],
    "development": ["sm", "dev", "qa"],
    "management": ["po", "bmad-orchestrator"]
  }
}
```

#### 2. 创建 `.vscode/settings.json`
```json
{
  "bmad.enabled": true,
  "bmad.agentsPath": "./bmad-core/agents",
  "bmad.configPath": "./.vscode/bmad-agents.json",
  "bmad.docsPath": "./docs",
  "bmad.projectType": "web",
  "bmad.techStack": ["react", "nodejs"],
  "bmad.collaboration": true,
  "bmad.autoSwitch": false,
  "github.copilot.enable": {
    "*": true
  },
  "github.copilot.chat.enable": true,
  "github.copilot.agent.enable": true
}
```

#### 3. 创建 `.vscode/tasks.json`
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "BMAD: Switch to Analyst",
      "type": "shell",
      "command": "echo '@analyst'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to Architect", 
      "type": "shell",
      "command": "echo '@architect'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to BMad Master",
      "type": "shell", 
      "command": "echo '@bmad-master'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to Orchestrator",
      "type": "shell",
      "command": "echo '@bmad-orchestrator'", 
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to Dev",
      "type": "shell",
      "command": "echo '@dev'",
      "presentation": {
        "echo": true,
        "reveal": "never", 
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to PM",
      "type": "shell",
      "command": "echo '@pm'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to PO",
      "type": "shell",
      "command": "echo '@po'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to QA",
      "type": "shell",
      "command": "echo '@qa'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to SM",
      "type": "shell",
      "command": "echo '@sm'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "BMAD: Switch to UX Expert",
      "type": "shell",
      "command": "echo '@ux-expert'",
      "presentation": {
        "echo": true,
        "reveal": "never",
        "focus": false,
        "panel": "shared"
      }
    }
  ]
}
```

### 第二步：创建GitHub Copilot集成配置

#### 1. 创建 `.copilot/bmad-agents.json`
```json
{
  "agents": {
    "analyst": {
      "file": "bmad-core/agents/analyst.md",
      "name": "Analyst",
      "description": "市场研究和竞品分析专家",
      "context": ["docs/prd.md", "docs/architecture.md"],
      "focus": "market research, competitor analysis, user research"
    },
    "architect": {
      "file": "bmad-core/agents/architect.md",
      "name": "Architect", 
      "description": "系统架构设计专家",
      "context": ["docs/architecture.md", "docs/prd.md"],
      "focus": "system architecture, tech stack, API design"
    },
    "bmad-master": {
      "file": "bmad-core/agents/bmad-master.md",
      "name": "BMad Master",
      "description": "万能任务执行器",
      "context": ["bmad-core/"],
      "focus": "any BMad task execution"
    },
    "bmad-orchestrator": {
      "file": "bmad-core/agents/bmad-orchestrator.md",
      "name": "BMad Orchestrator",
      "description": "协调器",
      "context": ["bmad-core/agents/"],
      "focus": "agent coordination and workflow management"
    },
    "dev": {
      "file": "bmad-core/agents/dev.md",
      "name": "James",
      "description": "全栈开发专家",
      "context": ["src/", "docs/stories/", "docs/architecture/"],
      "focus": "code implementation, testing, optimization"
    },
    "pm": {
      "file": "bmad-core/agents/pm.md",
      "name": "John",
      "description": "产品经理",
      "context": ["docs/prd.md", "docs/architecture.md"],
      "focus": "PRD creation, requirement management, product planning"
    },
    "po": {
      "file": "bmad-core/agents/po.md",
      "name": "Sarah",
      "description": "产品负责人",
      "context": ["docs/prd/", "docs/stories/"],
      "focus": "product management, document sharding, story validation"
    },
    "qa": {
      "file": "bmad-core/agents/qa.md",
      "name": "Quinn",
      "description": "高级开发者和QA架构师",
      "context": ["src/", "tests/", "docs/stories/"],
      "focus": "code review, refactoring, quality assurance"
    },
    "sm": {
      "file": "bmad-core/agents/sm.md",
      "name": "Bob",
      "description": "Scrum Master",
      "context": ["docs/prd/", "docs/stories/"],
      "focus": "story creation, process management, agile guidance"
    },
    "ux-expert": {
      "file": "bmad-core/agents/ux-expert.md",
      "name": "UX Expert",
      "description": "用户体验专家",
      "context": ["docs/architecture.md", "src/"],
      "focus": "UI design, UX optimization, frontend specifications"
    }
  }
}
```

## 🎯 使用方法

### 方法一：使用VSCode命令面板
1. 按 `Ctrl+Shift+P` (Windows) 或 `Cmd+Shift+P` (Mac)
2. 输入 "BMAD"
3. 选择对应的agent任务

### 方法二：使用GitHub Copilot Chat
```
@analyst 请进行市场研究
@architect 请设计系统架构
@bmad-master 请执行任何任务
@bmad-orchestrator 请协调开发流程
@dev 请实现功能
@pm 请创建PRD
@po 请分片文档
@qa 请审查代码
@sm 请创建故事
@ux-expert 请设计用户界面
```

### 方法三：直接调用agent文件
每个agent都有对应的 `.md` 文件，包含完整的角色定义和命令。

## 🎯 实际示例

### 示例1：使用Orchestrator协调
```
@bmad-orchestrator 我想开发用户认证功能，请帮我协调

Orchestrator: "🎭 我是BMad Orchestrator，让我帮你协调开发流程。

基于你的需求，我建议以下流程：
1. @analyst - 进行用户研究
2. @pm - 创建PRD
3. @architect - 设计架构
4. @sm - 创建故事
5. @dev - 实现功能
6. @qa - 代码审查

你想从哪个阶段开始？"
```

### 示例2：使用BMad Master执行任务
```
@bmad-master 请帮我创建PRD文档

BMad Master: "🧙 我是BMad Master，可以执行任何BMAD任务。

我将使用PM的create-doc任务和PRD模板来创建文档。
请告诉我项目的基本信息..."
```

### 示例3：使用PO分片文档
```
@po 请分片PRD文档

PO: "📝 我是产品负责人Sarah，专门负责文档管理。

我将使用shard-doc任务来分片docs/prd.md到docs/prd/文件夹。
正在执行分片操作..."
```

## 🔧 关键优势

1. **文件映射**: 每个角色都对应实际的 `.md` 文件
2. **完整定义**: 每个agent文件包含完整的角色定义、命令、依赖
3. **灵活切换**: 可以随时切换不同的agent
4. **上下文共享**: 所有agents都能访问项目文档
5. **工作流程**: 从规划到实现的完整流程

你想现在就开始设置吗？我可以帮你：
1. 创建具体的配置文件
2. 设置agent映射
3. 演示完整的工作流程 