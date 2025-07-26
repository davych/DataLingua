# 智能自然语言数据可视化平台 Product Requirements Document (PRD)

## Goals and Background Context

### Goals
- 用户可用自然语言查询数据库并获得可视化结果
- 降低数据分析门槛，提升非技术用户体验
- 支持多种主流数据库和常见图表类型
- 提供智能图表推荐，提升数据洞察效率

### Background Context
本项目基于 Project Brief，旨在解决非技术用户难以直接分析数据库数据的问题。通过集成 LLM，将自然语言转为 SQL 并自动执行，结合智能图表推荐和可视化，极大提升数据分析的易用性和智能化水平。

### Change Log
| Date       | Version | Description         | Author |
|------------|---------|---------------------|--------|
| 2025-07-26 | 1.0     | 初始版本            | pm     |

## Requirements

### Functional
1. FR1: 用户可输入自然语言查询，系统自动转为 SQL 并执行
2. FR2: 查询结果以结构化数据返回
3. FR3: 系统自动推理并推荐适配的图表类型
4. FR4: 前端可渲染多种主流可视化图表，支持切换
5. FR5: 支持结果导出

### Non Functional
1. NFR1: 响应时间<3秒
2. NFR2: 数据安全与权限合规
3. NFR3: 支持主流浏览器和终端

## User Interface Design Goals

### Overall UX Vision
简洁直观，零学习成本，用户输入自然语言即可获得可视化结果。

### Key Interaction Paradigms
- 输入框+一键查询
- 图表自动切换与手动选择
- 结果导出与分享

### Core Screens and Views
- 登录/注册页
- 查询主界面（输入+结果展示）
- 图表切换与配置面板

### Accessibility: WCAG AA
### Branding: 企业风格，简洁现代
### Target Device and Platforms: Web Responsive

## Technical Assumptions
- Repository Structure: Monorepo
- Service Architecture: 前后端分离，RESTful API
- Testing Requirements: Unit + Integration
- Additional Technical Assumptions and Requests: 前端 React + ECharts，后端 Python/Node.js + LLM API，数据库 MySQL/PostgreSQL

## Epic List
1. Epic 1: 项目基础与核心功能 - 项目初始化、用户认证、自然语言转SQL、基础图表渲染
2. Epic 2: 智能图表推荐与多样化可视化 - 图表类型推理、支持多种图表、交互优化
3. Epic 3: 数据安全与权限管理 - 权限体系、数据合规、日志与监控
4. Epic 4: 用户体验与扩展 - 导出、分享、移动端适配、后续功能扩展

---
如需详细故事拆解或补充，请随时告知。
