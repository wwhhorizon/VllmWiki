# vllm-project/vllm#34297: [Feature]: User-specified expert→EP-rank placement file for MoE expert parallelism

| 字段 | 值 |
| --- | --- |
| Issue | [#34297](https://github.com/vllm-project/vllm/issues/34297) |
| 状态 | open |
| 标签 | feature request;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: User-specified expert→EP-rank placement file for MoE expert parallelism

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Hi vLLM people, I’m working with MoE expert-parallel (EP) deployments and would like to propose a small, optional extension to allow users to supply a static expert→EP-rank placement. Motivation: For some EP deployments, especially topology-aware or locality-sensitive setups, it’s useful to control which experts are assigned to which EP ranks in a stable, user-defined way (e.g. to reduce unnecessary cross-rank communication or variance). Today, placement is limited to the built-in "linear" and "round_robin" strategies. Proposed approach (minimal and fully optional): - Add an optional CLI/config knob such as: `--expert-placement-file /path/to/placement.json` - The file would contain a simple mapping: `{ "expert_to_ep_rank": [ ... ] }` where the list length equals `global_num_experts` and each value is an EP rank in `[0, ep_size)`. - When this option is not provided, default behavior remains unchanged. Implementation sketch: - The mapping would be consumed at model init time and used to construct the same `(local_num_experts, expert_map, expert_mask)` that is currently produced by `determine_expert_map`. - No kernel, NCCL, or routing logic cha...

## 候选优化模式

- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Feature]: User-specified expert→EP-rank placement file for MoE expert parallelism feature request;stale ### 🚀 The feature, motivation and pitch Hi vLLM people, I’m working with MoE expert-parallel (EP) deployments and...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: User-specified expert→EP-rank placement file for MoE expert parallelism feature request;stale ### 🚀 The feature, motivation and pitch Hi vLLM people, I’m working with MoE expert-parallel (EP) deployments and...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e]: User-specified expert→EP-rank placement file for MoE expert parallelism feature request;stale ### 🚀 The feature, motivation and pitch Hi vLLM people, I’m working with MoE expert-parallel (EP) deployments and would l...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . Proposed approach (minimal and fully optional): - Add an optional CLI/config knob such as: `--expert-placement-file /path/to/placement.json` - The file would contain a simple mapping: `{ "expert_to_ep_rank": [ ... ] }...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ecified expert→EP-rank placement file for MoE expert parallelism feature request;stale ### 🚀 The feature, motivation and pitch Hi vLLM people, I’m working with MoE expert-parallel (EP) deployments and would like to prop...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
