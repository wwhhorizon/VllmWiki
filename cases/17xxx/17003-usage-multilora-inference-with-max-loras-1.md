# vllm-project/vllm#17003: [Usage]: multilora_inference with max_loras>1

| 字段 | 值 |
| --- | --- |
| Issue | [#17003](https://github.com/vllm-project/vllm/issues/17003) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: multilora_inference with max_loras>1

### Issue 正文摘录

### Your current environment ```text vLLM on H100 using Llama2 7B. ``` ### How would you like to use vllm I would like to know how to come up with the max concurrency (aka batch_size) we can achieve assuming each of the request in the batch has it's own LoRA adapters, can we get some back of envelop memory compute for batch_size 16 for Llama 7B on H100 GPU? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: th max_loras>1 usage;stale ### Your current environment ```text vLLM on H100 using Llama2 7B. ``` ### How would you like to use vllm I would like to know how to come up with the max concurrency (aka batch_size) we can a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: multilora_inference with max_loras>1 usage;stale ### Your current environment ```text vLLM on H100 using Llama2 7B. ``` ### How would you like to use vllm I would like to know how to come up with the max concur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s>1 usage;stale ### Your current environment ```text vLLM on H100 using Llama2 7B. ``` ### How would you like to use vllm I would like to know how to come up with the max concurrency (aka batch_size) we can achieve assu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
