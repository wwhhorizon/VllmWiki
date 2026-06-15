# vllm-project/vllm#23761: [Feature Request]: Per-rank log files (especially per-actor for Ray)

| 字段 | 值 |
| --- | --- |
| Issue | [#23761](https://github.com/vllm-project/vllm/issues/23761) |
| 状态 | open |
| 标签 | feature request;ray;unstale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request]: Per-rank log files (especially per-actor for Ray)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch This is essential for debugging various Ray problems (hangs, slow task allocation). By default, Ray consolidates all logs to central log-files, but these can be quite hard to decrypt (especially if hangs happen). For debugging hangs, it's great to have simple, per-rank / non-consolidated, readable, vim-able, greppable log files (that is the rank should be both in the file name and in every log line, and no ANSI coloring, so that vim does not choke) in the spirit of: - https://github.com/modelscope/Trinity-RFT/issues/167#issuecomment-3213803351 I hope this could also help with: - https://github.com/vllm-project/vllm/issues/5052#issuecomment-2294294943 It would be nice to have some built-in customized logging format knobs, e.g. logging the prompts / responses / VRAM stats etc, and might be logging as `jsonl`, so that every line could also be deserialized as JSON. This should also be useful for non-ray backend as well. And especially if vllm itself gets more complex and has several processes and async/rpc-comms between them which can hang - it's useful to be able to have per-process (or per-thread if relevant) good old log files. ### Alternativ...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ring, so that vim does not choke) in the spirit of: - https://github.com/modelscope/Trinity-RFT/issues/167#issuecomment-3213803351 I hope this could also help with: - https://github.com/vllm-project/vllm/issues/5052#iss...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature Request]: Per-rank log files (especially per-actor for Ray) feature request;ray;unstale ### 🚀 The feature, motivation and pitch This is essential for debugging various Ray problems (hangs, slow task allocation)...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ld also be deserialized as JSON. This should also be useful for non-ray backend as well. And especially if vllm itself gets more complex and has several processes and async/rpc-comms between them which can hang - it's u...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature Request]: Per-rank log files (especially per-actor for Ray) feature request;ray;unstale ### 🚀 The feature, motivation and pitch This is essential for debugging various Ray problems (hangs, slow task allocation)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
