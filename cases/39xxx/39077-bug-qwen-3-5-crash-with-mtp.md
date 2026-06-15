# vllm-project/vllm#39077: [Bug]: qwen 3.5 crash with mtp

| 字段 | 值 |
| --- | --- |
| Issue | [#39077](https://github.com/vllm-project/vllm/issues/39077) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: qwen 3.5 crash with mtp

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Tested on Hopper ``` torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` Maybe introduced by d9b90a07a How to reproduce: ``` vllm serve Qwen/Qwen3.5-35B-A3B --language-model-only --speculative-config '{"method":"mtp","num_speculative_tokens":2}' ``` There will be no issue when using the TRITON MoE backend or no mtp ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;speculative_decoding cuda;moe;operator;triton build_erro...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: tp bug ### Your current environment ### 🐛 Describe the bug Tested on Hopper ``` torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` Maybe introduced by d9b90a07a How to reproduce: ``` vllm s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen 3.5 crash with mtp bug ### Your current environment ### 🐛 Describe the bug Tested on Hopper ``` torch.AcceleratorError: CUDA error: an illegal memory access was encountered ``` Maybe introduced by d9b90a07a...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ,"num_speculative_tokens":2}' ``` There will be no issue when using the TRITON MoE backend or no mtp ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot l...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: peculative_tokens":2}' ``` There will be no issue when using the TRITON MoE backend or no mtp ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
