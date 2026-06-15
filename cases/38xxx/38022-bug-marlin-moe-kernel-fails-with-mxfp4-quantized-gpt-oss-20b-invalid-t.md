# vllm-project/vllm#38022: [Bug]: Marlin MoE kernel fails with MXFP4-quantized GPT-OSS 20B - Invalid thread config for non-aligned dimensions (K=2880, N=2880)

| 字段 | 值 |
| --- | --- |
| Issue | [#38022](https://github.com/vllm-project/vllm/issues/38022) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;fp8;gemm;kernel;moe;operator;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Marlin MoE kernel fails with MXFP4-quantized GPT-OSS 20B - Invalid thread config for non-aligned dimensions (K=2880, N=2880)

### Issue 正文摘录

### Your current environment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10.0+cu128 - **CUDA version**: 12.8 - **GPU**: NVIDIA RTX PRO 6000 Blackwell Server Edition (96 GB) - **Driver**: 580.126.09 - **Python**: 3.12.3 - **Transformers**: 4.57.3 - **compressed-tensors**: 0.13.0 - **OS**: Ubuntu (Linux 6.17.0-1009-aws) ## Model `openai/gpt-oss-20b` — a Mixture-of-Experts model with 32 experts (4 active per token), `hidden_size=2880`, `intermediate_size=2880`, `head_dim=64`. The model was fine-tuned (LoRA SFT), merged, and quantized to MXFP4 format using `llmcompressor` with `compressed-tensors`. The resulting `config.json` shows `quant_method: "compressed-tensors"` with `format: "mxfp4-pack-quantized"`, `group_size: 32`, `num_bits: 4`. ### 🐛 Describe the bug ## How to reproduce ```bash vllm serve \ --dtype bfloat16 \ --max-model-len 32768 \ --gpu-memory-utilization 0.90 ``` The model loads successfully to GPU, but crashes on the first inference request. ## Description When serving an MXFP4-quantized GPT-OSS 20B model (MoE architecture), vLLM crashes at inference time with a `RuntimeError` from the Marlin MoE GEMM kernel. The kernel fails to compute a valid thread configurat...

## 现有链接修复摘要

#38222 [Bugfix] Add dimension alignment check to Marlin MoE kernel selection

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [Bug]: Marlin MoE kernel fails with MXFP4-quantized GPT-OSS 20B - Invalid thread config for non-aligned dimensions (K=2880, N=2880) bug ### Your current environment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d dimensions (K=2880, N=2880) bug ### Your current environment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10.0+cu128 - **CUDA version**: 12.8 - **GPU**: NVIDIA RTX PRO 6000 Blackwell Server Edition (96 GB) - **...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10.0+cu128 - **CUDA version**: 12.8 - **GPU**: NVIDIA RTX PRO 6000 Blackwell Server Edition (96 GB) - **Driver**: 580.126.09 - **Python**: 3.12.3 - **Transformers...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Marlin MoE kernel fails with MXFP4-quantized GPT-OSS 20B - Invalid thread config for non-aligned dimensions (K=2880, N=2880) bug ### Your current environment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Marlin MoE kernel fails with MXFP4-quantized GPT-OSS 20B - Invalid thread config for non-aligned dimensions (K=2880, N=2880) bug ### Your current environment - **vLLM version**: 0.18.0 - **PyTorch version**: 2.10...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#38222](https://github.com/vllm-project/vllm/pull/38222) | closes_keyword | 0.95 | [Bugfix] Add dimension alignment check to Marlin MoE kernel selection | Fixes #38022 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
