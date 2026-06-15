# vllm-project/vllm#44281: [Bug]:  Deployed Qwen3.5-122B-A10B at L20 node 8; after a period of operation, the EngineCore encountered an issue.

| 字段 | 值 |
| --- | --- |
| Issue | [#44281](https://github.com/vllm-project/vllm/issues/44281) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Deployed Qwen3.5-122B-A10B at L20 node 8; after a period of operation, the EngineCore encountered an issue.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Would Moe models not be suitable for L20? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cache;cuda;moe;oper...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 20? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Deployed Qwen3.5-122B-A10B at L20 node 8; after a period of operation, the EngineCore encountered an issue. bug ### Your current environment ### 🐛 Describe the bug Would Moe models not be suitable for L20? ### Be...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: bug ### Your current environment ### 🐛 Describe the bug Would Moe models not be suitable for L20? ### Before submitting a new issue... - [ ] Make sure you already searched for relevant issues, and asked the chatbot livi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: oe;sampling_logits;speculative_decoding cache;cuda;moe;operator;sampling;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
