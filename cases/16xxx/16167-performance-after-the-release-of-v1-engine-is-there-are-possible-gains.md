# vllm-project/vllm#16167: [Performance]: After the release of V1 Engine is there are possible gains by implementing the Engine in a more performance language ?

| 字段 | 值 |
| --- | --- |
| Issue | [#16167](https://github.com/vllm-project/vllm/issues/16167) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: After the release of V1 Engine is there are possible gains by implementing the Engine in a more performance language ?

### Issue 正文摘录

### Proposal to improve performance I am very inspired by vLLM and would like to make it as efficient as possible. Some time ago I rewrote the vLLM engine in Rust: https://github.com/atoma-network/atoma-infer And I would like to know from the maintainers and core contributors if there is any appetite to rewrite some components of the v1 Engine in a more performance language other than Python (C/C++, Rust, etc). One key advantages of Rust is that it makes very explicit where and how you want to optimize things and asynchronous code is very robust. Through some profiling on vLLM I noticed that a still relevant time of compute is spent on CPU cycles, so curious to know everyone's thoughts on this.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: performance I am very inspired by vLLM and would like to make it as efficient as possible. Some time ago I rewrote the vLLM engine in Rust: https://github.com/atoma-network/atoma-infer And I would like to know from the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: by implementing the Engine in a more performance language ? performance;stale ### Proposal to improve performance I am very inspired by vLLM and would like to make it as efficient as possible. Some time ago I rewrote th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nt to optimize things and asynchronous code is very robust. Through some profiling on vLLM I noticed that a still relevant time of compute is spent on CPU cycles, so curious to know everyone's thoughts on this.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
