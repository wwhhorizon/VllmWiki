# vllm-project/vllm#35663: [Bug]: Nightly takes >3x time to load weights compared to v0.16.0 and earlier nightlies

| 字段 | 值 |
| --- | --- |
| Issue | [#35663](https://github.com/vllm-project/vllm/issues/35663) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Nightly takes >3x time to load weights compared to v0.16.0 and earlier nightlies

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Loosely, but not completely related to https://github.com/vllm-project/vllm/issues/35547. For `Loading safetensors checkpoint shards`: Multiple models such as MiniMax-M2.5 (up from 1-3 seconds/shard to 19 seconds/shard), Kimi-K2.5 (up from 10 seconds/shard to 35 seconds/shard) are taking much longer to load in the nightly releases after v0.16.0 on A100 GPUs, at the very least. Started somewhere around `nightly-8fae54faff485e446dc8d1a700417f07659ef89e`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: are taking much longer to load in the nightly releases after v0.16.0 on A100 GPUs, at the very least. Started somewhere around `nightly-8fae54faff485e446dc8d1a700417f07659ef89e`. ### Before submitting a new issue... - [...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm/issues/35547. For `Loading safetensors checkpoint shards`: Multiple models such as MiniMax-M2.5 (up from 1-3 seconds/shard to 19 seconds/shard), Kimi-K2.5 (up from 10 seconds/shard to 35 seconds/shard) are taking muc...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Yo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
