# vllm-project/vllm#35154: [Performance]: Optimized Deployment Recipe for Qwen3.5

| 字段 | 值 |
| --- | --- |
| Issue | [#35154](https://github.com/vllm-project/vllm/issues/35154) |
| 状态 | open |
| 标签 | performance;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Optimized Deployment Recipe for Qwen3.5

### Issue 正文摘录

### Proposal to improve performance Currently https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html does not reflect the optimal deployment configurations for Qwen3.5. In the updated recipe, we would like to have ideally throughput-focused and latency-focused deployment configurations on different hardware (H200, B200, GB200) and different setups (single-node, multi-node) ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: mprove performance Currently https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html does not reflect the optimal deployment configurations for Qwen3.5. In the updated recipe, we would like to have ideally thr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d latency-focused deployment configurations on different hardware (H200, B200, GB200) and different setups (single-node, multi-node) ### Report of performance regression _No response_ ### Misc discussion on performance...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Optimized Deployment Recipe for Qwen3.5 performance;stale ### Proposal to improve performance Currently https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html does not reflect the optimal deplo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Performance]: Optimized Deployment Recipe for Qwen3.5 performance;stale ### Proposal to improve performance Currently https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html does not reflect the optimal deplo...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Optimized Deployment Recipe for Qwen3.5 performance;stale ### Proposal to improve performance Currently https://docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3.5.html does not reflect the optimal deplo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
