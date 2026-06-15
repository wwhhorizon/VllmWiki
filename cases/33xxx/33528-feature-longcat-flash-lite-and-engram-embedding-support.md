# vllm-project/vllm#33528: [Feature]: LongCat-Flash-Lite and "Engram" embedding support

| 字段 | 值 |
| --- | --- |
| Issue | [#33528](https://github.com/vllm-project/vllm/issues/33528) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: LongCat-Flash-Lite and "Engram" embedding support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch LongCat-Flash-Lite did something similar to DeepSeek, but applies it to token embedding rather than attention layers, and that these embedding layers can fit onto disk instead of needing to bloat up VRAM (?) https://huggingface.co/meituan-longcat/LongCat-Flash-Lite https://github.com/deepseek-ai/Engram/ ### Alternatives Both llama.cpp and vLLM don't have that much support yet I think? ### Additional context https://github.com/sgl-project/sglang/pull/17838 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: layers can fit onto disk instead of needing to bloat up VRAM (?) https://huggingface.co/meituan-longcat/LongCat-Flash-Lite https://github.com/deepseek-ai/Engram/ ### Alternatives Both llama.cpp and vLLM don't have that...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: LongCat-Flash-Lite and "Engram" embedding support feature request;unstale ### 🚀 The feature, motivation and pitch LongCat-Flash-Lite did something similar to DeepSeek, but applies it to token embedding rather...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 838 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
