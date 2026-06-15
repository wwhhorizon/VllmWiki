# vllm-project/vllm#18121: [Usage]: Set the kv cache size

| 字段 | 值 |
| --- | --- |
| Issue | [#18121](https://github.com/vllm-project/vllm/issues/18121) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | memory |
| Operator 关键词 | cache |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Set the kv cache size

### Issue 正文摘录

### Your current environment ``` vLLM served through docker on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to explicitly set its size or limit memory usage for the KV cache? I couldn't find this in the documentation. The flag --gpu-memory-utilization doesn't address this since if the percentage is too low, vllm will trigger an error. Thanks! ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: e size usage;stale ### Your current environment ``` vLLM served through docker on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to explicitly set its size...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge;stale ### Your current environment ``` vLLM served through docker on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to explicitly set its size or limit...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Set the kv cache size usage;stale ### Your current environment ``` vLLM served through docker on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to explicitly set its size or limit memory usage for the KV cache? I couldn't find this in the documentat...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Set the kv cache size usage;stale ### Your current environment ``` vLLM served through docker on rtx a6000 ``` ### How would you like to use vllm Hi, I'm trying to configure the KV cache size. Is there a way to...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
