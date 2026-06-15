# vllm-project/vllm#15268: vector search

| 字段 | 值 |
| --- | --- |
| Issue | [#15268](https://github.com/vllm-project/vllm/issues/15268) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vector search

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Are there any Python libraries for knowledge base retrieval? I want to search for relevant information in a knowledge base based on user input. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: vation and pitch Are there any Python libraries for knowledge base retrieval? I want to search for relevant information in a knowledge base based on user input. ### Alternatives _No response_ ### Additional context _No...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: vector search feature request ### 🚀 The feature, motivation and pitch Are there any Python libraries for knowledge base retrieval? I want to search for relevant information in a knowledge base based on user input. ### A...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: libraries for knowledge base retrieval? I want to search for relevant information in a knowledge base based on user input. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vector search feature request ### 🚀 The feature, motivation and pitch Are there any Python libraries for knowledge base retrieval? I want to search for relevant information in a knowledge base based on user input. ### A...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
