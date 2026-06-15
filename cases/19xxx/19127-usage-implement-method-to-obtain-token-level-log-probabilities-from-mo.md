# vllm-project/vllm#19127: [Usage]: Implement Method to Obtain Token-Level Log Probabilities from Models with Different Weights for KL Divergence Calculation

| 字段 | 值 |
| --- | --- |
| Issue | [#19127](https://github.com/vllm-project/vllm/issues/19127) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Implement Method to Obtain Token-Level Log Probabilities from Models with Different Weights for KL Divergence Calculation

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I need to create a sample for evaluation to obtain the probabilities of the same text under different strategies. Specifically, I have two model weights, and I want to calculate the KL divergence using this formula: negative_approx_kl = log_prob - old_log_prob ppo_kl = torch.mean(-negative_approx_kl) Where: log_prob: Log probability of the text sequence using the current/updated model weights. old_log_prob: Log probability of the text sequence using a previous/baseline set of model weights. how to get log_prob? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ` ``` ### How would you like to use vllm I need to create a sample for evaluation to obtain the probabilities of the same text under different strategies. Specifically, I have two model weights, and I want to calculate...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Token-Level Log Probabilities from Models with Different Weights for KL Divergence Calculation usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: obtain the probabilities of the same text under different strategies. Specifically, I have two model weights, and I want to calculate the KL divergence using this formula: negative_approx_kl = log_prob - old_log_prob pp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ob? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Implement Method to Obtain Token-Level Log Probabilities from Models with Different Weights for KL Divergence Calculation usage;stale ### Your current environment ```text The output of `python collect_env.py` `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
