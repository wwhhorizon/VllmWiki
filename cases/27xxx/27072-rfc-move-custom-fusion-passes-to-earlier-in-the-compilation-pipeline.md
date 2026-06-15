# vllm-project/vllm#27072: [RFC]: Move custom fusion passes to earlier in the compilation pipeline

| 字段 | 值 |
| --- | --- |
| Issue | [#27072](https://github.com/vllm-project/vllm/issues/27072) |
| 状态 | closed |
| 标签 | RFC;torch.compile;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Move custom fusion passes to earlier in the compilation pipeline

### Issue 正文摘录

### Motivation. #24604 introduces pattern matching using torch implementations of custom ops. @zou3519 pointed out is brittle and could break if Inductor transforms the graph such that the traced torch pattern for the custom op no longer matches. ### Proposed Change. We will move pattern matcher custom passes that rely on custom ops (basically all of them right now) from `post_grad_custom_post_pass` to `post_grad_custom_pre_pass`. Alternatively, we could move it to `joint_graph_pass`. We will create a new pass manager object with similar semantics to the current `PostGradPassManager` (we'll rename them to make it clearer, perhaps `PostGradPostPassManager` and `PostGradPrePassManager`). Most current passes will move to the new manager (except for `FixFunctionalizationPass`, but that one will hopefully be deprecated anyway). What we still need to figure out: - our passes rely on some peephoole optimizations (removing noop slices, views, reshapes, etc.) - I think those currently run after `post_grad_custom_pre_pass`. We could run them manually, adapt our patterns, or improve pattern matcher support to match "through" certain pointwise operations. - there is in-progress work (#164273)...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ew pass manager object with similar semantics to the current `PostGradPassManager` (we'll rename them to make it clearer, perhaps `PostGradPostPassManager` and `PostGradPrePassManager`). Most current passes will move to...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ve custom fusion passes to earlier in the compilation pipeline RFC;torch.compile;stale ### Motivation. #24604 introduces pattern matching using torch implementations of custom ops. @zou3519 pointed out is brittle and co...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m fusion passes to earlier in the compilation pipeline RFC;torch.compile;stale ### Motivation. #24604 introduces pattern matching using torch implementations of custom ops. @zou3519 pointed out is brittle and could brea...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
