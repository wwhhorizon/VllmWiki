# vllm-project/vllm#13861: [Feature]: proxy load balance function use like: vllm proxy --server-address ... --server-port ...

| 字段 | 值 |
| --- | --- |
| Issue | [#13861](https://github.com/vllm-project/vllm/issues/13861) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: proxy load balance function use like: vllm proxy --server-address ... --server-port ...

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am accustomed to using vllm and typically construct load balancing logic on the client side. However, I recently discovered that the lmdeploy library includes a proxy command that can dynamically manage model instances and select load balancing modes. I believe this functionality would be very useful in vllm, as it can make vllm appear as a black-box model while achieving several times the throughput (depending on the number of instances). Therefore, I hope to see this feature expanded. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tion use like: vllm proxy --server-address ... --server-port ... feature request;stale ### 🚀 The feature, motivation and pitch I am accustomed to using vllm and typically construct load balancing logic on the client sid...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: make vllm appear as a black-box model while achieving several times the throughput (depending on the number of instances). Therefore, I hope to see this feature expanded. ### Alternatives _No response_ ### Additional co...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: d pitch I am accustomed to using vllm and typically construct load balancing logic on the client side. However, I recently discovered that the lmdeploy library includes a proxy command that can dynamically manage model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: he lmdeploy library includes a proxy command that can dynamically manage model instances and select load balancing modes. I believe this functionality would be very useful in vllm, as it can make vllm appear as a black-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
