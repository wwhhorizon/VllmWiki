# vllm-project/vllm#30801: [Bug]: distilbert/distilgpt2 with graph_mode on ROCm platform generates garbage output

| 字段 | 值 |
| --- | --- |
| Issue | [#30801](https://github.com/vllm-project/vllm/issues/30801) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: distilbert/distilgpt2 with graph_mode on ROCm platform generates garbage output

### Issue 正文摘录

### Your current environment Enable graph_mode for model distilbert/distilgpt2 on ROCm platform will generate garbage output. ### 🐛 Describe the bug For model distilbert/distilgpt2, if graph_mode (enforce_eager=False) is enabled, vLLM will generate garbage output like "!!!!!!!!!!!!!!!" no matter what the prompt is. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: distilbert/distilgpt2 with graph_mode on ROCm platform generates garbage output bug;rocm ### Your current environment Enable graph_mode for model distilbert/distilgpt2 on ROCm platform will generate garbage outpu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: the bug For model distilbert/distilgpt2, if graph_mode (enforce_eager=False) is enabled, vLLM will generate garbage output like "!!!!!!!!!!!!!!!" no matter what the prompt is. ### Before submitting a new issue... - [x]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: bage output bug;rocm ### Your current environment Enable graph_mode for model distilbert/distilgpt2 on ROCm platform will generate garbage output. ### 🐛 Describe the bug For model distilbert/distilgpt2, if graph_mode (e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
