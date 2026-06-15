# vllm-project/vllm#44110: [Bug] MarlinFP8 kernel silently skips weight transpose for square matrices (N==K), corrupting FP8 inference on sm_75–sm_88 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#44110](https://github.com/vllm-project/vllm/issues/44110) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;gemm;kernel;quantization |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] MarlinFP8 kernel silently skips weight transpose for square matrices (N==K), corrupting FP8 inference on sm_75–sm_88 GPUs

### Issue 正文摘录

## Environment - **GPU**: sm_75–sm_88 (e.g. A10, A40, RTX A6000) — any GPU where `supports_fp8()` returns `False` - **Model**: any FP8 model with square weight matrices, e.g. `ibm-granite/granite-4.1-8b-fp8` - **Quantization**: `compressed-tensors` or `modelopt` FP8 with channel/tensor-wise scales ## Symptoms FP8 models produce garbage output (repeated punctuation, incoherent tokens) on GPUs lacking native FP8 compute, while the identical non-FP8 model works correctly on the same hardware. No errors, no NaN — silent data corruption. ``` # FP8 model on A40 (sm_86) OUTPUT: ',,,,,,,,,,,,,,,,,,,,' # BF16 model on A40 (sm_86) OUTPUT: 'The capital of France is Paris...' ``` ## Root Cause `MarlinFP8ScaledMMLinearKernel.process_weights_after_loading` uses a shape comparison to decide whether to transpose the weight to `(K, N)` before passing it to the Marlin kernel: ```python # vllm/model_executor/kernels/linear/scaled_mm/marlin.py if w_q.shape != (layer.input_size_per_partition, layer.output_size_per_partition): replace_parameter(layer, "weight", w_q.t()) ``` For **square matrices where `N == K`** (e.g. `q_proj` and `o_proj` where `hidden_dim × hidden_dim = 4096×4096`), the tuples `(N, K...

## 现有链接修复摘要

#44113 [Bugfix] Fix MarlinFP8 weight transpose silently skipped for square matrices (N==K)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug] MarlinFP8 kernel silently skips weight transpose for square matrices (N==K), corrupting FP8 inference on sm_75–sm_88 GPUs ## Environment - **GPU**: sm_75–sm_88 (e.g. A10, A40, RTX A6000) — any GPU where `supports_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: LinearKernel.process_weights_after_loading` uses a shape comparison to decide whether to transpose the weight to `(K, N)` before passing it to the Marlin kernel: ```python # vllm/model_executor/kernels/linear/scaled_mm/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: weight transpose for square matrices (N==K), corrupting FP8 inference on sm_75–sm_88 GPUs ## Environment - **GPU**: sm_75–sm_88 (e.g. A10, A40, RTX A6000) — any GPU where `supports_fp8()` returns `False` - **Model**: an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: the tuples `(N, K)` and `(K, N)` are **identical**. The condition always evaluates `False` and the transpose is silently skipped. The weight stays in `(N, K)` checkpoint orientation when Marlin requires `(K, N)`, produc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: 8 (e.g. A10, A40, RTX A6000) — any GPU where `supports_fp8()` returns `False` - **Model**: any FP8 model with square weight matrices, e.g. `ibm-granite/granite-4.1-8b-fp8` - **Quantization**: `compressed-tensors` or `mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44113](https://github.com/vllm-project/vllm/pull/44113) | closes_keyword | 0.95 | [Bugfix] Fix MarlinFP8 weight transpose silently skipped for square matrices (N==K) | Fixes #44110. ### Root Cause `process_weights_after_loading` used a shape comparison to decide whether to transpose the weight to `(K, N)` before passing it to Marlin: ``` |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
