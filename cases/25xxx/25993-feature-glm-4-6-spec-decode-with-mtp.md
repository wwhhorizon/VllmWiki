# vllm-project/vllm#25993: [Feature]: GLM-4.6 spec decode with mtp

| 字段 | 值 |
| --- | --- |
| Issue | [#25993](https://github.com/vllm-project/vllm/issues/25993) |
| 状态 | open |
| 标签 | feature request;unstale |
| 评论 | 21; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GLM-4.6 spec decode with mtp

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vllm==0.10.2 vllm serve GLM-4.6 --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":1, "model":"GLM-4.6"}' --tensor-parallel-size 8 gives error: ValueError: Following weights were not initialized from checkpoint: {'model.embed_tokens.weight', 'model.layers.92.shared_head.head.weight' This command works fine with GLM-4.5，but not in GLM-4.6， can you support GLM-4.6？Since it's a strong model. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Feature]: GLM-4.6 spec decode with mtp feature request;unstale ### 🚀 The feature, motivation and pitch vllm==0.10.2 vllm serve GLM-4.6 --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":1, "model":...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: re, motivation and pitch vllm==0.10.2 vllm serve GLM-4.6 --speculative-config '{"method":"deepseek_mtp","num_speculative_tokens":1, "model":"GLM-4.6"}' --tensor-parallel-size 8 gives error: ValueError: Following weights...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
