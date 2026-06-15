# vllm-project/vllm#36805: [Bug]: Misleading error message for FP8 quantization: refers to CUDA version instead of GPU compute capability

| 字段 | 值 |
| --- | --- |
| Issue | [#36805](https://github.com/vllm-project/vllm/issues/36805) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Misleading error message for FP8 quantization: refers to CUDA version instead of GPU compute capability

### Issue 正文摘录

### Your current environment ## Bug description When running vLLM with an FP8 TorchAO quantized model, the following error occurs: ```bash AssertionError: Float8 dynamic activation quantization is only supported on CUDA>=8.9 and MI300+ ``` However, this message is misleading because CUDA toolkit versions are unrelated to the requirement being checked. The code path appears to check GPU compute capability (SM version) instead. ## Root cause The assertion originates from TorchAO: `torchao/quantization/quant_api.py` Relevant code: ```python if torch.cuda.is_available(): assert is_sm_at_least_89() or is_MI300(), ( "Float8 dynamic activation quantization is only supported on CUDA>=8.9 and MI300+" ) ``` The check calls: `is_sm_at_least_89()` which refers to GPU compute capability ≥ 8.9, not a CUDA toolkit version. Therefore, the error message: `CUDA>=8.9` is incorrect and should instead refer to SM / compute capability ≥ 8.9. ## Expected behaviour The message should clarify that the requirement refers to GPU compute capability, not CUDA toolkit version. Example of clearer wording: ```bash Float8 dynamic activation quantization is only supported on GPUs with compute capability >= 8.9 (e....

## 现有链接修复摘要

#36854 [Bugfix] Clear error message for FP8 torchao quantization on unsupported GPUs | #37033 fix: correct FP8 error message to reference compute capability | #37036 fix: correct misleading FP8 error message about CUDA version vs compute capability

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Misleading error message for FP8 quantization: refers to CUDA version instead of GPU compute capability bug ### Your current environment ## Bug description When running vLLM with an FP8 TorchAO quantized model, t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Misleading error message for FP8 quantization: refers to CUDA version instead of GPU compute capability bug ### Your current environment ## Bug description When running vLLM with an FP8 TorchAO quantized model, t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Misleading error message for FP8 quantization: refers to CUDA version instead of GPU compute capability bug ### Your current environment ## Bug description When running vLLM with an FP8 TorchAO quantized model, t...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;mismatch;nan_inf dtype;env_dependency #36854 [Bugfix] Clear error message for FP8 torchao quantization on unsupported GPUs | #3...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: tive_decoding cuda;fp8;operator;quantization;sampling;triton build_error;mismatch;nan_inf dtype;env_dependency #36854 [Bugfix] Clear error message for FP8 torchao quantization on unsupported GPUs | #37033 fix: correct F...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36854](https://github.com/vllm-project/vllm/pull/36854) | closes_keyword | 0.95 | [Bugfix] Clear error message for FP8 torchao quantization on unsupported GPUs | Fixes #36805. When using FP8 activation torchao configs (e.g., `Float8DynamicActivationFloat8WeightConfig`) on GPUs with compute capability < 8.9, torchao raises a confusing `Asser |
| [#37033](https://github.com/vllm-project/vllm/pull/37033) | closes_keyword | 0.95 | fix: correct FP8 error message to reference compute capability | Fixes #36805 ## Details The upstream `torchao` assertion in `quant_api.py` checks `is_sm_at_least_89()` but produces the error: ``` Float8 dynamic activation quantization is onl |
| [#37036](https://github.com/vllm-project/vllm/pull/37036) | closes_keyword | 0.95 | fix: correct misleading FP8 error message about CUDA version vs compute capability | Fixes #36805: The upstream TorchAO assertion error says `CUDA>=8.9` when FP8 dynamic activation quantization fails, but the actual requirement is **GPU compute capability >= 8.9** |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
