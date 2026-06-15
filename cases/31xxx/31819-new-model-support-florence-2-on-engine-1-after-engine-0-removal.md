# vllm-project/vllm#31819: [New Model]: Support Florence-2 on Engine 1 After Engine 0 Removal

| 字段 | 值 |
| --- | --- |
| Issue | [#31819](https://github.com/vllm-project/vllm/issues/31819) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: Support Florence-2 on Engine 1 After Engine 0 Removal

### Issue 正文摘录

### The model to consider. Since Engine 0 was removed, vLLM versions newer than 0.9.1 can no longer run Florence-2 models; could support for Florence-2 be added to the current engine architecture? ### The closest model vllm already supports. florence-2 ### What's your difficulty of supporting the model you want? Unknown. Florence-2 is an encoder-decoder model, and its compatibility with Engine 1 after the removal of Engine 0 is currently unclear. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: l new-model ### The model to consider. Since Engine 0 was removed, vLLM versions newer than 0.9.1 can no longer run Florence-2 models; could support for Florence-2 be added to the current engine architecture? ### The cl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce-2 models; could support for Florence-2 be added to the current engine architecture? ### The closest model vllm already supports. florence-2 ### What's your difficulty of supporting the model you want? Unknown. Floren...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [New Model]: Support Florence-2 on Engine 1 After Engine 0 Removal new-model ### The model to consider. Since Engine 0 was removed, vLLM versions newer than 0.9.1 can no longer run Florence-2 models; could support for F...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: lty of supporting the model you want? Unknown. Florence-2 is an encoder-decoder model, and its compatibility with Engine 1 after the removal of Engine 0 is currently unclear. ### Before submitting a new issue... - [x] M...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
