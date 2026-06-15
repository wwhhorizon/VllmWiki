# vllm-project/vllm#32932: [Bug][cpu][arm]: Failure case for BF16 dispatch on non-bf16 supported arm HW

| 字段 | 值 |
| --- | --- |
| Issue | [#32932](https://github.com/vllm-project/vllm/issues/32932) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator |
| 症状 | build_error;crash;import_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][cpu][arm]: Failure case for BF16 dispatch on non-bf16 supported arm HW

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Problem: Failure case on non-bf16 hardware ```python import torch from vllm._custom_ops import cpu_attn_reshape_and_cache key = torch.randn(10, 2, 64, dtype=torch.bfloat16) value = torch.randn(10, 2, 64, dtype=torch.bfloat16) key_cache = torch.empty(8, 2, 16, 64, dtype=torch.bfloat16) value_cache = torch.empty_like(key_cache) slot_mapping = torch.arange(10, dtype=torch.int64) cpu_attn_reshape_and_cache(key, value, key_cache, value_cache, slot_mapping, "neon") ``` ### Error: ```text WARNING 01-23 10:24:27 [interface.py:222] Failed to import from vllm._C: ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') Traceback (most recent call last): File "/path/to/minimal_repro.py", line 10, in cpu_attn_reshape_and_cache(key, value, key_cache, value_cache, slot_mapping, "neon") File "/path/to/site-packages/vllm/_custom_ops.py", line 2942, in cpu_attn_reshape_and_cache torch.ops._C.cpu_attn_reshape_and_cache( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/path/to/site-packages/torch/_ops.py", line 1365, in __getattr__ raise AttributeError( AttributeError: '_OpNamespace' '_C' object has no attribute '...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: cribe the bug ### Problem: Failure case on non-bf16 hardware ```python import torch from vllm._custom_ops import cpu_attn_reshape_and_cache key = torch.randn(10, 2, 64, dtype=torch.bfloat16) value = torch.randn(10, 2, 6...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug][cpu][arm]: Failure case for BF16 dispatch on non-bf16 supported arm HW bug;cpu ### Your current environment ### 🐛 Describe the bug ### Problem: Failure case on non-bf16 hardware ```python import torch from vllm._c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: :24:27 [interface.py:222] Failed to import from vllm._C: ImportError('libcudart.so.12: cannot open shared object file: No such file or directory') Traceback (most recent call last): File "/path/to/minimal_repro.py", lin...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 16, 64, dtype=torch.bfloat16) value_cache = torch.empty_like(key_cache) slot_mapping = torch.arange(10, dtype=torch.int64) cpu_attn_reshape_and_cache(key, value, key_cache, value_cache, slot_mapping, "neon") ``` ### Err...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug][cpu][arm]: Failure case for BF16 dispatch on non-bf16 supported arm HW bug;cpu ### Your current environment ### 🐛 Describe the bug ### Problem: Failure case on non-bf16 hardware ```python import torch from vllm._c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
