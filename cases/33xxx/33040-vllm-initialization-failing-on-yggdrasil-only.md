# vllm-project/vllm#33040: vLLM initialization failing on yggdrasil only

| 字段 | 值 |
| --- | --- |
| Issue | [#33040](https://github.com/vllm-project/vllm/issues/33040) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 |  |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel |
| 症状 | crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM initialization failing on yggdrasil only

### Issue 正文摘录

## Summary vLLM fails to initialize on yggdrasil with `RuntimeError: Engine core initialization failed`, while identical code works on pando. ## Evidence Ran `smoke_vllm_1turn_reasoning` batch (18 experiments): - **pando**: 6 success, 0 failed - **yggdrasil**: 0 success, 12 failed Both servers have identical code: - format-tax: `c9c7e7a0f51ce4885e1621c9ca9883eae7e9017f` - vLLM fork: `4b30e5f629e86acc048b847b648ca4685f2a91ae` ## Error ``` RuntimeError: Engine core initialization failed. See root cause above. Failed core proc(s): {} ``` Full traceback: ``` File "run_single.py", line 698, in main backend = BackendClass(**backend_kwargs) File "vllm_backend.py", line 149, in __init__ self._llm = LLM(**llm_kwargs) ... File "vllm/v1/executor/multiproc_executor.py", line 660, in wait_for_ready raise e from None Exception: WorkerProc initialization failed due to an exception in a background process. ``` ## Observations - Failures started around 11:51 on Jan 25 - GPU memory is clean (0 MiB on all GPUs) - No OOM or GPU errors in kernel logs (`dmesg`) - Shared memory segments existed in `/dev/shm/` (cleaned but issue persisted) - Issue affects all models (smollm3-3b, qwen3-32b, nemotron3-nano...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: **yggdrasil**: 0 success, 12 failed Both servers have identical code: - format-tax: `c9c7e7a0f51ce4885e1621c9ca9883eae7e9017f` - vLLM fork: `4b30e5f629e86acc048b847b648ca4685f2a91ae` ## Error ``` RuntimeError: Engine co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Steps - [ ] Check if yggdrasil needs a reboot - [ ] Compare CUDA/driver versions between servers - [ ] Check for zombie processes or stale CUDA contexts - [ ] Try `VLLM_ENABLE_V1_MULTIPROCESSING=0` to test V0 engine per...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ization failed`, while identical code works on pando. ## Evidence Ran `smoke_vllm_1turn_reasoning` batch (18 experiments): - **pando**: 6 success, 0 failed - **yggdrasil**: 0 success, 12 failed Both servers have identic...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ocess. ``` ## Observations - Failures started around 11:51 on Jan 25 - GPU memory is clean (0 MiB on all GPUs) - No OOM or GPU errors in kernel logs (`dmesg`) - Shared memory segments existed in `/dev/shm/` (cleaned but...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: {} ``` Full traceback: ``` File "run_single.py", line 698, in main backend = BackendClass(**backend_kwargs) File "vllm_backend.py", line 149, in __init__ self._llm = LLM(**llm_kwargs) ... File "vllm/v1/executor/multipro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
