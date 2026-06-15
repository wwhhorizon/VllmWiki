# vllm-project/vllm#24454: [Bug]: Hangs on mulit-node setup when len(prompt) > max_model_len

| 字段 | 值 |
| --- | --- |
| Issue | [#24454](https://github.com/vllm-project/vllm/issues/24454) |
| 状态 | closed |
| 标签 | bug;good first issue;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Hangs on mulit-node setup when len(prompt) > max_model_len

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running on a single node, an assertion gets raised and propagated correctly: ``` AssertionError: Sampled token IDs exceed the max model length. Total number of tokens: 10001 > max_model_len: 10000 ``` However, on multi-node vLLM just hangs until it eventually times out and gets killed. I'm assuming one of the ranks crashes with the same assertion but the error does not get propagated correctly, causing the other ranks to hang. This is using the `LLM` python api instead of `vllm serve` running with `tp=8`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 8`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pi;hardware_porting;model_support;sampling_logits cuda;operator;sampling;triton build_error;crash;nan_inf env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: Hangs on mulit-node setup when len(prompt) > max_model_len bug;good first issue;stale ### Your current environment ### 🐛 Describe the bug When running on a single node, an assertion gets raised and propagated cor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: n mulit-node setup when len(prompt) > max_model_len bug;good first issue;stale ### Your current environment ### 🐛 Describe the bug When running on a single node, an assertion gets raised and propagated correctly: ``` As...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
