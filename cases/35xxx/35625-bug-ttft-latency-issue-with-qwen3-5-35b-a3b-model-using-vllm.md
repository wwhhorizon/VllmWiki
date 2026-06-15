# vllm-project/vllm#35625: [Bug]: TTFT latency issue with Qwen3.5-35B-A3B model using vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#35625](https://github.com/vllm-project/vllm/issues/35625) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: TTFT latency issue with Qwen3.5-35B-A3B model using vllm

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hello, I am experiencing severe tail latency for TTFT when running a concurrency benchmark on a Blackwell 6000 Pro and DGX Spark Reproduce command: ``` vllm serve Qwen/Qwen3.5-35B-A3B \ --port 8000 \ --tensor-parallel-size 1 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' \ --gpu-memory-utilization 0.8 \ --language-model-only ``` Output: ``` ============ Serving Benchmark Result ============ Successful requests: 1000 Failed requests: 0 Maximum request concurrency: 100 Benchmark duration (s): 38.30 Total input tokens: 128000 Total generated tokens: 128000 Request throughput (req/s): 26.11 Output token throughput (tok/s): 3341.89 Peak output token throughput (tok/s): 2100.00 Peak concurrent requests: 161.00 Total token throughput (tok/s): 6683.78 ---------------Time to First Token---------------- Mean TTFT (ms): 611.98 Median TTFT (ms): 191.57 P99 TTFT (ms): 4756.51 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 24.27 Median TPOT (ms): 22.93 P99 TPOT (ms): 49.27 ---------------Inter-token Latency---------------- Mean ITL (ms): 58...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: TTFT latency issue with Qwen3.5-35B-A3B model using vllm bug ### Your current environment ### 🐛 Describe the bug Hello, I am experiencing severe tail latency for TTFT when running a concurrency benchmark on a Bla...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Your current environment ### 🐛 Describe the bug Hello, I am experiencing severe tail latency for TTFT when running a concurrency benchmark on a Blackwell 6000 Pro and DGX Spark Reproduce command: ``` vllm serve Qwen/Qwe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g severe tail latency for TTFT when running a concurrency benchmark on a Blackwell 6000 Pro and DGX Spark Reproduce command: ``` vllm serve Qwen/Qwen3.5-35B-A3B \ --port 8000 \ --tensor-parallel-size 1 \ --max-model-len...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: TTFT latency issue with Qwen3.5-35B-A3B model using vllm bug ### Your current environment ### 🐛 Describe the bug Hello, I am experiencing severe tail latency for TTFT when running a concurrency benchmark on a Bla...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lel-size 1 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":2}' \ --gpu-memory-utilization 0.8 \ --language-model-only ``` Output: ``` =====...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
