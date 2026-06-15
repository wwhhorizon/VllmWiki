# vllm-project/vllm#23554: [Bug]: [V1][V0.9.1][PD disaggregation] Infinite waiting loop when kv cache is only capable for one long text request

| 字段 | 值 |
| --- | --- |
| Issue | [#23554](https://github.com/vllm-project/vllm/issues/23554) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cache;cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [V1][V0.9.1][PD disaggregation] Infinite waiting loop when kv cache is only capable for one long text request

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug To reproduce this bug, we need to run a long text (For example set --max-model-len 34000), and make sure kv cache can only support one max-model-len request at one time. In PD disaggregation scenario, D Node will pre-allocate kv cache space for the requests from P Node, then some blocks are allocated for those request, and the blocks left are not capable for one long text request, which means this request will be preempted. Later, the V1 scheduler will append the preempted_req to the first place of waiting queue, but the blocks are not enough for this request, since this is the reason it is preempted. Then the scheduler will run this infinite waiting loop. Here are some logs I got ``` Maximum concurrency for 34,000 tokens per request: 1.01x GPU KV cache size: 37,632 tokens Maximum concurrency for 34,000 tokens per request: 1.11x GPU KV cache size: 34,304 tokens Maximum concurrency for 34,000 tokens per request: 1.01x GPU KV cache size: 37,632 tokens Maximum concurrency for 34,000 tokens per request: 1.11x GPU KV cache size: 34,304 tokens Maximum concurrency for 34,000 tokens per request: 1.01x GPU KV cache size: 37,632 tokens Max...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: [V1][V0.9.1][PD disaggregation] Infinite waiting loop when kv cache is only capable for one long text request bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce this bug, we need to run a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;frontend_api;hardware_porting;model_support;scheduler_memory cache;cuda build_error env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: st bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce this bug, we need to run a long text (For example set --max-model-len 34000), and make sure kv cache can only support one max-model-len reque...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: [V1][V0.9.1][PD disaggregation] Infinite waiting loop when kv cache is only capable for one long text request bug;stale ### Your current environment ### 🐛 Describe the bug To reproduce this bug, we need to run a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
