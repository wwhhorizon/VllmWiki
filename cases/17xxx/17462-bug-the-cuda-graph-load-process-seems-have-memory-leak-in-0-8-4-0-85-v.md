# vllm-project/vllm#17462: [Bug]: The cuda graph load process seems have memory leak in 0.8.4/0.85 V1 engine

| 字段 | 值 |
| --- | --- |
| Issue | [#17462](https://github.com/vllm-project/vllm/issues/17462) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;operator;triton |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The cuda graph load process seems have memory leak in 0.8.4/0.85 V1 engine

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```vllm serve Qwen3-32B --tensor-parallel-size 2 ``` then compile a long time end with cuda oom ``` ray-test-create-ai-node2-rqy511-head-7qd62:12171:12984 [1] NCCL INFO ncclCommInitRank comm 0x2aa6cd00 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId 20 commId 0xb0f2a75f6fb6730b - Init COMPLETE INFO 04-30 16:20:37 [kv_cache_utils.py:634] GPU KV cache size: 67,856 tokens INFO 04-30 16:20:37 [kv_cache_utils.py:637] Maximum concurrency for 16,384 tokens per request: 4.14x INFO 04-30 16:20:37 [kv_cache_utils.py:634] GPU KV cache size: 67,856 tokens INFO 04-30 16:20:37 [kv_cache_utils.py:637] Maximum concurrency for 16,384 tokens per request: 4.14x (VllmWorker rank=1 pid=12171) ERROR 04-30 16:21:27 [multiproc_executor.py:380] WorkerProc hit an exception: %s (VllmWorker rank=1 pid=12171) ERROR 04-30 16:21:27 [multiproc_executor.py:380] Traceback (most recent call last): (VllmWorker rank=1 pid=12171) ERROR 04-30 16:21:27 [multiproc_executor.py:380] File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 375, in worker_busy_loop (VllmWorker rank=1 pid=12171) ERROR 04-30 16:21:27 [multiproc_executor.p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ibe the bug ```vllm serve Qwen3-32B --tensor-parallel-size 2 ``` then compile a long time end with cuda oom ``` ray-test-create-ai-node2-rqy511-head-7qd62:12171:12984 [1] NCCL INFO ncclCommInitRank comm 0x2aa6cd00 rank...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: The cuda graph load process seems have memory leak in 0.8.4/0.85 V1 engine bug;stale ### Your current environment ### 🐛 Describe the bug ```vllm serve Qwen3-32B --tensor-parallel-size 2 ``` then compile a long ti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ### Your current environment ### 🐛 Describe the bug ```vllm serve Qwen3-32B --tensor-parallel-size 2 ``` then compile a long time end with cuda oom ``` ray-test-create-ai-node2-rqy511-head-7qd62:12171:12984 [1] NCCL INF...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: File "/home/ray/anaconda3/lib/python3.10/site-packages/vllm/compilation/backends.py", line 677, in __call__ (VllmWorker rank=1 pid=12171) ERROR 04-30 16:21:27 [multiproc_executor.py:380] with torch.cuda.graph(cudagraph,...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 32B --tensor-parallel-size 2 ``` then compile a long time end with cuda oom ``` ray-test-create-ai-node2-rqy511-head-7qd62:12171:12984 [1] NCCL INFO ncclCommInitRank comm 0x2aa6cd00 rank 1 nranks 2 cudaDev 1 nvmlDev 1 b...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
