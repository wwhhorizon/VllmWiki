# vllm-project/vllm#40851: [Feature]: DeepSeek-V4 Flash sm_80 (A100/A800) support

| 字段 | 值 |
| --- | --- |
| Issue | [#40851](https://github.com/vllm-project/vllm/issues/40851) |
| 状态 | open |
| 标签 | feature request;DSv4 |
| 评论 | 20; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 | latency_reg |
| Operator 关键词 | fp8;kernel;moe |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: DeepSeek-V4 Flash sm_80 (A100/A800) support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am trying to run DeepSeek-V4-Flash on NVIDIA A800 GPUs, which are sm_80 / Ampere GPUs. Currently, using `vllm/vllm-openai:deepseekv4-cu129`, the model fails during initialization with: ```text RuntimeError: Assertion error (.../deepgemm-src/csrc/apis/hyperconnection.hpp:56): Unsupported architecture ``` This still happens with --enforce-eager, so it seems related to the DeepGEMM / HyperConnection kernels rather than torch.compile. Are there any plans to support sm_80 GPUs such as A100/A800 for DeepSeek-V4, possibly with a slower fallback path? A100/A800 GPUs are still widely used in many research and production clusters, so even a functional fallback would be very helpful. ### Alternatives The current alternatives seem to be: 1. Use newer GPUs such as H100/H200/B200. 2. Wait for a backend/kernel fallback that supports sm_80. I am not sure whether sm_80 support is planned or whether it should currently be considered unsupported for this model. ### Additional context Environment: - GPU: NVIDIA A800, sm_80 / Ampere - vLLM image: `vllm/vllm-openai:deepseekv4-cu129` - Model: `DeepSeek-V4-Flash` - Single node, 8 GPUs Simplified command: ```bash...

## 现有链接修复摘要

#40906 [WIP][New Model] Add A100/SM80 support for DeepSeek V4 Flash

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Feature]: DeepSeek-V4 Flash sm_80 (A100/A800) support feature request;DSv4 ### 🚀 The feature, motivation and pitch I am trying to run DeepSeek-V4-Flash on NVIDIA A800 GPUs, which are sm_80 / Ampere GPUs. Currently, usi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: eems related to the DeepGEMM / HyperConnection kernels rather than torch.compile. Are there any plans to support sm_80 GPUs such as A100/A800 for DeepSeek-V4, possibly with a slower fallback path? A100/A800 GPUs are sti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: /workspace/DeepSeek-V4-Flash \ --served-model-name dsv4-flash \ --dtype bfloat16 \ --kv-cache-dtype fp8 \ --enable-expert-parallel \ --data-parallel-size 4 \ --enforce-eager ``` ### Before submitting a new issue... - [x...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: ing initialization with: ```text RuntimeError: Assertion error (.../deepgemm-src/csrc/apis/hyperconnection.hpp:56): Unsupported architecture ``` This still happens with --enforce-eager, so it seems related to the DeepGE...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ort sm_80 GPUs such as A100/A800 for DeepSeek-V4, possibly with a slower fallback path? A100/A800 GPUs are still widely used in many research and production clusters, so even a functional fallback would be very helpful....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40906](https://github.com/vllm-project/vllm/pull/40906) | closes_keyword | 0.95 | [WIP][New Model] Add A100/SM80 support for DeepSeek V4 Flash | Fix #40851 This PR adds DeepSeek V4 support on A100/A800 (SM80), where DeepGEMM (hyperconnection / fp8_einsum / fp8_fp4_(paged_)mqa_logits) and FlashMLA-Sparse are unavailable, an |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
