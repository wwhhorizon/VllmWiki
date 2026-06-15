# vllm-project/vllm#26700: [Bug][ROCm]: W8A8BlockFp8LinearOp does not use AITER on MI355X

| 字段 | 值 |
| --- | --- |
| Issue | [#26700](https://github.com/vllm-project/vllm/issues/26700) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;quantization;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug][ROCm]: W8A8BlockFp8LinearOp does not use AITER on MI355X

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug On MI355X, `W8A8BlockFp8LinearOp` chooses the fallback branch `_run_triton` instead of the more performant branch `_run_aiter`. This results in suboptimal performance. ## Root cause Incorrect use of the `is_fp8_fnuz` condition. The `is_fp8_fnuz` condition should only be used to check if FP8 indeed uses the FP8-FNUZ (Finite and NaN Only) format. It should not be used as generic condition to disable kernels on platforms older than MI300X. MI355X does not use the FP8-FNUZ format, and thus `is_fp8_fnuz` returns False. https://rocm.docs.amd.com/projects/HIP/en/latest/reference/low_fp_types.html#fp8-quarter-precision The issue was introduced in PR #21242 commit [e626d28](https://github.com/vllm-project/vllm/commit/e626d286f5ac997bca5bd635c3db9e457fe91df9) vllm/model_executor/layers/quantization/utils/fp8_utils.py line 86 ## Proposed fix Each kernel (ar at least each group of associated kernels) should have its own list of supported archs, making it straightforward to enable a kernel on new archs without affecting other code. It is not acceptable to make `is_fp8_fnuz` return True on MI355X, as that would cause incorrect normalization an...

## 现有链接修复摘要

#21242 [FEAT] [ROCm] [AITER]: Add AITER HIP block quant kernel | #26701 [ROCm]: W8A8BlockFp8LinearOp should use AITER on MI355X

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug][ROCm]: W8A8BlockFp8LinearOp does not use AITER on MI355X bug;rocm ### Your current environment ### 🐛 Describe the bug On MI355X, `W8A8BlockFp8LinearOp` chooses the fallback branch `_run_triton` instead of the more...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug][ROCm]: W8A8BlockFp8LinearOp does not use AITER on MI355X bug;rocm ### Your current environment ### 🐛 Describe the bug On MI355X, `W8A8BlockFp8LinearOp` chooses the fallback branch `_run_triton` instead of the more...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: md.com/projects/HIP/en/latest/reference/low_fp_types.html#fp8-quarter-precision The issue was introduced in PR #21242 commit [e626d28](https://github.com/vllm-project/vllm/commit/e626d286f5ac997bca5bd635c3db9e457fe91df9...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug][ROCm]: W8A8BlockFp8LinearOp does not use AITER on MI355X bug;rocm ### Your current environment ### 🐛 Describe the bug On MI355X, `W8A8BlockFp8LinearOp` chooses the fallback branch `_run_triton` instead of the more...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: s.amd.com/projects/HIP/en/latest/reference/low_fp_types.html#fp8-quarter-precision The issue was introduced in PR #21242 commit [e626d28](https://github.com/vllm-project/vllm/commit/e626d286f5ac997bca5bd635c3db9e457fe91...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#21242](https://github.com/vllm-project/vllm/pull/21242) | mentioned | 0.45 | [FEAT] [ROCm] [AITER]: Add AITER HIP block quant kernel | w_fp_types.html#fp8-quarter-precision the issue was introduced in pr #21242 commit [e626d28](https://github.com/vllm-project/vllm/commit/e626d286f5ac997bca5bd635c3db9e457fe91df9)… |
| [#26701](https://github.com/vllm-project/vllm/pull/26701) | closes_keyword | 0.95 | [ROCm]: W8A8BlockFp8LinearOp should use AITER on MI355X | Closes: #26700 On MI355X, `W8A8BlockFp8LinearOp` chooses the fallback branch `_run_triton` instead of the more performant branch `_run_aiter`. This results in suboptimal performan |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
