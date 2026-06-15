# vllm-project/vllm#9790: [Usage]: prefix caching support for multimodal models 

| 字段 | 值 |
| --- | --- |
| Issue | [#9790](https://github.com/vllm-project/vllm/issues/9790) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: prefix caching support for multimodal models 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi I want to perform offline batch inference with prefix caching to accelerate inference. But It looks like it is not supported yet when I initialize LLM with enable_prefix_caching=True `--enable-prefix-caching is currently not supported for multimodal models and has been disabled. ` Would it be supported in near future and/or can I get some reference on how to implement it myself? Currently I'm trying to make batch inference with prefix cache work using huggingface transformers, but it looks like I can't get padding and/or cache position and/or attention_mask right so I get gibberish outputs. ref: https://docs.vllm.ai/en/stable/getting_started/examples/offline_inference_with_prefix.html https://docs.vllm.ai/en/stable/getting_started/examples/offline_inference_vision_language.html https://github.com/huggingface/transformers/issues/34232#issuecomment-2425907897 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: prefix caching support for multimodal models usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi I want to perform offline batch infe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 897 ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: o implement it myself? Currently I'm trying to make batch inference with prefix cache work using huggingface transformers, but it looks like I can't get padding and/or cache position and/or attention_mask right so I get...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: prefix caching support for multimodal models usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Hi I want to perform offline batch infe...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
