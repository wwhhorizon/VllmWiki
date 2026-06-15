# vllm-project/vllm#29657: [Bug]: GPT-OSS-120B Eagle-3 High concurrency perf drop

| 字段 | 值 |
| --- | --- |
| Issue | [#29657](https://github.com/vllm-project/vllm/issues/29657) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPT-OSS-120B Eagle-3 High concurrency perf drop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug B200 machine. current TOT perf ``` Maximum request concurrency: 512 ============ Serving Benchmark Result ============ Successful requests: 2560 Benchmark duration (s): 241.27 Total input tokens: 2621440 Total generated tokens: 2621440 Request throughput (req/s): 10.61 Output token throughput (tok/s): 10865.38 Total Token throughput (tok/s): 21730.75 ---------------Time to First Token---------------- Mean TTFT (ms): 938.20 Median TTFT (ms): 416.17 P99 TTFT (ms): 6024.36 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 43.62 Median TPOT (ms): 42.69 P99 TPOT (ms): 65.47 ---------------Inter-token Latency---------------- Mean ITL (ms): 903.22 Median ITL (ms): 870.80 P99 ITL (ms): 1903.97 ================================================== ``` We found the regression PR: https://github.com/vllm-project/vllm/pull/27922 before PR27922 it could get 17096.80 Output token throughput (tok/s). @njhill Benjamin told me you already had the fix: https://github.com/vllm-project/vllm/pull/29542 I tried PR29542, but it still cannot reach 17096.80. It only got 11986.50. Repro command export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 se...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: rrent TOT perf ``` Maximum request concurrency: 512 ============ Serving Benchmark Result ============ Successful requests: 2560 Benchmark duration (s): 241.27 Total input tokens: 2621440 Total generated tokens: 262144
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: 80. It only got 11986.50. Repro command export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --tokenizer openai/g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: owing repo. git clone https://github.com/kimbochen/bench_serving.git pip install pandas datasets --break-system-packages ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: y perf drop bug ### Your current environment ### 🐛 Describe the bug B200 machine. current TOT perf ``` Maximum request concurrency: 512 ============ Serving Benchmark Result ============ Successful requests: 2560 Benchm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-120B Eagle-3 High concurrency perf drop bug ### Your current environment ### 🐛 Describe the bug B200 machine. current TOT perf ``` Maximum request concurrency: 512 ============ Serving Benchmark Result ==...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
