# vllm-project/vllm#30853: [Performance]: DeepSeek V3.2 Benchmarking: Significant performance discrepancy between initial and subsequent runs

| 字段 | 值 |
| --- | --- |
| Issue | [#30853](https://github.com/vllm-project/vllm/issues/30853) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api |
| 子分类 | wrong_output |
| Operator 关键词 | cache;cuda |
| 症状 | build_error;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: DeepSeek V3.2 Benchmarking: Significant performance discrepancy between initial and subsequent runs

### Issue 正文摘录

### Proposal to improve performance **Description** I followed the benchmarking instructions for DeepSeek V3.2 provided in the documentation: [https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3\_2.html\#benchmarking](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarking) ### Report of performance regression I noticed a massive performance difference between the first execution of `vllm bench serve` and the subsequent execution against the same server instance. **Observation** **1st Run Result:** The Mean TTFT is extremely high (\~21s), and throughput is lower. ```shell ============ Serving Benchmark Result ============ Successful requests: 100 Failed requests: 0 Request rate configured (RPS): 10.00 Benchmark duration (s): 131.78 Total input tokens: 204800 Total generated tokens: 102400 Request throughput (req/s): 0.76 Output token throughput (tok/s): 777.04 Peak output token throughput (tok/s): 1386.00 Peak concurrent requests: 100.00 Total Token throughput (tok/s): 2331.11 ---------------Time to First Token---------------- Mean TTFT (ms): 21727.85 Median TTFT (ms): 21310.34 P99 TTFT (ms): 43883.54 -----Time per Output Token (ex...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 7: [Performance]: DeepSeek V3.2 Benchmarking: Significant performance discrepancy between initial and subsequent runs performance ### Proposal to improve performance **Description** I followed the benchmarking instructions...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: sing `--dataset-name random`, I assume this improvement is NOT due to KV Cache hits (unless the random seed is fixed and produces identical prompts that trigger prefix caching). I suspect the first run includes signific...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eek V3.2 provided in the documentation: [https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3\_2.html\#benchmarking](https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html#benchmarki...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: x caching). I suspect the first run includes significant overhead from **CUDA graph capture** or **compilation**, acting effectively as a "warmup" phase. 2. **Accuracy:** If the above is true, the results from the first...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m using `--dataset-name random`, I assume this improvement is NOT due to KV Cache hits (unless the random seed is fixed and produces identical prompts that trigger prefix caching). I suspect the first run includes signi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
