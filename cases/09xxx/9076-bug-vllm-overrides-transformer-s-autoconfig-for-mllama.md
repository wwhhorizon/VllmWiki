# vllm-project/vllm#9076: [Bug]: vllm overrides transformer's Autoconfig for mllama

| 字段 | 值 |
| --- | --- |
| Issue | [#9076](https://github.com/vllm-project/vllm/issues/9076) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm overrides transformer's Autoconfig for mllama

### Issue 正文摘录

### Your current environment vllm 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug This line overrides transformer's autoconfig for mllama, which should be removed https://github.com/vllm-project/vllm/blob/e5dc713c2343b3549b43d6e2764a1036e4052bf8/vllm/transformers_utils/config.py#L41 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm overrides transformer's Autoconfig for mllama bug ### Your current environment vllm 0.6.2 ### Model Input Dumps _No response_ ### 🐛 Describe the bug This line overrides transformer's autoconfig for mllama, w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: L41 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
