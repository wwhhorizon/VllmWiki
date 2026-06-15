# vllm-project/vllm#18289: [Feature]: Access and combine raw logits at inference time

| 字段 | 值 |
| --- | --- |
| Issue | [#18289](https://github.com/vllm-project/vllm/issues/18289) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Access and combine raw logits at inference time

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We are working on decoding algorithms that combines the raw logits of two models and then run inference based on the combined logits. More specifically, we'd like to load two models (potentially on different servers/processes/GPUs) using vllm, and then at every inference step, extract the raw logits of both models, combine them using a self-defined function and perform (greedy/beam-search) inference based on the combined logits. ### Alternatives An alternative solution is to extend a logits processor to include another model. Model 1 will use this logit processor which takes in model 2 and prompt as arguments, run decoding to get the logits from Model 2 and combine them with Model 1. ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Access and combine raw logits at inference time feature request;stale ### 🚀 The feature, motivation and pitch We are working on decoding algorithms that combines the raw logits of two models and then run infe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: two models and then run inference based on the combined logits. More specifically, we'd like to load two models (potentially on different servers/processes/GPUs) using vllm, and then at every inference step, extract the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s, combine them using a self-defined function and perform (greedy/beam-search) inference based on the combined logits. ### Alternatives An alternative solution is to extend a logits processor to include another model. M...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e are working on decoding algorithms that combines the raw logits of two models and then run inference based on the combined logits. More specifically, we'd like to load two models (potentially on different servers/proc...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
