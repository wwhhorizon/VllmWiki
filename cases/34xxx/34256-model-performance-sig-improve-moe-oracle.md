# vllm-project/vllm#34256: [Model Performance SIG]: Improve MoE Oracle

| 字段 | 值 |
| --- | --- |
| Issue | [#34256](https://github.com/vllm-project/vllm/issues/34256) |
| 状态 | closed |
| 标签 | feature request;rocm;model-bash |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | fp8;kernel;moe;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Model Performance SIG]: Improve MoE Oracle

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We have recently created programmatic interface for selecting NVFP4 and FP8 MoE kernels. Currently, we have a single "ordering" of kernels for all hardware, device configs, etc. We should make this oracle smarter by having different defaults for different devices / models. We should do this for: - [ ] DeepSeekV3 - [ ] Qwen3MoE - [ ] GLM - [ ] Llama4 Maverick / Scout - [ ] gpt-oss On the following params: - [ ] Device ---> Blackwell, Hopper, MI300, MI350 - [ ] Quantization ---> FP8, FP4 - [ ] Parallel Config ---> A2A backend, EP vs TP ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#35457 [Model Performance] Add Qwen3MoE tuned MoE configs for H200

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Model Performance SIG]: Improve MoE Oracle feature request;rocm;model-bash ### 🚀 The feature, motivation and pitch We have recently created programmatic interface for selecting NVFP4 and FP8 MoE kernels. Currently, we...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: and pitch We have recently created programmatic interface for selecting NVFP4 and FP8 MoE kernels. Currently, we have a single "ordering" of kernels for all hardware, device configs, etc. We should make this oracle smar...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Model Performance SIG]: Improve MoE Oracle feature request;rocm;model-bash ### 🚀 The feature, motivation and pitch We have recently created programmatic interface for selecting NVFP4 and FP8 MoE kernels. Currently, we
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 0, MI350 - [ ] Quantization ---> FP8, FP4 - [ ] Parallel Config ---> A2A backend, EP vs TP ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you alr...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Model Performance SIG]: Improve MoE Oracle feature request;rocm;model-bash ### 🚀 The feature, motivation and pitch We have recently created programmatic interface for selecting NVFP4 and FP8 MoE kernels. Currently, we...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35457](https://github.com/vllm-project/vllm/pull/35457) | mentioned | 0.6 | [Model Performance] Add Qwen3MoE tuned MoE configs for H200 | BF16 (both tuned): - 10-17% faster at batch sizes 4+ Addresses issue #34256 (Improve MoE Oracle for Qwen3MoE on Hopper) |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
