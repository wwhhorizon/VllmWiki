# vllm-project/vllm#33302: [Usage]: What would happen if the offloading KV cache size is larger than config the max_local_cpu_size ?

| 字段 | 值 |
| --- | --- |
| Issue | [#33302](https://github.com/vllm-project/vllm/issues/33302) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What would happen if the offloading KV cache size is larger than config the max_local_cpu_size ?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Usage]: What would happen if the offloading KV cache size is larger than config the max_local_cpu_size ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Usage]: What would happen if the offloading KV cache size is larger than config the max_local_cpu_size ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ading KV cache size is larger than config the max_local_cpu_size ? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
