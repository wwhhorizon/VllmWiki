# vllm-project/vllm#35730: [Feature]: Load Mistral format LoRA when `--load-format=mistral` and `--enable-lora`

| 字段 | 值 |
| --- | --- |
| Issue | [#35730](https://github.com/vllm-project/vllm/issues/35730) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Load Mistral format LoRA when `--load-format=mistral` and `--enable-lora`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The state dict of Mistral format LoRA contains keys like the following. So it uses e.g. `wk` instead of `k_proj`. It would be convenient to be able to load these directly instead of having to first rename the keys in the state dict and then load. ``` layers.7.attention.wk.lora_A.weight layers.7.attention.wk.lora_B.weight layers.7.attention.wo.lora_A.weight layers.7.attention.wo.lora_B.weight layers.7.attention.wq.lora_A.weight layers.7.attention.wq.lora_B.weight layers.7.attention.wv.lora_A.weight layers.7.attention.wv.lora_B.weight layers.7.feed_forward.w1.lora_A.weight layers.7.feed_forward.w1.lora_B.weight layers.7.feed_forward.w2.lora_A.weight layers.7.feed_forward.w2.lora_B.weight layers.7.feed_forward.w3.lora_A.weight layers.7.feed_forward.w3.lora_B.weight ``` ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ral format LoRA when `--load-format=mistral` and `--enable-lora` feature request;stale ### 🚀 The feature, motivation and pitch The state dict of Mistral format LoRA contains keys like the following. So it uses e.g. `wk`...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: Load Mistral format LoRA when `--load-format=mistral` and `--enable-lora` feature request;stale ### 🚀 The feature, motivation and pitch The state dict of Mistral format LoRA contains keys like the following....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
