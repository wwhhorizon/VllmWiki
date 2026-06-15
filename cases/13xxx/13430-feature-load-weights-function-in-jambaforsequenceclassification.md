# vllm-project/vllm#13430: [Feature]:  load_weights function in JambaForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#13430](https://github.com/vllm-project/vllm/issues/13430) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  load_weights function in JambaForSequenceClassification

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Working on my first contribution, and wanted to start with something light. I was reading #10860 which had a TODO for explicitly casting weights to float 32, but at the moment it just casts `self.scores` to float, and does not affect weights. I would like to submit a little 2 liner to have weights cast explicitly to float32 and score to float32. If I am misunderstanding something, please let me know. As far as I am aware, there are no open PRs or issues addressing this small change. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: w. As far as I am aware, there are no open PRs or issues addressing this small change. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ature]: load_weights function in JambaForSequenceClassification feature request;stale ### 🚀 The feature, motivation and pitch Working on my first contribution, and wanted to start with something light. I was reading #10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: art with something light. I was reading #10860 which had a TODO for explicitly casting weights to float 32, but at the moment it just casts `self.scores` to float, and does not affect weights. I would like to submit a l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: would like to submit a little 2 liner to have weights cast explicitly to float32 and score to float32. If I am misunderstanding something, please let me know. As far as I am aware, there are no open PRs or issues addres...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
