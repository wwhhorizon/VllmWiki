# vllm-project/vllm#15604: [Bug]: Failed to run deepseek v2 lite model with tp = 8 when enabling expert parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#15604](https://github.com/vllm-project/vllm/issues/15604) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run deepseek v2 lite model with tp = 8 when enabling expert parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Running the following code: ```bash vllm serve deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct --tensor-parallel-size 8 --trust-remote-code --enable-expert-parallel ``` VLLM works well when I set the tp size to 4. But I got same error for tp size = 2. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;sampling_logits attention;cuda;moe;operator;sampling;triton build_er...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 2. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Failed to run deepseek v2 lite model with tp = 8 when enabling expert parallel bug ### Your current environment ### 🐛 Describe the bug Running the following code: ```bash vllm serve deepseek-ai/DeepSeek-Coder-V2-...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: g;model_support;moe;sampling_logits attention;cuda;moe;operator;sampling;triton build_error;crash env_dependency;shape Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Failed to run deepseek v2 lite model with tp = 8 when enabling expert parallel bug ### Your current environment ### 🐛 Describe the bug Running the following code: ```bash vllm serve deepseek-ai/DeepSeek-Coder-V2-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
