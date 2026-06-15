# vllm-project/vllm#18112: [Bug]: shanearora/OLMo-7B-1124-h model not found

| 字段 | 值 |
| --- | --- |
| Issue | [#18112](https://github.com/vllm-project/vllm/issues/18112) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: shanearora/OLMo-7B-1124-h model not found

### Issue 正文摘录

### Your current environment https://github.com/vllm-project/vllm/blob/9a2a6357de8aa112692dab93f7d40b2d7e75ac67/tests/models/registry.py#L208 this model not found in huggingface.co, this is should fix? @2015aroras If need fix, please tell me, i will submit a pr. ### 🐛 Describe the bug no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: shanearora/OLMo-7B-1124-h model not found bug ### Your current environment https://github.com/vllm-project/vllm/blob/9a2a6357de8aa112692dab93f7d40b2d7e75ac67/tests/models/registry.py#L208 this model not found in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: no ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: thub.com/vllm-project/vllm/blob/9a2a6357de8aa112692dab93f7d40b2d7e75ac67/tests/models/registry.py#L208 this model not found in huggingface.co, this is should fix? @2015aroras If need fix, please tell me, i will submit a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
