# vllm-project/vllm#40182: [RFC]: Unified ModelOpt Quantization in vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#40182](https://github.com/vllm-project/vllm/issues/40182) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;gemm_linear;hardware_porting;model_support;quantization |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;quantization |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Unified ModelOpt Quantization in vLLM

### Issue 正文摘录

## Summary This issue proposes implementing a bridge that routes ModelOpt checkpoints through vLLM's existing Compressed-Tensors (CT) infrastructure, rather than keeping them on an isolated native path. This mirrors what [SGLang PR #19101](https://github.com/sgl-project/sglang/pull/19101/changes) did with some enhancement proposals --- ## Background This issue aims to expand vLLM's ModelOpt quantization support from the current limited implementation to encompass the full suite of NVIDIA Model Optimizer quantization recipes. Rather than building separate implementations for each format, we propose a unified architecture that bridges ModelOpt checkpoints to vLLM's existing compressed-tensors (llm-compressor) infrastructure, enabling code reuse, kernel sharing, and consistent performance across quantization methods. --- ### Proposed Change The changes need to be done at two levels when ingesting a ModelOpt checkpoint into vLLM through CT infrastructure. 1. The CT config class receives a ModelOpt-shaped dict when it expects a CT-shaped dict. It needs to translate (bridge) the ModelOpt config into the CT style config -> **modelopt_config_to_compressed_tensors_config** 2. The .safetens...

## 现有链接修复摘要

#40888 [Bugfix][Model] Qwen3-VL-MoE NVFP4 (ModelOpt) per-expert weight loading

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: [RFC]: Unified ModelOpt Quantization in vLLM RFC ## Summary This issue proposes implementing a bridge that routes ModelOpt checkpoints through vLLM's existing Compressed-Tensors (CT) infrastructure, rather than keeping...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: building separate implementations for each format, we propose a unified architecture that bridges ModelOpt checkpoints to vLLM's existing compressed-tensors (llm-compressor) infrastructure, enabling code reuse, kernel s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [RFC]: Unified ModelOpt Quantization in vLLM RFC ## Summary This issue proposes implementing a bridge that routes ModelOpt checkpoints through vLLM's existing Compressed-Tensors (CT) infrastructure, rather than keeping...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: caled_mm | ✅ Existing | INT8_DEFAULT_CFG | CompressedTensorsW8A8Int8 | CUTLASS INT8 | 🆕 New | P2(-) INT8_SMOOTHQUANT_CFG | CompressedTensorsW8A8Int8 | CUTLASS INT8 | 🆕 New | P2(-) INT4_AWQ_CFG | CompressedTensorsWNA16 |...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ion to encompass the full suite of NVIDIA Model Optimizer quantization recipes. Rather than building separate implementations for each format, we propose a unified architecture that bridges ModelOpt checkpoints to vLLM'...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40888](https://github.com/vllm-project/vllm/pull/40888) | mentioned | 0.6 | [Bugfix][Model] Qwen3-VL-MoE NVFP4 (ModelOpt) per-expert weight loading | . This PR is **not** a duplicate: the only adjacent open work is RFC #40182 (long-term unified ModelOpt path) and the per-model fix series #39045/#39256/#39084/#39406 (Gemma 4 onl… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
