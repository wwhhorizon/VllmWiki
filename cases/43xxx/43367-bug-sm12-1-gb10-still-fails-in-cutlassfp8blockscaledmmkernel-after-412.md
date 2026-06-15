# vllm-project/vllm#43367: [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel after #41215

| 字段 | 值 |
| --- | --- |
| Issue | [#43367](https://github.com/vllm-project/vllm/issues/43367) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel after #41215

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug CutlassFp8BlockScaledMMKernel still fails on GB10 / SM12.1 in the refreshed `cu129-nightly-aarch64` image that includes #41215. The server fails during startup/profile when vLLM selects the CUTLASS FP8 block-scaled kernel: Selected `CutlassFp8BlockScaledMMKernel` for `Fp8LinearMethod` Disabling only that kernel makes the same model/config start successfully through `TritonFp8BlockScaledMMKernel`, so the failure appears isolated to the SM120 CUTLASS blockwise FP8 path rather than the model, CUDA visibility, long context, or server configuration. `export VLLM_DISABLED_KERNELS=CutlassFp8BlockScaledMMKernel` With that workaround, vLLM selects: `Selected TritonFp8BlockScaledMMKernel for Fp8LinearMethod` The workaround is diagnostic only. We do not want GB10 / SM12.1 permanently routed away from the optimized CUTLASS FP8 block-scaled path. ## Minimal reproducer This reproduces the same `cutlass_gemm_caller.cuh:61` Error Internal outside the OpenAI server path, using only the vLLM custom op and synthetic tensors. It does not require downloading the full model. Run inside `vllm/vllm-openai:cu129-nightly-aarch64 `on GB10 / SM12.1: ```pyth...

## 现有链接修复摘要

#41215 [Bugfix] Use enable_sm120_family for per-tensor FP8 CUTLASS kernels on SM12.1

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel after #41215 bug ### Your current environment ### 🐛 Describe the bug CutlassFp8BlockScaledMMKernel still fails on GB10 / SM12.1 in the refreshed `cu129-n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: de `vllm/vllm-openai:cu129-nightly-aarch64 `on GB10 / SM12.1: ```python import torch from vllm import _custom_ops as ops m, n, k = 1, 16384, 5120 a = torch.randn((m, k), device="cuda").to(torch.float8_e4m3fn) # Match vL...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel after #41215 bug ### Your current environment ### 🐛 Describe the bug CutlassFp8BlockScaledMMKernel still fails on GB10 / SM12.1 in the refreshed `cu129-n...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: SM12.1 / GB10 still fails in CutlassFp8BlockScaledMMKernel after #41215 bug ### Your current environment ### 🐛 Describe the bug CutlassFp8BlockScaledMMKernel still fails on GB10 / SM12.1 in the refreshed `cu129-n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Kernel` for `Fp8LinearMethod` Disabling only that kernel makes the same model/config start successfully through `TritonFp8BlockScaledMMKernel`, so the failure appears isolated to the SM120 CUTLASS blockwise FP8 path rat...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#41215](https://github.com/vllm-project/vllm/pull/41215) | mentioned | 0.45 | [Bugfix] Use enable_sm120_family for per-tensor FP8 CUTLASS kernels on SM12.1 | / sm12.1 in the refreshed `cu129-nightly-aarch64` image that includes #41215. the server fails during startup/profile when vllm selects the cutlass fp8 block-scaled kernel: select… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
