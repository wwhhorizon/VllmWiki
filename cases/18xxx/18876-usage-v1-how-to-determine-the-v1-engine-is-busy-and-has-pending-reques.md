# vllm-project/vllm#18876: [Usage][V1]: How to determine the V1 engine is busy and has pending requests?

| 字段 | 值 |
| --- | --- |
| Issue | [#18876](https://github.com/vllm-project/vllm/issues/18876) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage][V1]: How to determine the V1 engine is busy and has pending requests?

### Issue 正文摘录

### Your current environment ```text N/A ``` ### How would you like to use vllm I have a cluster that runs multiple vllm instances on different nodes. It allocate incoming requests to the nodes with load-balancing. Therefore, I need to know if a node is busy so that it will not receive new requests temporarily. For V0 engine I have `len(engine.scheduler.waiting)` for this purpose. However I find V1 engine uses MPClient so that I can't reach the real engine to get the above stats. I want to know is there any helper function to do this? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Usage][V1]: How to determine the V1 engine is busy and has pending requests? usage;stale ### Your current environment ```text N/A ``` ### How would you like to use vllm I have a cluster that runs multiple vllm instance...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: fferent nodes. It allocate incoming requests to the nodes with load-balancing. Therefore, I need to know if a node is busy so that it will not receive new requests temporarily. For V0 engine I have `len(engine.scheduler...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: is? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
