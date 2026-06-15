# vllm-project/vllm#35473: [Feature]: Request vllm support agent skills

| 字段 | 值 |
| --- | --- |
| Issue | [#35473](https://github.com/vllm-project/vllm/issues/35473) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Request vllm support agent skills

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Does vllm have plan to support agent skill in API? If Yes, if the system prompt related is hardcoded or can be configured? https://developers.openai.com/cookbook/examples/skills_in_api/ ```python response = client.responses.create( model="gpt-5.2", tools=[ { "type": "shell", "environment": { "type": "local", "skills": [ {"type": "skill_reference", "skill_id": " "}, {"type": "skill_reference", "skill_id": " ", "version": 2}, ], }, } ], input="Use the configured skills and run locally to summarize today's CSV reports in this repo.", ) ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: kill in API? If Yes, if the system prompt related is hardcoded or can be configured? https://developers.openai.com/cookbook/examples/skills_in_api/ ```python response = client.responses.create( model="gpt-5.2", tools=[...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Request vllm support agent skills feature request;stale ### 🚀 The feature, motivation and pitch Does vllm have plan to support agent skill in API? If Yes, if the system prompt related is hardcoded or can be c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: " "}, {"type": "skill_reference", "skill_id": " ", "version": 2}, ], }, } ], input="Use the configured skills and run locally to summarize today's CSV reports in this repo.", ) ``` ### Alternatives _No response_ ### Add...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
