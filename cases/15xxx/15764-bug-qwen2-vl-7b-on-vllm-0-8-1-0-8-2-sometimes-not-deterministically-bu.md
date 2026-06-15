# vllm-project/vllm#15764: [Bug]: qwen2-vl 7b, on vllm 0.8.1 & 0.8.2, sometimes (not deterministically but depends on data) I got: ValueError: Attempted to assign 702 = 702 multimodal tokens to 703 placeholders

| 字段 | 值 |
| --- | --- |
| Issue | [#15764](https://github.com/vllm-project/vllm/issues/15764) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 29; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen2-vl 7b, on vllm 0.8.1 & 0.8.2, sometimes (not deterministically but depends on data) I got: ValueError: Attempted to assign 702 = 702 multimodal tokens to 703 placeholders

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have: enforce_eager: false enable_chunked_prefill: false But still got the "ValueError" thing. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: qwen2-vl 7b, on vllm 0.8.1 & 0.8.2, sometimes (not deterministically but depends on data) I got: ValueError: Attempted to assign 702 = 702 multimodal tokens to 703 placeholders bug ### Your current environment ##...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: qwen2-vl 7b, on vllm 0.8.1 & 0.8.2, sometimes (not deterministically but depends on data) I got: ValueError: Attempted to assign 702 = 702 multimodal tokens to 703 placeholders bug ### Your current environment ##...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: qwen2-vl 7b, on vllm 0.8.1 & 0.8.2, sometimes (not deterministically but depends on data) I got: ValueError: Attempted to assign 702 = 702 multimodal tokens to 703 placeholders bug ### Your current environment ##...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ng. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: nt environment ### 🐛 Describe the bug I have: enforce_eager: false enable_chunked_prefill: false But still got the "ValueError" thing. ### Before submitting a new issue... - [x] Make sure you already searched for releva...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
