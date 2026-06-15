# vllm-project/vllm#7619: [Performance]: Block manager v2 has low throughput with prefix caching warmup

| 字段 | 值 |
| --- | --- |
| Issue | [#7619](https://github.com/vllm-project/vllm/issues/7619) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Block manager v2 has low throughput with prefix caching warmup

### Issue 正文摘录

### Report of performance regression Benchmark prefix caching with block manager v1 and v2 on L4: v1: ``` python3 benchmarks/benchmark_prefix_caching.py \ --model neuralmagic/Meta-Llama-3-8B-Instruct-FP8 \ --output-len 200 \ --enable-prefix-caching ------warm up------ cost time 14.582656621932983 ------start generating------ cost time 13.347810745239258 ``` v2: ``` python3 benchmarks/benchmark_prefix_caching.py \ --model neuralmagic/Meta-Llama-3-8B-Instruct-FP8 \ --output-len 200 \ --enable-prefix-caching \ --use-v2-block-manager ------warm up------ cost time 24.060877799987793 ------start generating------ cost time 13.424522161483765 ``` We can see that v2 uses 10 more seconds in the warmup batch, but the latency of the second batch is same as v1. So, if we change the warmup batch size to 1: v1 ``` ------warm up------ cost time 2.6070663928985596 ------start generating------ cost time 13.225520372390747 ``` v2 ``` ------warm up------ cost time 2.612058162689209 ------start generating------ cost time 13.256183385848999 ```

## 现有链接修复摘要

#7822 [Performance][BlockManagerV2] Mark prefix cache block as computed after schedule

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Performance]: Block manager v2 has low throughput with prefix caching warmup performance ### Report of performance regression Benchmark prefix caching with block manager v1 and v2 on L4: v1: ``` python3 benchmarks/benc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ark_prefix_caching.py \ --model neuralmagic/Meta-Llama-3-8B-Instruct-FP8 \ --output-len 200 \ --enable-prefix-caching ------warm up------ cost time 14.582656621932983 ------start generating------ cost time 13.3478107452...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: wdown dtype;memory_layout;shape #7822 [Performance][BlockManagerV2] Mark prefix cache block as computed after schedule Report of performance regression
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Performance]: Block manager v2 has low throughput with prefix caching warmup performance ### Report of performance regression Benchmark prefix caching with block manager v1 and v2 on L4: v1: ``` python3 benchmarks/benc...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 2 on L4: v1: ``` python3 benchmarks/benchmark_prefix_caching.py \ --model neuralmagic/Meta-Llama-3-8B-Instruct-FP8 \ --output-len 200 \ --enable-prefix-caching ------warm up------ cost time 14.582656621932983 ------star...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7822](https://github.com/vllm-project/vllm/pull/7822) | closes_keyword | 0.95 | [Performance][BlockManagerV2] Mark prefix cache block as computed after schedule | Closes #7619 With the investigation in #7619, the root cause of block manager v2 low throughput with prefix caching is that block manager v2 doesn't mark prefix cache hit block |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
