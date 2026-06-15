# vllm-project/vllm#13752: [Usage]: difference between vllm’s cuda graph and torch.compile's reduce-overhead mode

| 字段 | 值 |
| --- | --- |
| Issue | [#13752](https://github.com/vllm-project/vllm/issues/13752) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: difference between vllm’s cuda graph and torch.compile's reduce-overhead mode

### Issue 正文摘录

### My Question It seems like "reduce-overhead" mode of torch.compile support cuda graph, does vllm support different torch.compile mode? What's the difference between vllm's cuda graph and torch.compile reduce-overhead mode? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Usage]: difference between vllm’s cuda graph and torch.compile's reduce-overhead mode usage;stale ### My Question It seems like "reduce-overhead" mode of torch.compile support cuda graph, does vllm support different to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: difference between vllm’s cuda graph and torch.compile's reduce-overhead mode usage;stale ### My Question It seems like "reduce-overhead" mode of torch.compile support cuda graph, does vllm support different to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: between vllm’s cuda graph and torch.compile's reduce-overhead mode usage;stale ### My Question It seems like "reduce-overhead" mode of torch.compile support cuda graph, does vllm support different torch.compile mode? Wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency My Question

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
