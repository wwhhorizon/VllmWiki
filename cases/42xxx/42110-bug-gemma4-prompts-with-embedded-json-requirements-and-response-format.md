# vllm-project/vllm#42110: [Bug]: gemma4 prompts with embedded json requirements AND response_format.json_schema cause timeouts

| 字段 | 值 |
| --- | --- |
| Issue | [#42110](https://github.com/vllm-project/vllm/issues/42110) |
| 状态 | open |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: gemma4 prompts with embedded json requirements AND response_format.json_schema cause timeouts

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug sending the above payload to vllm can reproduce the problem - it seems to just hangs for >6min (our timeout value) if we tweak the request and remove the json requirement in the system prompt - it seems to work just fine. the EXACT failure json going into `gpt-oss-120b` does not deadlock like that. which leads me to think there might be some issues in the parser for gemma4. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: gemma4 prompts with embedded json requirements AND response_format.json_schema cause timeouts bug ### Your current environment ### 🐛 Describe the bug sending the above payload to vllm can reproduce the problem -
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;sampling_logits;speculative_decoding cuda;moe;operator;s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: - it seems to just hangs for >6min (our timeout value) if we tweak the request and remove the json requirement in the system prompt - it seems to work just fine. the EXACT failure json going into `gpt-oss-120b` does not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: a4. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: gemma4 prompts with embedded json requirements AND response_format.json_schema cause timeouts bug ### Your current environment ### 🐛 Describe the bug sending the above payload to vllm can reproduce the problem -

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
