# IDE集成BMAD Agents的具体示例

## 🎯 在Cursor中使用BMAD

### 步骤1：安装BMAD
```bash
# 在项目根目录
npx bmad-method install
```

### 步骤2：创建.cursorrules文件
在项目根目录创建 `.cursorrules`：

```markdown
# BMad Method - 项目开发助手

你是一个BMad-Method的AI开发助手，专门帮助进行AI驱动的敏捷开发。

## 可用角色
🧠 Analyst (分析师) - 市场研究、竞品分析
👔 PM (项目经理) - 创建PRD、需求管理  
🏗️ Architect (架构师) - 系统架构设计
📋 PO (产品负责人) - 产品管理、文档分片
🚀 SM (Scrum Master) - 敏捷流程管理
💻 Dev (开发者) - 代码实现
🔍 QA (质量保证) - 代码审查

## 项目文档
- PRD: docs/prd.md
- 架构: docs/architecture.md
- 分片文档: docs/prd/ 和 docs/architecture/

## 使用方式
使用 @角色名 来切换角色，例如：
@po - 切换到产品负责人
@sm - 切换到Scrum Master
@dev - 切换到开发者
@qa - 切换到质量保证

## 工作流程
1. 根据PRD和架构文档实现功能
2. 使用@dev进行代码实现
3. 使用@qa进行代码审查
4. 使用@sm管理开发流程

## 当前项目
这是一个待办事项应用项目，使用React + Node.js技术栈。
```

### 步骤3：使用BMAD Agents

#### 示例1：分片PRD文档
在Cursor中：
```
@po 请帮我分片PRD文档，将docs/prd.md分片到docs/prd/文件夹
```

PO会：
1. 读取 `docs/prd.md`
2. 按章节拆分成小文件
3. 保存到 `docs/prd/` 文件夹

#### 示例2：创建开发故事
```
@sm 请基于PRD创建下一个开发故事
```

SM会：
1. 读取分片后的PRD
2. 分析用户故事
3. 创建具体的开发任务

#### 示例3：实现功能
```
@dev 请实现用户认证功能，包括登录和注册
```

Dev会：
1. 读取架构文档
2. 实现认证逻辑
3. 编写相关测试

#### 示例4：代码审查
```
@qa 请审查这段代码的质量和安全性
```

QA会：
1. 检查代码质量
2. 识别潜在问题
3. 提供改进建议

## 🎯 在VSCode中使用BMAD

### 步骤1：安装BMAD
```bash
npx bmad-method install
```

### 步骤2：创建VSCode配置
创建 `.vscode/settings.json`：

```json
{
  "bmad.enabled": true,
  "bmad.agents": ["pm", "architect", "po", "sm", "dev", "qa"],
  "bmad.docsPath": "./docs",
  "bmad.projectType": "web",
  "bmad.techStack": ["react", "nodejs"]
}
```

### 步骤3：使用GitHub Copilot + BMAD

#### 结合使用示例：
1. **BMAD负责项目管理**：
   ```
   @sm create-next-story
   @dev implement-todo-list
   @qa review-code
   ```

2. **Copilot负责代码生成**：
   - 根据BMAD的指导生成代码
   - 提供代码补全和建议
   - 协助重构和优化

## 🎯 实际工作流程示例

### 场景：开发待办事项应用

#### 1. 项目初始化
```bash
# 创建项目
mkdir todo-app
cd todo-app
npx bmad-method install
```

#### 2. 保存Web UI生成的文档
```bash
mkdir docs
# 将Claude生成的PRD保存为 docs/prd.md
# 将架构文档保存为 docs/architecture.md
```

#### 3. 在Cursor中开始开发
```
@po 请分片PRD文档
```

PO回复：
```
📋 我是产品负责人，现在帮你分片PRD文档。

正在读取 docs/prd.md...
正在创建 docs/prd/ 文件夹...
正在分片文档...

分片完成！创建了以下文件：
- docs/prd/project-overview.md
- docs/prd/functional-requirements.md  
- docs/prd/user-stories.md
- docs/prd/acceptance-criteria.md

现在可以使用 @sm 创建开发故事了。
```

#### 4. 创建开发故事
```
@sm 请创建第一个开发故事
```

SM回复：
```
🚀 我是Scrum Master，基于PRD创建开发故事。

分析用户故事...
创建开发任务...

## 故事1：用户认证功能
**Epic**: 用户管理
**Story**: 作为用户，我希望能够注册和登录账户

**任务**:
1. 创建注册页面组件
2. 实现注册API接口
3. 创建登录页面组件
4. 实现登录API接口
5. 添加表单验证
6. 编写单元测试

**技术栈**: React + Node.js + SQLite
**预估时间**: 8小时

现在可以使用 @dev 开始实现第一个任务。
```

#### 5. 实现功能
```
@dev 请实现注册页面组件
```

Dev回复：
```
💻 我是开发者，现在实现注册页面组件。

基于架构文档，我将创建：
- React函数组件
- TypeScript类型定义
- 表单验证逻辑
- 错误处理

正在生成代码...
```

#### 6. 代码审查
```
@qa 请审查注册组件的代码
```

QA回复：
```
🔍 我是质量保证，正在审查代码。

**代码质量检查**:
✅ 组件结构清晰
✅ TypeScript类型定义完整
✅ 表单验证逻辑正确
✅ 错误处理完善

**建议改进**:
1. 添加加载状态处理
2. 增加密码强度检查
3. 添加单元测试

**安全性检查**:
✅ 输入验证正确
✅ 无XSS漏洞
✅ 密码处理安全

代码质量良好，可以继续开发。
```

## 🎯 关键优势

### 1. 角色专业化
- 每个agent都有专门的知识和技能
- 避免角色混乱和职责不清
- 提供更精准的建议和指导

### 2. 上下文连续性
- 文档在agents之间共享
- 保持项目上下文的一致性
- 避免信息丢失

### 3. 工作流程标准化
- 遵循敏捷开发流程
- 标准化代码审查流程
- 确保质量保证

### 4. 工具集成
- 与现有IDE无缝集成
- 配合GitHub Copilot使用
- 支持版本控制

## 🚀 立即开始

1. **选择IDE**: Cursor (推荐) 或 VSCode
2. **安装BMAD**: `npx bmad-method install`
3. **创建配置文件**: 根据上面的示例
4. **开始使用**: 使用@命令调用agents

你想现在就开始设置吗？我可以帮你：
1. 配置具体的IDE环境
2. 设置BMAD agents
3. 演示完整的工作流程 