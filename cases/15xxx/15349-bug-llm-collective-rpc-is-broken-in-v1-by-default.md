# vllm-project/vllm#15349: [Bug]: LLM.collective_rpc is broken in v1 by default

| 字段 | 值 |
| --- | --- |
| Issue | [#15349](https://github.com/vllm-project/vllm/issues/15349) |
| 状态 | closed |
| 标签 | bug;good first issue |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: LLM.collective_rpc is broken in v1 by default

### Issue 正文摘录

### Your current environment v0.8.1 ### 🐛 Describe the bug see https://github.com/vllm-project/vllm/pull/15324#discussion_r2008716131 for details. because `self.llm_engine.model_executor` is in a different process. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ss. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: pull/15324#discussion_r2008716131 for details. because `self.llm_engine.model_executor` is in a different process. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
