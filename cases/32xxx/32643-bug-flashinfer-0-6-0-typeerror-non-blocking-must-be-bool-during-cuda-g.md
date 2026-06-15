# vllm-project/vllm#32643: [Bug] FlashInfer >=0.6.0 TypeError: non_blocking must be bool during CUDA graph capture

| 字段 | 值 |
| --- | --- |
| Issue | [#32643](https://github.com/vllm-project/vllm/issues/32643) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] FlashInfer >=0.6.0 TypeError: non_blocking must be bool during CUDA graph capture

### Issue 正文摘录

vLLM fails during CUDA graph capture with FlashInfer >=0.6.0. Error: TypeError: copy_(): argument 'non_blocking' must be bool, not NoneType Crash site: flashinfer/decode.py:940 self._paged_kv_indptr_buf.copy_(indptr, non_blocking=non_blocking) Root cause: FlashInfer 0.6.0 (commit 3346a8bb, merged Jan 6 2026) added `o_data_type` parameter to `BatchDecodeWithPagedKVCacheWrapper.plan()`. Without this parameter, positional arguments shift by one position. The `None` intended for `block_tables` lands on `non_blocking`. Workaround: `--enforce-eager` (skips CUDA graph capture) Fix submitted: PR #32515

## 现有链接修复摘要

#32515 [Bugfix] Add missing o_data_type parameter for FlashInfer >=0.6.0 compatibility

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] FlashInfer >=0.6.0 TypeError: non_blocking must be bool during CUDA graph capture vLLM fails during CUDA graph capture with FlashInfer >=0.6.0. Error: TypeError: copy_(): argument 'non_blocking' must be bool, not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug] FlashInfer >=0.6.0 TypeError: non_blocking must be bool during CUDA graph capture vLLM fails during CUDA graph capture with FlashInfer >=0.6.0. Error: TypeError: copy_(): argument 'non_blocking' must be bool, not...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Bug] FlashInfer >=0.6.0 TypeError: non_blocking must be bool during CUDA graph capture vLLM fails during CUDA graph capture with FlashInfer >=0.6.0. Error: TypeError: copy_(): argument 'non_blocking' must be bool, not...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: gument 'non_blocking' must be bool, not NoneType Crash site: flashinfer/decode.py:940 self._paged_kv_indptr_buf.copy_(indptr, non_blocking=non_blocking) Root cause: FlashInfer 0.6.0 (commit 3346a8bb, merged Jan 6 2026)...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32515](https://github.com/vllm-project/vllm/pull/32515) | closes_keyword | 0.95 | [Bugfix] Add missing o_data_type parameter for FlashInfer >=0.6.0 compatibility | Fixes #32643 ## Purpose Fix compatibility with FlashInfer >=0.6.0 which added `o_data_type` parameter to `BatchDecodeWithPagedKVCacheWrapper.plan()` (commit 3346a8bb, merged Jan |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
