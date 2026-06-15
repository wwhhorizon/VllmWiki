# vllm-project/vllm#25826: [Bug]: AttributeError: 'DPMetadata' object has no attribute 'cu_tokens_across_dp_cpu'

| 字段 | 值 |
| --- | --- |
| Issue | [#25826](https://github.com/vllm-project/vllm/issues/25826) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'DPMetadata' object has no attribute 'cu_tokens_across_dp_cpu'

### Issue 正文摘录

### Your current environment https://github.com/vllm-project/vllm-ascend/actions/runs/18071117010/job/51421019918 ### 🐛 Describe the bug AttributeError: 'DPMetadata' object has no attribute 'cu_tokens_across_dp_cpu' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pu' ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug]: AttributeError: 'DPMetadata' object has no attribute 'cu_tokens_across_dp_cpu' bug ### Your current environment https://github.com/vllm-project/vllm-ascend/actions/runs/18071117010/job/51421019918 ### 🐛 Describe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
