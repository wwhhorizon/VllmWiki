# vllm-project/vllm#40632: [Feature]: Support DFlash for Kimi K2.5 and Qwen3.5-27B for AMD

| 字段 | 值 |
| --- | --- |
| Issue | [#40632](https://github.com/vllm-project/vllm/issues/40632) |
| 状态 | closed |
| 标签 | feature request;rocm;speculative-decoding |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;frontend_api;hardware_porting;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | attention |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support DFlash for Kimi K2.5 and Qwen3.5-27B for AMD

### Issue 正文摘录

### 🚀 The feature, motivation and pitch **Feature Proposal Description** Enable support for non-causal attention in AMD backends to allow diffusion-based speculative decoders like DFlash (used with models such as Kimi-K2.5 and Qwen 3.5-27B) to run successfully on AMD hardware. **Motivation** DFlash is a diffusion-based speculative decoding approach with vLLM support that currently works on NVIDIA GPUs but fails on AMD platforms. This limits the usability of emerging decoding techniques and models (e.g., Kimi-K2.5, Qwen3.5-27B) within the AMD ecosystem, creating a feature gap compared to competing hardware. This feature/models works fine on Nvidia ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Support DFlash for Kimi K2.5 and Qwen3.5-27B for AMD feature request;rocm;speculative-decoding ### 🚀 The feature, motivation and pitch **Feature Proposal Description** Enable support for non-causal attention...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e]: Support DFlash for Kimi K2.5 and Qwen3.5-27B for AMD feature request;rocm;speculative-decoding ### 🚀 The feature, motivation and pitch **Feature Proposal Description** Enable support for non-causal attention in AMD...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Support DFlash for Kimi K2.5 and Qwen3.5-27B for AMD feature request;rocm;speculative-decoding ### 🚀 The feature, motivation and pitch **Feature Proposal Description** Enable support for non-causal attention...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: re Proposal Description** Enable support for non-causal attention in AMD backends to allow diffusion-based speculative decoders like DFlash (used with models such as Kimi-K2.5 and Qwen 3.5-27B) to run successfully on AM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development attention_kv_cache;frontend_api;hardware_porting;speculative_decoding att...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
