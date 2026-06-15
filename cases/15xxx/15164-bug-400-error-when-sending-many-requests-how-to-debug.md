# vllm-project/vllm#15164: [Bug]: 400 error when sending many requests... how to debug?

| 字段 | 值 |
| --- | --- |
| Issue | [#15164](https://github.com/vllm-project/vllm/issues/15164) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 400 error when sending many requests... how to debug?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm getting `openai.BadRequestError: Invalid HTTP request received. When I get this, I save the request and then try resend it later, and it works. I am running a few thousand requests in parallel when I get the 400 error, and a single request when I don't. Still trying to repro, but struggling -- any hints or ways to get a better error trace? Amusingly I can't seem to unpickle the openai.BadRequestError if I pickle it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: 400 error when sending many requests... how to debug? bug;stale ### Your current environment ### 🐛 Describe the bug I'm getting `openai.BadRequestError: Invalid HTTP request received. When I get this, I save the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: it. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
