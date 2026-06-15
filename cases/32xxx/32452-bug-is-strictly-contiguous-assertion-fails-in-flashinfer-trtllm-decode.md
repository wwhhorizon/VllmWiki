# vllm-project/vllm#32452: [Bug]: `is_strictly_contiguous` assertion fails in FlashInfer TRTLLM decode path on Blackwell for Scout

| 字段 | 值 |
| --- | --- |
| Issue | [#32452](https://github.com/vllm-project/vllm/issues/32452) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;fp8;moe;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: `is_strictly_contiguous` assertion fails in FlashInfer TRTLLM decode path on Blackwell for Scout

### Issue 正文摘录

### Your current environment - vLLM version: main (post PR #32008) - GPU: NVIDIA B200 (Blackwell, SM100) - PyTorch version: 2.x - CUDA version: 12.x - OS: Linux ## Model Information - Model: `meta-llama/Llama-4-Scout-17B-16E-Instruct` (MoE model) - TP Size: 2 - Quantization: None (also reproduces with FP8) ### 🐛 Describe the bug After PR #32008 introduced `is_strictly_contiguous` checks in the FlashInfer TRTLLM attention path, an assertion fails during decode on Blackwell (B200) GPUs: ``` AssertionError: assert is_strictly_contiguous(decode_query) ``` The issue occurs at `vllm/v1/attention/backends/flashinfer.py` line 1507. ### Root Cause The problem is that `.contiguous()` alone doesn't guarantee canonical strides for tensors with singleton dimensions. When `decode_query` is sliced from the padded query tensor: ```python decode_query = query[:num_decode_tokens] # line 1453 decode_query = decode_query.contiguous() # line 1500 ``` The sliced tensor may have "degenerate strides" - where a dimension has size 1 but the stride doesn't match the expected canonical contiguous layout. PyTorch's `.is_contiguous()` returns `True` for such tensors, but `is_strictly_contiguous()` correctly id...

## 现有链接修复摘要

#32008 [MISC] Add strict contiguity check for FlashInfer attention tensors

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: strictly_contiguous` assertion fails in FlashInfer TRTLLM decode path on Blackwell for Scout bug ### Your current environment - vLLM version: main (post PR #32008) - GPU: NVIDIA B200 (Blackwell, SM100) - PyTorch version...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ode path on Blackwell for Scout bug ### Your current environment - vLLM version: main (post PR #32008) - GPU: NVIDIA B200 (Blackwell, SM100) - PyTorch version: 2.x - CUDA version: 12.x - OS: Linux ## Model Information -...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : `meta-llama/Llama-4-Scout-17B-16E-Instruct` (MoE model) - TP Size: 2 - Quantization: None (also reproduces with FP8) ### 🐛 Describe the bug After PR #32008 introduced `is_strictly_contiguous` checks in the FlashInfer...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: `is_strictly_contiguous` assertion fails in FlashInfer TRTLLM decode path on Blackwell for Scout bug ### Your current environment - vLLM version: main (post PR #32008) - GPU: NVIDIA B200 (Blackwell, SM100) - PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: well, SM100) - PyTorch version: 2.x - CUDA version: 12.x - OS: Linux ## Model Information - Model: `meta-llama/Llama-4-Scout-17B-16E-Instruct` (MoE model) - TP Size: 2 - Quantization: None (also reproduces with FP8) ###...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32008](https://github.com/vllm-project/vllm/pull/32008) | mentioned | 0.45 | [MISC] Add strict contiguity check for FlashInfer attention tensors | n: none (also reproduces with fp8) ### 🐛 describe the bug after pr #32008 introduced `is_strictly_contiguous` checks in the flashinfer trtllm attention path, an assertion fails du… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
