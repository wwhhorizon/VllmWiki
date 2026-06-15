# vllm-project/vllm#11247: [Bug]: disaggregated prefilling hangs when TP=2 

| 字段 | 值 |
| --- | --- |
| Issue | [#11247](https://github.com/vllm-project/vllm/issues/11247) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: disaggregated prefilling hangs when TP=2 

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run the script vllm/benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh with TP=2 for both prefill and decode instance. The prefill instance or decode instance hung after receiving several requests from the proxy server. I received messages similar to the message below from the command line repeatedly when one of the instances hung ``` DEBUG 12-17 00:40:47 metrics.py:460] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.0%, CPU KV cache usage: 0.0%. DEBUG 12-17 00:40:47 engine.py:190] Waiting for new requests in engine loop. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50 client.py:186] Waiting for output from MQLLMEngine. DEBUG 12-17 00:40:50...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: disaggregated prefilling hangs when TP=2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run the script vllm/benchmarks/disagg_benchmarks/disagg_perfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: } main() { (which wget && which curl) || (apt-get update && apt-get install -y wget curl) (which jq) || (apt-get -y install jq) (which socat) || (apt-get -y install socat) pip install quart httpx matplotlib aiohttp cd "...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 2 PG GUID 3 Ran
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: efilling hangs when TP=2 bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I tried to run the script vllm/benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh with...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: s _No response_ ### 🐛 Describe the bug I tried to run the script vllm/benchmarks/disagg_benchmarks/disagg_performance_benchmark.sh with TP=2 for both prefill and decode instance. The prefill instance or decode instance...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | frame #4: clone + 0x3f (0x7f1d1d31cacf in /lib/x86_64-linux-gnu/libc.so.6) ``` example script modified from disagg |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | frame #6: clone + 0x3f (0x7f1d1d31cacf in /lib/x86_64-linux-gnu/libc.so.6) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
