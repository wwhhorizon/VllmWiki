# vllm-project/vllm#34331: [RFC]: Ahead of time dequantization of weights for quantization emulation (OCP MX, NVFP4) on unsupported devices

| 字段 | 值 |
| --- | --- |
| Issue | [#34331](https://github.com/vllm-project/vllm/issues/34331) |
| 状态 | closed |
| 标签 | rocm;RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | hardware_porting;moe;quantization |
| 子分类 | precision |
| Operator 关键词 | moe;quantization |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Ahead of time dequantization of weights for quantization emulation (OCP MX, NVFP4) on unsupported devices

### Issue 正文摘录

### Motivation. Hi, opening this for comment. At the moment, vLLM has some support for quantization simulation of MXFP4/MXFP6/NVFP4 models for execution on devices that do not support these dtypes: - Quark OCP MX (dense & MOE) at https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py - compressed-tensors NVFP4 (e.g. https://huggingface.co/RedHatAI/Qwen3-8B-NVFP4, no MOE emulation support atm) This is for example useful for research purposes on microscaling data types, where simulating large models execution with high throughput is critical (e.g. running eval). The current behavior is to keep weights in low precision, and dequantize them in forward calls, see e.g. https://github.com/vllm-project/vllm/blob/e09546cf05f12c041083c289c24ecb48896f9620/vllm/model_executor/layers/quantization/quark/schemes/quark_ocp_mx.py#L342-L345 or https://github.com/vllm-project/vllm/blob/e09546cf05f12c041083c289c24ecb48896f9620/vllm/model_executor/layers/quantization/utils/nvfp4_emulation_utils.py#L128-L137 Although working, dequantizing weights at each forward call is not tractable when running large workloads with such models (e.g. end-to...

## 现有链接修复摘要

#34481 [Bugfix][Hardware][AMD] Add ahead-of-time weight dequantization for quantization emulation | #38728 [Quantization] Convert NVFP4 weights to FP8 on Hopper for faster inference

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [RFC]: Ahead of time dequantization of weights for quantization emulation (OCP MX, NVFP4) on unsupported devices rocm;RFC ### Motivation. Hi, opening this for comment. At the moment, vLLM has some support for quantizati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: , vLLM has some support for quantization simulation of MXFP4/MXFP6/NVFP4 models for execution on devices that do not support these dtypes: - Quark OCP MX (dense & MOE) at https://github.com/vllm-project/vllm/blob/main/v...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: eights for quantization emulation (OCP MX, NVFP4) on unsupported devices rocm;RFC ### Motivation. Hi, opening this for comment. At the moment, vLLM has some support for quantization simulation of MXFP4/MXFP6/NVFP4 model...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: croscaling data types, where simulating large models execution with high throughput is critical (e.g. running eval). The current behavior is to keep weights in low precision, and dequantize them in forward calls, see e....
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: cal (e.g. running eval). The current behavior is to keep weights in low precision, and dequantize them in forward calls, see e.g. https://github.com/vllm-project/vllm/blob/e09546cf05f12c041083c289c24ecb48896f9620/vllm/m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#34481](https://github.com/vllm-project/vllm/pull/34481) | mentioned | 0.6 | [Bugfix][Hardware][AMD] Add ahead-of-time weight dequantization for quantization emulation | LLM_EMULATION_DEQUANT_WEIGHTS_AOT=1 vllm serve <model> ``` Addresses #34331 ## Test plan - Run MXFP4 model on MI300X with and without `VLLM_EMULATION_DEQUANT_WEIGHTS_AOT=1` — veri… |
| [#38728](https://github.com/vllm-project/vllm/pull/38728) | mentioned | 0.6 | [Quantization] Convert NVFP4 weights to FP8 on Hopper for faster inference | not a duplicate of any existing PR — the closest upstream work is RFC #34331 (AOT dequant to BF16) which uses 4x more memory. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
