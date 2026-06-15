# vllm-project/vllm#24408: [Usage]: Does the qwen3 model extrapolate automatically, or do I need to set the rope_scaling parameter?

| 字段 | 值 |
| --- | --- |
| Issue | [#24408](https://github.com/vllm-project/vllm/issues/24408) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does the qwen3 model extrapolate automatically, or do I need to set the rope_scaling parameter?

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. Does the qwen3 model extrapolate automatically, or do I need to set the rope_scaling parameter? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. Does the qwen3 model extrapolate automatically, or do I need to set the rop...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Does the qwen3 model extrapolate automatically, or do I need to set the rope_scaling parameter? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: er? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ate automatically, or do I need to set the rope_scaling parameter? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
