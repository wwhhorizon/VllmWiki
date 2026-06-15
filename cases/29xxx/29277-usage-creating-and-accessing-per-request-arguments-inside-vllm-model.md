# vllm-project/vllm#29277: [Usage]: Creating and accessing per request arguments inside vLLM model

| 字段 | 值 |
| --- | --- |
| Issue | [#29277](https://github.com/vllm-project/vllm/issues/29277) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Creating and accessing per request arguments inside vLLM model

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to implement token compression techniques on the output embeddings of Qwen-2.5VL which would occur dynamically as the number of requests change. Is there anyway to implement this in vLLM? I see that SamplingParams seem to be the only way to use per request custom arguments but I don’t believe it can be accessed within the model code directly? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Creating and accessing per request arguments inside vLLM model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to implement t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Creating and accessing per request arguments inside vLLM model usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to implement t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
