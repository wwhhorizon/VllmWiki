# vllm-project/vllm#27607: [Bug]: `KeyError: 'layers.47.mlp.experts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model

| 字段 | 值 |
| --- | --- |
| Issue | [#27607](https://github.com/vllm-project/vllm/issues/27607) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `KeyError: 'layers.47.mlp.experts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model

### Issue 正文摘录

### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One of the layers in the model is unquantized: - Layer 0~46: NVFP4 - Layer 47: BF16 The model is published on HuggingFace: https://huggingface.co/Benasd/Qwen3-30B-A3B-Instruct-2507-NVFP4-BF16-MIXED Serving an NVFP4/BF16 mixed-quantized Qwen3-MoE checkpoint fails during model loading. It seems that vLLM tries to load the unquantized layer as NVFP4. The error does not occur when all layers are quantized to NVFP4. Serve the model: ```bash VLLM_USE_FLASHINFER_MOE_FP4=1 vllm serve Benasd/Qwen3-30B-A3B-Instruct-2507-NVFP4-BF16-MIXED --max_model_len 40960 --host 0.0.0.0 --port 8000 ``` Error: ``` KeyError: 'layers.47.mlp.experts.w2_weight' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#27608 [Bugfix] Respect ignore list for NVFP4/BF16 mixed MoE checkpoints

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: `KeyError: 'layers.47.mlp.experts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model bug;stale ### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One o...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: erts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model bug;stale ### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One of the layers in the model is unquant...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: rror: 'layers.47.mlp.experts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model bug;stale ### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One of the layers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sion `llm-compressor` model bug;stale ### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One of the layers in the model is unquantized: - Layer 0~46: NVFP4 - Layer 47: BF16 The mode...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: `KeyError: 'layers.47.mlp.experts.w2_weight'` loading a NVFP4 + BF16 mixed-precision `llm-compressor` model bug;stale ### Your current environment GPU: RTX 5090 vLLM version: git main ### 🐛 Describe the bug One o...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27608](https://github.com/vllm-project/vllm/pull/27608) | closes_keyword | 0.95 | [Bugfix] Respect ignore list for NVFP4/BF16 mixed MoE checkpoints | Fix #27607 The entire model shares the same quantization configuration, so vLLM attempts to load all layers as NVFP4. None of the methods in the call stack check whether a layer i |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
