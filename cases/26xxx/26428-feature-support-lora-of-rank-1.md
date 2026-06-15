# vllm-project/vllm#26428: [Feature]: Support LoRA of rank 1

| 字段 | 值 |
| --- | --- |
| Issue | [#26428](https://github.com/vllm-project/vllm/issues/26428) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Support LoRA of rank 1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm working on finetuning / RL / GRPO, and I'm working with VLLM as my rollout engine. At the moment, I only support for LoRA of [rank 8, 16, etc.](https://github.com/vllm-project/vllm/blob/127c8b782a63010e56bc33d45e87baf3a6415568/vllm/config/lora.py#L106). I'm trying to reproduce the [LoRA without Regret](https://thinkingmachines.ai/blog/lora/) blog post, but this validation, and I presume support, is a bit in the way. Is this something vLLM would consider supporting? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: a63010e56bc33d45e87baf3a6415568/vllm/config/lora.py#L106). I'm trying to reproduce the [LoRA without Regret](https://thinkingmachines.ai/blog/lora/) blog post, but this validation, and I presume support, is a bit in the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: com/vllm-project/vllm/blob/127c8b782a63010e56bc33d45e87baf3a6415568/vllm/config/lora.py#L106). I'm trying to reproduce the [LoRA without Regret](https://thinkingmachines.ai/blog/lora/) blog post, but this validation, an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: Support LoRA of rank 1 feature request ### 🚀 The feature, motivation and pitch I'm working on finetuning / RL / GRPO, and I'm working with VLLM as my rollout engine. At the moment, I only support for LoRA of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
