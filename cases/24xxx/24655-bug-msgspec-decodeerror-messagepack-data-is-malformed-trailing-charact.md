# vllm-project/vllm#24655: [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 198)

| 字段 | 值 |
| --- | --- |
| Issue | [#24655](https://github.com/vllm-project/vllm/issues/24655) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 198)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I deploy Qwen3-embedding via: ``` vllm serve Qwen/Qwen3-Embedding-0.6B --port 5001 -dp 3 --gpu-memory-utilization 0.95 --max-num-batched-tokens 128000 --max-num-seqs 8192 ``` This server continually works well for about 1 days. But it suddenly shutdown by this error: ``` (APIServer pid=2249146) INFO: 20.98.116.19:59208 - "POST /score HTTP/1.1" 200 OK [1773/1826] (APIServer pid=2249146) INFO: 20.98.116.19:59218 - "POST /score HTTP/1.1" 200 OK (APIServer pid=2249146) INFO: 20.98.116.19:59220 - "POST /score HTTP/1.1" 200 OK (APIServer pid=2249146) INFO: 20.98.116.19:59202 - "POST /score HTTP/1.1" 200 OK (APIServer pid=2249146) INFO 09-11 06:22:48 [loggers.py:123] Engine 000: Avg prompt throughput: 77889.2 tokens/s, Avg generation throughpu t: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 5.5% (APIServer pid=2249146) INFO 09-11 06:22:48 [loggers.py:123] Engine 001: Avg prompt throughput: 78240.2 tokens/s, Avg generation throughpu t: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 5.5% (APIServer pid=2249146) INFO 09-11 06:22:48 [logger...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: msgspec.DecodeError: MessagePack data is malformed: trailing characters (byte 198) bug;stale ### Your current environment ### 🐛 Describe the bug I deploy Qwen3-embedding via: ``` vllm serve Qwen/Qwen3-Embedding-0...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory cache;cuda;operator;triton build_error;crash;slowdown e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ;stale ### Your current environment ### 🐛 Describe the bug I deploy Qwen3-embedding via: ``` vllm serve Qwen/Qwen3-Embedding-0.6B --port 5001 -dp 3 --gpu-memory-utilization 0.95 --max-num-batched-tokens 128000 --max-num...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 249146) ERROR 09-11 06:22:49 [async_llm.py:453] File "/root/ms-deepresearch/.venv/lib/python3.11/site-packages/vllm/v1/e ngine/async_llm.py", line 412, in output_handler (APIServer pid=2249146) ERROR 0
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: eration throughpu t: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs, GPU KV cache usage: 0.0%, Prefix cache hit rate: 5.5% (APIServer pid=2249146) INFO 09-11 06:22:48 [loggers.py:123] Engine 001: Avg prompt throughput:...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
