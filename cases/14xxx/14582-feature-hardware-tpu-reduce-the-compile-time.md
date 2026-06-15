# vllm-project/vllm#14582: [Feature][Hardware][TPU]:Reduce the compile time

| 字段 | 值 |
| --- | --- |
| Issue | [#14582](https://github.com/vllm-project/vllm/issues/14582) |
| 状态 | closed |
| 标签 | feature request;tpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Hardware][TPU]:Reduce the compile time

### Issue 正文摘录

### 🚀 The feature, motivation and pitch After the fix of https://github.com/vllm-project/vllm/pull/14310, We have num_token_bucket compilations for the main model and num_token_bucket x num_reqs_bucket for the logits processor. We can make some improvement on this, as the num_token_bucket x num_reqs_bucket only happens on hidden_states[logits_indices], where we select part of the hidden states. Therefore, we can partition the graph to 3 parts: main model: num_token_bucket hidden_states[logits_indices]: num_token_bucket x num_reqs_bucket logits: num_reqs_bucket ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature][Hardware][TPU]:Reduce the compile time feature request;tpu ### 🚀 The feature, motivation and pitch After the fix of https://github.com/vllm-project/vllm/pull/14310, We have num_token_bucket compilations for th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ect/vllm/pull/14310, We have num_token_bucket compilations for the main model and num_token_bucket x num_reqs_bucket for the logits processor. We can make some improvement on this, as the num_token_bucket x num_reqs_buc...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][Hardware][TPU]:Reduce the compile time feature request;tpu ### 🚀 The feature, motivation and pitch After the fix of https://github.com/vllm-project/vllm/pull/14310, We have num_token_bucket compilations for th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
