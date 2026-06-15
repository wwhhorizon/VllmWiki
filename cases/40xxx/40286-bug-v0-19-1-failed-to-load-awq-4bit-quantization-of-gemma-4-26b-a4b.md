# vllm-project/vllm#40286: [Bug]: v0.19.1 failed to load AWQ 4bit quantization of Gemma 4 26B-A4B

| 字段 | 值 |
| --- | --- |
| Issue | [#40286](https://github.com/vllm-project/vllm/issues/40286) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.19.1 failed to load AWQ 4bit quantization of Gemma 4 26B-A4B

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug It fails to load and gives the error below: ``` KeyError: 'layers.0.moe.experts.0.down_proj_packed' ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding cuda;m...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: v0.19.1 failed to load AWQ 4bit quantization of Gemma 4 26B-A4B bug ### Your current environment ### 🐛 Describe the bug It fails to load and gives the error below: ``` KeyError: 'layers.0.moe.experts.0.down_proj_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: v0.19.1 failed to load AWQ 4bit quantization of Gemma 4 26B-A4B bug ### Your current environment ### 🐛 Describe the bug It fails to load and gives the error below: ``` KeyError: 'layers.0.moe.experts.0.down_proj_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;moe;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
