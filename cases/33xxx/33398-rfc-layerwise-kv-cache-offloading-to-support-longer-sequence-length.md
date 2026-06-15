# vllm-project/vllm#33398: [RFC]: Layerwise KV cache offloading to support longer sequence length

| 字段 | 值 |
| --- | --- |
| Issue | [#33398](https://github.com/vllm-project/vllm/issues/33398) |
| 状态 | open |
| 标签 | RFC;unstale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Layerwise KV cache offloading to support longer sequence length

### Issue 正文摘录

## Motivation. Currently, in vLLM v1 there are already some KV cache offload approaches such as `LMCacheConnector` proposed by PR ([#16625](https://github.com/vllm-project/vllm/pull/16625)) and `OffloadingConnector` proposed by RFC ([#19854](https://github.com/vllm-project/vllm/issues/19854)), which mainly aim to increase prefix cache hit rate by offloading KV cache of finished requests to CPU and onload them when cache hit, thus reduce ttft and improve throughput. In long sequence inference scenario, the KV cache size has become one of the inference bottlenecks. Refer to existing KV cache offload approaches, we propose another layerwise KV cache offload approach, aims to reduce GPU memory usage of KV cache, thus improve the maximum model context length (max-model-len) we can support. The main idea of this approach is: 1. **Layerwise KV cache offload:** Offload KV cache of part of the layers to cpu, reduce GPU memory usage and support longer sequence. For each layer, we need to onload its KV cache before its forward pass, and offload its KV cache after its forward pass to make room for other layers behind. 2. **Asynchronous pipeline onload/offload:** Since we don't want KV cache o...

## 候选优化模式

- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 6: [RFC]: Layerwise KV cache offloading to support longer sequence length RFC;unstale ## Motivation. Currently, in vLLM v1 there are already some KV cache offload approaches such as `LMCacheConnector` proposed by PR ([#166...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: h, aims to reduce GPU memory usage of KV cache, thus improve the maximum model context length (max-model-len) we can support. The main idea of this approach is: 1. **Layerwise KV cache offload:** Offload KV cache of par...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ests to CPU and onload them when cache hit, thus reduce ttft and improve throughput. In long sequence inference scenario, the KV cache size has become one of the inference bottlenecks. Refer to existing KV cache offload...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: timization, we also notice that this KV cache offloading approach is especially efficient for **sparse attention** based model: Take [DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) as an example, altho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: layers, we are able to minimize the additional overhead of KV cache transmission. Inspired by [SparseServe](https://arxiv.org/pdf/2509.24626), an LLM serving system designed for sparse attention optimization, we also no...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
