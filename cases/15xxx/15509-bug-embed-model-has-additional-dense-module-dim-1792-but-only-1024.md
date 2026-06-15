# vllm-project/vllm#15509: [Bug]: Embed model has additional dense module(dim=1792, but only 1024)

| 字段 | 值 |
| --- | --- |
| Issue | [#15509](https://github.com/vllm-project/vllm/issues/15509) |
| 状态 | closed |
| 标签 | bug;help wanted;good first issue;stale |
| 评论 | 18; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Embed model has additional dense module(dim=1792, but only 1024)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The embed model has an additional dense module with an output dimension of 1792, but the actual output dimension of vllm is still 1024. same issue in TEI: [https://github.com/huggingface/text-embeddings-inference/issues/423](https://github.com/huggingface/text-embeddings-inference/issues/423) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;shape Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 23) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Embed model has additional dense module(dim=1792, but only 1024) bug;help wanted;good first issue;stale ### Your current environment ### 🐛 Describe the bug The embed model has an additional dense module with an o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: l dense module(dim=1792, but only 1024) bug;help wanted;good first issue;stale ### Your current environment ### 🐛 Describe the bug The embed model has an additional dense module with an output dimension of 1792, but the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
