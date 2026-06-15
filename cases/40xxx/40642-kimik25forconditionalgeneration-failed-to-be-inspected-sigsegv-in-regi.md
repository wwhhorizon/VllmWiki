# vllm-project/vllm#40642: KimiK25ForConditionalGeneration failed to be inspected — SIGSEGV in registry subprocess during process exit
  (GB200)

| 字段 | 值 |
| --- | --- |
| Issue | [#40642](https://github.com/vllm-project/vllm/issues/40642) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> KimiK25ForConditionalGeneration failed to be inspected — SIGSEGV in registry subprocess during process exit   (GB200)

### Issue 正文摘录

## Problem vLLM's model registry inspection subprocess (`python3 -m vllm.model_executor.models.registry`) crashes with SIGSEGV (signal 11) during **process exit**, after the inspection has already completed successfully and written its output. The parent process sees exit code 139, raises `CalledProcessError`, and reports a misleading error: ``` pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, Model architectures ['KimiK25ForConditionalGeneration'] failed to be inspected. Please check the logs for more details. ``` The inspection **did not fail** — the subprocess wrote correct model metadata to its output file. The crash occurs during Python interpreter shutdown when native extension cleanup handlers (atexit / static destructors) run. ## Environment - **vLLM**: v0.19.0 (also reproduces on v0.19.1) - **Hardware**: NVIDIA GB200 (Blackwell), 4× GPU, aarch64 - **Model**: Kimi-K2.5 (`KimiK25ForConditionalGeneration`) with `trust_remote_code=True` - **Python**: 3.10 - **CUDA**: 12.9.1 - **PyTorch**: 2.10.0 - **nixl-cu12**: 1.0.1 (does NOT reproduce with 1.0.0 — see "Workarounds" below) ## GDB Backtrace The crash occurs in UCX's topology clean...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: nux-gnu/libc.so.6 ``` The `libucs.so` is bundled inside the `nixl-cu12` wheel at `nixl_cu12.libs/libucs.so`. The md5sum of this file differs between `nixl-cu12==1.0.0` (no crash) and `nixl-cu12==1.0.1` (crash). The subp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: in registry subprocess during process exit (GB200) ## Problem vLLM's model registry inspection subprocess (`python3 -m vllm.model_executor.models.registry`) crashes with SIGSEGV (signal 11) during **process exit**, afte...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: to be inspected — SIGSEGV in registry subprocess during process exit (GB200) ## Problem vLLM's model registry inspection subprocess (`python3 -m vllm.model_executor.models.registry`) crashes with SIGSEGV (signal 11) dur...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: dware_porting;model_support cuda build_error;crash env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation Problem
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: it / static destructors) run. ## Environment - **vLLM**: v0.19.0 (also reproduces on v0.19.1) - **Hardware**: NVIDIA GB200 (Blackwell), 4× GPU, aarch64 - **Model**: Kimi-K2.5 (`KimiK25ForConditionalGeneration`) with `tr...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | c:128 #3 0x0000fffff7fc5398 in ?? () from /lib/ld-linux-aarch64.so.1 #4 0x0000fffff7cfcde8 in ?? () from /usr/lib/aarch64-linux-gnu/libc.so.6 #5 0x0000fffff7cfcf0c in exit () from |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | 0000fffff7cfcf0c in exit () from /usr/lib/aarch64-linux-gnu/libc.so.6 #6 0x0000fffff7ce7400 in ?? () from /usr/lib/aarch64-linux-gnu/libc.so.6 #7 0x0000fffff7ce74cc in __libc_start |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 0x0000fffff7ce7400 in ?? () from /usr/lib/aarch64-linux-gnu/libc.so.6 #7 0x0000fffff7ce74cc in __libc_start_main () from /usr/lib/aarch64-linux-gnu/libc.so.6 ``` the `libucs.so` is |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
