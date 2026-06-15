# vllm-project/vllm#27641: [Bug]: Streaming tool call randomly failed when using gpt-oss-120b/20b

| 字段 | 值 |
| --- | --- |
| Issue | [#27641](https://github.com/vllm-project/vllm/issues/27641) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Streaming tool call randomly failed when using gpt-oss-120b/20b

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have two servers running `vLLM` with `gpt-oss-20b` and `gpt-oss-120b` respectively, and they both exhibit the following problem: When the tools content is relatively large/extensive, and the system prompt is also quite long, if I call the model without streaming (non-stream), it almost always calls the tools correctly. However, if I call the model with streaming (stream), a significant portion of the tool call is very likely to be output into the reasoning content. Here's out put: The key point is: Why does the non-stream approach succeed almost every time, while the stream approach is likely to fail? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: il? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Streaming tool call randomly failed when using gpt-oss-120b/20b bug;stale ### Your current environment ### 🐛 Describe the bug I have two servers running `vLLM` with `gpt-oss-20b` and `gpt-oss-120b` respectively,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ug]: Streaming tool call randomly failed when using gpt-oss-120b/20b bug;stale ### Your current environment ### 🐛 Describe the bug I have two servers running `vLLM` with `gpt-oss-20b` and `gpt-oss-120b` respectively, an...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
