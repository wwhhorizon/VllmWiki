# vllm-project/vllm#39356: [torch.compile] Proper PassManager infrastructure

| 字段 | 值 |
| --- | --- |
| Issue | [#39356](https://github.com/vllm-project/vllm/issues/39356) |
| 状态 | open |
| 标签 | torch.compile;vllm-ir |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [torch.compile] Proper PassManager infrastructure

### Issue 正文摘录

### Motivation Currently, we bundle custom torch.compile passes using the `PostGradPassManager`. This manager is set as the `current_platform.pass_key` (default: `"post_grad_custom_post_pass"`), and individual passes within it are enabled/disabled using individual flags. This lacks scalability and control: every additional pass requires a new flag, which we often skip for utility passes (leaving no way to disable them). Platforms also have to choose a single `pass_key` as opposed to plugging into multiple points in the PyTorch compilation pipeline. This inhibits debugging from the CLI, requiring manual code modifications. It also requires platforms to reimplement a lot of the pass management (enablement, cache hash, etc.). Another example is vLLM-Spyre, which currently plugs into `"post_grad_custom_post_pass"` for custom codegen transformations, colliding with the default vLLM pass manager. ### Proposal We should create a base `PassManager` class, which can handle invoking multiple passes and properly exposes a `uuid()` method to Inductor/AOTAutograd caching. We should also add a way to manually specify the full list of passes on the command line/in Python. Current flags can stick...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [torch.compile] Proper PassManager infrastructure torch.compile;vllm-ir ### Motivation Currently, we bundle custom torch.compile passes using the `PostGradPassManager`. This manager is set as the `current_platform.pass_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rently plugs into `"post_grad_custom_post_pass"` for custom codegen transformations, colliding with the default vLLM pass manager. ### Proposal We should create a base `PassManager` class, which can handle invoking mult...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: pass` becomes a proper `CustomGraphPass`. Depending on interest from OOT backends, this can be prioritized earlier.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [torch.compile] Proper PassManager infrastructure torch.compile;vllm-ir ### Motivation Currently, we bundle custom torch.compile passes using the `PostGradPassManager`. This manager is set as the `current_platform.pass_...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
