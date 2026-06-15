# vllm-project/vllm#21852: [Performance]: Higher AllReduce Kernel Overhead in V1 Engine Compared to V0

| 字段 | 值 |
| --- | --- |
| Issue | [#21852](https://github.com/vllm-project/vllm/issues/21852) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Higher AllReduce Kernel Overhead in V1 Engine Compared to V0

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression We observed a significant higher latency in V1 engine in the AllReduce kernel compared to V0, while the performance of other kernels remained consistently matched. The high discrepancy is observed in both the Llama 4 Maverick and DeepSeek R1 model. **### Profiling result of DeepSeek R1** The AllReduce kernel latency in DeepSeek R1 reported for V1 is significantly high, inflating the cumulative kernel latency. Using the AllRreduce timing from V0 corrects the discrepancy and aligns kernel profiling with LLMPerf’s ITL. Setup: * vLLM version: 0.9.1 * Model: DeepSeek R1 * Profiling tool: Torch Profiler and LLMPerf **Key Observations:** * V0: Kernel latencies sum to 17.08 ms, approximately 99% of the ITL, indicating good consistency. * V1: Kernel latencies sum to 51.24 ms, approximately 3x the ITL, highlighting a mismatch attributed to AllReduce kernel timing. * Replacing V1’s AllReduce latency with V0’s measurement brings the total down to 16.65 ms, approximately 101% of the ITL, restoring internal consistency. **### Profiling result of Llama 4 Maverick** The discrepancy can be up to 570.46 ms. Speci...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: screpancy and aligns kernel profiling with LLMPerf’s ITL. Setup: * vLLM version: 0.9.1 * Model: DeepSeek R1 * Profiling tool: Torch Profiler and LLMPerf **Key Observations:** * V0: Kernel latencies sum to 17.08 ms, appr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: el latencies sum to 51.24 ms, approximately 3x the ITL, highlighting a mismatch attributed to AllReduce kernel timing. * Replacing V1’s AllReduce latency with V0’s measurement brings the total down to 16.65 ms, approxim...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: roposal to improve performance _No response_ ### Report of performance regression We observed a significant higher latency in V1 engine in the AllReduce kernel compared to V0, while the performance of other kernels rema...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ained consistently matched. The high discrepancy is observed in both the Llama 4 Maverick and DeepSeek R1 model. **### Profiling result of DeepSeek R1** The AllReduce kernel latency in DeepSeek R1 reported for V1 is sig...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Higher AllReduce Kernel Overhead in V1 Engine Compared to V0 performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression We observed a significant higher latency in V1 engine...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
