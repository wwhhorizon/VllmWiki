# vllm-project/vllm#41817: [Bug]: OverflowError in mamba_utils.collect_mamba_copy_meta on XPU when device pointer ≥ 2^63 (hybrid models with align-mode prefix caching)

| 字段 | 值 |
| --- | --- |
| Issue | [#41817](https://github.com/vllm-project/vllm/issues/41817) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;triton |
| 症状 | crash;nan_inf;nondeterministic;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: OverflowError in mamba_utils.collect_mamba_copy_meta on XPU when device pointer ≥ 2^63 (hybrid models with align-mode prefix caching)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug `collect_mamba_copy_meta` in `vllm/v1/worker/mamba_utils.py` deterministically crashes on XPU at the first multi-block mamba state copy during decode for any hybrid (attention + GDN/Mamba) model with prefix caching enabled in align mode. The buffers `src_ptrs` and `dst_ptrs` are allocated as `torch.int64` (signed). On XPU, device pointers returned by `tensor.data_ptr()` can have the most-significant bit set — i.e., values in the range `[2^63, 2^64 − 1]`. These are valid 64-bit pointers when interpreted as unsigned, but they overflow `np.int64` when numpy tries to assign them via `PyLong_AsLong()`: ``` File "vllm/v1/worker/mamba_utils.py", line 128, in collect_mamba_copy_meta src_ptrs_np[offset] = copy_spec.start_addr OverflowError: Python int too large to convert to C long ``` ### Why this is XPU-specific The bug is in platform-agnostic Python code, but only triggers on platforms whose memory allocator returns addresses in the upper half of the 64-bit address space: - **CUDA on x86_64 Linux:** virtual addresses typically = 2^63), + # which occur on XPU, are stored by bit pattern rather than rejected as + #...

## 现有链接修复摘要

#30877 [V1][Hybrid] Mamba Prefix Caching with align mode | #41995 Fix Mamba copy metadata high-bit pointers

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 4: be the bug `collect_mamba_copy_meta` in `vllm/v1/worker/mamba_utils.py` deterministically crashes on XPU at the first multi-block mamba state copy during decode for any hybrid (attention + GDN/Mamba) model with prefix c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: stically crashes on XPU at the first multi-block mamba state copy during decode for any hybrid (attention + GDN/Mamba) model with prefix caching enabled in align mode. The buffers `src_ptrs` and `dst_ptrs` are allocated...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: or returns addresses in the upper half of the 64-bit address space: - **CUDA on x86_64 Linux:** virtual addresses typically = 2^63), + # which occur on XPU, are stored by bit pattern rather than rejected as + # signed-i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: rker/mamba_utils.py` deterministically crashes on XPU at the first multi-block mamba state copy during decode for any hybrid (attention + GDN/Mamba) model with prefix caching enabled in align mode. The buffers `src_ptrs...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _utils.collect_mamba_copy_meta on XPU when device pointer ≥ 2^63 (hybrid models with align-mode prefix caching) bug ### Your current environment ### 🐛 Describe the bug ### 🐛 Describe the bug `collect_mamba_copy_meta` in...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30877](https://github.com/vllm-project/vllm/pull/30877) | mentioned | 0.45 | [V1][Hybrid] Mamba Prefix Caching with align mode | 64` allocation traces back to the original align-mode introduction in #30877, where buffers were initially cuda tensors. the signed-int64 assumption has been present since day one… |
| [#41995](https://github.com/vllm-project/vllm/pull/41995) | closes_keyword | 0.95 | Fix Mamba copy metadata high-bit pointers | Fixes #41817. ### Summary `collect_mamba_copy_meta` stores source and destination device pointers in NumPy-backed CPU buffers before Triton consumes them as pointer arguments. On |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
