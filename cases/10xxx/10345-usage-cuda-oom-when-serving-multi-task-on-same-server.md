# vllm-project/vllm#10345: [Usage]: cuda oom when serving multi task on same server

| 字段 | 值 |
| --- | --- |
| Issue | [#10345](https://github.com/vllm-project/vllm/issues/10345) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: cuda oom when serving multi task on same server

### Issue 正文摘录

### Your current environment ```text vllm 0.6.0 qwen2.5-14b cuda 12.4 ``` ### How would you like to use vllm I would serving task generate and embedding on same server, but cuda oom can i serving generate on gpu , but embedding on cpu? please advice ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: cuda oom when serving multi task on same server usage;stale ### Your current environment ```text vllm 0.6.0 qwen2.5-14b cuda 12.4 ``` ### How would you like to use vllm I would serving task generate and embeddi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: cuda oom when serving multi task on same server usage;stale ### Your current environment ```text vllm 0.6.0 qwen2.5-14b cuda 12.4 ``` ### How would you like to use vllm I would serving task generate and embeddi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: same server usage;stale ### Your current environment ```text vllm 0.6.0 qwen2.5-14b cuda 12.4 ``` ### How would you like to use vllm I would serving task generate and embedding on same server, but cuda oom can i serving...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: cuda oom when serving multi task on same server usage;stale ### Your current environment ```text vllm 0.6.0 qwen2.5-14b cuda 12.4 ``` ### How would you like to use vllm I would serving task generate and embeddi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api cuda oom Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
