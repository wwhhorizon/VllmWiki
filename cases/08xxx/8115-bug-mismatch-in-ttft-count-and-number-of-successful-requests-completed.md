# vllm-project/vllm#8115: [Bug]: Mismatch in TTFT count and number of successful requests completed 

| 字段 | 值 |
| --- | --- |
| Issue | [#8115](https://github.com/vllm-project/vllm/issues/8115) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Mismatch in TTFT count and number of successful requests completed 

### Issue 正文摘录

### Your current environment - vLLM version: v0.5.3.post1 (Public Docker Image ) - Model: Llama 3 70 B - Dtype: FP16 - GPU: Nvidia H100 ### 🐛 Describe the bug The vLLM metrics endpoint is showing discrepancies between 'time_to_first_token_seconds_count' and the total number of successful requests completed. According to my understanding, the time to first token seconds count should align with the total number of requests processed. Example: vllm:time_to_first_token_seconds_count{model_name="meta-llama/Meta-Llama-3-70B-Instruct"} 8060.0 vllm:request_success_total{finished_reason="stop",model_name="meta-llama/Meta-Llama-3-70B-Instruct"} 3810.0 vllm:request_success_total{finished_reason="length",model_name="meta-llama/Meta-Llama-3-70B-Instruct"} 108.0 The TTFT count (8060) is higher that the total number of request (3810+108 = 3918). Added the entire metrics endpoint output for the reference. ``` # HELP python_gc_objects_collected_total Objects collected during gc # TYPE python_gc_objects_collected_total counter python_gc_objects_collected_total{generation="0"} 170852.0 python_gc_objects_collected_total{generation="1"} 1.0068423e+07 python_gc_objects_collected_total{generation="2"} 7...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: Mismatch in TTFT count and number of successful requests completed bug;stale ### Your current environment - vLLM version: v0.5.3.post1 (Public Docker Image ) - Model: Llama 3 70 B - Dtype: FP16 - GPU: Nvidia H100...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rrent environment - vLLM version: v0.5.3.post1 (Public Docker Image ) - Model: Llama 3 70 B - Dtype: FP16 - GPU: Nvidia H100 ### 🐛 Describe the bug The vLLM metrics endpoint is showing discrepancies between 'time_to_fir...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ssful requests completed bug;stale ### Your current environment - vLLM version: v0.5.3.post1 (Public Docker Image ) - Model: Llama 3 70 B - Dtype: FP16 - GPU: Nvidia H100 ### 🐛 Describe the bug The vLLM metrics endpoint...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Mismatch in TTFT count and number of successful requests completed bug;stale ### Your current environment - vLLM version: v0.5.3.post1 (Public Docker Image ) - Model: Llama 3 70 B - Dtype: FP16 - GPU: Nvidia H100...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: a/Meta-Llama-3-70B-Instruct"} 438.11926794052124 # HELP vllm:e2e_request_latency_seconds Histogram of end to end request latency in seconds. # TYPE vllm:e2e_request_latency_seconds histogram vllm:e2e_request_latency_sec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
