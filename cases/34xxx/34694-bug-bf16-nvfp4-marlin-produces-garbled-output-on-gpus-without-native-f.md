# vllm-project/vllm#34694: [Bug]: BF16 NVFP4 Marlin produces garbled output on GPUs without native FP4 support

| 字段 | 值 |
| --- | --- |
| Issue | [#34694](https://github.com/vllm-project/vllm/issues/34694) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: BF16 NVFP4 Marlin produces garbled output on GPUs without native FP4 support

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Describe NVFP4 quantized models produce garbled output when running with `--dtype bfloat16` on GPUs without native FP4 support (e.g., RTX 4090 SM89, V100 SM70). These GPUs fall back to the Marlin kernel for FP4 weight dequantization. `dequant_fp8_scales ` in `csrc/quantization/marlin/dequant.h` has incorrect exponent widening from S0E5M3 (5-bit exponent, bias 15) to BF16 (8-bit exponent, bias 127). The 3 middle exponent bits are always zero, producing BF16 exponent `E4 0 0 0 E3 E2 E1 E0` instead of the correct `E4 !E4 !E4 !E4 E3 E2 E1 E0`. This creates a gap in the exponent space — for most real model scale values (E4=0), the BF16 scale is interpreted as ~2^(-112) instead of ~2^0, causing weight × scale to underflow to zero. This affects **all** BF16 NVFP4 models on non-native-FP4 GPUs. FP16 path is unaffected (5-bit exponent maps directly to FP16's 5-bit exponent). ## How to reproduce ```bash vllm serve --dtype bfloat16 # on any GPU without native FP4 (SM < 100) # model outputs are completely wrong / garbled ``` Tested with [GLM-4.7-Flash-NVFP4](https://huggingface.co/GadflyII/GLM-4.7-Flash-NVFP4): - 54.7% of output values ar...

## 现有链接修复摘要

#34577 [Bugfix] Rescale NVFP4 weight scales to fix BF16 dequant underflow

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 10: [Bug]: BF16 NVFP4 Marlin produces garbled output on GPUs without native FP4 support bug ### Your current environment ### 🐛 Describe the bug ## Describe NVFP4 quantized models produce garbled output when running with `--...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: unning with `--dtype bfloat16` on GPUs without native FP4 support (e.g., RTX 4090 SM89, V100 SM70). These GPUs fall back to the Marlin kernel for FP4 weight dequantization. `dequant_fp8_scales ` in `csrc/quantization/ma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: it exponent, bias 127). The 3 middle exponent bits are always zero, producing BF16 exponent `E4 0 0 0 E3 E2 E1 E0` instead of the correct `E4 !E4 !E4 !E4 E3 E2 E1 E0`. This creates a gap in the exponent space — for most...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: cted (5-bit exponent maps directly to FP16's 5-bit exponent). ## How to reproduce ```bash vllm serve --dtype bfloat16 # on any GPU without native FP4 (SM < 100) # model outputs are completely wrong / garbled ``` Tested...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rrent environment ### 🐛 Describe the bug ## Describe NVFP4 quantized models produce garbled output when running with `--dtype bfloat16` on GPUs without native FP4 support (e.g., RTX 4090 SM89, V100 SM70). These GPUs fal...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34577](https://github.com/vllm-project/vllm/pull/34577) | closes_keyword | 0.95 | [Bugfix] Rescale NVFP4 weight scales to fix BF16 dequant underflow | fix) Related #34694 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
