# vllm-project/vllm#37363: fix(compilation): fix piecewise CUDA graph bugs with splitting_ops

| 字段 | 值 |
| --- | --- |
| Issue | [#37363](https://github.com/vllm-project/vllm/issues/37363) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> fix(compilation): fix piecewise CUDA graph bugs with splitting_ops

### Issue 正文摘录

## Description Two bugs in piecewise CUDA graph compilation that surface when a `splitting_op` produces multiple outputs or allocates new output tensors. **Bug 1 — `backends.py`: cycle in `split_graph()`** `getitem` nodes of a multi-output `splitting_op` were assigned to the same subgraph, creating a dependency cycle that causes `torch.fx.passes.split_module` to raise. **Bug 2 — `cuda_graph.py`: stale tensor addresses during replay** When a `splitting_op` allocates new tensors (e.g. via `torch.bmm`), the next piece's CUDA graph replays with stale addresses → silent data corruption. Both are general vLLM issues, not tied to any specific model. They surface whenever a `splitting_op` produces multiple outputs or allocates new tensors. ## Fix PR: https://github.com/vllm-project/vllm/pull/37361

## 现有链接修复摘要

#37395 Fix piecewise CUDA graph bugs in split_graph and cuda_graph replay

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: lti-output `splitting_op` were assigned to the same subgraph, creating a dependency cycle that causes `torch.fx.passes.split_module` to raise. **Bug 2 — `cuda_graph.py`: stale tensor addresses during replay** When a `sp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ` produces multiple outputs or allocates new output tensors. **Bug 1 — `backends.py`: cycle in `split_graph()`** `getitem` nodes of a multi-output `splitting_op` were assigned to the same subgraph, creating a dependency...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: fix(compilation): fix piecewise CUDA graph bugs with splitting_ops ## Description Two bugs in piecewise CUDA graph compilation that surface when a `splitting_op` produces multiple outputs or allocates new output tensors...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: data corruption. Both are general vLLM issues, not tied to any specific model. They surface whenever a `splitting_op` produces multiple outputs or allocates new tensors. ## Fix PR: https://github.com/vllm-project/vllm/p...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ses `torch.fx.passes.split_module` to raise. **Bug 2 — `cuda_graph.py`: stale tensor addresses during replay** When a `splitting_op` allocates new tensors (e.g. via `torch.bmm`), the next piece's CUDA graph replays with...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37395](https://github.com/vllm-project/vllm/pull/37395) | closes_keyword | 0.95 | Fix piecewise CUDA graph bugs in split_graph and cuda_graph replay | Fix for issue #37363: Two bugs in piecewise CUDA graph compilation Bug 1 - backends.py: cycle in split_graph() Fixed the handling of getitem nodes that reference multi-output spli |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
