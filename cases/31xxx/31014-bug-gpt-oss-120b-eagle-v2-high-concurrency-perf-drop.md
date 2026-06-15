# vllm-project/vllm#31014: [Bug]: GPT-OSS-120B Eagle-v2 High concurrency perf drop

| 字段 | 值 |
| --- | --- |
| Issue | [#31014](https://github.com/vllm-project/vllm/issues/31014) |
| 状态 | closed |
| 标签 | bug;speculative-decoding |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: GPT-OSS-120B Eagle-v2 High concurrency perf drop

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Only in B200 machine. The regression is caused by https://github.com/vllm-project/vllm/pull/29624. I use commit:75eb302a as baseline. In commit 75eb302a, ============ Serving Benchmark Result ============ Successful requests: 2560 Benchmark duration (s): 1597.51 Total input tokens: 2621440 Total generated tokens: 20971520 Request throughput (req/s): 1.60 Output token throughput (tok/s): 13127.61 Total Token throughput (tok/s): 14768.56 ---------------Time to First Token---------------- Mean TTFT (ms): 902.42 Median TTFT (ms): 230.73 P99 TTFT (ms): 6494.69 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 36.55 Median TPOT (ms): 37.21 P99 TPOT (ms): 51.62 ---------------Inter-token Latency---------------- Mean ITL (ms): 749.75 Median ITL (ms): 780.64 P99 ITL (ms): 1314.17 ================================================== In commit 75eb302a and revert https://github.com/vllm-project/vllm/pull/29624. ============ Serving Benchmark Result ============ Successful requests: 2560 Benchmark duration (s): 1268.58 Total input tokens: 2621440 Total generated tokens: 20971520 Request throughput (req/s): 2.02 Output token th...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: rrent environment ### 🐛 Describe the bug Only in B200 machine. The regression is caused by https://github.com/vllm-project/vllm/pull/29624. I use commit:75eb302a as baseline. In commit 75eb302a, ============ Serving Ben...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: rom 16531 to 13127 (20%). Repro command export VLLM_USE_FLASHINFER_MOE_MXFP4_MXFP8=1 server-side: python3 -m vllm.entrypoints.openai.api_server --host 0.0.0.0 --port 8087 --model openai/gpt-oss-120b --tokenizer openai/g...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: owing repo. git clone https://github.com/kimbochen/bench_serving.git pip install pandas datasets --break-system-packages ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ecoding ### Your current environment ### 🐛 Describe the bug Only in B200 machine. The regression is caused by https://github.com/vllm-project/vllm/pull/29624. I use commit:75eb302a as baseline. In commit 75eb302a, =====...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: GPT-OSS-120B Eagle-v2 High concurrency perf drop bug;speculative-decoding ### Your current environment ### 🐛 Describe the bug Only in B200 machine. The regression is caused by https://github.com/vllm-project/vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
