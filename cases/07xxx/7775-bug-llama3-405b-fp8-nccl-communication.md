# vllm-project/vllm#7775: [Bug]: llama3-405b-fp8 NCCL communication

| 字段 | 值 |
| --- | --- |
| Issue | [#7775](https://github.com/vllm-project/vllm/issues/7775) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8;kernel |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: llama3-405b-fp8 NCCL communication

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 目前在8 * A800上进行推理，vllm推理的40b fp8版本，然后tp=8，一开始能推理，试了几个case以后就通信异常了 INFO 08-22 06:23:22 metrics.py:406] Avg prompt throughput: 36.2 tokens/s, Avg generation throughput: 4.6 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.1%, CPU KV cache usage: 0.0%. INFO 08-22 06:23:27 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 19.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0%. INFO 08-22 06:23:32 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 19.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.2%, CPU KV cache usage: 0.0%. INFO 08-22 06:23:37 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 19.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage: 0.0%. INFO 08-22 06:23:42 metrics.py:406] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 19.8 tokens/s, Running: 1 reqs, Swapped: 0 reqs, Pending: 0 reqs, GPU KV cache usage: 0.3%, CPU KV cache usage...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ne 491, in _wait ERROR 08-22 06:24:42 async_llm_engine.py:57] await waiter ERROR 08-22 06:24:42 async_llm_engine.py:57] asyncio.exceptions.CancelledError ERROR 08-22 06:24:42 async_llm_engine.py:57] ERROR 08-22 06:24:42...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: llama3-405b-fp8 NCCL communication bug;stale ### Your current environment ### 🐛 Describe the bug 目前在8 * A800上进行推理，vllm推理的40b fp8版本，然后tp=8，一开始能推理，试了几个case以后就通信异常了 INFO 08-22 06:23:22 metrics.py:406] Avg prompt thr...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: llama3-405b-fp8 NCCL communication bug;stale ### Your current environment ### 🐛 Describe the bug 目前在8 * A800上进行推理，vllm推理的40b fp8版本，然后tp=8，一开始能推理，试了几个case以后就通信异常了 INFO 08-22 06:23:22 metrics.py:406] Avg prompt thr...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: oop ERROR 08-22 06:24:42 async_llm_engine.py:57] done, _ = await asyncio.wait( ERROR 08-22 06:24:42 async_llm_engine.py:57] File "/usr/lib/python3.10/asyncio/tasks.py", line 384, in wait ERROR 08-22 06:24:42 async_llm_e...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ocess pid=161) WARNING 08-22 06:24:42 shm_broadcast.py:386] No available block found in 60 second. (VllmWorkerProcess pid=158) WARNING 08-22 06:24:42 shm_broadcast.py:386] No available block found in 60 second. (VllmWor...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0xdc253 (0x7f468e4b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #5: <unknow |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | x94ac3 (0x7f468fbdcac3 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #6: clone + 0x44 (0x7f468fc6dbf4 in /usr/lib/x86_64-linux-gnu/libc.so.6) bug stale |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
