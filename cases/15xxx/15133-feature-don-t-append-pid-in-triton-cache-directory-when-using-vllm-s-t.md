# vllm-project/vllm#15133: [Feature]: Don't append pid in triton cache directory when using vllm's torch_compile_cache

| 字段 | 值 |
| --- | --- |
| Issue | [#15133](https://github.com/vllm-project/vllm/issues/15133) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Don't append pid in triton cache directory when using vllm's torch_compile_cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch reported in https://vllm-dev.slack.com/archives/C07QP347J4D/p1742083045279469 . since we redirect the cache to different directory for every rank in v1 ( see https://docs.vllm.ai/en/latest/design/v1/torch_compile.html ), we don't need to append pid anymore. requested change would be: https://github.com/vllm-project/vllm/blob/073d1ed354902a99c788d1a834198a7653b4a256/vllm/executor/multiproc_worker_utils.py#L319 update the condition, exclude `maybe_set_triton_cache_manager` when we have piecewise compilation (also need to change the function argument to vllm config so that we can access the compilation level in this function) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Feature]: Don't append pid in triton cache directory when using vllm's torch_compile_cache feature request ### 🚀 The feature, motivation and pitch reported in https://vllm-dev.slack.com/archives/C07QP347J4D/p1742083045...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ure]: Don't append pid in triton cache directory when using vllm's torch_compile_cache feature request ### 🚀 The feature, motivation and pitch reported in https://vllm-dev.slack.com/archives/C07QP347J4D/p174208304527946...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: he feature, motivation and pitch reported in https://vllm-dev.slack.com/archives/C07QP347J4D/p1742083045279469 . since we redirect the cache to different directory for every rank in v1 ( see https://docs.vllm.ai/en/late...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: piecewise compilation (also need to change the function argument to vllm config so that we can access the compilation level in this function) ### Alternatives _No response_ ### Additional context _No response_ ### Befor...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in triton cache directory when using vllm's torch_compile_cache feature request ### 🚀 The feature, motivation and pitch reported in https://vllm-dev.slack.com/archives/C07QP347J4D/p1742083045279469 . since we redirect t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
