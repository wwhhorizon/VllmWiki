# vllm-project/vllm#39068: [Bug]: Duplicate parameter name in convert_vertical_slash_indexes op schema — kv_seqlens registered as q_seqlens

| 字段 | 值 |
| --- | --- |
| Issue | [#39068](https://github.com/vllm-project/vllm/issues/39068) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;hardware_porting;model_support |
| 子分类 | wrong_output |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Duplicate parameter name in convert_vertical_slash_indexes op schema — kv_seqlens registered as q_seqlens

### Issue 正文摘录

## Describe the bug The PyTorch op schema strings registered in `csrc/torch_bindings.cpp` for `convert_vertical_slash_indexes` and `convert_vertical_slash_indexes_mergehead` have a **duplicate parameter name**: `Tensor q_seqlens` appears twice. The second occurrence should be `Tensor kv_seqlens`. ```cpp // BUGGY (both ops affected): " Tensor q_seqlens, Tensor q_seqlens, " // <-- kv_seqlens written as q_seqlens // CORRECT: " Tensor q_seqlens, Tensor kv_seqlens, " ``` The C++ function signatures in `csrc/ops.h` and the Python wrappers in `vllm/_custom_ops.py` are both correct — the mismatch is only in the schema string passed to `ops.def(...)`. ## Impact PyTorch op schema registration with duplicate argument names causes a **runtime error** when the kernel is dispatched: ``` RuntimeError: ... duplicate argument name 'q_seqlens' in schema ``` This affects the sparse/blocksparse vertical-slash attention path (non-ROCm only, guarded by `#ifndef USE_ROCM`). ## Reproduction ```python import torch import vllm._custom_ops as ops q_seqlens = torch.tensor([16], dtype=torch.int32, device="cuda") kv_seqlens = torch.tensor([16], dtype=torch.int32, device="cuda") # Any call through the vertical_...

## 现有链接修复摘要

#39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: n-ROCm only, guarded by `#ifndef USE_ROCM`). ## Reproduction ```python import torch import vllm._custom_ops as ops q_seqlens = torch.tensor([16], dtype=torch.int32, device="cuda") kv_seqlens = torch.tensor([16], dtype=t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: nd the Python wrappers in `vllm/_custom_ops.py` are both correct — the mismatch is only in the schema string passed to `ops.def(...)`. ## Impact PyTorch op schema registration with duplicate argument names causes a **ru...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: simply load vLLM and trigger the sparse attention path via a blocksparse model. ## Root cause `csrc/torch_bindings.cpp` lines 83 and 94: ```cpp // Line 83 (convert_vertical_slash_indexes): " Tensor q_seqlens, Tensor q_s...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ;operator mismatch dtype;env_dependency #39067 [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema Describe the bug
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: h duplicate argument names causes a **runtime error** when the kernel is dispatched: ``` RuntimeError: ... duplicate argument name 'q_seqlens' in schema ``` This affects the sparse/blocksparse vertical-slash attention p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39067](https://github.com/vllm-project/vllm/pull/39067) | closes_keyword | 0.95 | [Transformers/Bugfix] Fix Gemma4 MoE top_k lookup + duplicate kv_seqlens in op schema | Fixes #39068** The PyTorch op schema strings for \`convert_vertical_slash_indexes\` and \`convert_vertical_slash_indexes_mergehead\` in \`csrc/torch_bindings.cpp\` listed \`Tensor |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
