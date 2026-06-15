# vllm-project/vllm#8045: [Bug]: Inconsistent generation with guided_json, speculative decoding and temp > 0.0

| 字段 | 值 |
| --- | --- |
| Issue | [#8045](https://github.com/vllm-project/vllm/issues/8045) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistent generation with guided_json, speculative decoding and temp > 0.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vLLM built from source. Not sure if it is a bug or expected but vLLM fails to generate consistent JSON (with guided_json) if speculative decoding (ngram) is active and temperature > 0.0. This is not the case when speculative decoding is disabled. Edit: guided_json (outlines) also has a significant speed impact when temp = 0. Generation is about about 3-5 times slower in my use case. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_depend...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: se. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Inconsistent generation with guided_json, speculative decoding and temp > 0.0 bug;stale ### Your current environment ### 🐛 Describe the bug vLLM built from source. Not sure if it is a bug or expected but vLLM fai...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ots of frequently asked questions. correctness ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf;slowdown env_dependency Your current environm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
