# vllm-project/vllm#43207: [Feature]: GRPC interface for Pooling

| 字段 | 值 |
| --- | --- |
| Issue | [#43207](https://github.com/vllm-project/vllm/issues/43207) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: GRPC interface for Pooling

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Is there any plan to support pooling-based APIs like classify, score and rerank in vLLM gRPC service? These interfaces are missing in the current proto file as shown in the link：[https://github.com/lightseekorg/smg/blob/main/crates/grpc_client/proto/vllm_engine.proto](url) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: current proto file as shown in the link：[https://github.com/lightseekorg/smg/blob/main/crates/grpc_client/proto/vllm_engine.proto](url) ### Alternatives _No response_ ### Additional context _No response_ ### Before subm...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ? These interfaces are missing in the current proto file as shown in the link：[https://github.com/lightseekorg/smg/blob/main/crates/grpc_client/proto/vllm_engine.proto](url) ### Alternatives _No response_ ### Additional...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: GRPC interface for Pooling feature request ### 🚀 The feature, motivation and pitch Is there any plan to support pooling-based APIs like classify, score and rerank in vLLM gRPC service? These interfaces are mi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
