# vllm-project/vllm#30464: [Usage]: How can I use the local pre-compiled wheel of vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#30464](https://github.com/vllm-project/vllm/issues/30464) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How can I use the local pre-compiled wheel of vllm

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Every time I use `VLLM_USE_PRECOMPILED=1 uv pip install --editable .` to build vllm, it always takes much time to download the pre-compiled wheel. Would it be possible to build it by using a locally downloaded wheel file instead? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: How can I use the local pre-compiled wheel of vllm usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Every time I use `VLLM_USE_PRECOM...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ad? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How can I use the local pre-compiled wheel of vllm usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm Every time I use `VLLM_USE_PRECOM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
