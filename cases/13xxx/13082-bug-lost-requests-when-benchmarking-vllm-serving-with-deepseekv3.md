# vllm-project/vllm#13082: [Bug]: Lost requests when benchmarking vllm serving with deepseekv3

| 字段 | 值 |
| --- | --- |
| Issue | [#13082](https://github.com/vllm-project/vllm/issues/13082) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | precision |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Lost requests when benchmarking vllm serving with deepseekv3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### error info We benchmarking vllm serving with sglang found that there are always missing some requests. For instance, we test 10000 requests and the log shows only 9996 successful requests ``` ============ Serving Benchmark Result ============ Backend: vllm Traffic request rate: inf Max reqeuest concurrency: 1024 Successful requests: 9996 Benchmark duration (s): 11118.99 Total input tokens: 10339244 Total generated tokens: 10304727 Total generated tokens (retokenized): 10260625 Request throughput (req/s): 0.90 Input token throughput (tok/s): 929.87 Output token throughput (tok/s): 926.77 Total token throughput (tok/s): 1856.64 Concurrency: 927.81 ----------------End-to-End Latency---------------- ... ============ Serving Benchmark Result ============ Backend: vllm Traffic request rate: inf Max reqeuest concurrency: 1024 Successful requests: 9985 Benchmark duration (s): 5175.95 Total input tokens: 10328360 Total generated tokens: 5178613 Total generated tokens (retokenized): 5157160 Request throughput (req/s): 1.93 Input token throughput (tok/s): 1995.45 Output token throughput (tok/s): 1000.51 Total token throughput (tok/s): 2...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Lost requests when benchmarking vllm serving with deepseekv3 bug;stale ### Your current environment ### 🐛 Describe the bug ### error info We benchmarking vllm serving with sglang found that there are always missi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support cuda;triton build_error;nan_inf;slowdown env_dependency Your current env...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ccessful requests ``` ============ Serving Benchmark Result ============ Backend: vllm Traffic request rate: inf Max reqeuest concurrency: 1024 Successful requests: 9996 Benchmark du
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ing.html#running-vllm-on-multiple-nodes 2. start serving ``` vllm serve models/hf_hub/models--deepseek-ai--DeepSeek-V3/snapshots/4c1f24cc10a2a1894304c7ab52edd9710c047571 \ --enforce-eager \ --trust-remote-code \ --tenso...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
