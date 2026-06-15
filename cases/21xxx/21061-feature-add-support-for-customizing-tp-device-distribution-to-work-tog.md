# vllm-project/vllm#21061: [Feature]: Add support for customizing TP device distribution to work together with VLLM_PP_LAYER_PARTITION

| 字段 | 值 |
| --- | --- |
| Issue | [#21061](https://github.com/vllm-project/vllm/issues/21061) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add support for customizing TP device distribution to work together with VLLM_PP_LAYER_PARTITION

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I have a device that has GPUs with uneven memory, and it's good to know that there is an env var "VLLM_PP_LAYER_PARTITION" to help aligning memory in full pipeline parallel situation. However that makes TP x PP impossible without memory waste. Is it possible to add another env var, making it possible to set TP groups manually? ### Alternatives It's also great if vllm could recognize uneven GPU setup and align TP groups correct automatically. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: evice distribution to work together with VLLM_PP_LAYER_PARTITION feature request ### 🚀 The feature, motivation and pitch I have a device that has GPUs with uneven memory, and it's good to know that there is an env var "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
