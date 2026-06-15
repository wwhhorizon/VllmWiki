# vllm-project/vllm#40994: [Bug]: vllm does not expose /v1/audio/transcriptions for google/gemma-4-E4B-it

| 字段 | 值 |
| --- | --- |
| Issue | [#40994](https://github.com/vllm-project/vllm/issues/40994) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm does not expose /v1/audio/transcriptions for google/gemma-4-E4B-it

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When serving google/gemma-4-E4B-it with: `vllm serve google/gemma-4-E4B-it` the OpenAI-compatible `/v1/audio/transcriptions` endpoint is not available. This is an issue because `google/gemma-4-E4B-it` is a multimodal model with audio support, but local agents and client applications commonly rely on `/v1/audio/transcriptions` for speech/audio input. As a result, the model cannot be used as a drop-in local backend for these agent workflows. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: vllm does not expose /v1/audio/transcriptions for google/gemma-4-E4B-it bug ### Your current environment ### 🐛 Describe the bug When serving google/gemma-4-E4B-it with: `vllm serve google/gemma-4-E4B-it` the Open...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding cuda;ope...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ch/audio input. As a result, the model cannot be used as a drop-in local backend for these agent workflows. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ws. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: vllm does not expose /v1/audio/transcriptions for google/gemma-4-E4B-it bug ### Your current environment ### 🐛 Describe the bug When serving google/gemma-4-E4B-it with: `vllm serve google/gemma-4-E4B-it` the Open...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
