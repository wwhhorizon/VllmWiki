# vllm-project/vllm#29791: [Feature]: Model Generation Monitoring and Intervention (including 1. request-level thinking budget control as supported in Qwen/Claude APIs 2. repetition detection and truncation)

| 字段 | 值 |
| --- | --- |
| Issue | [#29791](https://github.com/vllm-project/vllm/issues/29791) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;moe;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Model Generation Monitoring and Intervention (including 1. request-level thinking budget control as supported in Qwen/Claude APIs 2. repetition detection and truncation)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Summary We are proposing two model generation monitoring and intervention features for more intelligent, efficient, controlled generation: - [ ] Request-level thinking budget control as supported in Qwen/Claude APIs - [ ] Efficient and async repetition detection and truncation These two features support most reasoning models, including open-source openai gpt-oss, deepseek, qwen, and doubao, and all non-reasoning models in a plug-and-play way, as the generation monitoring and intervention are model agnostic and only modifying the final sampled tokens with guided decoding. No fine-tuning is needed! ### Integration with Existing Techniques We tested on a variant of vllm, and these two features successfully support simple integration with all the below features: - Architecture-agnostic: dense/MoE and full/sparse models are supported - Complied CUDA graph - PD disaggregation - Multi-batch inference with continuous batch - Multi-token speculative decoding including MTP, ngram, SAM decoding. (EAGLE is not tested) - Online request-level thinking budget control - Low overhead and async repetition detection and truncation for both thinking and sum...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Model Generation Monitoring and Intervention (including 1. request-level thinking budget control as supported in Qwen/Claude APIs 2. repetition detection and truncation) feature request;stale ### 🚀 The featur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Model Generation Monitoring and Intervention (including 1. request-level thinking budget control as supported in Qwen/Claude APIs 2. repetition detection and truncation) feature request;stale ### 🚀 The featur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: eneration monitoring and intervention features for more intelligent, efficient, controlled generation: - [ ] Request-level thinking budget control as supported in Qwen/Claude APIs - [ ] Efficient and async repetition de...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s successfully support simple integration with all the below features: - Architecture-agnostic: dense/MoE and full/sparse models are supported - Complied CUDA graph - PD disaggregation - Multi-batch inference with conti...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: integration with all the below features: - Architecture-agnostic: dense/MoE and full/sparse models are supported - Complied CUDA graph - PD disaggregation - Multi-batch inference with continuous batch - Multi-token spec...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
