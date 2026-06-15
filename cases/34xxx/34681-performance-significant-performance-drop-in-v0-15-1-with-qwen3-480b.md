# vllm-project/vllm#34681: [Performance]: Significant performance drop in v0.15.1 with Qwen3-480B?

| 字段 | 值 |
| --- | --- |
| Issue | [#34681](https://github.com/vllm-project/vllm/issues/34681) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Significant performance drop in v0.15.1 with Qwen3-480B?

### Issue 正文摘录

### Proposal to improve performance Hi everyone, I just upgraded from v0.10.1 to v0.15.1 and I'm seeing a noticeable slowdown in performance using Qwen3-coder-480-a35B-instruct. My setup is: 16 x H100 GPUs TP=8, PP=2 I'm using the exact same configuration as before, but the throughput/latency is significantly worse. Before I deep dive into profiling, I wanted to check: Is anyone else experiencing performance regressions with the 0.15.x releases, specifically on multi-node or PP/TP setups? Would love to know if this is a known issue or if there are new default settings in v0.15.1 that I should tweak (like chunked prefill or CUDA graph changes). Thanks! ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: s TP=8, PP=2 I'm using the exact same configuration as before, but the throughput/latency is significantly worse. Before I deep dive into profiling, I wanted to check: Is anyone else experiencing performance regressions...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: in performance using Qwen3-coder-480-a35B-instruct. My setup is: 16 x H100 GPUs TP=8, PP=2 I'm using the exact same configuration as before, but the throughput/latency is significantly worse. Before I deep dive into pro...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: re I deep dive into profiling, I wanted to check: Is anyone else experiencing performance regressions with the 0.15.x releases, specifically on multi-node or PP/TP setups? Would love to know if this is a known issue or...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Significant performance drop in v0.15.1 with Qwen3-480B? performance;stale ### Proposal to improve performance Hi everyone, I just upgraded from v0.10.1 to v0.15.1 and I'm seeing a noticeable slowdown in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e]: Significant performance drop in v0.15.1 with Qwen3-480B? performance;stale ### Proposal to improve performance Hi everyone, I just upgraded from v0.10.1 to v0.15.1 and I'm seeing a noticeable slowdown in performance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
