# vllm-project/vllm#5167: [Performance]: What can we learn from OctoAI

| 字段 | 值 |
| --- | --- |
| Issue | [#5167](https://github.com/vllm-project/vllm/issues/5167) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cache;cuda;fp8;kernel |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: What can we learn from OctoAI

### Issue 正文摘录

OctoAI use vLLM as a benchmark to demonstrate how fast they are https://octo.ai/blog/acceleration-is-all-you-need-techniques-powering-octostacks-10x-performance-boost: | Single User Throughput | Multi-user Throughput | Inter-Token Latency | |--------|--------|--------| | ![](https://www.datocms-assets.com/45680/1714684979-octostack-single-user-throughput-compared-to-vllm-chart.png) | ![](https://www.datocms-assets.com/45680/1714760904-octostack-multi-user-throughput-compared-to-vllm-chart-4.png) | ![](https://www.datocms-assets.com/45680/1714682977-octostack-compared-to-vllm-inter-token-latency-chart.png) | Their main optimisations appear to be: - FP8 quantisation of the model (currently we only support KV cache) - The `CustomAllReduce` kernel from Nvidia TRT LLM - CUDA graphs - Speculative decoding (which we have thanks to @cadedaniel!) - Dynamic SplitFuse (A.K.A. Chunked Prefill, which we have thanks to @rkooo567!) My question is, **what do we need to do to reach performance parity?** Some clear things are: - Make all of these features compatible with eachother - See what can be learned from the TRT LLM `CustomAllReduce` - Support executing models in FP8 Notable issues: - https:...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ter-token-latency-chart.png) | Their main optimisations appear to be: - FP8 quantisation of the model (currently we only support KV cache) - The `CustomAllReduce` kernel from Nvidia TRT LLM - CUDA graphs - Speculative d...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ormance]: What can we learn from OctoAI performance OctoAI use vLLM as a benchmark to demonstrate how fast they are https://octo.ai/blog/acceleration-is-all-you-need-techniques-powering-octostacks-10x-performance-boost:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ache) - The `CustomAllReduce` kernel from Nvidia TRT LLM - CUDA graphs - Speculative decoding (which we have thanks to @cadedaniel!) - Dynamic SplitFuse (A.K.A. Chunked Prefill, which we have thanks to @rkooo567!) My qu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: y support KV cache) - The `CustomAllReduce` kernel from Nvidia TRT LLM - CUDA graphs - Speculative decoding (which we have thanks to @cadedaniel!) - Dynamic SplitFuse (A.K.A. Chunked Prefill, which we have thanks to @rk...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: appear to be: - FP8 quantisation of the model (currently we only support KV cache) - The `CustomAllReduce` kernel from Nvidia TRT LLM - CUDA graphs - Speculative decoding (which we have thanks to @cadedaniel!) - Dynamic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
