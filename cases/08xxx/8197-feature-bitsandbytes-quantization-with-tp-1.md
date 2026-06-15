# vllm-project/vllm#8197: [Feature]: BitsandBytes quantization with TP>1

| 字段 | 值 |
| --- | --- |
| Issue | [#8197](https://github.com/vllm-project/vllm/issues/8197) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: BitsandBytes quantization with TP>1

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Any QLoRA adapters trained on large checkpoints (e.g., 70B) are unusable as we cannot use TP>1 to shard the model over multiple GPUs. Therefore, resolving this would enable models that were trained with quantization, rather than having to rely on GPTQ and AWQ, which are applied post-hoc after training. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: BitsandBytes quantization with TP>1 feature request;stale ### 🚀 The feature, motivation and pitch Any QLoRA adapters trained on large checkpoints (e.g., 70B) are unusable as we cannot use TP>1 to shard the mo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: BitsandBytes quantization with TP>1 feature request;stale ### 🚀 The feature, motivation and pitch Any QLoRA adapters trained on large checkpoints (e.g., 70B) are unusable as we cannot use TP>1 to shard the mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: checkpoints (e.g., 70B) are unusable as we cannot use TP>1 to shard the model over multiple GPUs. Therefore, resolving this would enable models that were trained with quantization, rather than having to rely on GPTQ and...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
