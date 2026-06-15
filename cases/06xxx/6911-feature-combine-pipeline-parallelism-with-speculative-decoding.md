# vllm-project/vllm#6911: [Feature]: Combine pipeline parallelism with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#6911](https://github.com/vllm-project/vllm/issues/6911) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Combine pipeline parallelism with speculative decoding

### Issue 正文摘录

### 🚀 The feature, motivation and pitch We can combine pipeline parallelism with speculative decoding to get latency reductions, especially when serving Llama 405b over two nodes. The speculative decoding framework design should support pipeline parallelism by wrapping normal workers inside the speculative decode worker. But it needs to be tried / issues ironed out. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Feature]: Combine pipeline parallelism with speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch We can combine pipeline parallelism with speculative decoding to get latency reductions, es...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ine parallelism with speculative decoding to get latency reductions, especially when serving Llama 405b over two nodes. The speculative decoding framework design should support pipeline parallelism by wrapping normal wo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Feature]: Combine pipeline parallelism with speculative decoding feature request;stale ### 🚀 The feature, motivation and pitch We can combine pipeline parallelism with speculative decoding to get latency reductions, es...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: speculative decoding to get latency reductions, especially when serving Llama 405b over two nodes. The speculative decoding framework design should support pipeline parallelism by wrapping normal workers inside the spec...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ch We can combine pipeline parallelism with speculative decoding to get latency reductions, especially when serving Llama 405b over two nodes. The speculative decoding framework design should support pipeline parallelis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
