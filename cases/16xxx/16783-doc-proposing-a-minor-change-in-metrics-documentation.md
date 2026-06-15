# vllm-project/vllm#16783: [Doc]: Proposing a minor change in "Metrics" documentation.

| 字段 | 值 |
| --- | --- |
| Issue | [#16783](https://github.com/vllm-project/vllm/issues/16783) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: Proposing a minor change in "Metrics" documentation.

### Issue 正文摘录

### 📚 The doc issue In the "Metrics" section of the vLLM website, the vllm:generation_tokens_total metric is currently described as: [vllm:generation_tokens_total – Generation Tokens/Sec](https://docs.vllm.ai/en/latest/design/v1/metrics.html#grafana-dashboard) However, since this metric is of the counter type, it may be more accurate to document it as "Generation Tokens" rather than "Generation Tokens/Sec." ### Suggest a potential alternative/fix AS-IS: - `vllm:generation_tokens_total - Generation Tokens/Sec` TO-BE: - `vllm:generation_tokens_total - Generation Tokens` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ns` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: neration_tokens_total – Generation Tokens/Sec](https://docs.vllm.ai/en/latest/design/v1/metrics.html#grafana-dashboard) However, since this metric is of the counter type, it may be more accurate to document it as "Gener...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
