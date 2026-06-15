# vllm-project/vllm#43400: [Usage]: vLLM 启动后 69GB 是总占用，其中 62.18GiB 是 KV cache 预留池。 单个请求只用了约 50MiB KV cache。 我是否可以理解为：62.18GiB 大部分是预分配但当前空闲的 blocks，而当前请求活跃显存约等于 non_kv_cache_memory + request KV cache？

| 字段 | 值 |
| --- | --- |
| Issue | [#43400](https://github.com/vllm-project/vllm/issues/43400) |
| 状态 | open |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM 启动后 69GB 是总占用，其中 62.18GiB 是 KV cache 预留池。 单个请求只用了约 50MiB KV cache。 我是否可以理解为：62.18GiB 大部分是预分配但当前空闲的 blocks，而当前请求活跃显存约等于 non_kv_cache_memory + request KV cache？

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: vLLM 启动后 69GB 是总占用，其中 62.18GiB 是 KV cache 预留池。 单个请求只用了约 50MiB KV cache。 我是否可以理解为：62.18GiB 大部分是预分配但当前空闲的 blocks，而当前请求活跃显存约等于 non_kv_cache_memory + request KV cache？ usage ### Your current environment ```text The...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 是 KV cache 预留池。 单个请求只用了约 50MiB KV cache。 我是否可以理解为：62.18GiB 大部分是预分配但当前空闲的 blocks，而当前请求活跃显存约等于 non_kv_cache_memory + request KV cache？ usage ### Your current environment ```text The output of `python collect_env.py` ``` #...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
