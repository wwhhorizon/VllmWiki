# vllm-project/vllm#15182: [Bug]:  the issue of "cuda out of memory" arises

| 字段 | 值 |
| --- | --- |
| Issue | [#15182](https://github.com/vllm-project/vllm/issues/15182) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;moe;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;moe;triton |
| 症状 | build_error;crash;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  the issue of "cuda out of memory" arises

### Issue 正文摘录

### Your current environment ### current environment Use 8 A800 80 GPU cards, report the following error: Deepseek is using the Q4 gguf model. ### command: python3 api_server.py --host 0.0.0.0 --port 7803 --model /data/models/DeepSeek-R1-Q2/ --served-model-name deepseek-r1 --max-model-len 8192 --enable-reasoning --reasoning-parser deepseek_r1 --gpu-memory-utilization 0.9 --tensor-parallel-size 8 --trust-remote-code (VllmWorker rank=0 pid=3013) INFO 03-20 03:14:59 [shm_broadcast.py:258] vLLM message queue communication handle: Handle(local_reader_ranks=[1, 2, 3, 4, 5, 6, 7], buffer_handle=(7, 4194304, 6, 'psm_5030d6c2'), local_subscribe_addr='ipc:///tmp/54feae1f-3d13-452d-9e9e-1bf1fffe271e', remote_subscribe_addr=None, remote_addr_ipv6=False) (VllmWorker rank=1 pid=3024) INFO 03-20 03:14:59 [parallel_state.py:967] rank 1 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 1 (VllmWorker rank=6 pid=3085) INFO 03-20 03:14:59 [parallel_state.py:967] rank 6 in world size 8 is assigned as DP rank 0, PP rank 0, TP rank 6 (VllmWorker rank=1 pid=3024) INFO 03-20 03:14:59 [cuda.py:186] Using Triton MLA backend on V1 engine. (VllmWorker rank=0 pid=3013) INFO 03-20 03:14:59 [parallel_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: lmWorker rank=4 pid=3061) WARNING 03-20 03:15:06 [config.py:3670] `torch.compile` is turned on, but the model /data/models/DeepSeek-R1-Q2/ does not support it. Please open an issue on GitHub if you want it to be support...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: the issue of "cuda out of memory" arises bug;stale ### Your current environment ### current environment Use 8 A800 80 GPU cards, report the following error: Deepseek is using the Q4 gguf model. ### command: pytho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: the issue of "cuda out of memory" arises bug;stale ### Your current environment ### current environment Use 8 A800 80 GPU cards, report the following error: Deepseek is using the Q4 gguf model. ### command: pytho...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: k 6 (VllmWorker rank=1 pid=3024) INFO 03-20 03:14:59 [cuda.py:186] Using Triton MLA backend on V1 engine. (VllmWorker rank=0 pid=3013) INFO 03-20 03:14:59 [parallel_state.py:967] rank 0 in world size 8 is assigned as DP...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ils.py", line 558, in make_layers (VllmWorker rank=5 pid=3073) maybe_offload_to_cpu(layer_fn(prefix=f"{prefix}.{idx}")) (VllmWorker rank=5 pid=3073) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=5 pid=3073) File "...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
