# vllm-project/vllm#18877: [Questions]: The problem of repeated capture of cudagraph during weight update phase?

| 字段 | 值 |
| --- | --- |
| Issue | [#18877](https://github.com/vllm-project/vllm/issues/18877) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Questions]: The problem of repeated capture of cudagraph during weight update phase?

### Issue 正文摘录

### Your current environment None ### How would you like to use vllm If I use vLLM Backend in veRL, how can I avoid repeated cudagraph capture during the rollout weight update phase? Thanks~ Is there any good official implementation? related issue: https://github.com/volcengine/verl/issues/1655 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Questions]: The problem of repeated capture of cudagraph during weight update phase? usage;stale ### Your current environment None ### How would you like to use vllm If I use vLLM Backend in veRL, how can I avoid repea...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ent environment None ### How would you like to use vllm If I use vLLM Backend in veRL, how can I avoid repeated cudagraph capture during the rollout weight update phase? Thanks~ Is there any good official implementation...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e during the rollout weight update phase? Thanks~ Is there any good official implementation? related issue: https://github.com/volcengine/verl/issues/1655 ### Before submitting a new issue... - [x] Make sure you already...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: oblem of repeated capture of cudagraph during weight update phase? usage;stale ### Your current environment None ### How would you like to use vllm If I use vLLM Backend in veRL, how can I avoid repeated cudagraph captu...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
