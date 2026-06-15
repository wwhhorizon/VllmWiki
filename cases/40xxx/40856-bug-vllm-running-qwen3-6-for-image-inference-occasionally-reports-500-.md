# vllm-project/vllm#40856: [Bug]: VLLM running qwen3.6 for image inference occasionally reports 500 Internal Server Error

| 字段 | 值 |
| --- | --- |
| Issue | [#40856](https://github.com/vllm-project/vllm/issues/40856) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;gemm |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM running qwen3.6 for image inference occasionally reports 500 Internal Server Error

### Issue 正文摘录

### Your current environment VLLM version: 0.16.0rc2.dev496+g4a9c07a0a System environment: Ubuntu 22.04.5 LTS Graphics card type: H200 series What causes this 500 error, or how to output the detailed reason for the 500 error ### 🐛 Describe the bug Service startup command: VLLM_LOGGING_LEVEL=DEBUG vllm serve /sharedFile/jiuding/models/models/Qwen/Qwen3___6-35B-A3B --port 6008 --tensor-parallel-size 8 --max-model-len 262144 --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-log-requests --trust-remote-code --served-model-name JinQuan2604 The error log is as follows： (APIServer pid=6051) DEBUG 04-25 02:26:25 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 98.6% (APIServer pid=6051) DEBUG 04-25 02:26:35 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 98.6% (APIServer pid=6051) INFO: 10.10.7.200:4...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: n3 --enable-auto-tool-choice --tool-call-parser qwen3_coder --enable-log-requests --trust-remote-code --served-model-name JinQuan2604 The error log is as follows： (APIServer pid=6051) DEBUG 04-25 02:26:25 [v1/metrics/lo...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: neration throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 98.6% (APIServer pid=6051) DEBUG 04-25 02:26:35 [v1/metrics/loggers.py:259]...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: VLLM running qwen3.6 for image inference occasionally reports 500 Internal Server Error bug ### Your current environment VLLM version: 0.16.0rc2.dev496+g4a9c07a0a System environment: Ubuntu 22.04.5 LTS Graphics c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ns/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 0.0%, MM cache hit rate: 98.6% (APIServer pid=6051) DEBUG 04-25 02:26:35 [v1/metrics/loggers.py:259] Engine 000: Avg prompt throug...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: reports 500 Internal Server Error bug ### Your current environment VLLM version: 0.16.0rc2.dev496+g4a9c07a0a System environment: Ubuntu 22.04.5 LTS Graphics card type: H200 series What causes this 500 error, or how to o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
