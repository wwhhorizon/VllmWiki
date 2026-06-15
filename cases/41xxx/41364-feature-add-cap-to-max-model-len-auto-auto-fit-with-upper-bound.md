# vllm-project/vllm#41364: [Feature]: Add cap to --max-model-len auto (auto-fit with upper bound)

| 字段 | 值 |
| --- | --- |
| Issue | [#41364](https://github.com/vllm-project/vllm/issues/41364) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Add cap to --max-model-len auto (auto-fit with upper bound)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch vLLM already supports `--max-model-len auto`, which is very useful because vLLM can determine the maximum context length that fits the current memory budget after loading the model and profiling memory usage. I would like to request combining this `auto` behavior with a user-defined upper bound. Example: ``` vllm serve \ --max-model-len auto \ --max-model-len-cap 131072 ``` Semantics: _fitted_len_ = maximum context length vLLM can fit in the configured memory budget _effective_max_model_len_ = min(fitted_len, max_model_len_cap) ### Motivation auto is great when the goal is “use as much context as possible”. However, on shared or restricted hardware, this can be undesirable. If a model supports a very large context length, e.g. 1M tokens, auto may consume the available vLLM memory budget for KV cache, leaving less room for other local applications or parallel serving processes. Simply reducing --gpu-memory-utilization or setting a fixed memory budget does not fully solve this. The useful context length depends on model weight size, architecture, KV cache dtype, parallelism, and other runtime details. A small model can consume the same memory...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 4: h, e.g. 1M tokens, auto may consume the available vLLM memory budget for KV cache, leaving less room for other local applications or parallel serving processes. Simply reducing --gpu-memory-utilization or setting a fixe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ully solve this. The useful context length depends on model weight size, architecture, KV cache dtype, parallelism, and other runtime details. A small model can consume the same memory budget as a larger model simply by...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Add cap to --max-model-len auto (auto-fit with upper bound) feature request ### 🚀 The feature, motivation and pitch vLLM already supports `--max-model-len auto`, which is very useful because vLLM can determin...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t length that fits the current memory budget after loading the model and profiling memory usage. I would like to request combining this `auto` behavior with a user-defined upper bound. Example: ``` vllm serve \ --max-mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for other local applications or parallel serving processes. Simply reducing --gpu-memory-utilization or setting a fixed memory budget does not fully solve this. The useful context length depends on model weight size, ar...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
