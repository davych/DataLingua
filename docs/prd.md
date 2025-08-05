## mvp - phase2
- 用户模块
- 创建application
- 创建sql连接，同步schema
- 编辑schema，补充prompt注释
- 预览对话
> 计划fastify as backend framework, admin portal- antd
> dia portal - tailwindcss


## mvp - phase3
每个application有固定的nlu agent 和sqlcoder agent。
不管是nlu还是sqlcoder，都可以采用去改变大模型一小片区域的方式进行微调- PEFT -> LoRA。
开放feedback收集，收集到的数据作为 单个application的微调训练数据。
反复增强针对单个application的nlu的llm和sqlcoder llm的能力。