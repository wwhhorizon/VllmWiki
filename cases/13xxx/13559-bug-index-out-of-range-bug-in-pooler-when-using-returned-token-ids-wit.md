# vllm-project/vllm#13559: [Bug]: Index Out of Range Bug in Pooler when Using returned_token_ids with hidden_states

| 字段 | 值 |
| --- | --- |
| Issue | [#13559](https://github.com/vllm-project/vllm/issues/13559) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Index Out of Range Bug in Pooler when Using returned_token_ids with hidden_states

### Issue 正文摘录

### Your current environment pip install vllm ### 🐛 Describe the bug There is a bug in the StepPool class, specifically in the extract_states method. The current implementation attempts to index the hidden_states tensor with returned_token_ids (e.g., hidden_states[: , returned_token_ids]), but this approach is incorrect. The hidden_states tensor does not have a dimension corresponding to the vocabulary size (vocab_size), and therefore, using returned_token_ids to index it will result in an "index out of range" error if the returned_token_ids exceed the actual size of the hidden_states tensor. This issue violates the logic of indexing, as returned_token_ids should correspond to valid positions within the hidden_states tensor, which does not have the same dimensionality as the token IDs. The method should ensure that the returned_token_ids are within the bounds of the hidden_states tensor before performing the indexing. code: how to trigger this bug: Notice that 12902 exceeds hidden_size:4096, which would cause index out of range bug. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: token_ids with hidden_states bug;stale ### Your current environment pip install vllm ### 🐛 Describe the bug There is a bug in the StepPool class, specifically in the extract_states method. The current implementation att...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ug. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Range Bug in Pooler when Using returned_token_ids with hidden_states bug;stale ### Your current environment pip install vllm ### 🐛 Describe the bug There is a bug in the StepPool class, specifically in the extract_state...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
