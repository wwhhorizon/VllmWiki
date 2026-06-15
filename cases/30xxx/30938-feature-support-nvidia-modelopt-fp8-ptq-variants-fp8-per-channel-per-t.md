# vllm-project/vllm#30938: [Feature]: Support NVIDIA ModelOpt FP8 PTQ variants (FP8_PER_CHANNEL_PER_TOKEN / FP8_PB_WO) in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#30938](https://github.com/vllm-project/vllm/issues/30938) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;frontend_api;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | fp8;quantization |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support NVIDIA ModelOpt FP8 PTQ variants (FP8_PER_CHANNEL_PER_TOKEN / FP8_PB_WO) in vLLM

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Current behavior vLLM’s built-in modelopt quantization support only recognizes a limited set of ModelOpt checkpoint formats (e.g., quant_algo: "FP8" and NVFP4). When loading newer ModelOpt FP8 PTQ exports such as: - FP8_PER_CHANNEL_PER_TOKEN (per-channel weight scale + per-token dynamic activation quantization) - fp8_pb_wo / FP8_PB_WO (block-scaled FP8 weight-only with 4D block scales) vLLM fails early during config parsing / quantization method selection (e.g., “Unknown ModelOpt quant algo …”), so these checkpoints cannot be loaded for inference. ### Motivation ModelOpt FP8 PTQ variants are increasingly used on Hopper/H200 to balance model size, throughput, and accuracy. Being able to directly load and serve these HuggingFace-exported ModelOpt checkpoints in vLLM (via quantization="modelopt") would: - reduce conversion friction for users already using ModelOpt, - enable straightforward benchmarking across ModelOpt FP8 variants, - make vLLM a more complete inference target for ModelOpt PTQ pipelines. ### Alternatives ### Proposed change Extend the modelopt quantization path to: - recognize quant_algo values FP8_PER_CHANNEL_PER_TOKEN and...

## 现有链接修复摘要

#30957 [Feature]: Support NVIDIA ModelOpt HF FP8 variants FP8_PER_CHANNEL_PER_TOKEN and FP8_PB_WO in vLLM

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Feature]: Support NVIDIA ModelOpt FP8 PTQ variants (FP8_PER_CHANNEL_PER_TOKEN / FP8_PB_WO) in vLLM feature request;stale ### 🚀 The feature, motivation and pitch ### Current behavior vLLM’s built-in modelopt quantizatio...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Feature]: Support NVIDIA ModelOpt FP8 PTQ variants (FP8_PER_CHANNEL_PER_TOKEN / FP8_PB_WO) in vLLM feature request;stale ### 🚀 The feature, motivation and pitch ### Current behavior vLLM’s built-in modelopt quantizatio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: PTQ variants are increasingly used on Hopper/H200 to balance model size, throughput, and accuracy. Being able to directly load and serve these HuggingFace-exported ModelOpt checkpoints in vLLM (via quantization="modelop...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ce. ### Motivation ModelOpt FP8 PTQ variants are increasingly used on Hopper/H200 to balance model size, throughput, and accuracy. Being able to directly load and serve these HuggingFace-exported ModelOpt checkpoints in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: + per-token dynamic activation quantization) - fp8_pb_wo / FP8_PB_WO (block-scaled FP8 weight-only with 4D block scales) vLLM fails early during config parsing / quantization method selection (e.g., “Unknown ModelOpt qu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#30957](https://github.com/vllm-project/vllm/pull/30957) | closes_keyword | 0.95 | [Feature]: Support NVIDIA ModelOpt HF FP8 variants FP8_PER_CHANNEL_PER_TOKEN and FP8_PB_WO  in vLLM | Fixes/Addresses: Issue #30938 ## Test Plan Local (artifact-gated) unit tests: - VLLM_TEST_MODELOPT_FP8_PC_PT_MODEL_PATH=/path/to/hf_fp8_pc_pt pytest -q tests/ quantiza |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
