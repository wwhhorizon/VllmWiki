# vllm-project/vllm#5072: [Performance]: A few performance-related questions.

| 字段 | 值 |
| --- | --- |
| Issue | [#5072](https://github.com/vllm-project/vllm/issues/5072) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: A few performance-related questions.

### Issue 正文摘录

### Proposal to improve performance 1. What are some common tips for improving throughput? 2. Which version performs the best? Is it necessary to use an older version of VLLM? 3. Which has higher throughput, GPTQ or AWQ? Also, can the performance gap between these two quantization methods be disregarded? 4. I'm using a 4080 GPU with 16GB of memory. When running an 8B and a 14B model, the 14B model's concurrency is only one-fifth of the 8B model's when running with 64 threads due to a small batch size. Is solving the memory bottleneck issue through multi-GPU parallel computing the only solution in this case? Are there any other alternatives? 5. How does the performance of flash attn2 compare to flashinfer? 6. In what aspects does flash attn2 outperform xformers? Is the performance improvement more pronounced when running on a single GPU versus multi-GPU parallel computing? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: posal to improve performance 1. What are some common tips for improving throughput? 2. Which version performs the best? Is it necessary to use an older version of VLLM? 3. Which has higher throughput, GPTQ or AWQ? Also,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ther alternatives? 5. How does the performance of flash attn2 compare to flashinfer? 6. In what aspects does flash attn2 outperform xformers? Is the performance improvement more pronounced when running on a single GPU v...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ormance 1. What are some common tips for improving throughput? 2. Which version performs the best? Is it necessary to use an older version of VLLM? 3. Which has higher throughput, GPTQ or AWQ? Also, can the performance...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: throughput, GPTQ or AWQ? Also, can the performance gap between these two quantization methods be disregarded? 4. I'm using a 4080 GPU with 16GB of memory. When running an 8B and a 14B model, the 14B model's concurrency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s only one-fifth of the 8B model's when running with 64 threads due to a small batch size. Is solving the memory bottleneck issue through multi-GPU parallel computing the only solution in this case? Are there any other...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
