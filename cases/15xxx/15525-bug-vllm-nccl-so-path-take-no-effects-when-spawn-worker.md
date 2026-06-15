# vllm-project/vllm#15525: [Bug]: VLLM_NCCL_SO_PATH take no effects when spawn worker

| 字段 | 值 |
| --- | --- |
| Issue | [#15525](https://github.com/vllm-project/vllm/issues/15525) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM_NCCL_SO_PATH take no effects when spawn worker

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using vllm v1 engine and set the env variable `VLLM_NCCL_SO_PATH` to another nccl so path. The `VLLM_WORKER_MULTIPROC_METHOD` is set to `spawn`. I enable the nccl debug log by `NCCL_DEBUG=version`. Due to some reason, i cannot use the system's nccl lib, and put another nccl lib in other directory. I see the main process of vllm outputs the correct version, but then output the system's version after worker finish torch compile. Some logs: ```log INFO 03-26 14:53:08 __init__.py:207] Automatically detected platform cuda. INFO 03-26 14:53:09 core.py:50] Initializing a V1 LLM engine (v0.7.3) with config: xxx INFO 03-26 14:53:09 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', ... (VllmWorker rank=2 pid=24018) INFO 03-26 14:53:30 utils.py:906] Found nccl from environment variable VLLM_NCCL_SO_PATH=/opt/tiger/nccl/lib/libnccl.so (VllmWorker rank=0 pid=23960) INFO 03-26 14:53:30 utils.py:906] Found nccl from environment variable VLLM_NCCL_SO_PATH=/opt/tiger/nccl/lib/libnccl.so (VllmWorker rank=3 pid=24053) INFO 03-26 14:53:30 utils.py:906] Found nccl from environment variable VLLM_NCCL_SO_...

## 现有链接修复摘要

#43505 Bump the minor-update group across 1 directory with 145 updates | #43993 Bump the minor-update group across 1 directory with 147 updates

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: OC_METHOD` is set to `spawn`. I enable the nccl debug log by `NCCL_DEBUG=version`. Due to some reason, i cannot use the system's nccl lib, and put another nccl lib in other directory. I see the main process of vllm outp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ... (VllmWorker rank=1 pid=23988) INFO 03-26 14:53:34 cuda.py:157] Using Flash Attention backend on V1 engine. (VllmWorker rank=2 pid=24018) INFO 03-26 14:53:34 cuda.py:157] Using Flash Attention backend on V1 engine. (...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: log INFO 03-26 14:53:08 __init__.py:207] Automatically detected platform cuda. INFO 03-26 14:53:09 core.py:50] Initializing a V1 LLM engine (v0.7.3) with config: xxx INFO 03-26 14:53:09 shm_broadcast.py:258] vLLM messag...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: FO 03-26 14:53:09 core.py:50] Initializing a V1 LLM engine (v0.7.3) with config: xxx INFO 03-26 14:53:09 shm_broadcast.py:258] vLLM message queue communication handle: Handle(connect_ip='127.0.0.1', ... (VllmWorker rank...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: VLLM_NCCL_SO_PATH take no effects when spawn worker bug;stale ### Your current environment ### 🐛 Describe the bug I'm using vllm v1 engine and set the env variable `VLLM_NCCL_SO_PATH` to another nccl so path. The...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#43505](https://github.com/vllm-project/vllm/pull/43505) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 145 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15525">#15525</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🌐 Update translatio… |
| [#43993](https://github.com/vllm-project/vllm/pull/43993) | mentioned | 0.6 | Bump the minor-update group across 1 directory with 147 updates | . PR <a href="https://redirect.github.com/fastapi/fastapi/pull/15525">#15525</a> by <a href="https://github.com/tiangolo"><code>@​tiangolo</code></a>.</li> <li>🌐 Update translatio… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
